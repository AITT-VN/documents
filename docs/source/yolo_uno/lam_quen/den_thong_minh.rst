7. Đèn thông minh
======

1. Mục tiêu
-----
--------

Chúng ta hãy cùng lập trình một chiếc đèn thông minh, có thể bật tắt tự động dựa vào ánh sáng nhé. Cụ thể, khi trời tối (độ sáng < 30%) thì đèn sẽ tự bật. Ngược lại, khi trời sáng thì đèn sẽ tự tắt.

2. Thiết bị cần sử dụng
---------
----------

- Mạch Yolo UNO:

..  image:: images/yolo_uno.png
    :scale: 60%
    :align: center 
|

- Module led RGB kèm dây tín hiệu: 

..  image:: images/tiny_rgb.png
    :scale: 90%
    :align: center 
|

- Module cảm biến ánh sáng kèm dây tín hiệu:

..  image:: images/cb_anh_sang.png
    :scale: 90%
    :align: center 
|

3. Kết nối phần cứng
-------
--------

- Module Led RGB kết nối vào cổng D3 - D4

- Module cảm biến ánh sáng kết nối vào cổng A1 - A2

..  figure:: images/den_thong_minh_1.png
    :scale: 100%
    :align: center 

    Cảm biến ánh sáng có giá trị trả về là analog, do đó bạn có thể kết nối với các chân P0, P1, P2 trên mạch mở rộng


4. Chương trình lập trình
------
------

- **Câu lệnh điều kiện:**

Trong phần này, chúng ta sẽ dùng đến khối lệnh điều kiện trong mục LOGIC:

..  image:: images/den_thong_minh_2.png
    :scale: 90%
    :align: center 
|
    
Câu lệnh đọc kết quả của cảm biến ánh sáng: 

..  image:: images/den_thong_minh_3.png
    :scale: 80%
    :align: center    
|

- **Chương trình lập trình:**

..  image:: images/den_thong_minh_4.png
    :scale: 80%
    :align: center 
|

5. Chương trình mẫu
----
-----

Nhấp vào chữ tại đây để xem chương trình mẫu, hoặc quét mã QR bên dưới để xem chương trình.

Đèn thông minh: `Tại đây <https://app.ohstem.vn/#!/share/yolouno/2aLkkP7V7pWAljBZJrYZPhB9lvo>`_

..  image:: images/den_thong_minh_5.png
    :scale: 100%
    :align: center 
|
