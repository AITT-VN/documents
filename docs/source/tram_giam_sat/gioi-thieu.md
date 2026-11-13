# 1. Giới thiệu trạm giám sát thành phố thông minh

## Giới thiệu

Trạm giám sát thành phố thông minh là một dự án STEM ứng dụng thực tế, mô phỏng hệ thống giám sát môi trường đô thị hiện đại. Dự án sử dụng bo mạch **Yolo UNO** kết hợp với nhiều loại cảm biến chuyên dụng để thu thập và phân tích các thông số môi trường quan trọng trong thành phố.

![Tổng quan trạm giám sát thành phố thông minh](/wiki-assets/images/yolo_uno/tram_giam_sat/images/smart_city1.jpg)

Với trạm giám sát này, học sinh sẽ được tìm hiểu cách các thành phố thông minh trên thế giới sử dụng công nghệ IoT (Internet of Things) để theo dõi và quản lý chất lượng môi trường sống, từ đó đưa ra các cảnh báo kịp thời cho người dân.


## Tại sao cần trạm giám sát thành phố thông minh?

Trong cuộc sống hiện đại, các thành phố phải đối mặt với nhiều vấn đề môi trường:

- **Ô nhiễm không khí:** Khí CO2 từ giao thông và công nghiệp ảnh hưởng nghiêm trọng đến sức khỏe người dân.
- **Biến đổi khí hậu:** Nhiệt độ tăng cao, độ ẩm thay đổi, thời tiết cực đoan ngày càng phổ biến.
- **Tia UV nguy hại:** Bức xạ tia cực tím mạnh gây hại cho da và sức khỏe con người.
- **Ô nhiễm tiếng ồn:** Tiếng ồn từ giao thông và hoạt động đô thị ảnh hưởng đến chất lượng sống.

Trạm giám sát thành phố thông minh giúp thu thập dữ liệu liên tục, từ đó:
- Cảnh báo khi chất lượng không khí xuống thấp
- Theo dõi chỉ số UV để bảo vệ sức khỏe
- Giám sát cường độ tiếng ồn môi trường
- Gửi dữ liệu lên OhStem IoT để theo dõi từ xa


## Các tính năng nổi bật

Dự án hướng dẫn xây dựng một trạm giám sát hoàn chỉnh với các chức năng sau:

1. **Đo áp suất khí quyển & nhiệt độ (BMP280):** Theo dõi áp suất không khí và nhiệt độ môi trường.
2. **Đo nhiệt độ & độ ẩm (DHT20):** Cảm biến I2C chính xác cho nhiệt độ và độ ẩm không khí.
3. **Đo cường độ tia UV (GUVA-S12SD):** Giám sát bức xạ tia cực tím, cảnh báo khi mức UV nguy hiểm.
4. **Đo nồng độ CO2 (ACD1100):** Theo dõi chất lượng không khí thông qua nồng độ khí carbon dioxide.
5. **Đo tốc độ gió:** Tính toán tốc độ gió bằng cảm biến analog.
6. **Đo cường độ tiếng ồn:** Phát hiện mức độ ô nhiễm tiếng ồn trong môi trường đô thị.
7. **Đo cường độ ánh sáng:** Theo dõi mức độ chiếu sáng tự nhiên.


## Thành phần cần chuẩn bị

### Mạch điều khiển

| STT | Tên linh kiện | Số lượng | Mô tả |
|-----|---------------|----------|-------|
| 1 | Yolo UNO | 1 | Bo mạch điều khiển chính |

### Các cảm biến

| STT | Tên cảm biến | Chân kết nối | Chức năng |
|-----|--------------|-------------|-----------|
| 1 | DHT20 | I2C2 | Đo nhiệt độ & độ ẩm không khí |
| 2 | ACD1100 | I2C | Đo nồng độ CO2 |
| 3 | Cảm biến âm thanh | A0 | Đo cường độ tiếng ồn |
| 4 | Cảm biến ánh sáng | A1 | Đo cường độ ánh sáng |
| 5 | Cảm biến tốc độ gió | A2 | Đo vận tốc gió |
| 6 | GUVA-S12SD | A3 | Đo cường độ tia UV |
| 7 | Màn hình LCD 1602 | I2C1 | Hiển thị thông số môi trường |


## Sơ đồ kết nối tổng quan

Các cảm biến được kết nối với Yolo UNO như sau:

| Cảm biến | Giao tiếp | Chân trên Yolo UNO |
|----------|-----------|-------------------|
| DHT20 | I2C | I2C2 |
| ACD1100 (CO2) | I2C | I2C |
| Màn hình LCD 1602 | I2C | I2C1 |
| Cảm biến âm thanh | Analog | A0 |
| Cảm biến ánh sáng | Analog | A1 |
| Cảm biến tốc độ gió | Analog | A2 |
| GUVA-S12SD (UV) | Analog | A3 |


## Hướng dẫn lắp ráp



[Hướng dẫn lắp ráp Trạm quan trắc thông minh](https://app.ohstem.vn/#!/aib/view/cloud/asmad45r/)




## Phần mềm lập trình

Dự án sử dụng phần mềm **OhStem App** với phương pháp lập trình kéo thả trực quan:

- **Truy cập:** [https://app.ohstem.vn](https://app.ohstem.vn)
- **Chọn thiết bị:** Yolo UNO
- **Thư viện mở rộng cần tải:**
    Vào mục **Mở rộng** → **Tải từ đường dẫn** và nhập: **https://github.com/AITT-VN/yolouno_extension_smartcity.git**
      ![minh họa tải thư viện](/wiki-assets/images/yolo_uno/yolo_uno_khoi_lenh/cam_bien/images/acd1100_04.png)

Hãy cùng bắt đầu xây dựng trạm giám sát thành phố thông minh nhé!
