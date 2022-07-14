4. Bài 1: Hiển thị độ ẩm đất
=================================

Mục tiêu
----------------------
----------------------

Độ ẩm đất là yếu tố ảnh hưởng lớn đến sự phát triển của cây trồng. Trong dự án đầu tiên, chúng ta sẽ đo lường và hiển thị giá trị này lên OhStem App nhé!

Thiết bị cần dùng
--------------------
--------------------

.. image:: images/planbit_29.png
    :scale: 100%
    :align: center
|
Kết nối
---------------------
---------------------

.. image:: images/planbit_30.png
    :scale: 100%
    :align: center
|
Kết nối **cảm biến độ ẩm đất** vào cổng P0

Giới thiệu khối lệnh
---------------------
---------------------



    .. image:: images/planbit_31.png
        :width: 900px
        :align: center  

    .. image:: images/planbit_32.png
        :width: 900px
        :align: center 

Viết chương trình
---------------------
---------------------
1. Kéo thả **khối lệnh hiện thông tin** vào phần lặp lại mãi mãi

.. image:: images/planbit_33.png
    :scale: 100%
    :align: center
|
2. Kéo thả **khối lệnh đọc độ ẩm đất** vào **khối lệnh hiện thông tin**. Sau đó thêm **khối lệnh tạm dừng** với thời gian là 1000ms (1 giây)

.. image:: images/planbit_34.png
    :scale: 100%
    :align: center
|