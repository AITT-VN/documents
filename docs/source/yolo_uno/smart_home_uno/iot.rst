5. Nhận và gửi thông tin lên server IoT
========

1. Mục tiêu
-----
--------

Với hướng dẫn này, chúng ta sẽ thực hiện dự án gửi thông tin nhiệt độ, độ ẩm nhận được từ cảm biến DHT20 lên bảng điều khiển IoT và thực hiện điều khiển đèn, quạt từ xa thông qua bảng điều khiển IoT. 

2. Thiết bị cần sử dụng
---------
----------

- Mạch Yolo UNO:

..  image:: images/yolo_uno.png
    :scale: 60%
    :align: center 
|

- Cảm biến nhiệt độ độ ẩm DHT20 kèm dây tín hiệu:

..  image:: images/dht20.png
    :scale: 90%
    :align: center 
|

- Module 4 LED RGB:

..  image:: images/tiny_rgb.png
    :scale: 90%
    :align: center 
|


- Module quạt mini:

..  image:: images/mini_fan.png
    :scale: 90%
    :align: center 
|


3. Kết nối 
-----
--------

- Kết nối cảm biến DHT20 vào chân I2C trên Yolo UNO, 4 LED RGB ở chân D5-D6, quạt mini ở chân D7-D8: 
 
..  figure:: images/iot_1.png
    :scale: 100%
    :align: center 
|

4. Tạo bảng điều khiển IoT
-------
--------

Truy cập vào `<https://app.ohstem.vn/>`_, chọn **Bảng điều khiển IoT** và tạo một bảng điều mới.

Với bảng điều khiển mới, bạn cần thực hiện các thao tác sau:

    1. Đặt lại tên cho Username (đặt thêm ký tự hoặc số để không trùng với các username khác)

..  figure:: images/iot_2.png
    :scale: 100%
    :align: center 
|

2. Kéo thả các widget ra màn hình bảng điều khiển. Đặt lại tên của widget và kênh thông tin (Mỗi đối tượng sẽ chọn 1 kênh thông tin khác nhau)
        
    - Nhiệt độ - Kênh thông tin V1. 
    - Độ ẩm - Kênh thông tin V2. 
    - Bật tắt đèn - Kênh thông tin V3. 
    - Bật tắt quạt - Kênh thông tin V4.

..  figure:: images/iot_3.png
    :scale: 100%
    :align: center 
|

Kết quả như sau:

..  figure:: images/iot_4.png
    :scale: 100%
    :align: center 
|

..  figure:: images/iot_16.png
    :scale: 100%
    :align: center 
|
5. Chương trình lập trình
-------
--------

**5.1 Giới thiệu khối lệnh**
----------

1. Mở tab mới và truy cập vào `<https://app.ohstem.vn/>`_. Chọn thiết bị lập trình **Yolo UNO** và chọn **Lập trình**.  

..  figure:: images/iot_5.png
    :scale: 100%
    :align: center 
|

2. Vào mục **Nâng cao**, chọn danh mục khối lệnh **IoT**:

..  figure:: images/iot_6.png
    :scale: 100%
    :align: center 
|

Chúng ta sẽ sử dụng các khối lệnh sau: 

- Câu lệnh dùng để kết nối wifi và kết nối đến user đã đặt trong mục Huấn luyện mô hình AI. 

..  figure:: images/iot_7.png
    :scale: 100%
    :align: center 
|

- Câu lệnh gửi kết quả từ thiết bị lên bảng điều khiển

..  figure:: images/iot_8.png
    :scale: 100%
    :align: center 
|

- Câu lệnh nhận thông tin từ kênh dữ liệu của server để điều khiển thiết bị hoạt động. 

..  figure:: images/iot_9.png
    :scale: 90%
    :align: center 
|

- Câu lệnh dùng để so sánh kết quả thông tin thiết bị nhận được từ server.

..  figure:: images/iot_10.png
    :scale: 90%
    :align: center 
|


**5.2 Viết chương trình**
----------

Thực hiện các thao tác sau để mở chương trình **Nhận và gửi thông tin lên server**:

..  image:: images/iot_11.png
    :scale: 100%
    :align: center 
|


**5.3 Giải thích chương trình**
----------

- **Bước 1:** Lập trình để Yolo UNO kết nối wifi. Cần nhập đúng tên, mật khẩu wifi mà máy tính/ điện thoại đang kết nối và username của bảng điều khiển. 

..  image:: images/iot_13.png
    :scale: 100%
    :align: center 
|

Giải thích: Khi Yolo UNO khởi động, đèn LED trên board sẽ đổi màu đỏ. Sau khi kết nối thành công với wifi và bảng điều khiển IoT, đèn LED trên board sẽ sáng xanh. 

- **Bước 2:** Gửi thông tin lên bảng điều khiển

..  image:: images/iot_14.png
    :scale: 100%
    :align: center 
|

Giải thích: Sau mỗi 5 giây, thông tin từ cảm biến nhiệt độ và độ ẩm sẽ gửi kết quả lên bảng điều khiển. 

- **Bước 3**:  Điều khiển đèn LED trên board từ bảng điều khiển IoT:

..  image:: images/iot_15.png
    :scale: 100%
    :align: center 
|

- **Bước 4**:  Điều khiển quạt trên board từ bảng điều khiển IoT:

..  image:: images/iot_17.png
    :scale: 100%
    :align: center 
|


Giải thích: Sau mỗi 5 giây, thông tin từ cảm biến nhiệt độ và độ ẩm sẽ gửi kết quả lên bảng điều khiển. 

- **Bước 4**: Kết nối đến Yolo UNO và quan sát kết quả trên bảng điều khiển. 
