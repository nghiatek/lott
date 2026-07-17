# crawler_2
import requests
from bs4 import BeautifulSoup
from datetime import datetime
import json, csv
import os

URL = "https://vietlott.vn/vi/trung-thuong/ket-qua-trung-thuong/655.html"

def scrape_power_655():
    # Giả lập Trình duyệt để tránh bị chặn (403 Forbidden)
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Language": "vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7"
    }

    try:
        response = requests.get(URL, headers=headers, timeout=15)
        if response.status_code != 200:
            print(f"Lỗi truy cập: Báo mã lỗi {response.status_code}")
            return None
        
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # 1. Tìm khu vực chứa kết quả chi tiết của kỳ quay mới nhất
        # Vietlott bọc vùng kết quả trong class 'box_kqtt_hp' hoặc cấu trúc cây thẻ tương đương
        result_box = soup.find('div', class_='result') or soup.find('div', class_='box_kqtt_hp')
        
        if not result_box:
            # Fallback nếu giao diện đổi wrapper chính, tìm thẳng cụm chứa số
            result_box = soup
            
        # 2. Bóc tách thông tin Kỳ quay và Ngày quay
        # Thông thường nằm trong thẻ h5 hoặc thẻ chứa chữ "Kỳ quay số..."
        meta_info = result_box.find('h5')
        if meta_info:
            meta_text = meta_info.get_text(separator=" ").strip()
            # Ví dụ chuỗi: "Kỳ quay số: #01050 | Ngày quay thưởng: 16/07/2026"
            # Ta sẽ bẻ nhỏ chuỗi để lấy thông tin sạch
            parts = meta_text.split('|')
            draw_id = parts[0].replace("Kỳ quay số:", "").replace("#", "").strip()
            draw_date = parts[1].replace("Ngày quay thưởng:", "").strip()
        else:
            # Giải pháp dự phòng nếu không tìm thấy h5
            draw_id = "Không rõ"
            draw_date = datetime.now().strftime("%d/%m/%Y")

        # 3. Trích xuất bộ số trúng thưởng (Các quả bóng đỏ và vàng)
        # Bộ số của Vietlott sử dụng class 'day_so_ket_qua' chứa các thẻ span có class 'wh_cuc_tuyet' hoặc 'bi-so'
        numbers = []
        
        # Tìm tất cả các thẻ span đại diện cho quả bóng số
        ball_spans = result_box.find_all('span', class_='wh_cuc_tuyet') 
        if not ball_spans:
            # Lớp dự phòng nếu Vietlott cập nhật lại class bóng số
            ball_spans = result_box.select('.day_so_ket_qua span')

        for span in ball_spans:
            num_txt = span.get_text().strip()
            if num_txt.isdigit():
                numbers.append(int(num_txt))

        # Xác thực cấu trúc mảng số cho giải Power 6/55 (Phải đủ 7 số: 6 số chính + 1 số vàng)
        if len(numbers) >= 7:
            main_numbers = sorted(numbers[:6]) # 6 số đầu tiên (được sắp xếp tăng dần để dễ thống kê)
            bonus_number = numbers[6]          # Số thứ 7 là số đặc biệt (Cầu vàng)
        elif len(numbers) == 6:
            main_numbers = sorted(numbers)
            bonus_number = None
            print("Cảnh báo: Không tìm thấy số đặc biệt (Bonus), cấu trúc trang có thể đã đổi.")
        else:
            print("Không thể parse được bộ số. Vui lòng kiểm tra lại cấu trúc HTML.")
            return None

        # 4. Tổ chức lại cấu trúc dữ liệu JSON sạch
        output = {
            "draw_id": draw_id,
            "date": draw_date,
            "numbers": main_numbers,
            "bonus": bonus_number,
            "scraped_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        
        return output

    except Exception as e:
        print(f"Có lỗi xảy ra trong quá trình cào dữ liệu: {e}")
        return None
        
def save_data(new_record):
    # 1. Lưu vào JSON
    # json_path = 'data/power655.json'
    json_path = '655.json'
    existing_data = []
    
    if os.path.exists(json_path):
        with open(json_path, 'r', encoding='utf-8') as f:
            try:
                existing_data = json.load(f)
            except json.JSONDecodeError:
                pass
                
    # Tránh trùng lặp kỳ quay
    if not any(item['draw_id'] == new_record['draw_id'] for item in existing_data):
        existing_data.insert(0, new_record) # Thêm vào đầu danh sách để lấy mới nhất trước
        with open(json_path, 'w', encoding='utf-8') as f:
            json.dump(existing_data, f, ensure_ascii=False, indent=4)
            
    # 2. Lưu vào CSV
    csv_path = '655.csv'
    file_exists = os.path.exists(csv_path)
    
    if not any(item['draw_id'] == new_record['draw_id'] for item in existing_data[:-1]): # Nếu là bản ghi mới
        with open(csv_path, 'a', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            if not file_exists:
                writer.writerow(['Kỳ quay', 'Ngày', 'Số 1', 'Số 2', 'Số 3', 'Số 4', 'Số 5', 'Số 6', 'Số Bonus', 'Cập nhật'])
            '''error
            writer.writerow([
                new_record['draw_id'], new_record['date'],
                *new_record['numbers'], new_record['bonus'], new_record['updated_at']
            ])
            '''
            writer.writerow([
                new_record['draw_id'], new_record['date'],
                *new_record['numbers'], new_record['bonus'], 
                new_record.get('scraped_at', new_record.get('updated_at', ''))
            ])

if __name__ == "__main__":
    # Test thử script chạy trực tiếp
    result = scrape_power_655()
    if result:
        print("\nDữ liệu thô cào về thành công:")
        #print(json.dumps(data, indent=4, ensure_ascii=False))
        save_data(result)
        print("Cào dữ liệu thành công!")
        
