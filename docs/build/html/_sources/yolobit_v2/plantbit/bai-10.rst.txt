13. Bài 10: Cảnh báo mực nước 
====================================

Mục tiêu
------------------
-----------------

Ở bài học này, chúng ta sẽ thực hiện chương trình kiểm tra mực nước trong bể chứa và bật đèn LED Yolo:Bit để cảnh báo: hiển thị mặt cười khi bể còn nước, hiển thị mặt buồn và phát âm thanh báo động khi nước trong bể cạn.

Thiết bị cần dùng
-------------------
------------------

.. image:: images/planbit_82.png
    :scale: 100%
    :align: center
|
Kết nối
-------------------
-------------------

- Cảm biến khoảng cách nối vào chân P10/P13

.. image:: images/planbit_83.png
    :scale: 100%
    :align: center
|
Giới thiệu khối lệnh
-----------------
----------------

.. image:: images/planbit_84.png
    :scale: 100%
    :align: center
|
Viết chương trình
-------------------
-------------------

1. Khởi tạo màn hình cảm biến khoảng cách và Reset bộ đếm thời gian

.. image:: images/planbit_85.png
    :scale: 100%
    :align: center
|
2. Tạo điều kiện: Nếu bộ đếm thời gian lớn hơn 5 giây

.. image:: images/planbit_86.png
    :scale: 100%
    :align: center
|
3. Lồng một điều kiện bên trong:

- Nếu cảm biến khoảng cách đọc được > 10cm (nước cạn), hiện mặt buồn và phát chuông báo

- Nếu không, hiện mặt vui

.. image:: images/planbit_87.png
    :scale: 100%
    :align: center
|
4. Đặt lại bộ đếm thời gian

.. image:: images/planbit_88.png
    :scale: 100%
    :align: center
|