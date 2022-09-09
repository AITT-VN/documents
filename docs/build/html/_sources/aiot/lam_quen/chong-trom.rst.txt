10. Hệ thống chống trộm 
================

1. Mục tiêu 
----------
---------------

Trong bài học này, chúng ta sẽ cùng lập trình một hệ thống chống trộm, có thể tự động phát ra âm thanh cảnh báo và bật đèn báo động khi có người đến gần khu vực bảo vệ nhé!

2. Thiết bị cần dùng 
-------
-------------

- Mạch Yolo:Bit
- Mạch mở rộng Yolo:Bit.

.. image:: images/4.1.jpg
    :width: 300px
    :align: center
|
- Module 4 LED RGB 

.. image:: images/4.2.jpg
    :scale: 40 %
    :align: center
|
- Cảm biến hồng ngoại PIR

.. image:: images/10.1.jpg
    :scale: 40 %
    :align: center
|

3. Kết nối 
-------
------------

- Kết nối đèn 4 LED RGB vào cổng P14/P15
- Kết nối cảm biến PIR vào cổng P16/P12

.. image:: images/10.2.png
    :width: 450px
    :align: center
| 

4. Lập trình 
-------
----------

Để sử dụng cảm biến phát hiện chuyển động PIR, chúng ta sẽ dùng khối lệnh sau:

.. image:: images/10.3.png
    :scale: 100 %
    :align: center
|
Hãy cùng lập trình tính năng đầu tiên: Nếu như cảm biến chuyển động phát hiện được có người, hệ thống sẽ chớp tắt đèn đỏ 3 lần. Ngược lại, nếu phát hiện không có người thì hệ sẽ tắt đèn (đèn màu đen). Chương trình lúc này sẽ như sau:

.. image:: images/10.4.png
    :scale: 90 %
    :align: center
|
Bên cạnh đó, chúng ta sẽ sử dụng thêm 1 buzzer (1 chiếc loa nhỏ) để phát âm thanh báo hiệu. Trên mạch Yolo:Bit đã được tích hợp một buzzer nhỏ để phát âm thanh. 

Để bật âm thanh trên buzzer, các bạn sử dụng 2 khối lệnh sau, nằm ở danh mục **ÂM NHẠC**:

.. image:: images/10.5.png
    :scale: 100 %
    :align: center
|
Kết hợp 2 khối lệnh trên vào chương trình, ta được chương trình hoàn chỉnh như hình:

.. image:: images/10.6.png
    :scale: 100 %
    :align: center
|

5. Chương trình mẫu 
-------
------------

- Hệ thống chống trộm : `Tại đây <https://app.ohstem.vn/#!/share/yolobit/2EWQbm1hEdLHupryuGeGg4o3ytC>`_

.. image:: images/10.7.png
    :width: 200px
    :align: center 