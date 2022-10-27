4. Cảm biến độ ẩm đất điện dung
==============

.. image:: images/4.1.png
    :width: 400px
    :align: center 
| 

- Cảm biến độ ẩm đất điện dung sẽ sử dụng cảm biến điện dung để phát hiện độ ẩm của đất và phản hồi tín hiệu về. Bạn có thể ứng dụng cảm biến này vào các dự án như đo độ ẩm của đất để chăm sóc cây trồng,…

- Sản phẩm có độ bền cao, ít bị ăn mòn và có thể sử dụng lâu dài.

**1. Mua sản phẩm**
-----------
----------

..  image:: images/gio.png
    :alt: some image
    :target: https://ohstem.vn/product/cam-bien-do-am-dat-dien-dung/
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
     - .. image:: images/4.1.png
          :width: 200px
          :align: center
   * - Máy tính lập trình Yolo:Bit
     - Mạch mở rộng cho Yolo:Bit
     - Cảm biến độ ẩm đất điện dung (kèm dây Grove)
   * - `Mua sản phẩm <https://ohstem.vn/product/may-tinh-lap-trinh-yolobit/>`_
     - `Mua sản phẩm <https://ohstem.vn/product/grove-shield/>`_
     - `Mua sản phẩm <https://ohstem.vn/product/cam-bien-do-am-dat-dien-dung/>`_

- **Bước 2**: Cắm Yolo:Bit vào mạch mở rộng
- **Bước 3**: Sử dụng dây Grove cắm vào cảm biến
- **Bước 4**: Kết nối cảm biến độ ẩm đất vào **chân P1 trên mạch mở rộng**


..  figure:: images/4.2.png
    :scale: 90%
    :align: center 

..  attention::

    Cảm biến độ độ ẩm đất điện dung có giá trị trả về là analog, trên mạch mở rộng có 3 chân có giá trị analog là P0, P1, P2. Bạn có thể kết nối vào 1 trong 3 chân này để làm việc với cảm biến. 


**3. Hướng dẫn lập trình**
--------
------------

- **Bước 1:** Tải thư viện **AIOT KIT**, xem hướng dẫn tải thư viện `tại đây <https://docs.ohstem.vn/en/latest/module/cai-dat-thu-vien.html>`_


    .. image:: images/aiot.png
        :width: 300px
        :align: center 
    |

    Sau khi tải thư viện, trong danh mục khối lệnh sẽ xuất hiện các khối lệnh tương ứng:

    .. image:: images/lenh_aiot.png
        :width: 800px
        :align: center 
    |


- **Bước 2**: Gửi chương trình sau xuống Yolo:Bit

..  image:: images/3.3.png
    :scale: 100%
    :align: center 
|

.. note::

    **Giải thích chương trình:** Phần trăm độ ẩm đất sẽ được hiển thị lên màn hình LED của Yolo:Bit sau mỗi giây. 

