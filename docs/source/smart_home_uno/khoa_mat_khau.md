# 4. Khóa mật khẩu

## 1. Mục tiêu
Với hướng dẫn này, chúng ta thực hiện tính năng mở khóa cửa bằng mật khẩu, sử dụng bàn phím keypad4x3.

## 2. Thiết bị cần sử dụng
- Mạch Yolo UNO:
![yolo uno](/wiki-assets/images/yolo_uno/smart_home_uno/images/yolo_uno.png)


- Bàn phím cảm ứng diện dung
![keypad01](/wiki-assets/images/yolo_uno/smart_home_uno/images/keypad01.png)


- Động cơ servo:
![servo01](/wiki-assets/images/yolo_uno/smart_home_uno/images/servo01.png)


- Màn hình LCD:
![lcd 1602](/wiki-assets/images/yolo_uno/smart_home_uno/images/lcd_1602.png)


## 3. Kết nối phần cứng
- Kết nối bàn phím cảm ứng ở cổng I2C.

- Kết nối động cơ servo vào chân D2.

- Kết nối màn hình LCd vào cổng I2C.
![keypad02](/wiki-assets/images/yolo_uno/smart_home_uno/images/keypad02.png)


## 4. Chương trình lập trình
- **Giới thiệu khối lệnh:**
![keypad03](/wiki-assets/images/yolo_uno/smart_home_uno/images/keypad03.png)


*Các câu lệnh sử dụng cho tính năng mở mật khẩu*
![keypad04](/wiki-assets/images/yolo_uno/smart_home_uno/images/keypad04.png)


*Câu lệnh kiểm tra phím được nhấn*
![keypad05](/wiki-assets/images/yolo_uno/smart_home_uno/images/keypad05.png)


*Câu lệnh kiểm tra các phím đã được nhấn*
![keypad06](/wiki-assets/images/yolo_uno/smart_home_uno/images/keypad06.png)


*Câu lệnh xóa các phím đã được nhấn*

Với hình kết nối trên, động cơ servo chân D2 gắn với cánh cửa để làm cửa tự động ra vào.
- **Chương trình lập trình:**
![keypad07](/wiki-assets/images/yolo_uno/smart_home_uno/images/keypad07.png)
