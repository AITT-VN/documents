13. Máy rửa tay không chạm
=====================================

1. Mục tiêu 
----------
---------------

Thực hiện một hệ thống máy rửa tay không tiếp xúc sử dụng cảm biến siêu âm và bơm mini góp phần phòng chống các bệnh lây nhiễm.

2. Thiết bị cần dùng 
-------
-------------

- Mạch Yolo:Bit
- Mạch mở rộng Yolo:Bit.

.. image:: images/4.1.jpg
    :width: 300px
    :align: center
|

- Module đóng ngắt 2 kênh

.. image:: images/12.2.jpg
    :scale: 40 %
    :align: center
|

- Máy bơm mini

.. image:: images/12.3.jpg
    :scale: 40 %
    :align: center
|

- Cảm biến siêu âm

.. image:: images/13.1.jpg
    :scale: 40 %
    :align: center
|

3. Kết nối 
-------
------------

- Kết nối module đóng ngắt 2 kênh vào cổng P14/15
- Kết nối máy bơm mini ở cổng output1
- Kết nối cảm biến siêu âm với cổng P10/13

.. image:: images/13.2.png
    :width: 500px
    :align: center
| 

4. Lập trình 
-------
----------

- **Giới thiệu khối lệnh**
Để làm việc cảm biến siêu âm, chúng ta sẽ sử dụng các khối lệnh sau:

.. image:: images/13.3.png
    :scale: 100 %
    :align: center
| 

Khối lệnh đầu tiên sẽ giúp chúng ta đo khoảng cách từ cảm biến đến vật thể. Khối lệnh thứ 2 sẽ đo khoảng cách từ cảm biến và so sánh với điều kiện nhập vào. 

- **Lập trình**

Khi sử dụng cảm biến siêu âm, trước tiên, chúng ta cần khai báo tên cổng mà bạn cắm cảm biến trên mạch mở rộng:

.. image:: images/13.4.png
    :scale: 100 %
    :align: center
| 

Ở dự án này, để đơn giản nhất, chúng ta sẽ sử dụng khối lệnh thứ 2: 

.. image:: images/13.5.png
    :scale: 100 %
    :align: center
| 

Chúng ta sẽ kết hợp khối lệnh trên với câu lệnh điều kiện để viết chương trình: Nếu khoảng cách bé hơn 5cm, máy bơm sẽ bật 3 giây rồi tắt. Ngược lại, nếu khoảng cách lớn hơn 5cm,  máy bơm sẽ không hoạt động.

Chương trình sẽ như sau:

.. image:: images/13.6.png
    :scale: 100 %
    :align: center
| 

Ghép hai chương trình lại với nhau, ta có chương trình hoàn chỉnh như sau:

.. image:: images/13.7.png
    :scale: 80 %
    :align: center
| 


5. Chương trình mẫu 
-------
------------

- Máy rửa tay tự động: `Tại đây <https://app.ohstem.vn/#!/share/yolobit/2EWaqT2WCLVzMDowaSU8ntHQa63>`_

.. image:: images/13.8.png
    :width: 200px
    :align: center 