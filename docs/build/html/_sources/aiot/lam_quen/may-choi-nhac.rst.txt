14. Máy chơi nhạc 
===========

1. Mục tiêu 
----------
---------------

Trong dự án này, chúng ta sẽ sử dụng remote trong bộ kit AIoT kết hợp với Yolo:Bit để tạo thành một chiếc máy chơi nhạc từ xa. Mỗi nút nhấn trên remote sẽ tương ứng với một nốt nhạc. 

Bạn có thể nhấn các nút này trên remote để Yolo:Bit phát ra giai điệu âm nhạc theo ý mình từ xa, thông qua mắt thu nhận tín hiệu hồng ngoại.

2. Thiết bị cần dùng 
-------
-------------

- Mạch Yolo:Bit
- Mạch mở rộng Yolo:Bit.

.. image:: images/4.1.jpg
    :width: 300px
    :align: center
| 
- Remote

.. image:: images/6.1.jpg
    :scale: 40 %
    :align: center
|
- Mắt đọc tín hiệu hồng ngoại IR

.. image:: images/6.2.jpg
    :scale: 40 %
    :align: center
|

3. Kết nối 
-------
------------

- Kết nối mắt thu tín hiệu IR vào cổng P1

.. image:: images/14.1.png
    :width: 450px
    :align: center
| 

4. Lập trình 
-------
----------

Trên mạch Yolo:Bit có tích hợp 1 loa buzzer nhỏ dùng để phát nhạc. Để sử dụng các câu lệnh phát nhạc, bạn vào mục  M NHẠC và chọn khối lệnh như bên dưới:

.. image:: images/14.2.png
    :scale: 100 %
    :align: center
|

Để sử dụng mắt thu tín hiệu IR, chúng ta sẽ sử dụng khối lệnh sau:

.. image:: images/14.3.png
    :scale: 100 %
    :align: center
|

Để phát nốt Đô (ký hiệu là C) khi nhấn nút C, ta viết chương trình như sau:

.. image:: images/14.4.png
    :scale: 100 %
    :align: center
|

Tương tự với các nốt khác như D= Rê, E=Mi, F=Fa, G=Sol, A=La, B= Si, chúng ta sẽ làm một tập hợp các khối lệnh tương ứng với nốt nhạc:

.. image:: images/14.5.png
    :scale: 100 %
    :align: center
|

Sau khi đã nhận được tín hiệu và thực hiện lệnh, chúng ta cần xóa lệnh tín hiệu đã đọc trước đó và chờ nhận tín hiệu lệnh mới, thông qua khối lệnh sau:

.. image:: images/14.8.png
    :scale: 100 %
    :align: center
|

Kết hợp các khối lệnh trên, ta sẽ được một chương trình hoàn chỉnh như hình dưới:

.. image:: images/14.6.png
    :scale: 100 %
    :align: center
|

5. Chương trình mẫu 
-------
------------

- Máy chơi nhạc: `Tại đây <https://app.ohstem.vn/#!/share/yolobit/2EWc0xGjIXMAdWlCLrtl2ahiY3W>`_

.. image:: images/14.7.png
    :width: 200px
    :align: center 