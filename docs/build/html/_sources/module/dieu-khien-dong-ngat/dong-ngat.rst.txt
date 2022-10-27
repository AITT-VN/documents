2. Module đóng ngắt 2 kênh
==========

.. image:: images/2.1.png
    :width: 400px
    :align: center 
| 

- Module đóng ngắt 2 kênh thường được dùng để điều khiển bật tắt các thiết bị sử dụng cổng USB như máy bơm, đèn LED màu,…

- Module này có chức năng chuyển đổi từ cổng tín hiệu Grove sang cổng cắm USB, để bạn dễ dàng kết nối với các module điện tử phù hợp


**1. Mua sản phẩm**
-----------
----------

..  image:: images/gio.png
    :alt: some image
    :target: https://ohstem.vn/product/module-dong-ngat-2-kenh/
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
     - .. image:: images/2.1.png
          :width: 200px
          :align: center
     - .. image:: images/may_bom.png
          :width: 300px
          :align: center
   * - Máy tính lập trình Yolo:Bit
     - Mạch mở rộng cho Yolo:Bit
     - Module đóng ngắt (kèm dây Grove) 
     - Máy bơm mini 
   * - `Mua sản phẩm <https://ohstem.vn/product/may-tinh-lap-trinh-yolobit/>`_
     - `Mua sản phẩm <https://ohstem.vn/product/grove-shield/>`_
     - `Mua sản phẩm <https://ohstem.vn/product/module-dong-ngat-2-kenh/>`_
     - `Mua sản phẩm <https://ohstem.vn/product/may-bom-mini/>`_


- **Bước 2**: Cắm Yolo:Bit vào mạch mở rộng

- **Bước 3**: Kết nối máy bơm mini với module đóng ngắt 2 kênh

- **Bước 4**: Kết nối thiết bị vào **chân P14/P15 trên mạch mở rộng**


..  figure:: images/2.2.png
    :scale: 100%
    :align: center 

    Để làm việc với module đóng ngắt 2 kênh, bạn sẽ kết nối vào cổng có 2 chân kết nối.

**3. Hướng dẫn lập trình**
--------
------------

- Sử dụng các khối lệnh trong danh mục **CHÂN CẮM** để làm việc với đèn module đóng ngắt 2 kênh. 

- Gửi chương trình sau vào Yolo:Bit: 

..  figure:: images/2.3.png
    :scale: 100%
    :align: center 

    Chương trình bật tắt máy bơm kết nối với cổng USB thứ hai. 

.. note::

    Trong trường hợp muốn điều khiển đồng thời 2 máy bơm, trong chương trình sẽ thêm câu lệnh điều khiển bật tắt trạng thái chân P14. Và máy bơm còn lại sẽ kết nối với cổng USB thứ 1.

- **Hoặc có thể sử dụng câu lệnh sau trong thư viện AIoT KIT để điều khiển module đóng ngắt 2 kênh:**

.. image:: images/2.4.png
    :scale: 100%
    :align: center