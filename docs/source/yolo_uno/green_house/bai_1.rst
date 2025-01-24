2. Đo nhiệt độ và độ ẩm bên trong nhà kính
=================================

1. Mục tiêu
-----
--------

Theo dõi các thông số nhiệt độ và độ ẩm không khí thu được từ cảm biến DHT20 và hiển thị lên màn hình LCD 1602.

2. Thiết bị cần sử dụng
---------
----------

- Mạch Yolo UNO:

..  image:: images/yolouno.png
    :scale: 50%
    :align: center 
|

- Module LCD1602 kèm dây tín hiệu: 

..  image:: images/lcd1602.png
    :scale: 50%
    :align: center 
|

- Cảm biến nhiệt độ độ ẩm DHT20 kèm dây tín hiệu:

..  image:: images/dht20.png
    :scale: 50%
    :align: center 
|

3. Kết nối phần cứng
-------
--------

- Kết nối LCD vào cổng I2C1

- Kết nối cảm biến DHT20 vào cổng I2C4 của Yolo UNO

..  figure:: images/bai_1.1.png
    :scale: 100%
    :align: center 
|


4. Chương trình lập trình
------
------

- **Giới thiệu khối lệnh:** Khối lệnh dùng để đọc thông số nhiệt độ hoặc độ ẩm của cảm biến DHT20

..  image:: images/bai_1.2.png
    :scale: 70%
    :align: center 
|

- **Chương trình lập trình:**

..  figure:: images/bai_1.3.png
    :scale: 90%
    :align: center 

    Link chương trình `<https://app.ohstem.vn/#!/share/yolouno/2s1Of1S2hfCES5PQOQZogHUMrQc>`_

- **Giải thích chương trình:**  Sau khi cấp điện, mạch Yolo UNO sẽ hiển thị đèn led màu trên bo từ đỏ sang xanh lá cây. Sau mỗi 5s, thông tin nhiệt độ độ ẩm sẽ được cập nhật và hiển thị trên màn hình LCD, dựa vào thông tin đó chúng ta sẽ biết được nhiệt độ và độ ẩm trong nhà kín.