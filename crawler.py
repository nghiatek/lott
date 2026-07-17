# crawler.py - Vietlott Power 6/55 Crawler (Fixed)
import requests
from bs4 import BeautifulSoup
from datetime import datetime
import json
import os
import csv

URL = "https://vietlott.vn/vi/trung-thuong/ket-qua-trung-thuong/655.html"

def scrape_power_655():
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Language": "vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7"
    }

    try:
        response = requests.get(URL, headers=headers, timeout=15)
        print(f"Status code: {response.status_code}")
        
        if response.status_code != 200:
            print(f"Lỗi truy cập: {response.status_code}")
            return None
        
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Tìm vùng kết quả
        result_box = (soup.find('div', class_='result') or 
                     soup.find('div', class_='box_kqtt_hp') or 
                     soup)

        # Lấy thông tin kỳ quay
        meta_info = result_box.find('h5')
        if meta_info:
            meta_text = meta_info.get_text(separator=" ").strip()
            parts = meta_text.split('|')
            draw_id = parts[0].replace("Kỳ quay số:", "").replace("#", "").strip()
            draw_date = parts[1].replace("Ngày quay thưởng:", "").strip() if len(parts) > 1 else ""
        else:
            draw_id = "Không rõ"
            draw_date = datetime.now().strftime("%d/%m/%Y")

        # Lấy các số
        numbers = []
        ball_spans = result_box.find_all('span', class_='wh_cuc_tuyet') 
        if not ball_spans:
            ball_spans = result_box.select('.day_so_ket_qua span, .ball, span[class*="ball"]')

        for span in ball_spans:
            num_txt = span.get_text().strip()
            if num_txt.isdigit():
                numbers.append(int(num_txt))

        if len(numbers) >= 6:
            main_numbers = sorted(numbers[:6])
            bonus_number = numbers[6] if len(numbers) > 6 else None
        else:
            print("Không parse được bộ số. Cấu trúc trang có thể đã thay đổi.")
            return None

        output = {
            "draw_id": draw_id,
            "date": draw_date,
            "numbers": main_numbers,
            "bonus": bonus_number,
            "scraped_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        
        print(f"✅ Crawled successfully: Kỳ {draw_id}")
        return output

    except Exception as e:
        print(f"❌ Lỗi khi cào dữ liệu: {e}")
        return None


def save_data(new_record):
    # === LƯU JSON ===
    json_path = '655.json'
    existing_data = []
    
    if os.path.exists(json_path):
        try:
            with open(json_path, 'r', encoding='utf-8') as f:
                existing_data = json.load(f)
        except:
            existing_data = []

    # Chỉ thêm nếu chưa có kỳ này
    if not any(item.get('draw_id') == new_record['draw_id'] for item in existing_data):
        existing_data.insert(0, new_record)
        with open(json_path, 'w', encoding='utf-8') as f:
            json.dump(existing_data, f, ensure_ascii=False, indent=4)
        print(f"💾 Đã lưu JSON: {json_path}")

    # === LƯU CSV (tùy chọn) ===
    csv_path = '655.csv'
    file_exists = os.path.exists(csv_path)
    
    try:
        with open(csv_path, 'a', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            if not file_exists:
                writer.writerow(['Kỳ quay', 'Ngày', 'Số 1', 'Số 2', 'Số 3', 'Số 4', 'Số 5', 'Số 6', 'Số Bonus', 'Cập nhật'])
            
            writer.writerow([
                new_record['draw_id'], 
                new_record['date'],
                *new_record['numbers'], 
                new_record['bonus'], 
                new_record['scraped_at']
            ])
        print(f"💾 Đã lưu CSV: {csv_path}")
    except Exception as e:
        print(f"⚠️ Lỗi khi lưu CSV: {e}")


if __name__ == "__main__":
    result = scrape_power_655()
    if result:
        save_data(result)
        print("🎉 Hoàn tất cào dữ liệu!")
    else:
        print("❌ Không lấy được dữ liệu.")
