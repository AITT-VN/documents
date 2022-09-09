8. Máy đo nhiệt độ phòng
============================================

1. Mục tiêu 
----------
---------------

Trong bài học này, chúng ta sẽ cùng lập trình để hiển thị giá trị nhiệt độ, độ ẩm của môi trường lên màn hình LCD bằng cảm biến DHT20 (sau 5 giây sẽ cập nhật 1 lần).

2. Thiết bị cần dùng 
-------
-------------

- Mạch Yolo:Bit
- Mạch mở rộng Yolo:Bit.

.. image:: images/4.1.jpg
    :width: 300px
    :align: center
|

- Màn hình LCD1602

.. image:: images/7.1.jpg
    :scale: 40 %
    :align: center
|
- Cảm biến ánh sáng

.. image:: images/5.1.jpg
    :width: 30 %
    :align: center
| 

- Cảm biến nhiệt độ độ ẩm DHT20

.. image:: images/8.1.jpg
    :width: 30 %
    :align: center
| 

3. Kết nối 
-------
------------

- Kết nối cảm biến ánh sáng với cổng P0
- Kết nối cảm biến DHT20 và màn hình LCD vào hai cổng I2C

.. image:: images/8.2.png
    :width: 400px
    :align: center
| 

4. Lập trình 
-------
----------

- **Giới thiệu khối lệnh:**

Để sử dụng cảm biến nhiệt độ độ ẩm DHT20, chúng ta sẽ dùng 2 khối lệnh: 

.. image:: images/8.3.png
    :width: 100 %
    :align: center
|
Khối lệnh đầu tiên sẽ đọc giá trị nhiệt độ hoặc độ ẩm từ cảm biến, khối lệnh thứ 2 dùng để cập nhật nhiệt độ độ ẩm.

- **Lập trình**

Để hiển thị nhiệt độ nhận được từ cảm biến lên LCD, chúng ta sẽ sử dụng khối lệnh hiển thị lên LCD như bài trước. Khi ghép lại các khối lệnh sẽ như sau:

.. image:: images/8.4.png
    :width: 100 %
    :align: center
|
Chương trình hoàn chỉnh sẽ như hình:

.. image:: images/8.5.png
    :width: 100 %
    :align: center
|
5. Chương trình mẫu 
-------
------------

- Đo nhiệt độ phòng: `Tại đây <https://app.ohstem.vn/#!/share/yolobit/2EWNBTjiLMLWwaVvItmiXABdyFP>`_

.. image:: images/8.6.png
    :width: 200px
    :align: center 