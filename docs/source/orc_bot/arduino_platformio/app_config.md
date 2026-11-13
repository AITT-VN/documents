# Cấu hình AppConfig.h

File `include/AppConfig.h` chứa tất cả các tham số cấu hình robot. Đây là nơi duy nhất bạn cần chỉnh sửa để thiết lập robot theo phần cứng thực tế.

## Địa chỉ I2C

```cpp
constexpr uint8_t MOTOR_DRIVER_ADDR = 0x54;  // Motor Driver V2
constexpr uint8_t PS4_RECEIVER_ADDR = 0x55;  // Bộ thu PS4
constexpr uint8_t LINE_SENSOR_ADDR  = 0x23;  // Cảm biến dò line
```

Các địa chỉ này phải khớp với phần cứng thực tế. Khi khởi động, chương trình sẽ tự quét I2C bus và in ra các thiết bị tìm thấy.

## Đảo chiều động cơ

```cpp
constexpr bool MOTOR_1_REVERSED = false;
constexpr bool MOTOR_2_REVERSED = true;
constexpr bool MOTOR_3_REVERSED = true;
constexpr bool MOTOR_4_REVERSED = true;
constexpr bool MOTOR_5_REVERSED = false;
```

Nếu động cơ chạy ngược chiều mong muốn, chuyển giá trị từ `false` → `true` hoặc ngược lại. Motor 1-4 là 4 bánh lái, Motor 5 là động cơ phụ (ví dụ: cơ cấu gắp).

## Công tắc tính năng (Feature Flags)

```cpp
constexpr bool ENABLE_PS4_RECEIVER    = true;   // Bật/tắt tay cầm PS4
constexpr bool ENABLE_IMU             = true;   // Bật/tắt cảm biến góc MPU6050
constexpr bool ENABLE_LINE_SENSOR     = false;  // Bật/tắt cảm biến dò line
constexpr bool ENABLE_AUTONOMOUS_DEMO = false;  // Bật/tắt demo tự động
constexpr bool USE_GYRO_FOR_TURNS     = true;   // Dùng gyro khi quay
constexpr bool ENABLE_SERVOS          = true;   // Bật/tắt servo
```

### Chế độ hoạt động

| Cấu hình | Kết quả |
|-----------|---------|
| `ENABLE_PS4_RECEIVER = true` | Robot ở chế độ **điều khiển từ xa** bằng tay cầm PS4 |
| `ENABLE_PS4_RECEIVER = false`, `ENABLE_AUTONOMOUS_DEMO = true` | Robot chạy **demo di chuyển tự động** |
| Cả hai đều `false` | Robot đứng im, bạn tự viết logic |

## Thông số vật lý robot

```cpp
constexpr float DEFAULT_SPEED     = 80.0f;   // Tốc độ mặc định (%)
constexpr float DEFAULT_MIN_SPEED = 40.0f;   // Tốc độ tối thiểu (%)
constexpr float WHEEL_DIAMETER_MM = 80.0f;   // Đường kính bánh (mm)
constexpr float ROBOT_WIDTH_MM    = 300.0f;  // Khoảng cách giữa 2 bánh (mm)
```

## Thông số Encoder

```cpp
constexpr float    ENCODER_RPM   = 350.0f;  // Tốc độ vòng quay tối đa
constexpr uint16_t ENCODER_PPR   = 11;      // Xung mỗi vòng
constexpr uint16_t ENCODER_GEARS = 34;      // Tỷ số truyền bánh răng
```

## Thông số Servo

```cpp
constexpr int SERVO_1_MIN_LIMIT = 0;
constexpr int SERVO_1_MAX_LIMIT = 180;
constexpr int SERVO_2_MIN_LIMIT = 0;
constexpr int SERVO_2_MAX_LIMIT = 80;
constexpr int SERVO_SPEED       = 100;
constexpr int SERVO_STEP        = 5;    // Bước nhỏ khi tinh chỉnh bằng nút gamepad
```

### Ánh xạ nút tay cầm → servo

| Nút | Hành động |
|-----|-----------|
| **L1** | Servo 1 → góc 180° |
| **L2** | Servo 1 → góc 0° |
| **R1** | Servo 2 → góc 80° |
| **R2** | Servo 2 → góc 0° |
| **△** | Servo 1 tăng 5° |
| **✕** | Servo 1 giảm 5° |
| **□** | Servo 2 tăng 5° |
| **○** | Servo 2 giảm 5° |
