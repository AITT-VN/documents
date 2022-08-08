6. Bài 3: Bật tắt máy bơm 
==================================

Mục tiêu
----------------------
----------------------

Trong bài này, chúng ta sẽ điều khiển bật tắt máy bơm nước bằng cách nhấn nút A và B trên Yolo:Bit.

Thiết bị cần dùng
-----------------------
-----------------------

- Mạch mở rộng gắn sẵn Yolo:Bit

.. image:: images/planbit_31.png
    :width: 200px
    :align: center
|
-  Module đóng ngắt 2 kênh

.. image:: images/planbit_45.png
    :width: 200px
    :align: center
|
-  Động cơ bơm nước

.. image:: images/planbit_46.png
    :width: 200px
    :align: center
|

Kết nối
-----------------------
-----------------------

- Kết nối **Module đóng ngắt 2 kênh** vào cổng P14/P15. 

- Nối **động cơ bơm nước** vào cổng USB Output1

.. image:: images/planbit_47.png
    :width: 400px
    :align: center
|


Giới thiệu khối lệnh
-----------------------
-----------------------

.. image:: images/planbit_48.png
    :width: 400px
    :align: center  
|
.. image:: images/planbit_49.png
    :width: 1000px
    :align: center 
|


Viết chương trình
-----------------------
-----------------------

1. Chọn **khối lệnh khi nút được nhấn** từ mục **Ngõ vào**

.. image:: images/planbit_50.png
    :width: 300px
    :align: center
|
2. Kéo thả **khối lệnh bật máy bơm** vào **khối lệnh khi nút được nhấn** và chọn tốc độ là 50

Tiếp tục, gắn thêm **khối lệnh đổi màu tất cả LED** và chọn màu xanh lá

.. image:: images/planbit_51.png
    :width: 600px
    :align: center
|
3. Tương tụ, tạo sự kiện khi nút B được nhấn:

- Tắt máy bơm (tốc độ = 0%)

- Tắt đèn (đổi màu LED thành màu đen)

.. image:: images/planbit_52.png
    :width: 600px
    :align: center
|

**Ghi chú**: *Động cơ của máy bơm có thể hoạt động với tốc độ từ 0 - 100. Chúng ta nên sử dụng ở mức 50 để tránh tình trạng Yolo:Bit bị nóng (do máy bơm cần nguồn điện lớn để chạy).* 


Chương trình mẫu
---------------------
---------------------

- Bật tắt máy bơm: `Tại đây <https://app.ohstem.vn/#!/share/yolobit/2CymiptdeuphF0inMtfB5POwvPK>`_

.. image:: images/planbit_53.png
    :width: 200px
    :align: center
|

