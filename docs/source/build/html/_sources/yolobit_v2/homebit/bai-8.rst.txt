11. Bài 8: Cảnh báo cháy
=====================================

Mục tiêu
--------------------
--------------------
Trong bài này, chúng ta sẽ sử dụng cảm biến lửa để phát hiện có lửa cháy hay không, từ đó hiển thị lên màn hình LCD và phát ra âm thanh cảnh báo.

Thiết bị cần dùng
----------------------
----------------------

.. image:: images/homebit_81.png
    :width: 200px
    :align: center
|   

Kết nối
------------------------
------------------------

.. image:: images/homebit_82.png
    :width: 300px
    :align: center
|   
- Kết nối cảm biến lửa vào cổng P2

Giới thiệu khối lệnh
------------------------
------------------------

.. image:: images/homebit_83.png
    :width: 700px
    :align: center
|   
Viết chương trình
-----------------------
-----------------------

1. Tạo điều kiện: Nếu cảm biến chân P2 phát hiện
ra lửa

.. image:: images/homebit_84.png
    :width: 700px
    :align: center
|   
2. Khi phát hiện có lửa, chương trình bắt đầu xóa màn hình LCD trước đó, hiện 2 dòng chữ “Alarm - Fire detected!!!” lên LCD và phát ra âm thanh cảnh báo.

.. image:: images/homebit_85.png
    :width: 700px
    :align: center
|   