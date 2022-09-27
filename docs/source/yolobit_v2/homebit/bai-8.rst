11. Bài 8: Cảnh báo cháy
=====================================

Mục tiêu
--------------------
--------------------

Trong bài này, chúng ta sẽ sử dụng cảm biến lửa để phát hiện có lửa cháy hay không, từ đó hiển thị lên màn hình LCD và phát ra âm thanh cảnh báo.

Thiết bị cần dùng
----------------------
----------------------

- Cảm biến lửa 

.. image:: Images/homebit_91.png
    :width: 200px
    :align: center
|   

Kết nối
------------------------
------------------------

- Kết nối cảm biến lửa vào cổng P2

.. image:: Images/homebit_92.png
    :width: 500px
    :align: center
|   


Giới thiệu khối lệnh
------------------------
------------------------

.. image:: Images/homebit_93.png
    :width: 400px
    :align: center
| 


Viết chương trình
-----------------------
-----------------------

1. Tạo điều kiện: Nếu cảm biến chân P2 phát hiện
ra lửa

.. image:: Images/homebit_94.png
    :width: 550px
    :align: center
|   
2. Khi phát hiện có lửa, chương trình bắt đầu xóa màn hình LCD trước đó, hiện 2 dòng chữ “Alarm - Fire detected!!!” lên LCD và phát ra âm thanh cảnh báo.

.. image:: Images/homebit_95.png
    :width: 600px
    :align: center
|   

Chương trình mẫu
---------------------
---------------------

- Cảnh báo cháy: `Tại đây <https://app.ohstem.vn/#!/share/yolobit/2CycT2NG5NsIFWkXyDA4e1F1rmU>`_

.. image:: Images/homebit_96.png
    :width: 200px
    :align: center
|

