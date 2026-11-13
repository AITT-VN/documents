# 28. Cảm biến nhiệt độ hồng ngoại không tiếp xúc
![28.1](/wiki-assets/images/module/cam-bien/images/28.1.jpg)


MLX90614 là Cảm biến nhiệt độ kỹ thuật số hồng ngoại không tiếp xúc (IR) có thể được sử dụng để đo nhiệt độ của một đối tượng cụ thể, từ -70 ° C đến 382,2 ° C. Cảm biến sử dụng tia IR để đo nhiệt độ của đối tượng và giao tiếp với vi điều khiển bằng giao thức I2C.

**Các ứng dụng của MLX90614:**

- Đo nhiệt độ của các đối tượng chuyển động
- Súng nhiệt công nghiệp
- Đo nhiệt độ cơ thể con người
- Kiểm soát nhiệt độ tại nhà / văn phòng
- Giám sát chăn nuôi
- Phát hiện chuyển động

## 1. Mua sản phẩm
![gio](/wiki-assets/images/module/cam-bien/images/gio.png)


## 2. Thông số kỹ thuật
- Điện áp hoạt động: 3.3V đến 5V
- Dòng điện : 1.5mA
- Phạm vi nhiệt độ đối tượng: -70°C đến 382,2°C
- Phạm vi nhiệt độ môi trường: -40°C đến 125°C
- Độ chính xác: 0,02°C
- Góc quét: 80°
- Khoảng cách giữa đối tượng và cảm biến: 2cm-5cm (ước chừng)


## 3. Kết nối
- **Bước 1**: Chuẩn bị các thiết bị như sau:


| Hình ảnh | Sản phẩm | Mua hàng |
|:--------:|:---------|:--------:|
| ![yolo uno](/wiki-assets/images/module/cam-bien/images/yolo_uno.png) | Mạch lập trình Yolo UNO | [Mua sản phẩm ](https://shop.ohstem.vn/san-pham/yolo-uno/) |
| ![28.1](/wiki-assets/images/module/cam-bien/images/28.1.jpg) | Cảm biến (kèm dây Grove) | [Mua sản phẩm ](https://shop.ohstem.vn/san-pham/cam-bien-nhiet-do-hong-ngoai-khong-tiep-xuc/) |
| ![lcd 1602](/wiki-assets/images/module/cam-bien/images/lcd_1602.png) | Màn hình LCD 1602 (kèm dây Grove) | [Mua sản phẩm ](https://shop.ohstem.vn/san-pham/man-hinh-lcd-1602/) |
    
    
- **Bước 2**: Sử dụng dây Grove cắm vào cảm biến
- **Bước 3**: Kết nối cảm biến và màn hình LCD với **chân I2C trên Yolo UNO**.
![28.2](/wiki-assets/images/module/cam-bien/images/28.2.png)


    Cảm biến nhiệt độ hồng ngoại không tiếp xúc kết nối với Yolo UNO thông qua giao thức I2C
    
## 4. Hướng dẫn lập trình
1. Tải thư viện **MLX90614**
![28.3](/wiki-assets/images/module/cam-bien/images/28.3.png)


Các khối lệnh sau để làm việc với cảm biến:
![28.4](/wiki-assets/images/module/cam-bien/images/28.4.png)


2. Chương trình minh họa thực hiện chức năng tạo một máy đo nhiệt độ môi trường:
![28.5](/wiki-assets/images/module/cam-bien/images/28.5.png)


**Link chương trình mẫu:** [https://app.ohstem.vn/#!/share/yolouno/2fu1wQBlgZ4Qjl7Jh47QPcAsgly](https://app.ohstem.vn/#!/share/yolouno/2fu1wQBlgZ4Qjl7Jh47QPcAsgly)