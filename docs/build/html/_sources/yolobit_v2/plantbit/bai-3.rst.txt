6. Bài 3: Bật tắt máy bơm 
==================================

Mục tiêu
----------------------
----------------------

Trong bài này, chúng ta sẽ điều khiển bật tắt máy bơm nước bằng cách nhấn nút A và B trên Yolo:Bit.

Thiết bị cần dùng
-----------------------
-----------------------

.. image:: images/planbit_41.png
    :scale: 100%
    :align: center
|
Kết nối
-----------------------
-----------------------

.. image:: images/planbit_42.png
    :scale: 100%
    :align: center
|
Kết nối **Module đóng ngắt 2 kênh** vào cổng P14/P15. Nối **động cơ bơm nước** vào cổng USB Output1

Giới thiệu khối lệnh
-----------------------
-----------------------

    .. image:: images/planbit_43.png
        :width: 400px
        :align: center  

    .. image:: images/planbit_44.png
        :width: 900px
        :align: center 

Viết chương trình
-----------------------
-----------------------

1. Chọn **khối lệnh khi nút được nhấn** từ mục **Ngõ vào**

.. image:: images/planbit_45.png
    :scale: 100%
    :align: center
|
2. Kéo thả **khối lệnh bật máy bơm** vào **khối lệnh khi nút được nhấn** và chọn tốc độ là 50

Tiếp tục, gắn thêm **khối lệnh đổi màu tất cả LED** và chọn màu xanh lá

.. image:: images/planbit_46.png
    :scale: 100%
    :align: center
|
3. Tương tụ, tạo sự kiện khi nút B được nhấn:

- Tắt máy bơm (tốc độ = 0%)

- Tắt đèn (đổi màu LED thành màu đen)

.. image:: images/planbit_47.png
    :scale: 100%
    :align: center
|
**Ghi chú**: *Động cơ của máy bơm có thể hoạt động với tốc độ từ 0 - 100. Chúng ta nên sử dụng ở mức 50 để tránh tình trạng Yolo:Bit bị nóng (do máy bơm cần nguồn điện lớn để chạy).* 