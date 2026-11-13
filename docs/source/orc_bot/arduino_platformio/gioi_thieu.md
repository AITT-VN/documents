# Giới thiệu

Thư viện **OhStem Robotics C++** là bản port sang C++ của runtime robotics OhStem, cho phép bạn lập trình robot ORC bằng ngôn ngữ C/C++ trên nền tảng **PlatformIO** thay vì dùng khối lệnh trực quan (block-based) trên OhStem App.

## Tại sao dùng PlatformIO / Arduino?

- **Hiệu suất cao hơn**: Chương trình chạy trực tiếp trên phần cứng, không qua thông dịch.
- **Linh hoạt**: Có thể kết hợp với bất kỳ thư viện Arduino nào.
- **Chuyên nghiệp**: Phù hợp cho các đội thi ORC muốn tùy chỉnh sâu hơn.
- **Debugging**: Hỗ trợ Serial Monitor, breakpoint, và nhiều công cụ debug khác.

## Các tính năng hỗ trợ

| Tính năng | Mô tả |
|-----------|-------|
| **Motor Driver V2** | Điều khiển tối đa 5 động cơ DC qua I2C (địa chỉ `0x54`) |
| **DriveBase** | Hỗ trợ chế độ lái Mecanum 4 bánh |
| **Servo** | Điều khiển 2 servo với giới hạn góc tùy chỉnh |
| **Encoder** | Đọc encoder để di chuyển chính xác theo khoảng cách |
| **IMU (MPU6050)** | Cảm biến góc xoay để quay chính xác |
| **PS4 Gamepad** | Điều khiển robot qua tay cầm PS4 không dây |
| **Line Sensor** | Cảm biến dò line (tùy chọn) |

## Phần cứng cần thiết

- **Yolo UNO** (ESP32-S3)
- **ORC Hub** (Motor Driver V2)
- **Động cơ DC** với encoder (tùy cấu hình)
- **Servo** (tùy chọn)
- **Tay cầm PS4** + bộ thu PS4 I2C (tùy chọn)
- Cáp USB-C để kết nối với máy tính

## Mã nguồn tham khảo

Toàn bộ source code và ví dụ mẫu được lưu trên GitHub:

👉 **[orc_hub_arduino_examples](https://github.com/AITT-VN/orc_hub_arduino_examples)**

Tiếp theo, hãy cài đặt môi trường lập trình PlatformIO.
