22. Keypad - Bàn phím cảm ứng điện dung
====================

.. image:: images/23.1.png
    :width: 400px
    :align: center 
|

- Bàn phím cảm ứng điện sử dụng IC chuyên dụng MPR121 có khả năng nhận biết điện dung từ tay người qua 12 vị trí cảm ứng với độ chính xác và độ nhạy cao, bàn phím phù hợp với các ứng dụng cần độ bền, tạo sự độc đáo và chuyên nghiệp trong các ứng dụng điều khiển cảm ứng, bàn phím sử dụng giao tiếp I2C rất dễ kết nối và giao tiếp chỉ với 2 chân GPIO.


**1. Mua sản phẩm**
-----------
----------

..  image:: images/gio.png
    :alt: some image
    :target: https://ohstem.vn/product/keypad-ban-phim-cam-ung-dien-dung/
    :class: with-shadow
    :scale: 100%
    :align: center
|

**2. Thông số kỹ thuật**
---------
------------

- **Thông số kỹ thuật**

    + IC chính: MPR121
    + Điện áp sử dụng: 3.3VDC
    + Giao tiếp: I2C
    + Mức logic giao tiếp: TTL 3.3V


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
     - .. image:: images/23.1.png
          :width: 200px
          :align: center
   * - Máy tính lập trình Yolo:Bit
     - Mạch mở rộng cho Yolo:Bit
     - Keypad (kèm dây Grove)
   * - `Mua sản phẩm <https://ohstem.vn/product/may-tinh-lap-trinh-yolobit/>`_
     - `Mua sản phẩm <https://ohstem.vn/product/grove-shield/>`_
     


- **Bước 2**: Cắm Yolo:Bit vào mạch mở rộng
- **Bước 3**: Sử dụng dây Grove cắm vào cảm biến
- **Bước 4**: Kết nối cảm biến với **I2C trên mạch mở rộng**.

..  figure:: images/23.2.png
    :scale: 100%
    :align: center 

    Bạn có thể kết nối cảm biến vào 1 trong 2 chân I2C trên mạch mở rộng



**4. Hướng dẫn lập trình**
--------
------------

- **Bước 1:** Tải thư viện **Bàn phím cảm ứng**, xem hướng dẫn tải thư viện `tại đây <https://docs.ohstem.vn/en/latest/module/cai-dat-thu-vien.html>`_


    .. image:: images/banphim.png
        :width: 250px
        :align: center 
    |

    Sau khi tải thư viện, trong danh mục khối lệnh sẽ xuất hiện các khối lệnh tương ứng:

    .. image:: images/lenh_banphim.png
        :scale: 100%
        :align: center 
    |

- **Bước 2**: Gửi chương trình sau xuống Yolo:Bit

    ..  image:: images/23.3.png
        :scale: 100%
        :align: center 
    |

.. note::

    **Giải thích chương trình:** Khi nút trên bàn phím được nhấn, Yolo:Bit sẽ hiển thị thông tin ra màn hình LED tương ứng. 


