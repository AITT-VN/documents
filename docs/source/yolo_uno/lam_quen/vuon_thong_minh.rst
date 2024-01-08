10. Vườn thông minh
=========

1. Mục tiêu
-----
--------

Với hướng dẫn này, chúng ta thực hiện dự án “Vườn thông minh” với chức năng đo độ ẩm của đất sau mỗi giây, nếu độ ẩm nhỏ hơn 30% thì sẽ bật máy bơm cho đến khi độ ẩm đạt 70%. 

2. Thiết bị cần sử dụng
---------
----------

- Mạch Yolo UNO:

..  image:: images/yolo_uno.png
    :scale: 60%
    :align: center 
|

- Cảm biến độ ẩm đất kèm dây tín hiệu: 

..  image:: images/cb_do_am_dat.png
    :scale: 60%
    :align: center 
|

- Máy bơm mini:

..  image:: images/may_bom.png
    :scale: 50%
    :align: center 
|

- Module đóng ngắt 2 kênh, kèm dây tín hiệu: 

..  image:: images/dong_ngat.png
    :scale: 50%
    :align: center 
|

3. Kết nối phần cứng
-------
--------

- Kết nối cảm biến độ ẩm đất vào chân A1 - A2, do độ ẩm đất trả về giá trị Analog

- Kết nối máy bơm mini vào cổng USB_Output1 trên module đóng ngắt 2 kênh.

- Kết nối module đóng ngắt 2 kênh vào chân D9 - D10. 

..  figure:: images/vuon_1.png
    :scale: 100%
    :align: center 
|

4. Chương trình lập trình
------
------

- **Giới thiệu khối lệnh:**

..  image:: images/vuon_2.png
    :scale: 100%
    :align: center 
|
    
*Câu lệnh bật tắt quạt với các mức độ khác nhau từ 0 đến 100 %.*

..  image:: images/vuon_3.png
    :scale: 100%
    :align: center 
|

*Câu lệnh điều khiển thiết bị được kết nối trên Module đóng ngắt 2 kênh, ở các mức độ khác nhau từ 0 - 100%.*

Với hình kết nối trên, máy bơm được kết nối vào cổng USB 1, ở chân D9 - D10. Do đó, lập trình điều khiển máy bơm ở chân D9. 

- **Chương trình lập trình:**

..  image:: images/vuon_4.png
    :scale: 100%
    :align: center 
|

5. Chương trình mẫu
----
-----

Nhấp vào chữ tại đây để xem chương trình mẫu, hoặc quét mã QR bên dưới để xem chương trình.

Vườn thông minh: `Tại đây <https://app.ohstem.vn/#!/share/yolouno/2aTu7jGpV6HlFsOhzy6AKYax5Xr>`_

..  image:: images/vuon_5.png
    :scale: 100%
    :align: center 
|