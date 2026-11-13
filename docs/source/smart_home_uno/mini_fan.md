# 5. Quạt thông minh

## 1. Mục tiêu
Tiếp theo, chúng ta sẽ cùng nâng cấp dự án lên 1 cấp độ phức tạp hơn, kết hợp cảm biến DHT20 với màn hình LCD và quạt mini. Thực hiện dự án **Quạt thông minh**, tự hoạt động dựa vào nhiệt độ của môi trường.

Cụ thể, hệ thống sẽ hoạt động bằng cách kiểm tra dựa vào nhiệt độ mà cảm biến DHT20 gửi về **sau mỗi 5 giây**:

- Thông tin nhiệt độ và độ ẩm của không khí được hiển thị lên LCD

- Nếu nhiệt độ lớn hơn 27 độ thì quạt sẽ bật

- Nếu nhiệt độ nhỏ hơn 27 độ thì quạt sẽ tắt


## 2. Thiết bị cần sử dụng
- Mạch Yolo UNO:
![yolo uno](/wiki-assets/images/yolo_uno/smart_home_uno/images/yolo_uno.png)


- Module LCD kèm dây tín hiệu:
![lcd 1602](/wiki-assets/images/yolo_uno/smart_home_uno/images/lcd_1602.png)


- Cảm biến nhiệt độ độ ẩm DHT20 kèm dây tín hiệu:
![dht20](/wiki-assets/images/yolo_uno/smart_home_uno/images/dht20.png)


- Module quạt mini kèm dây tín hiệu:
![mini fan](/wiki-assets/images/yolo_uno/smart_home_uno/images/mini_fan.png)


## 3. Kết nối phần cứng
- cảm biến DHT20 và màn hình LCD kết nối vào cổng I2C1 và I2C2

- Module quạt kết nối vào cổng D7 - D8
![mini fan 1](/wiki-assets/images/yolo_uno/smart_home_uno/images/mini_fan_1.png)


## 4. Chương trình lập trình
- **Giới thiệu khối lệnh:**
![dht20 2](/wiki-assets/images/yolo_uno/smart_home_uno/images/dht20_2.png)


Câu lệnh bật tắt quạt với các mức độ khác nhau từ 0 đến 100 %.

- **Chương trình lập trình:**
![mini fan 3](/wiki-assets/images/yolo_uno/smart_home_uno/images/mini_fan_3.png)


    [https://app.ohstem.vn/#!/share/yolouno/2vFZQvYcoZE7M3kAeqt47cfxXhO](https://app.ohstem.vn/#!/share/yolouno/2vFZQvYcoZE7M3kAeqt47cfxXhO)
    
- **Giải thích chương trình:**  Sau mỗi 5 giây, thông tin nhiệt độ độ ẩm sẽ được cập nhật lên màn hình LCD1602 và nếu nhiệt độ lớn hơn 27 độ thì quạt sẽ bật.
