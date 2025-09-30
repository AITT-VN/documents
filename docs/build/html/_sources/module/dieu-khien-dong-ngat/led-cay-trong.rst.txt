3. Đèn LED màu kích thích cây trồng
========

.. image:: images/3.1.png
    :width: 400px
    :align: center 
| 

- Đèn LED màu kích thích cây trồng được ứng dụng trong các dự án như kích thích cây sinh trưởng trong môi trường thiếu sáng. Nếu bạn mới tiếp xúc và làm quen với các dự án IoT, đây sẽ là module phù hợp với bạn.

..  attention::
    
    Đèn LED này sử dụng cổng USB, không tương thích với cổng cắm Grove của Yolo:Bit. Do đó, bạn cần sử dụng thêm `module đóng ngắt 2 kênh <https://shop.ohstem.vn/san-pham/module-dong-ngat-2-kenh/>`_ khi thực hành kết nối đèn LED màu với Yolo:Bit để làm các dự án STEM thông minh nhé!

**1. Mua sản phẩm**
-----------
----------

..  image:: images/gio.png
    :alt: some image
    :target: https://shop.ohstem.vn/san-pham/den-led-mau-kich-thich-cay-trong/
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
     - .. image:: images/3.1.png
          :width: 300px
          :align: center
   * - Máy tính lập trình Yolo:Bit
     - Mạch mở rộng cho Yolo:Bit
     - Module đóng ngắt 2 kênh (kèm dây Grove) 
     - Đèn LED màu kích thích cây trồng
   * - `Mua sản phẩm <https://shop.ohstem.vn/san-pham/may-tinh-lap-trinh-yolobit/>`_
     - `Mua sản phẩm <https://shop.ohstem.vn/san-pham/grove-shield/>`_
     - `Mua sản phẩm <https://shop.ohstem.vn/san-pham/module-dong-ngat-2-kenh/>`_
     - `Mua sản phẩm <https://shop.ohstem.vn/san-pham/may-bom-mini/>`_


- **Bước 2**: Cắm Yolo:Bit vào mạch mở rộng

- **Bước 3**: Kết nối đèn LED với module đóng ngắt 2 kênh

- **Bước 4**: Kết nối thiết bị vào **chân P14/P15 trên mạch mở rộng**


..  figure:: images/3.2.png
    :scale: 100%
    :align: center 

    Để làm việc với module đóng ngắt 2 kênh, bạn sẽ kết nối vào cổng có 2 chân kết nối.

**4. Hướng dẫn lập trình**
--------
------------

- **Bước 1:** Tải thư viện **AIOT KIT**, xem hướng dẫn tải thư viện `tại đây <https://docs.ohstem.vn/en/latest/module/thu-vien-yolobit.html>`_


    .. image:: images/aiot.png
        :width: 300px
        :align: center 
    |

    Sau khi tải thư viện, trong danh mục khối lệnh sẽ xuất hiện các khối lệnh tương ứng:

    .. image:: images/lenh_aiot.png
        :width: 800px
        :align: center 
    |   

- **Bước 2:** Hãy gửi chương trình sau đến Yolo:Bit của bạn:  

..  image:: images/3.3.png
    :scale: 90%
    :align: center

.. note:: 

    **Giải thích chương trình**:

    Chúng ta sẽ sử dụng nút A trên mạch Yolo:Bit để bật đèn ở độ sáng 70%. Nút B để chuyển đèn về độ sáng 0% (tắt đèn). 

    Bạn có thể thay đổi độ sáng của đèn trong chương trình.


