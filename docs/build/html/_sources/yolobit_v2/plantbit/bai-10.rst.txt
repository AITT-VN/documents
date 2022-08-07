13. Bài 10: Cảnh báo mực nước 
====================================

Mục tiêu
------------------
-----------------

Ở bài học này, chúng ta sẽ thực hiện chương trình kiểm tra mực nước trong bể chứa và bật đèn LED Yolo:Bit để cảnh báo: hiển thị mặt cười khi bể còn nước, hiển thị mặt buồn và phát âm thanh báo động khi nước trong bể cạn.

Thiết bị cần dùng
---------------
---------------

- Mạch mở rộng gắn sẵn Yolo:Bit

.. image:: images/planbit_31.png
    :width: 200px
    :align: center
|
- Cảm biến khoảng cách 

.. image:: images/planbit_88.png
    :width: 250px
    :align: center
|


Kết nối
----------------
----------------

- Cảm biến khoảng cách nối vào chân P10/P13

.. image:: images/planbit_89.png
    :width: 300px
    :align: center
|


Giới thiệu khối lệnh
-----------------
----------------

.. image:: images/planbit_94.png
    :width: 800px
    :align: center
|


Viết chương trình
-------------------
-------------------

1. Khởi tạo màn hình cảm biến khoảng cách và Reset bộ đếm thời gian

.. image:: images/planbit_95.png
    :width: 600px
    :align: center
|
2. Tạo điều kiện: Nếu bộ đếm thời gian lớn hơn 5 giây

.. image:: images/planbit_96.png
    :width: 600px
    :align: center
|
3. Lồng một điều kiện bên trong:

- Nếu cảm biến khoảng cách đọc được > 10cm (nước cạn), hiện mặt buồn và phát chuông báo

- Nếu không, hiện mặt vui

.. image:: images/planbit_97.png
    :width: 600px
    :align: center
|
4. Đặt lại bộ đếm thời gian

.. image:: images/planbit_98.png
    :width: 600px
    :align: center
|


Chương trình mẫu
---------------------
---------------------

- Cảnh báo mực nước : `Tại đây <https://app.ohstem.vn/#!/share/yolobit/2Cyux73I7ZbVzygW90HtSUem1zC>`_

.. image:: images/planbit_99.png
    :width: 200px
    :align: center
|