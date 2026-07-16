// Thay 'username' và 'repo' bằng thông tin GitHub thực tế của bạn
// const DATA_URL = 'https://raw.githubusercontent.com/username/repo/main/data/power655.json';
const DATA_URL = 'https://raw.githubusercontent.com/nghiatek/lott/main/655.json';

async function loadVietlottData() {
    try {
        const response = await fetch(DATA_URL);
        const data = await response.json();
        
        const container = document.getElementById('vietlott-app');
        container.innerHTML = ''; // Xóa dòng "Đang tải..."

        // Hiển thị 5 kỳ quay gần nhất
        data.slice(0, 5).forEach(item => {
            const row = document.createElement('div');
            row.className = 'row';
            
            let ballsHtml = item.numbers.map(num => `<span class="ball">${num}</span>`).join('');
            if (item.bonus) {
                ballsHtml += `<span class="ball bonus">${item.bonus}</span>`;
            }

            row.innerHTML = `
                <h3>Kỳ quay: #${item.draw_id} - Ngày: ${item.date}</h3>
                <div>${ballsHtml}</div>
                <small style="color: gray">Cập nhật lúc: ${item.updated_at}</small>
            `;
            container.appendChild(row);
        });
    } catch (error) {
        document.getElementById('vietlott-app').innerText = 'Lỗi khi tải dữ liệu!';
        console.error(error);
    }
}

document.addEventListener('DOMContentLoaded', loadVietlottData);
                          
