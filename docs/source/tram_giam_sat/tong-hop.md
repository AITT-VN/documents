# 8. Tổng hợp trạm giám sát hoàn chỉnh

## 1. Mục tiêu

Trong bài này, chúng ta sẽ **tổng hợp tất cả các cảm biến** đã học để xây dựng một **trạm giám sát thành phố thông minh hoàn chỉnh**. Trạm sẽ thu thập đồng thời nhiều thông số môi trường, hiển thị trên màn hình LCD và gửi dữ liệu lên **OhStem IoT** để theo dõi từ xa.

![Trạm giám sát thành phố thông minh](/wiki-assets/images/yolo_uno/tram_giam_sat/images/smart_city1.jpg)


## 2. Tổng quan hệ thống

### Danh sách cảm biến sử dụng

| STT | Cảm biến | Chức năng | Chân kết nối |
|-----|----------|-----------|-------------|
| 1 | DHT20 | Nhiệt độ & Độ ẩm | I2C2 |
| 2 | ACD1100 | Nồng độ CO2 | I2C |
| 3 | Cảm biến âm thanh | Cường độ tiếng ồn | A0 |
| 4 | Cảm biến ánh sáng | Cường độ ánh sáng | A1 |
| 5 | Cảm biến tốc độ gió | Tốc độ gió | A2 |
| 6 | GUVA-S12SD | Chỉ số UV | A3 |
| 7 | Màn hình LCD 1602 | Hiển thị dữ liệu | I2C1 |


## 3. Kết nối tổng hợp

| Cổng Yolo UNO | Thiết bị | Ghi chú |
|---------------|----------|---------|
| I2C1 | Màn hình LCD 1602 | Màn hình hiển thị |
| I2C2 | DHT20 | Cảm biến nhiệt độ & độ ẩm |
| I2C | ACD1100 | Cảm biến CO2 |
| A0 | Cảm biến âm thanh | Tín hiệu analog |
| A1 | Cảm biến ánh sáng | Tín hiệu analog |
| A2 | Cảm biến tốc độ gió | Tín hiệu analog |
| A3 | GUVA-S12SD | Tín hiệu UV analog |


## 4. Viết chương trình tổng hợp

### Phần 1: Khởi động (khi Yolo UNO bắt đầu)

Khi khởi động, Yolo UNO sẽ kết nối WiFi và đăng nhập OhStem IoT, sau đó hiển thị màn hình chào:

![Khối lệnh khởi động](/wiki-assets/images/yolo_uno/tram_giam_sat/images/code1.png)

> **Giải thích:** Đèn đỏ báo hiệu đang kết nối WiFi. Khi đèn chuyển xanh, trạm đã sẵn sàng hoạt động.

---

### Phần 2: Gửi dữ liệu lên OhStem IoT (mỗi 10 giây)

Sau mỗi 10 giây, trạm sẽ đọc tất cả cảm biến và gửi lên 7 kênh IoT:

![Khối lệnh gửi dữ liệu IoT](/wiki-assets/images/yolo_uno/tram_giam_sat/images/code2.png)

**Bảng kênh IoT:**

| Kênh | Dữ liệu | Đơn vị |
|------|---------|--------|
| V1 | Nhiệt độ (DHT20) | °C |
| V2 | Độ ẩm (DHT20) | % |
| V3 | Nồng độ CO2 | ppm |
| V4 | Cường độ tiếng ồn | dB |
| V5 | Tốc độ gió | m/s |
| V6 | Chỉ số UV | — |
| V7 | Cường độ ánh sáng | % |

---

### Phần 3: Hiển thị trên màn hình LCD (mỗi 8 giây)

Màn hình LCD hiển thị luân phiên 3 trang, mỗi trang 2 giây:

**Trang 1 — Nhiệt độ & Âm thanh:**

![LCD Trang 1 - Nhiệt độ và Âm thanh](/wiki-assets/images/yolo_uno/tram_giam_sat/images/code3.png)

**Trang 2 — Độ ẩm, UV & CO2:**

![LCD Trang 2 - Độ ẩm, UV và CO2](/wiki-assets/images/yolo_uno/tram_giam_sat/images/code4.png)

**Trang 3 — Ánh sáng & Gió:**

![LCD Trang 3 - Ánh sáng và Gió](/wiki-assets/images/yolo_uno/tram_giam_sat/images/code5.png)

Toàn bộ khối lệnh hiển thị LCD (mỗi 8 giây):

![Khối lệnh hiển thị LCD 8 giây](/wiki-assets/images/yolo_uno/tram_giam_sat/images/code6.png)


## 5. Chương trình mẫu

Link chương trình mẫu: [Tại đây](https://app.ohstem.vn/#!/share/yolouno/3HDgYJkNBYScuesnObwpRRRU4Mg)


## 6. Bảng ngưỡng cảnh báo

| Thông số | Bình thường 🟢 | Cần chú ý 🟡 | Nguy hiểm 🔴 |
|----------|--------------|-------------|-------------|
| Nhiệt độ | 18–32°C | 32–38°C | > 38°C |
| Độ ẩm | 40–70% | 70–85% | > 85% |
| CO2 | < 800 ppm | 800–1500 ppm | > 1500 ppm |
| Tiếng ồn | < 60 dB | 60–85 dB | > 85 dB |
| UV Index | 0–5 | 6–7 | > 8 |
| Tốc độ gió | < 5.5 m/s | 5.5–10.7 m/s | > 10.8 m/s |
| Ánh sáng | 30–80% | < 30% | — |


## 7. Theo dõi dữ liệu từ xa

Sau khi nạp chương trình, mở **OhStem IoT Dashboard** để theo dõi biểu đồ dữ liệu thời gian thực từ tất cả 7 kênh V1–V7. Khi có thông số vượt ngưỡng, hệ thống sẽ ghi nhận sự kiện trên dashboard để cảnh báo người quản lý.

Link bảng IoT mẫu: [Tại đây](https://app.ohstem.vn/#!/share/iot-panels/3HDiQrA54zjBXHNTfFZMrv20yZU)

> **Chúc mừng!** Bạn đã hoàn thành việc xây dựng một trạm giám sát thành phố thông minh hoàn chỉnh với Yolo UNO! Trạm có thể thu thập 6 thông số môi trường quan trọng và gửi dữ liệu lên đám mây để theo dõi từ xa.
