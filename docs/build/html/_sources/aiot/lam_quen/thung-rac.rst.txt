15. Thùng rác thông minh
=============

1. Mục tiêu 
----------
---------------

Trong dự án này, chúng ta sẽ sử dụng cảm biến siêu âm và động cơ Servo để chế tạo ra một thùng rác thông minh, có thể tự đóng mở khi có người lại gần trong phạm vi được quy định trước.

2. Thiết bị cần dùng 
-------
-------------

- Mạch Yolo:Bit
- Mạch mở rộng Yolo:Bit.

.. image:: images/4.1.jpg
    :width: 300px
    :align: center
|

- Cảm biến siêu âm

.. image:: images/13.1.jpg
    :scale: 40 %
    :align: center
|

- Động cơ Servo 

.. image:: images/11.1.jpg
    :scale: 40 %
    :align: center
|

3. Kết nối 
-------
------------

- Kết nối cảm biến siêu âm với cổng P10/13
- Kết nối Servo ở hàng chân P6:

.. image:: images/15.1.png
    :width: 600px
    :align: center
| 

4. Lập trình 
-------
----------

**Yêu cầu của dự án:** Cảm biến siêu âm sẽ kiểm tra khoảng cách, nếu khoảng cách bé hơn 10cm thì sẽ xuất tín hiệu điều khiển servo quay 1 góc 90 độ để mở thùng rác, sau 4 giây sẽ tự động đóng nắp thùng rác lại.

Tương tự như ở các dự án trước, để sử dụng cảm biến đo khoảng cách, chúng ta cần khai báo chân cắm cho cảm biến ở phần bắt đầu của chương trình:

.. image:: images/15.2.png
    :scale: 100 %
    :align: center
|

Để kiểm tra điều kiện của cảm biến khoảng cách, chúng ta sẽ sử dụng câu điều kiện. Servo sẽ đóng hoặc mở thùng rác, tùy theo khoảng cách mà cảm biến đọc được:

.. image:: images/15.3.png
    :scale: 100 %
    :align: center
|

Nếu khoảng cách bé hơn 10cm, hệ thống sẽ thực hiệu quay servo chân P6 đến vị trí 90 độ sau đó chờ 3000ms giây (tương ứng với 3s), sau đó đóng nắp lại.

Chương trình hoàn chỉnh sẽ như sau:

.. image:: images/15.4.png
    :scale: 80 %
    :align: center
|

5. Chương trình mẫu 
-------
------------

- Thùng rác thông minh: `Tại đây <https://app.ohstem.vn/#!/share/yolobit/2EWd4DaPo061chR83xgXxLnovdH>`_

.. image:: images/15.5.png
    :width: 200px
    :align: center 