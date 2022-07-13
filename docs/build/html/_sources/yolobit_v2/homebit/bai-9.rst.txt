12. Bài 9: Cảnh báo động đất
=======================================

Mục tiêu 
------------------
------------------

Trong bài học này, chúng ta sẽ lập trình để ngôi nhà thông minh phát ra âm thanh báo động khi gặp phải động đất, dựa trên cảm biến gia tốc được tích hợp sẵn trên Yolo:Bit. Khi phát hiện bị lắc, Yolo:Bit sẽ phát ra âm thanh cảnh báo.

Thiết bị cần dùng
-------------------
-------------------

- Cảm biến gia tốc (tích hợp sẵn trên Yolo:Bit)

- Loa ( tích hợp sẵn trên Yolo:Bit)

Giới thiệu khối lệnh
-------------------
-------------------

.. image:: images/homebit_86.png
    :width: 700px
    :align: center
|   
Viết chương trình 
-------------------
-------------------

1. Tạo điều khiện: Nếu bị lắc với độ nhạy là 11

.. image:: images/homebit_87.png
    :width: 700px
    :align: center
|   

2. Khi phát hiện có động đất (ngôi nhà bị lắc), chương trình bắt đầu xóa màn hình LCD trước đó, hiện 2 dòng chữ "Alarm - Earthquake!!!" lên Lcd và phát ra âm thanh cảnh báo

.. image:: images/homebit_88.png
    :width: 700px
    :align: center
|   
