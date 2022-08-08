6. Bài 3: Hiển thị nhiệt độ 
==================================
Mục tiêu
---------------------
---------------------

Trong bài học này, chúng ta sẽ cùng lập trình để hiển thị giá trị nhiệt độ, độ ẩm của môi trường lên màn hình LCD bằng cảm biến DHT20 (sau 5 giây sẽ cập nhật 1 lần)

Thiết bị cần dùng
--------------------
--------------------

.. image:: images/homebit_38.png
    :width: 400px
    :align: center
|   
.. image:: images/homebit_39.png
    :width: 400px
    :align: center
|   
- Kết nối màn hình LCD vào cổng l2C 1
  
- Kết nối cảm biến DHT20 vào cổng I2C 2

Giới thiệu khối lệnh
-------------------------
-------------------------

.. image:: images/homebit_43.png
    :width: 600px
    :align: center
|   

Viết chương trình
-------------------------
-------------------------
1. Tạo điều kiện: Nếu bộ đếm thời gian ≥ 5000ms (5 giây). Điều kiện này giúp mỗi 5 giây chương trình sẽ thực hiện lệnh bên trong

.. image:: images/homebit_44.png
    :width: 400px
    :align: center
|   
2. Cập nhật cảm biến nhiệt độ độ ẩm và xóa các thông tin đang có trên LCD để chuẩn bị hiển thị giá trị nhiệt độ, độ ẩm mới

.. image:: images/homebit_48.png
    :width: 400px
    :align: center
|   
3. Hiển thị giá trị nhiệt độ, độ ẩm lên màn hình LCD  thành 2 hàng (hàng 0 và hàng 1)

.. image:: images/homebit_49.png
    :width: 400px
    :align: center
|   
4. Reset bộ đếm thời gian để bắt đầu đếm lại sau mỗi 5 giây:

.. image:: images/homebit_50.png
    :width: 400px
    :align: center
|   
