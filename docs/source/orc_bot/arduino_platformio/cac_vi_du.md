# Các ví dụ mở rộng

Thư viện OhStem Robotics đi kèm nhiều ví dụ mẫu trong thư mục `lib/OhStemRobotics/examples/`. Dưới đây là mô tả từng ví dụ:

## 1. BasicDrive — Di chuyển cơ bản

Ví dụ đơn giản nhất để kiểm tra robot hoạt động: tiến, lùi, quay trái, quay phải.

```cpp
robot.forwardFor(2.0, SECOND, BRAKE);
delay(500);
robot.backwardFor(2.0, SECOND, BRAKE);
delay(500);
robot.turnLeftFor(1.0, SECOND, BRAKE);
delay(500);
robot.turnRightFor(1.0, SECOND, BRAKE);
```

## 2. EncoderDistance — Di chuyển theo khoảng cách

Sử dụng encoder để đo khoảng cách di chuyển chính xác thay vì theo thời gian.

**Yêu cầu**: Motor 3 và Motor 4 phải có encoder.

## 3. MPU6050Heading — Đọc góc xoay

Sử dụng cảm biến IMU MPU6050 để đọc góc xoay (heading) của robot. Hữu ích cho các bài thi cần quay chính xác.

**Cấu hình**: `ENABLE_IMU = true` trong `AppConfig.h`.

## 4. GyroTurns — Quay chính xác bằng Gyro

Kết hợp IMU với DriveBase để quay robot đến một góc chính xác (ví dụ: quay 90° hoặc 180°).

**Cấu hình**: `USE_GYRO_FOR_TURNS = true`.

## 5. PreciseSquare — Đi hình vuông chính xác

Robot di chuyển theo hình vuông, sử dụng cả encoder (cho khoảng cách) và gyro (cho góc quay) để đạt độ chính xác cao.

## 6. LineFollower — Dò line

Robot dùng cảm biến dò line I2C (địa chỉ `0x23`) để bám theo đường kẻ đen trên nền trắng.

**Cấu hình**: `ENABLE_LINE_SENSOR = true`.

## 7. PS4Teleop — Điều khiển tay cầm

Chương trình điều khiển robot hoàn chỉnh bằng tay cầm PS4 với đầy đủ tính năng: lái Mecanum, servo, motor phụ.

Đây chính là chương trình demo chính trong `src/main.cpp`.

---

## Cách chạy một ví dụ

1. Mở file ví dụ trong folder `lib/OhStemRobotics/examples/`
2. Copy nội dung vào `src/main.cpp` (hoặc chỉnh `platformio.ini` để trỏ đến file ví dụ)
3. Build và Upload

## Tài nguyên bổ sung

- **GitHub**: [https://github.com/AITT-VN/orc_hub_arduino_examples](https://github.com/AITT-VN/orc_hub_arduino_examples)
- **Hỗ trợ**: Nếu gặp lỗi, liên hệ **support@ohstem.vn** hoặc đặt câu hỏi cho trợ lý AI trên wiki này.
