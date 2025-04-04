3. Đèn thông minh
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

- Đèn LED đơn kèm dây tín hiệu: 

..  image:: images/led_don.png
    :scale: 40%
    :align: center 
|

- Màn hình LCD kèm dây tín hiệu:

..  image:: images/cb_anh_sang.png
    :scale: 50%
    :align: center 
|

3. Kết nối phần cứng
-------
--------

- Module LED đơn kết nối vào cổng D3 - D4

- Module cảm biến ánh sáng kết nối vào cổng A1 - A2

..  figure:: images/3.2.png
    :scale: 80%
    :align: center 


4. Chương trình lập trình
------
------

- Câu lệnh điều kiện, khối lệnh nằm trong mục **LOGIC**:

..  image:: images/den_thong_minh_2.png
    :scale: 90%
    :align: center 
|
    
- Câu lệnh đọc kết quả của cảm biến ánh sáng, nằm trong mục **CẢM BIẾN**:: 

..  image:: images/den_thong_minh_3.png
    :scale: 80%
    :align: center    
|

- Câu lệnh đọc bắt đèn đèn LED đơn, nằm trong mục **HIỂN THỊ**:: 

..  image:: images/3.4.png
    :scale: 70%
    :align: center    
|

- **Chương trình lập trình:**

..  figure:: images/3.3.png
    :scale: 70%
    :align: center 

    `<https://app.ohstem.vn/#!/share/yolouno/2vFWXwvS5PbkhKooSzyJ0qrIkU8>`_

- **Giải thích chương trình:**  Sau khi thực hiện gửi chương trình lên Yolo UNO, đèn LED trên Yolo UNO sẽ chuyển sang đèn xanh. Hãy thử dùng tay che cảm biến ánh sáng, đèn LED sẽ sáng. 