1. Đo và hiển thị nhiệt độ & độ ẩm của ngôi nhà.
============

1. Mục tiêu
-----
--------

Đọc thông số nhiệt độ và độ ẩm không khí từ cảm biến DHT20 và hiển thị lên màn hình LCD 1602.


2. Thiết bị cần sử dụng
---------
----------

- Mạch Yolo UNO:

..  image:: images/yolo_uno.png
    :scale: 60%
    :align: center 
|

- Module LCD kèm dây tín hiệu: 

..  image:: images/lcd_1602.png
    :scale: 90%
    :align: center 
|

- Cảm biến nhiệt độ độ ẩm DHT20 kèm dây tín hiệu:

..  image:: images/dht20.png
    :scale: 90%
    :align: center 
|

3. Kết nối phần cứng
-------
--------

- Kết nối LCD vào cổng I2C1

- Kết nối cảm biến DHT20 vào cổng I2C2 của Yolo UNO

..  figure:: images/dht20_1.png
    :scale: 100%
    :align: center 
|

4. Chương trình lập trình
------
------

- **Giới thiệu khối lệnh:**

..  image:: images/dht20_2.png
    :scale: 90%
    :align: center 
|
    
Các khối lệnh để đọc thông số nhiệt độ hoặc độ ẩm của cảm biến DHT20

- **Chương trình lập trình:**

..  image:: images/dht20_3.png
    :scale: 90%
    :align: center 
|
