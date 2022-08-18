2. Bài 1: Robot Mèo dò đường
=================================

.. image:: images/meo_do_duong.jpg
    :width: 400px
    :align: center  
|

1.  Hướng dẫn lắp ráp
---------------
-------------------------

.. raw:: html

 <iframe width="560" height="315" src="https://www.youtube.com/embed/e0jEGLDBk8U?list=PLtkN2G0bngmuZSIHfJN7RDPv3TnY5HaRA" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
| 

2.  Cách thực hiện
---------------------------
----------------------

- Cho Robot đi thẳng liên tục

- Khi gặp vật cản sẽ dừng lại, đánh mắt sang phải để dò đường (quay servo đã gắn cảm biến khoảng cách sang phải). 
    
    + Nếu không có vật cản thì cho Robot rẽ phải và tiếp tục đi thẳng.
    + Nếu có vật cản thì đánh mắt sang trái để dò đường (quay servo đã gắn cảm biến khoảng cách sang trái). 

- Tiếp tục kiểm tra cảm biến khoảng cách.

    + Nếu không có vật cản thì cho Robot rẽ phải và tiếp tục đi thẳng
    + Nếu có vật cản thì cho Robot quay 180 độ và tiếp tục đi thẳng


3.  Viết chương trình
---------------------
--------------------------

1. Đầu tiên, chúng ta tạo biến **“vật cản”** để Robot có thể nhận biết vật cản (trước, phải, trái). Mỗi lần gặp vật cản, biến này sẽ cộng thêm 1 và sẽ trở về 0 nếu không còn phát hiện vật cản. 

.. image:: images/bai_1.1.png
    :width: 300px
    :align: center  
|
2.  Chúng ta khởi tạo các chế độ cho xe bằng cách sử dụng hàm.

    - Trước hết là trạng thái mặc định. Ở trạng thái này, ta thực hiện xoay mắt Robot về giữa (góc 90 độ) để Robot dò đường phía trước mặt. Cho Robot đi thẳng.

.. image:: images/bai_1.2.png
    :width: 450px
    :align: center  
|

    - Trạng thái tiếp theo sẽ hoạt động khi Robot gặp vật cản trước mặt, Robot sẽ quay đầu sang phải (góc 0 độ) để dò đường. Sau đó tiếp tục đọc cảm biến khoảng cách, nếu tiếp tục có vật cản bên phía phải thì chuyển sang dò đường bên phía trái bằng cách tăng biến “vật cản” lên 1.

.. image:: images/bai_1.3.png
    :width: 600px
    :align: center  
|

    - Tương tự như dò đường bên phải, Robot sẽ tiếp tục dò đường bên trái.

.. image:: images/bai_1.4.png
    :width: 600px
    :align: center  
|

    - Nếu sau khi dò đường bên trái mà vẫn có vật cản, thì chắc chắn là chúng ta phải “quay xe” thôi. Ngoài ra, đèn sẽ bật và có nhạc nền để báo hiệu quay xe. Sau đó ta đặt xe về trạng thái mặc định bằng cách cho biến vật cản về 0.

.. image:: images/bai_1.5.png
    :width: 500px
    :align: center  
|

    - Cuối cùng, ở chương trình chính, chúng ta cho kiểm tra cảm biến khoảng cách một cách liên tục để chuyển trạng thái cho Robot khi Robot gặp vật cản.

.. image:: images/bai_1.6.png
    :width: 600px
    :align: center  
|


4. Chương trình mẫu
--------------
-------------------

- Nhấp vào chữ **tại đây** để xem chương trình mẫu, hoặc quét mã QR bên dưới để xem chương trình.

- Robot Mèo dò đường: `Tại đây <https://app.ohstem.vn/#!/share/yolobit/2DQ4vfyrjzSZteuAPKMeztt1EOg>`_

.. image:: images/bai_1.7.png
    :width: 200px
    :align: center 
| 

