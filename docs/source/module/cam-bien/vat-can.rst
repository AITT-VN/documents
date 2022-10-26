5. Cảm biến vật cản hồng ngoại 
==============

.. image:: images/5.1.png
    :width: 400px
    :align: center 
| 

- Cảm biến vật cản sử dụng tia hồng ngoại để phát hiện có vật cản ở trước mặt hay không, với khoảng cách gần. 

- **Các ứng dụng:** 
    
    + Thùng rác thông minh giúp phát hiện rác đầy
    + Máy rửa tay tự động… 

**1. Mua sản phẩm**
-----------
----------

..  image:: images/gio.png
    :alt: some image
    :target: https://ohstem.vn/product/cam-bien-vat-can/
    :class: with-shadow
    :scale: 100%
    :align: center
|

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
     - .. image:: images/5.1.png
          :width: 200px
          :align: center
   * - Máy tính lập trình Yolo:Bit
     - Mạch mở rộng cho Yolo:Bit
     - Cảm biến vật cản (kèm dây Grove)
   * - `Mua sản phẩm <https://ohstem.vn/product/may-tinh-lap-trinh-yolobit/>`_
     - `Mua sản phẩm <https://ohstem.vn/product/grove-shield/>`_
     - `Mua sản phẩm <https://ohstem.vn/product/cam-bien-vat-can/>`_


- **Bước 2**: Cắm Yolo:Bit vào mạch mở rộng
- **Bước 3**: Sử dụng dây Grove cắm vào cảm biến
- **Bước 4**: Kết nối thiết bị vào **chân P0 trên mạch mở rộng**

..  figure:: images/5.2.png
    :scale: 100%
    :align: center 

    Cảm biến vật cản bạn có thể kết nối vào bất kỳ chân nào trên mạch mở rộng

**3. Hướng dẫn lập trình**
--------
------------

- Gửi chương trình sau vào Yolo:Bit: 

.. image:: images/5.3.png
    :scale: 100%
    :align: center 
|

.. note::

    Sử dụng câu lệnh **trạng thái bật tắt của chân P0** trong danh mục **CHÂN CẮM** để làm việc với cảm biến. 

        - Nếu chân P0 ở trạng thái là Tắt, khi đó cảm biến phát hiện có vật cản. Đèn LED sẽ chuyển sang màu vàng. 
        - Ngược lại, đèn sẽ tắt. 
    
    Chương trình được lặp lại liên tục
