# Cấu hình project PlatformIO

## File platformio.ini

Đây là file cấu hình chính của PlatformIO, định nghĩa board, framework và các tùy chọn build:

```ini
[env:yolo_uno]
platform = espressif32
board = yolo_uno
framework = arduino
monitor_speed = 115200

build_flags =
    -D ARDUINO_USB_MODE=1
    ; Yolo Uno sử dụng native USB CDC cho Serial logging
    -D ARDUINO_USB_CDC_ON_BOOT=1

lib_deps =
    madhephaestus/ESP32Servo @ ^3.0.8
```

### Giải thích

| Tham số | Ý nghĩa |
|---------|---------|
| `platform = espressif32` | Nền tảng ESP32 |
| `board = yolo_uno` | Board definition tùy chỉnh (trong folder `boards/`) |
| `framework = arduino` | Dùng Arduino framework |
| `monitor_speed = 115200` | Tốc độ Serial Monitor |
| `ARDUINO_USB_MODE=1` | Chế độ USB |
| `ARDUINO_USB_CDC_ON_BOOT=1` | Bật native USB CDC cho Serial ngay khi khởi động |

## Board Definition — yolo_uno.json

File `boards/yolo_uno.json` định nghĩa board Yolo UNO tùy chỉnh cho PlatformIO. Board này dựa trên chip **ESP32-S3** với các thông số:

- Flash: 8MB
- PSRAM: Hỗ trợ
- USB: Native USB CDC
- Tần số: 240MHz

## Pin Mapping — pins_arduino.h

File `variants/yolo_uno/pins_arduino.h` định nghĩa các chân mặc định:

- **I2C**: `SDA` và `SCL` được cấu hình sẵn, có thể dùng `Wire.begin()` trực tiếp
- **Serial**: Sử dụng native USB CDC, không cần chuyển đổi UART

## Build và Upload

1. Nhấn nút **Build** (✓) trên thanh dưới cùng hoặc `Ctrl + Alt + B`
2. Nhấn nút **Upload** (→) hoặc `Ctrl + Alt + U` để nạp firmware
3. Nhấn nút **Serial Monitor** (🔌) hoặc `Ctrl + Alt + S` để xem log

> **Lưu ý**: Khi upload lần đầu cho Yolo UNO, có thể cần giữ nút **BOOT** trên board rồi nhấn **RESET** để vào chế độ upload.
