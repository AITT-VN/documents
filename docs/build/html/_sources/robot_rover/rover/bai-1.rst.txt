4. Bài 1: Cùng di chuyển nào
=================================

*Xin chào các bạn! Đã đến lúc bắt đầu hành trình khám phá những điều mới rồi! Hãy bắt đầu cùng Rover nào.*


Mục tiêu
---------------------
---------------------

- Hiểu được cách điều khiển động cơ để di chuyển cơ bản.


Bộ phận điện tử
---------------
-------------------------

- Động cơ là bộ phận giúp Robot Rover có thể di chuyển (tới, lùi, rẽ,...) cùng với tốc độ tùy chỉnh.

.. image:: images/bai_1.4.png
    :width: 300px
    :align: center
|    
- Rover có 2 động cơ bên trái và bên  phải, để Rover di chuyển, chúng ta  cần điều khiển 2 động cơ này

.. image:: images/bai_1.5.png
    :width: 300px
    :align: center
|    

Giới thiệu khối lệnh
---------------------------
----------------------

- Khối lệnh bắt đầu chương trình:

.. image:: images/bai_1.6.png
    :width: 400px
    :align: center
| 
- Khối lệnh lặp lại số lần:

.. image:: images/bai_1.7.png
    :width: 400px
    :align: center
|   
- Khối lệnh di chuyển:

 .. image:: images/bai_1.8.png
    :width: 1200px
    :align: center
|    


Viết chương trình
---------------------
--------------------------

**Chương trình đơn giản:** Đây là chương trình điều khiển Rover đi tới và lùi, giúp bạn làm quen với lập trình điều khiển Rover di chuyển

    1.  Gắn khối lệnh di chuyển vào lệnh lặp lại mãi

    .. image:: images/bai_1.9.png
        :width: 800px
        :align: center  
    |
    2. Chọn hướng di chuyển và chỉnh tốc độ mong muốn

        - Có 4 hướng di chuyển: tiến tới, lùi lại, rẽ trái, rẽ phải tương ứng với hình dạng mũi tên.

        - Tốc độ của động cơ có giá trị từ 0 (đứng yên) đến 100 (tối đa).

    .. image:: images/bai_1.10.png
        :width: 400px
        :align: center
    |
    3. Thêm khối tạm dừng 1 giây (1000ms)

    .. image:: images/bai_1.11.png
        :width: 700px
        :align: center
    |
    4. Làm tương tự để tạo thêm lệnh đi lùi trong 1 giây

    .. image:: images/bai_1.12.png
        :width: 400px
        :align: center
    |
    5. Chạy chương trình

    .. image:: images/bai_1.13.png
        :width: 700px
        :align: center 
    |
    6.  Bạn có thể nhấn nút tạm dừng để dừng chương trình lại

    .. image:: images/bai_1.14.png
        :width: 70px
        :align: center 
    


**Chương trình di chuyển với thời gian:**  Chương trình này sẽ giúp Rover đi theo hình vuông

    1.  Gắn khối lệnh lặp số lần vào lệnh bắt đầu

    .. image:: images/bai_1.15.png
        :width: 700px
        :align: center 
    |  
    2. Sử dụng các khối lệnh di chuyển để hoàn thiện chương trình như hình minh họa (để ý các thông số)

    .. image:: images/bai_1.16.png
        :width: 600px
        :align: center 
    |


Chương trình mẫu
--------------
-------------------

- Nhấp vào chữ **tại đây** để xem chương trình mẫu, hoặc quét mã QR bên dưới để xem chương trình.

- Robot di chuyển tới lui: `Tại đây <https://app.ohstem.vn/#!/share/yolobit/2BeTmtVhptwmDZJMtzCrBz2Hc5n>`_

.. image:: images/bai_1.17.png
    :width: 200px
    :align: center 
| 
- Robot di chuyển hình vuông: `Tại đây <https://app.ohstem.vn/#!/share/yolobit/2BeTxamvWwDappzIrPkZx9j7xl3>`_

.. image:: images/bai_1.18.png
    :width: 200px
    :align: center 
