# NYC 311 | Phân tích yêu cầu ở Queens

Notebook tiếng Việt dùng Python và pandas. Phạm vi tháng 1/2025, mốc chốt đầu ngày 01/03/2025. Kết quả lưu sẵn dùng 600 dòng mô phỏng.

Mở terminal trong thư mục này rồi chạy:

```text
python -m pip install -r requirements.txt
python -m notebook 01_nyc311.ipynb
```

Chọn **Run All**. Đọc lần lượt phần kiểm tra dữ liệu, cách xác định hồ sơ đã đóng và còn mở, rồi hai bảng và biểu đồ so sánh.

Để chạy bằng dữ liệu thật, dùng `python download.py` hoặc xuất CSV từ NYC Open Data với bộ lọc Queens, ngày tạo từ 01/01/2025 đến trước 01/02/2025. Đặt file tại `data/queens-2025-01.csv`. Notebook tự ưu tiên file này. Nếu tải gặp 403, dùng chức năng xuất dữ liệu của cổng NYC Open Data khi truy cập được.

[Nguồn NYC Open Data](https://data.cityofnewyork.us/Social-Services/311-Service-Requests-from-2020-to-Present/erm2-nwe9/data_preview)
