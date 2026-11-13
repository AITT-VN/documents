# 4. Đo và hiển thị nhiệt độ & độ ẩm

## 1. Mục tiêu
Đọc thông số nhiệt độ và độ ẩm không khí từ cảm biến DHT20 và hiển thị lên màn hình LCD 1602.


## 2. Thiết bị cần sử dụng
- Mạch Yolo UNO:
![yolo uno](/wiki-assets/images/yolo_uno/smart_home_uno/images/yolo_uno.png)


- Module LCD kèm dây tín hiệu:
![lcd 1602](/wiki-assets/images/yolo_uno/smart_home_uno/images/lcd_1602.png)


- Cảm biến nhiệt độ độ ẩm DHT20 kèm dây tín hiệu:
![dht20](/wiki-assets/images/yolo_uno/smart_home_uno/images/dht20.png)


## 3. Kết nối phần cứng
- Kết nối cảm biến DHT20 vào cổng I2C1 của Yolo UNO

- Kết nối LCD vào cổng I2C2
![dht20 1](/wiki-assets/images/yolo_uno/smart_home_uno/images/dht20_1.png)


## 4. Chương trình lập trình
- Các khối lệnh để đọc thông số nhiệt độ hoặc độ ẩm của cảm biến DHT20, nằm trong mục **CẢM BIẾN**
![dht20 2](/wiki-assets/images/yolo_uno/smart_home_uno/images/dht20_2.png)


- **Chương trình lập trình:**
![dht20 3](/wiki-assets/images/yolo_uno/smart_home_uno/images/dht20_3.png)


    [https://app.ohstem.vn/#!/share/yolouno/2vFY26QwrHuFoL2nqydhVI7auVH](https://app.ohstem.vn/#!/share/yolouno/2vFY26QwrHuFoL2nqydhVI7auVH)
    
- **Giải thích chương trình:**  Sau mỗi 5 giây, thông tin nhiệt độ độ ẩm sẽ được cập nhật lên màn hình LCD1602.
