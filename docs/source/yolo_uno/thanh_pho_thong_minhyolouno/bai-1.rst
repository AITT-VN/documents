2. Bài 1: Đèn công cộng thông minh
=================================

1. Mục tiêu:
------------
-----------------

Trong bài này, chúng ta sẽ cùng lập trình một chiếc đèn thông minh có thể tự sáng vào buổi tối. Các đèn này có thể gắn vào các khu vui chơi hoặc công viên tùy thích.


2. Kết nối 
----------
--------------

- Cảm biến ánh sáng (A3)

    .. image:: images/bai_1.1.3.png
        :width: 150px
        :align: center 
    |
- Module 4 LED RGB (D7-D8)

    .. image:: images/bai_1.1.1.png
        :width: 150px
        :align: center 
    |
- **Kết nối:**

    .. image:: images/bai_1.2.png
        :scale: 80%
        :align: center 
|


3. Lắp ráp 
-----------
----------------

Các thao tác được thực hiện như sau:

.. image:: images/bai_1.4.png
    :scale: 90%
    :align: center 
|

.. image:: images/bai_1.4.1.png
    :scale: 90%
    :align: center 
|


4. Giới thiệu khối lệnh
----------
----------------

- Khối lệnh của cảm biến ánh sáng

.. image:: images/cityuno01.PNG
    :scale: 90%
    :align: center 
|

- Khối lệnh điều khiển đèn 4 LED RGB:

.. image:: images/cityuno02.PNG
    :scale: 90%
    :align: center 
|

Viết chương trình
------------
--------------------

1. Kéo khối lệnh điều kiện vào khối lệnh kiểm tra theo thời sau **Sau mỗi 1 giây thực hiện**

.. image:: images/cityuno03.PNG
    :scale: 80%
    :align: center

|

2. Tạo điều kiện: nếu trời tối (độ sáng < 15) thì sẽ bật đèn (đổi sang thành màu trắng)

.. image:: images/cityuno04.PNG
    :scale: 100%
    :align: center 
|

3. Tạo điều kiện: nếu trời sáng (độ sáng > 35) thì sẽ tắt đèn (đổi sang thành màu đen)

.. image:: images/cityuno05.PNG
    :scale: 100%
    :align: center 
|

- Chương trình hoàn thiện: 

.. image:: images/cityuno06.PNG
    :scale: 100%
    :align: center 
|

- Link chương trình mẫu: `<https://app.ohstem.vn/#!/share/yolouno/2eImrFzleAHhhnxEm7l7IBnN7zU>`_



