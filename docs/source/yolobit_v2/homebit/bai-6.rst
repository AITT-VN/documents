9. Bài 6: Đèn cổng thông minh 
===================================

Mục tiêu
-----------------------
-----------------------

Chúng ta hãy cùng lập trình một chiếc đèn cổng thông minh, có thể bật tắt tự động dựa vào ánh sáng và khi phát hiện có người:

- Khi trời tối (độ sáng < 30%) và phát hiện có người ở trước nhà thì đèn tự bật

- Tắt đèn khi trời sáng hoặc không còn phát hiện người nữa

Thiết bị cần dùng
-----------------------
-----------------------

- Cảm biến ánh sáng

.. image:: images/homebit_65.png
    :width: 200px
    :align: center
| 
- Đèn 4 LED RGB

.. image:: images/homebit_66.png
    :width: 200px
    :align: center
|
-Cảm biến chuyển động PIR

.. image:: images/homebit_54.png
    :width: 200px
    :align: center
|

Kết nối
-----------------------
-----------------------
  
- Kết nối cảm biến ánh sáng vào cổng P0

- Kết nối đèn 4 LED RGB vào cổng P14

- Kết nối cảm biến chuyển động PIR vào cổng P16

.. image:: images/homebit_67.png
    :width: 600px
    :align: center
| 

Giới thiệu khối lệnh 
------------------------
------------------------

.. image:: images/homebit_68.png
    :width: 400px
    :align: center
|   
.. image:: images/homebit_69.png
    :width: 400px
    :align: center
| 
.. image:: images/homebit_70.png
    :width: 1000px
    :align: center
|


Viết chương trình
-------------
------------

1. Kéo **khối lệnh toán tử** VÀ vào **khối lệnh điều kiện**

.. image:: images/homebit_71.png
    :width: 300px
    :align: center
|   
2. Đặt điều kiện: khi trời tối (độ sáng < 30) và cảm biến PIR phát hiện có người

.. image:: images/homebit_72.png
    :width: 1400px
    :align: center
|   
3. Bật và tắt đèn LED RGB tùy theo từng trường hợp

.. image:: images/homebit_73.png
    :width: 1400px
    :align: center
|

Chương trình mẫu
---------------------
---------------------

- Đèn cổng thông minh: `Tại đây <https://app.ohstem.vn/#!/share/yolobit/2CvpiJvC0IDlQJzzfjrMegMBtRX>`_

.. image:: images/homebit_74.png
    :width: 200px
    :align: center
|

