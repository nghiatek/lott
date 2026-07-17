import os
import json
import csv
import requests
from bs4 import BeautifulSoup
from datetime import datetime

# URL kết quả Power 6/55 (Ví dụ minh họa, bạn cần kiểm tra chính xác cấu trúc HTML của trang nguồn)
URL = "https://vietlott.vn/vi/trung-thuong/ket-qua-trung-thuong/655.html"

def crawl_vietlott():
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
    response = requests.get(URL, headers=headers)
    if response.status_code != 200:
        print("Không thể truy cập trang web")
        return None
        
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # ⚠️ Đoạn này cần inspect HTML thực tế của Vietlott để parse cho đúng class/id
    # Giả định cấu trúc lấy kỳ quay, ngày quay và bộ số:
    draw_id = soup.find(class_="ky-quay").text.strip()
    draw_date = soup.find(class_="ngay-quay").text.strip()
    
    numbers = []
    for ball in soup.find_all(class_="bi-so"):
        numbers.append(int(ball.text.strip()))
        
    # Tách số đặc biệt (nếu có cấu trúc riêng cho số thứ 7 của Power 6/55)
    # numbers = [s1, s2, s3, s4, s5, s6] và bonus_number = s7
    
    new_data = {
        "draw_id": draw_id,
        "date": draw_date,
        "numbers": numbers[:6],
        "bonus": numbers[6] if len(numbers) > 6 else None,
        "updated_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    return new_data

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
    csv_path = 'data/power655.csv'
    file_exists = os.path.exists(csv_path)
    
    if not any(item['draw_id'] == new_record['draw_id'] for item in existing_data[:-1]): # Nếu là bản ghi mới
        with open(csv_path, 'a', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            if not file_exists:
                writer.writerow(['Kỳ quay', 'Ngày', 'Số 1', 'Số 2', 'Số 3', 'Số 4', 'Số 5', 'Số 6', 'Số Bonus', 'Cập nhật'])
            writer.writerow([
                new_record['draw_id'], new_record['date'],
                *new_record['numbers'], new_record['bonus'], new_record['updated_at']
            ])

if __name__ == "__main__":
    os.makedirs('data', exist_ok=True)
    result = crawl_vietlott()
    if result:
        save_data(result)
        print("Cào dữ liệu thành công!")
        
