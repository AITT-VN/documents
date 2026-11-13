# Điều khiển bằng tay cầm PS4

## Giới thiệu

Robot ORC hỗ trợ điều khiển từ xa qua **tay cầm PS4 không dây** thông qua bộ thu PS4 I2C (địa chỉ `0x55`).

## Khởi tạo

```cpp
#include <OhStemRobotics.h>
using namespace ohstem::robotics;

// Khởi tạo bộ thu PS4
PS4GamepadReceiver ps4Receiver(Wire, 0x55);
Gamepad gamepad(&ps4Receiver);
```

## Bật chế độ Teleop

Trong `AppConfig.h`, đặt:

```cpp
constexpr bool ENABLE_PS4_RECEIVER = true;
```

Code khởi tạo:

```cpp
bool ps4ReceiverReady = ps4Receiver.begin();
gamepad.attachReceiver(ps4ReceiverReady ? &ps4Receiver : nullptr);

// Chuyển robot sang chế độ điều khiển từ xa
robot.setAutoMode(false);
robot.setSideMoveMode(JOYSTICK);
```

## Sơ đồ điều khiển

### Joystick trái — Di chuyển robot

| Hướng joystick | Hành động |
|----------------|-----------|
| Đẩy lên | Tiến |
| Kéo xuống | Lùi |
| Nghiêng trái | Di chuyển ngang trái (Mecanum) |
| Nghiêng phải | Di chuyển ngang phải (Mecanum) |
| Xoay | Quay trái / phải |

### Joystick phải — Động cơ phụ

| Hướng | Hành động |
|-------|-----------|
| Sang trái (X < -50) | Motor 5 chạy ngược |
| Sang phải (X > 50) | Motor 5 chạy thuận |
| Trung tâm | Motor 5 dừng |
| Nhấn ThumbR | Motor 5 dừng ngay |

### Nút bấm — Servo

| Nút | Hành động |
|-----|-----------|
| **L1** | Servo 1 → 180° (mở) |
| **L2** | Servo 1 → 0° (đóng) |
| **R1** | Servo 2 → 80° (mở) |
| **R2** | Servo 2 → 0° (đóng) |
| **△** | Servo 1 tăng 5° |
| **✕** | Servo 1 giảm 5° |
| **□** | Servo 2 tăng 5° |
| **○** | Servo 2 giảm 5° |

## Vòng lặp chính (Teleop Loop)

```cpp
void updateGamepadTeleop() {
    // Đọc dữ liệu từ bộ thu
    if (ps4ReceiverReady) {
        gamepad.update();
    }

    // Cập nhật lái robot theo joystick
    robot.updateTeleop(gamepad.state(), TELEOP_ACCEL_STEPS);

    // Cập nhật servo và motor phụ
    updateExtraGamepadActions();

    delay(10);
}
```

## Cấu hình gia tốc

```cpp
constexpr uint8_t TELEOP_ACCEL_STEPS = 3;
```

Giá trị `TELEOP_ACCEL_STEPS` quyết định số bước tăng/giảm tốc. Giá trị nhỏ → phản hồi nhanh hơn, giá trị lớn → chuyển động mượt hơn.

## Lưu ý

- Nếu bộ thu PS4 không được phát hiện khi khởi động, chương trình vẫn chạy bình thường nhưng sẽ in cảnh báo `"Gamepad receiver not found"`.
- Serial Monitor hiển thị trạng thái kết nối gamepad mỗi giây (`GAMEPAD_STATUS_REPORT_MS = 1000`).
- Nếu không dùng bộ thu I2C, có thể dùng BLE/app để gửi trạng thái gamepad trực tiếp.
