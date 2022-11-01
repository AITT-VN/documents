1. Geek Servo 270 tương thích với Lego
==============

.. image:: images/1.1.png
    :width: 400px
    :align: center 
| 

Động cơ Geek Servo 270 tương thích với Lego, có thể dùng để lắp ráp vào các mô hình sáng tạo theo ý thích.

**1. Mua sản phẩm**
-----------
----------

..  image:: images/gio.png
    :alt: some image
    :target: https://ohstem.vn/product/geek-servo-270/
    :class: with-shadow
    :scale: 100%
    :align: center

**2. Kết nối**
------------
------------

- **Bước 1**: Chuẩn bị các thiết bị như sau: 

.. list-table:: 
   :widths: auto
   :header-rows: 1
     
   * - .. image:: images/yolo.png
          :width: 200px
          :align: center
     - .. image:: images/mmr.png
          :width: 200px
          :align: center
     - .. image:: images/1.1.png
          :width: 200px
          :align: center
   * - Máy tính lập trình Yolo:Bit
     - Mạch mở rộng cho Yolo:Bit
     - Động cơ Servo 270
   * - `Mua sản phẩm <https://ohstem.vn/product/may-tinh-lap-trinh-yolobit/>`_
     - `Mua sản phẩm <https://ohstem.vn/product/grove-shield/>`_
     - `Mua sản phẩm <https://ohstem.vn/product/geek-servo-270/>`_


- **Bước 2**: Cắm Yolo:Bit vào mạch mở rộng

- **Bước 3**: Kết nối thiết bị vào **chân P4 trên mạch mở rộng**

.. image:: images/1.2.png
    :width: 400px
    :align: center 
| 

**3. Hướng dẫn lập trình**
--------
------------

- Sử dụng các câu lệnh trong danh mục **CHÂN CẮM** để làm việc với Servo.

- Trước khi lập trình với Servo bạn cần chỉnh Servo về góc 20 trước khi lập trình, để xác định góc của servo. 

.. image:: images/1.3.png
    :scale: 100%
    :align: center
| 
- Sau đó gửi chương trình sau xuống Yolo:Bit: 

.. image:: images/1.4.png
    :scale: 100%
    :align: center
| 

.. note:: 
    **Giải thích chương trình**:

    Chương trình mô phỏng một cánh cửa tự động từ servo, nếu nút A được nhấn thì cửa mở (góc 20), nút B nhấn thì cửa đóng (góc 90)
