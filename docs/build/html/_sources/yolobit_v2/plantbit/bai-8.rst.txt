11. Bài 8: Bật tắt đèn tự động
=====================================

Mục tiêu
----------------
----------------

Để cây có đủ ánh sáng và sinh trưởng tốt hơn, chúng ta sẽ lập trình một tính năng thông minh cho Plant:Bit đó là: tự động bật đèn LED màu khi cây thiếu sáng (độ sáng của môi trường dưới 30) và tắt đèn khi đủ độ sáng.

Thiết bị cần dùng
-----------------
-----------------

- Mạch mở rộng gắn sẵn Yolo:Bit

.. image:: images/planbit_31.png
    :width: 200px
    :align: center
|
- Cảm biến ánh sáng

.. image:: images/planbit_60.png
    :width: 200px
    :align: center
|
-  Module đóng ngắt 2 kênh

.. image:: images/planbit_45.png
    :width: 200px
    :align: center
|
- Đèn LED màu 

.. image:: images/planbit_71.png
    :width: 200px
    :align: center
|


Kết nối
----------------
----------------

Kiểm tra lại kết nối tương tự như bài 6 và bài 7

    - Bài 6: Kết nối Module đóng ngắt 2 kênh vào cổng P14/P15. Kết nối đèn LED màu vào cổng USB Ouput2
   
    - Bài 7: Cảm biến ánh sáng nối vào chân P1


Viết chương trình
------------------
------------------

1. Tạo điều kiện: Nếu độ sáng ngoài trời ≤ 30 (cách thực hiện như bài 2)

.. image:: images/planbit_83.png
    :width: 500px
    :align: center
|
2. Nếu độ sáng ngoài trời ≤ 30, bật đèn LED màu với mức sáng là 70

.. image:: images/planbit_84.png
    :width: 600px
    :align: center
|
3. Nếu không, tắt đèn LED màu

.. image:: images/planbit_85.png
    :width: 600px
    :align: center
|

Chương trình mẫu
---------------------
---------------------

- Bật tắt đèn tự động: `Tại đây <https://app.ohstem.vn/#!/share/yolobit/2Cysomj5j0LLxeodbFFhkbV8lOw>`_

.. image:: images/planbit_86.png
    :width: 200px
    :align: center
|

