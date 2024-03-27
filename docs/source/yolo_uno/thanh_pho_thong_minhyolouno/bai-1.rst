2. Bài 1: Đèn công cộng thông minh
=================================

Mục tiêu:
------------
-----------------

Trong bài này, chúng ta sẽ cùng lập trình một chiếc đèn thông minh có thể tự sáng khi có người vào buổi tối. Các đèn này có thể gắn vào các khu vui chơi hoặc công viên tùy thích.


Kết nối 
----------
--------------

- Cảm biến ánh sáng (A3)

    .. image:: images/bai_1.1.3.png
        :width: 200px
        :align: center 
    |
- Module 4 LED RGB (D7-D8)

    .. image:: images/bai_1.1.1.png
        :width: 200px
        :align: center 
    |
**Kết nối**

    .. image:: images/bai_1.2.png
        :width: 800px
        :align: center 
    
Lắp ráp 
-----------
----------------


**Lắp ráp mô hình**

    .. image:: images/bai_1.4.png
        :width: 1000px
        :align: center 
    |
    .. image:: images/bai_1.4.1.png
        :width: 1000px
        :align: center 
    |


Giới thiệu khối lệnh
----------
----------------

.. image:: images/cityuno01.png
    :scale: 90%
    :align: center 
|
.. image:: images/cityuno02.png
    :scale: 90%
    :align: center 
|

Viết chương trình
------------
--------------------

1. Kéo khối lệnh điều kiện vào khối lệnh kiểm tra theo thời sau **Sau mỗi 1 giây thực hiện**

    .. image:: images/cityuno03.png
        :scale: 90%
        :align: center 
    |
2. Tạo điều kiện: nếu trời tối (độ sáng < 15) thì sẽ bật đèn (đổi sang thành màu trắng)

    .. image:: images/cityuno04.png
        :scale: 90%
        :align: center 
    |
3. Tạo điều kiện: nếu trời sáng (độ sáng > 35) thì sẽ tắt đèn (đổi sang thành màu đen)

    .. image:: images/cityuno05.png
        :scale: 90%
        :align: center 
    |


Chương trình mẫu

     .. image:: images/cityuno06.png
        :scale: 90%
        :align: center 
    |
------------
----------------

