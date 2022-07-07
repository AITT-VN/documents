18. Bài 14: Chỉ huy từ xa
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
            :scale: 65%
            :align: center   

    
    2. Giao diện Gamepad ảo

        .. image:: images/bai_14.2.png
            :scale: 65%
            :align: center   


Giới thiệu khối lệnh 
-----------------
---------------------------

- Khối lệnh sử dụng Bluetooth:

    .. image:: images/bai_14.3.png
        :scale: 65%
        :align: center   


- Khối lệnh đổi màu đèn LED:

    .. image:: images/bai_14.4.png
        :scale: 65%
        :align: center   


Viết chương trình
-----------
------------------

1. Viết thuật toán

    .. image:: images/bai_14.5.png
        :scale: 65%
        :align: center   


2. Bắt đầu, cho đèn LED hiển thị màu đỏ. Khi kết nối Bluetooth thành công, đèn LED chuyển sang màu xanh lá. Nếu bị ngắt kết nối, LED chuyển sang đỏ:

    .. image:: images/bai_14.6.png
        :scale: 65%
        :align: center 


3. Tạo sự kiện khi nhận được chuỗi: Nếu chuỗi là nút ↑ được nhấn, Rover tiến tới với tốc độ 50

    .. image:: images/bai_14.7.png
        :scale: 65%
        :align: center 


4. Tiếp tục, tạo thêm các điều kiện gộp tương ứng với các nút ↓ → ←

    .. image:: images/bai_14.8.png
        :scale: 65%
        :align: center 


5. Khi tất cả các điều kiện không đúng, dừng di chuyển

    .. image:: images/bai_14.9.png
        :scale: 65%
        :align: center




