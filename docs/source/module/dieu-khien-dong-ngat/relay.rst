5. Công tắc điện tử Relay
============

.. image:: images/5.1.png
    :width: 400px
    :align: center 
| 

- Relay là một công tắc điện từ được vận hành bởi một dòng điện tương đối nhỏ có thể bật hoặc tắt một dòng điện lớn hơn nhiều. Ta có thể sử dụng relay để điều khiển những động cơ tiêu thụ công suất lớn, đóng ngắt nguồn điện nhỏ khác,…

**1. Mua sản phẩm**
-----------
----------

..  image:: images/gio.png
    :alt: some image
    :target: https://ohstem.vn/product/relay/
    :class: with-shadow
    :scale: 100%
    :align: center
|

**2. Thông số kỹ thuật**
------------
-------------

- **Thông số kỹ thuật của Relay**

    + Điện áp: 3.3VDC
    + Dòng chịu đựng: 3A
    + Không có bảo vệ ngược cực, cần chú ý khi cấp nguồn
    + Tín hiệu điều khiển: Digital
    + Kích thước của mạch: 24mm x 48mm x 16mm


- **Pinout của Relay**

Module relay có 3 chân, và mỗi chân có chức năng như sau:

..  csv-table:: 
    :header: "STT", "Chân", "Chức năng"
    :widths: 10, 15, 30

    1, "GND", "Nối đất"
    2, "VCC", "Cấp nguồn"
    3, "NC", "Không sử dụng"
    4, "SIG", "Tín hiệu điều khiển"


**3. Kết nối**
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
     - Relay (kèm dây Grove)
   * - `Mua sản phẩm <https://ohstem.vn/product/may-tinh-lap-trinh-yolobit/>`_
     - `Mua sản phẩm <https://ohstem.vn/product/grove-shield/>`_
     - `Mua sản phẩm <https://ohstem.vn/product/relay/>`_


- **Bước 2**: Cắm Yolo:Bit vào mạch mở rộng
- **Bước 3**: Sử dụng dây Grove cắm vào relay
- **Bước 4**: Kết nối thiết bị vào **chân P0 trên mạch mở rộng**

..  figure:: images/5.2.png
    :scale: 100%
    :align: center 

    Relay có thể kết nối vào cổng điều khiển có 2 tín hiệu. 

**4. Hướng dẫn lập trình**
--------
------------

- Sử dụng các câu lệnh trong danh mục **CHÂN CẮM**, để làm việc với Relay. 

- Gửi chương trình sau xuống Yolo:Bit: 

..  figure:: images/5.3.png
    :scale: 100%
    :align: center 
|

.. note::

    **Giải thích chương trình:**

    Trong chương trình trên, câu lệnh hiện hình ảnh (YES/NO), tương ứng với 2 trạng thái bật và tắt của Relay. Khi hình ảnh trên 25 đèn của Yolo:Bit thay đổi, sẽ có một âm thanh nhẹ phát ra. Đó là lúc chân COM thay đổi kết nối với NO hoặc NC. Đây cũng là âm thanh đặc trưng để nhận biết rằng Relay đang hoạt động.
