9. Bài 6: Bật tắt đèn LED
===================================

Mục tiêu
----------------------
----------------------

Trong bài này chúng ta sẽ sử dụng nút A và B trên Yolo:Bit để bật tắt đèn LED màu - loại đèn LED có bước sóng thích hợp giúp cây tăng trưởng nhanh hơn trong điều kiện thiếu sáng.

Thiết bị cần dùng
----------------------
----------------------

- Mạch mở rộng gắn sẵn Yolo:Bit

.. image:: images/planbit_31.png
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
----------------------
----------------------

- Kết nối Module đóng ngắt 2 kênh vào cổng P14/P15
- Kết nối đèn LED màu vào cổng USB Output2

.. image:: images/planbit_72.png
    :width: 400px
    :align: center
|


Giới thiệu khối lệnh
----------------------
----------------------

.. image:: images/planbit_73.png
    :width: 600px
    :align: center
|


Viết chương trình
----------------------
----------------------

1. Bắt đầu với **khối lệnh khi nút được nhấn**

.. image:: images/planbit_74.png
    :width: 300px
    :align: center
|
2. Kéo thả **khối lệnh bật đèn LED màu** vào **khối lệnh khi nút được nhấn**

.. image:: images/planbit_75.png
    :width: 600px
    :align: center
|
3. Tương tự, khi nút B được nhấn, đèn sẽ tắt (mức sáng = 0)

.. image:: images/planbit_76.png
    :width: 600px
    :align: center
|


Chương trình mẫu
---------------------
---------------------

- Bật tắt đèn LED: `Tại đây <https://app.ohstem.vn/#!/share/yolobit/2Cyr51G6ISAKoJhKNoR22OYrQW3>`_

.. image:: images/planbit_77.png
    :width: 200px
    :align: center
|