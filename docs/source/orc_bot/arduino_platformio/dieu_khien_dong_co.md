# Điều khiển động cơ DC

## Khởi tạo

Thư viện sử dụng **MotorDriverV2** để giao tiếp với ORC Hub qua I2C:

```cpp
#include <OhStemRobotics.h>
using namespace ohstem::robotics;

// Khởi tạo Motor Driver
MotorDriverV2 mdV2(Wire, MOTOR_DRIVER_ADDR);  // 0x54

// Khởi tạo từng motor
DCMotor motor1(mdV2, M1, false);   // Motor 1, không đảo chiều
DCMotor motor2(mdV2, M2, true);    // Motor 2, đảo chiều
DCMotor motor3(mdV2, E1, true);    // Motor 3 (cổng encoder E1)
DCMotor motor4(mdV2, E2, true);    // Motor 4 (cổng encoder E2)
DCMotor motor5(mdV2, M3, false);   // Motor phụ
```

## Điều khiển motor đơn lẻ

```cpp
// Chạy motor ở tốc độ 80% (giá trị từ -100 đến 100)
motor1.run(80);

// Chạy ngược
motor1.run(-80);

// Dừng motor
motor1.stop();
```

## Sử dụng DriveBase

**DriveBase** cho phép điều khiển cả 4 bánh cùng lúc với chế độ lái Mecanum:

```cpp
// Khởi tạo DriveBase chế độ Mecanum
DriveBase robot(MODE_MECANUM, &motor1, &motor2, &motor3, &motor4);

// Cấu hình kích thước robot
robot.size(80.0, 300.0);    // Đường kính bánh 80mm, rộng 300mm
robot.speed(80.0, 40.0);    // Tốc độ mặc định 80%, tối thiểu 40%
```

## Các lệnh di chuyển

```cpp
// Di chuyển theo thời gian
robot.forwardFor(1.2, SECOND, BRAKE);    // Tiến 1.2 giây rồi phanh
robot.backwardFor(1.2, SECOND, BRAKE);   // Lùi 1.2 giây
robot.turnLeftFor(0.8, SECOND, BRAKE);   // Quay trái 0.8 giây
robot.turnRightFor(0.8, SECOND, BRAKE);  // Quay phải 0.8 giây

// Dừng
robot.stop();
```

## Sử dụng Encoder

Để di chuyển chính xác theo khoảng cách, cần thiết lập encoder:

```cpp
// Cấu hình encoder cho motor 3 và 4
motor3.setEncoder(350.0, 11, 34);  // RPM=350, PPR=11, Gear=34
motor4.setEncoder(350.0, 11, 34);
```

Sau khi cấu hình encoder, DriveBase có thể sử dụng các lệnh di chuyển theo khoảng cách (nếu thư viện hỗ trợ).

## Ví dụ hoàn chỉnh — Demo di chuyển tự động

```cpp
void runAutonomousDemo() {
    Serial.println("Move: forward");
    robot.forwardFor(1.2f, SECOND, BRAKE);
    delay(600);

    Serial.println("Move: backward");
    robot.backwardFor(1.2f, SECOND, BRAKE);
    delay(600);

    Serial.println("Move: turn left");
    robot.turnLeftFor(0.8f, SECOND, BRAKE);
    delay(600);

    Serial.println("Move: turn right");
    robot.turnRightFor(0.8f, SECOND, BRAKE);
    delay(1000);
}
```

Để chạy demo này, đặt trong `AppConfig.h`:

```cpp
constexpr bool ENABLE_PS4_RECEIVER    = false;
constexpr bool ENABLE_AUTONOMOUS_DEMO = true;
```
