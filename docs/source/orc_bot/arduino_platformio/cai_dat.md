# Cài đặt môi trường lập trình

## Bước 1: Cài đặt VS Code

Tải và cài đặt **Visual Studio Code** từ trang chính thức:

👉 [https://code.visualstudio.com](https://code.visualstudio.com)

## Bước 2: Cài đặt PlatformIO Extension

1. Mở VS Code
2. Bấm tổ hợp phím `Ctrl + Shift + X` để mở **Extensions**
3. Tìm kiếm **"PlatformIO IDE"**
4. Nhấn **Install** và đợi cài đặt hoàn tất
5. Khởi động lại VS Code sau khi cài xong

## Bước 3: Clone project mẫu

Mở Terminal trong VS Code (`Ctrl + ~`) và chạy lệnh:

```bash
git clone https://github.com/AITT-VN/orc_hub_arduino_examples.git
```

Hoặc tải trực tiếp file ZIP từ GitHub:

👉 [Tải ZIP](https://github.com/AITT-VN/orc_hub_arduino_examples/archive/refs/heads/main.zip)

## Bước 4: Mở project

1. Trong VS Code, vào **File → Open Folder**
2. Chọn thư mục `orc_hub_arduino_examples` vừa clone/giải nén
3. PlatformIO sẽ tự nhận diện project và cài đặt các dependency cần thiết

## Bước 5: Kiểm tra kết nối

1. Cắm Yolo UNO vào máy tính qua cáp **USB-C**
2. Trên thanh dưới cùng của VS Code, kiểm tra xem PlatformIO đã nhận cổng COM chưa
3. Nếu chưa nhận, cần cài thêm driver USB cho ESP32-S3

## Cấu trúc thư mục project

```
orc_hub_arduino_examples/
├── boards/
│   └── yolo_uno.json          # Board definition cho Yolo UNO
├── include/
│   └── AppConfig.h            # Cấu hình robot (địa chỉ, tốc độ, feature flags)
├── lib/
│   └── OhStemRobotics/        # Thư viện điều khiển robot
│       └── examples/          # Các ví dụ mẫu
├── src/
│   └── main.cpp               # Chương trình chính
├── variants/
│   └── yolo_uno/
│       └── pins_arduino.h     # Map chân mặc định
└── platformio.ini             # Cấu hình PlatformIO
```

Tiếp theo, hãy tìm hiểu cấu hình project PlatformIO.
