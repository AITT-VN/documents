18. Bài 15: Giao tiếp cùng đồng đội 
=========================================

*Yolo:Bit là đồng đội tiếp theo sẽ hỗ trợ Rover. Cả hai sẽ cùng giao tiếp với nhau để hoàn thành nhiệm vụ*

Mục tiêu
-----------
----------------

1. Làm quen với giao tiếp giữa 2 Yolo:Bit
2. Điều khiển cơ bản Rover với Yolo:Bit khác


Giao tiếp giữa Rover và Yolo:Bit
------------
--------------------

Các Yolo:Bit có thể giao tiếp với nhau. Bằng cách này chúng ta có thể sử dụng một Yolo:Bit khác như máy điều khiển để điều khiển hoạt động của Rover

    .. image:: images/bai_15.1.png
        :width: 400px
        :align: center 
|

**Đặt tên cho Yolo:Bit**

Để phân biệt Yolo:Bit trên Rover và Yolo:Bit còn lại chúng ta cần đặt tên cho chúng:

    1. Kết nối với Yolo:Bit

        .. image:: images/bai_15.2.png
            :width: 300px
            :align: center 


    2. Chọn mục cài đặt >> Đổi tên thiết bị

        .. image:: images/bai_15.3.png
            :width: 200px
            :align: center  


    3. Tiến hành đổi tên 

        .. image:: images/bai_15.4.png
            :width: 300px
            :align: center 


Viết chương trình
--------------
-----------------------

1. Viết thuật toán cho Yolo:Bit riêng lẻ

    .. image:: images/bai_15.5.png
        :width: 800px
        :align: center 
|
2. Tạo các sự kiện khi kết nối và ngắt kết nối Bluetooth
    
    .. image:: images/bai_15.6.png
        :width: 800px
        :align: center 
|
3. Kết nối Bluetooth tự động và sáng đèn màu đỏ

    .. image:: images/bai_15.7.png
        :width: 600px
        :align: center 
|
4. Tạo nhóm điều kiện gộp tương ứng với trạng thái nghiêng của Yolo:Bit

    .. image:: images/bai_15.8.png
        :width: 500px
        :align: center 
|
5. Đặt lệnh gửi đi tương ứng trong thuật toán

    .. image:: images/bai_15.9.png
        :width: 500px
        :align: center 
|
6. Tạm dừng 100milli giây ở cuối chương trình

    .. image:: images/bai_15.10.png
        :width: 500px
        :align: center 
|
7. Chương trình đầy đủ cho Yolo:Bit riêng lẻ

    .. image:: images/bai_15.11.png
        :width: 800px
        :align: center
|
8. Lưu chương trình vào Yolo:Bit      

    Để không bị mất chương trình trên Yolo:Bit sau khi ngắt kết nối, bạn cần lưu chương trình vào Yolo:Bit. Thực hiện như sau:

    .. image:: images/bai_15.12.png
        :width: 900px
        :align: center
|
9. Viết thuật toán cho Yolo:Bit trên Rover

    .. image:: images/bai_15.13.png
        :width: 800px
        :align: center
|
10. Viết các lệnh phù hợp với tín hiệu nhận được từ Yolo:Bit khác

    .. image:: images/bai_15.14.png
        :width: 800px
        :align: center


Chương trình mẫu
--------------
-------------------

- Giao tiếp cùng đồng đội: `Tại đây <https://app.ohstem.vn/#!/share/yolobit/2BeZHkGMwf5gCeaOPHSj5n60Inj>`_

.. image:: images/bai_15.15.png
    :width: 200px
    :align: center 




