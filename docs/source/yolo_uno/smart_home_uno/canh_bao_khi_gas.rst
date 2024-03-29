7. Cảnh báo khí gas
============

1. Mục tiêu
-----
--------

Đọc thông tin khí gas từ cảm biến MQ-2, nếu nồng độ khí Gas lên cao thì sẽ phát cảnh báo ra loa.


2. Thiết bị cần sử dụng
---------
----------

- Mạch Yolo UNO:

..  image:: images/yolo_uno.png
    :scale: 60%
    :align: center 
|

- Module SoundPlayer (D3-D4): 

..  image:: images/sound01.png
    :scale: 90%
    :align: center 
|

- Cảm biến nồng độ khí Gas MQ-2 (A1):

..  image:: images/mq2_01.png
    :scale: 90%
    :align: center 
|

3. Kết nối phần cứng
-------
--------

..  figure:: images/gas01.png
    :scale: 100%
    :align: center 
|

4. Chương trình lập trình
------
------

- **Giới thiệu khối lệnh:**

..  image:: images/mq2_02.png
    :scale: 90%
    :align: center 
|
    
Các khối lệnh để khai báo cảm biến khí Gas ở chân A1.

..  image:: images/sound02.png
    :scale: 90%
    :align: center 
|
    
Các khối lệnh để khai báo loa chân D3-D4

- **Chương trình lập trình:**

..  image:: images/gas02.png
    :scale: 90%
    :align: center 
|
