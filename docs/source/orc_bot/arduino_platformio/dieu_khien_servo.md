# Điều khiển Servo

## Khởi tạo

Servo được điều khiển qua ORC Hub (Motor Driver V2):

```cpp
#include <OhStemRobotics.h>
using namespace ohstem::robotics;

MotorDriverV2 mdV2(Wire, 0x54);

// Servo 1 trên cổng S1, góc tối đa 180°
ServoMotor servo1(mdV2, S1, 180);

// Servo 2 trên cổng S2, góc tối đa 180°
ServoMotor servo2(mdV2, S2, 180);
```

## Giới hạn góc quay

Để bảo vệ cơ cấu, nên đặt giới hạn góc:

```cpp
servo1.limit(0, 180);    // Servo 1: quay từ 0° đến 180°
servo2.limit(0, 80);     // Servo 2: quay từ 0° đến 80° (hạn chế)
```

## Xoay đến góc cố định

```cpp
// Xoay servo 1 đến góc 90° với tốc độ 100
servo1.runAngle(90, 100);

// Xoay servo 2 đến góc 45° với tốc độ 80
servo2.runAngle(45, 80);
```

## Đặt góc ngay lập tức

```cpp
// Đặt servo 1 về 0° ngay (không có tốc độ chuyển tiếp)
servo1.setAngle(0);

// Đặt servo 2 về 80°
servo2.setAngle(80);
```

## Xoay từng bước nhỏ

Tinh chỉnh servo theo từng bước nhỏ, phù hợp khi dùng nút gamepad:

```cpp
// Tăng 5°
servo1.runSteps(5, 100);

// Giảm 5°
servo1.runSteps(-5, 100);
```

## Ánh xạ nút gamepad → servo

Trong chương trình demo, các nút tay cầm PS4 được gán cho servo:

```cpp
// Nút L1 → Servo 1 mở (180°)
robot.onTeleopCommand(GamepadButton::L1, []() {
    servo1.runAngle(180, 100);
});

// Nút L2 → Servo 1 đóng (0°)
robot.onTeleopCommand(GamepadButton::L2, []() {
    servo1.runAngle(0, 100);
});

// Nút R1 → Servo 2 mở (80°)
robot.onTeleopCommand(GamepadButton::R1, []() {
    servo2.runAngle(80, 100);
});

// Nút R2 → Servo 2 đóng (0°)
robot.onTeleopCommand(GamepadButton::R2, []() {
    servo2.runAngle(0, 100);
});
```

Ngoài ra, các nút **△ ✕ □ ○** được dùng để tinh chỉnh servo theo từng bước 5°.
