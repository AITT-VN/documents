# 7. Nhận và gửi thông tin lên server IoT

## 1. Mục tiêu
Với hướng dẫn này, chúng ta sẽ thực hiện dự án gửi thông tin nhiệt độ, độ ẩm nhận được từ cảm biến DHT20 lên bảng điều khiển IoT và thực hiện điều khiển đèn, quạt từ xa thông qua bảng điều khiển IoT.

## 2. Thiết bị cần sử dụng
- Mạch Yolo UNO:
![yolo uno](/wiki-assets/images/yolo_uno/smart_home_uno/images/yolo_uno.png)


- Cảm biến nhiệt độ độ ẩm DHT20 kèm dây tín hiệu:
![dht20](/wiki-assets/images/yolo_uno/smart_home_uno/images/dht20.png)


- Module 4 LED RGB:
![tiny rgb](/wiki-assets/images/yolo_uno/smart_home_uno/images/tiny_rgb.png)


- Module quạt mini:
![mini fan](/wiki-assets/images/yolo_uno/smart_home_uno/images/mini_fan.png)


## 3. Kết nối
- Kết nối cảm biến DHT20 vào chân I2C trên Yolo UNO
- Quạt mini ở chân D7-D8:
- Đèn 4 LED RGB ở chân D9-D10
![iot 1](/wiki-assets/images/yolo_uno/smart_home_uno/images/iot_1.png)


## 4. Tạo bảng điều khiển IoT
Truy cập vào [https://app.ohstem.vn/](https://app.ohstem.vn/), chọn **Bảng điều khiển IoT** và tạo một bảng điều mới.

Với bảng điều khiển mới, bạn cần thực hiện các thao tác sau:

    1. Đặt lại tên cho Username (đặt thêm ký tự hoặc số để không trùng với các username khác)
![iot 2](/wiki-assets/images/yolo_uno/smart_home_uno/images/iot_2.png)


2. Kéo thả các widget ra màn hình bảng điều khiển. Đặt lại tên của widget và kênh thông tin (Mỗi đối tượng sẽ chọn 1 kênh thông tin khác nhau)

    - Nhiệt độ - Kênh thông tin V1.
    - Độ ẩm - Kênh thông tin V2.
    - Bật tắt đèn - Kênh thông tin V3.
    - Bật tắt quạt - Kênh thông tin V4.
![iot 3](/wiki-assets/images/yolo_uno/smart_home_uno/images/iot_3.png)


Kết quả như sau:
![iot 4](/wiki-assets/images/yolo_uno/smart_home_uno/images/iot_4.png)
![iot 16](/wiki-assets/images/yolo_uno/smart_home_uno/images/iot_16.png)


## 5. Chương trình lập trình
## **5.1 Giới thiệu khối lệnh**
1. Mở tab mới và truy cập vào ](https://app.ohstem.vn/). Chọn thiết bị lập trình **Yolo UNO** và chọn **Lập trình**.
![iot 5](/wiki-assets/images/yolo_uno/smart_home_uno/images/iot_5.png)


2. Vào mục **Nâng cao**, chọn danh mục khối lệnh **IoT**:
![iot 6](/wiki-assets/images/yolo_uno/smart_home_uno/images/iot_6.png)


Chúng ta sẽ sử dụng các khối lệnh sau:

- Câu lệnh dùng để kết nối wifi và kết nối đến user đã đặt trong mục Huấn luyện mô hình AI.
![iot 7](/wiki-assets/images/yolo_uno/smart_home_uno/images/iot_7.png)


- Câu lệnh gửi kết quả từ thiết bị lên bảng điều khiển
![iot 8](/wiki-assets/images/yolo_uno/smart_home_uno/images/iot_8.png)


- Câu lệnh nhận thông tin từ kênh dữ liệu của server để điều khiển thiết bị hoạt động.
![iot 9](/wiki-assets/images/yolo_uno/smart_home_uno/images/iot_9.png)


- Câu lệnh dùng để so sánh kết quả thông tin thiết bị nhận được từ server.
![iot 10](/wiki-assets/images/yolo_uno/smart_home_uno/images/iot_10.png)


## **5.2 Viết chương trình**
Thực hiện các thao tác sau để mở chương trình **Nhận và gửi thông tin lên server**:
![iot 11](/wiki-assets/images/yolo_uno/smart_home_uno/images/iot_11.png)


    [https://app.ohstem.vn/#!/share/yolouno/2vFe6PGbnqNlVl1g0bLUgPK1QiC](https://app.ohstem.vn/#!/share/yolouno/2vFe6PGbnqNlVl1g0bLUgPK1QiC)
    
    
## **5.3 Giải thích chương trình**
- **Bước 1:** Lập trình để Yolo UNO kết nối wifi. Cần nhập đúng tên, mật khẩu wifi mà máy tính/ điện thoại đang kết nối và username của bảng điều khiển.
![iot 13](/wiki-assets/images/yolo_uno/smart_home_uno/images/iot_13.png)


Giải thích: Khi Yolo UNO khởi động, đèn LED trên board sẽ đổi màu đỏ. Sau khi kết nối thành công với wifi và bảng điều khiển IoT, đèn LED trên board sẽ sáng xanh.

- **Bước 2:** Gửi thông tin lên bảng điều khiển
![iot 14](/wiki-assets/images/yolo_uno/smart_home_uno/images/iot_14.png)


Giải thích: Sau mỗi 5 giây, thông tin từ cảm biến nhiệt độ và độ ẩm sẽ gửi kết quả lên bảng điều khiển.

- **Bước 3**:  Điều khiển đèn LED trên board từ bảng điều khiển IoT:
![iot 15](/wiki-assets/images/yolo_uno/smart_home_uno/images/iot_15.png)


- **Bước 4**:  Điều khiển quạt trên board từ bảng điều khiển IoT:
![iot 17](/wiki-assets/images/yolo_uno/smart_home_uno/images/iot_17.png)


Giải thích: Sau mỗi 5 giây, thông tin từ cảm biến nhiệt độ và độ ẩm sẽ gửi kết quả lên bảng điều khiển.

- **Bước 4**: Kết nối đến Yolo UNO và quan sát kết quả trên bảng điều khiển.
