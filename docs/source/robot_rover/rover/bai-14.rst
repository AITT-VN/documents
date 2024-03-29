17. Bài 14: Chỉ huy từ xa
=======================================

*Khi thực thi nhiệm vụ, Rover cần phải tuân theo hiệu lệnh của cấp trên, để hoàn thành các nhiệm vụ một cách tốt nhất. Bạn hãy chỉ huy và truyền đạt lại yêu cầu cho Rover nhé!*


Mục tiêu
------------
--------------

1. Làm quen với giao diện GamePad trên OhStem App
2. Lập trình điều khiển Rover với giao diện GamePad


Điều khiển bằng GamePad
---------------
------------------------

Trên OhStem App đã tích hợp sẵn một GamePad ảo, bạn có thể sử dụng giao diện này để điều khiển Rover từ xa

    1.  Chọn Menu Gamepad

        .. image:: images/bai_14.1.png
            :width: 150px
            :align: center   

    
    2. Giao diện Gamepad ảo

        .. image:: images/bai_14.2.png
            :width: 400px
            :align: center   


Giới thiệu khối lệnh 
-----------------
---------------------------

- Khối lệnh sử dụng Bluetooth:

    .. image:: images/bai_14.3.png
        :width: 900px
        :align: center   


- Khối lệnh đổi màu đèn LED:

    .. image:: images/bai_14.4.png
        :width: 600px
        :align: center   


Viết chương trình
-----------
------------------

1. Viết thuật toán

    .. image:: images/bai_14.5.png
        :width: 800px
        :align: center   
|
2. Bắt đầu, cho đèn LED hiển thị màu đỏ. Khi kết nối Bluetooth thành công, đèn LED chuyển sang màu xanh lá. Nếu bị ngắt kết nối, LED chuyển sang đỏ:

    .. image:: images/bai_14.6.png
        :width: 800px
        :align: center 
|
3. Tạo sự kiện khi nhận được chuỗi: Nếu chuỗi là nút ↑ được nhấn, Rover tiến tới với tốc độ 50

    .. image:: images/bai_14.7.png
        :width: 500px
        :align: center 
|
4. Tiếp tục, tạo thêm các điều kiện gộp tương ứng với các nút ↓ → ←

    .. image:: images/bai_14.8.png
        :width: 500px
        :align: center 
|
5. Khi tất cả các điều kiện không đúng, dừng di chuyển

    .. image:: images/bai_14.9.png
        :width: 800px
        :align: center


Chương trình mẫu
--------------
-------------------

- Chỉ huy từ xa: `Tại đây <https://app.ohstem.vn/#!/share/yolobit/2BeYnFfI3AtZaNJWfiKsVTP47iy>`_

.. image:: images/bai_14.10.png
    :width: 200px
    :align: center 

