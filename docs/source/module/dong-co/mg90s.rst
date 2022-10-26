3. Động cơ Servo MG90S
=============

.. image:: images/3.1.png
    :width: 400px
    :align: center 
| 

- Động cơ Servo MG90S với bánh răng được làm từ kim loại, mang lại lực kéo và độ bền cao hơn so với các dòng Servo khác. Động cơ này có kích thước nhỏ gọn, dễ ứng dụng vào các dự án điện tử.

- Bạn có thể lập trình điều khiển Servo MG90S tương tự như đối với các dòng Servo khác như MG996,… Sản phẩm phù hợp để ứng dụng vào các dự án như cánh tay robot, robot nhện, xe robot,…


**1. Mua sản phẩm**
-----------
----------

..  image:: images/gio.png
    :alt: some image
    :target: https://ohstem.vn/product/dong-co-servo-mg90s/
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
     - .. image:: images/3.1.png
          :width: 200px
          :align: center
   * - Máy tính lập trình Yolo:Bit
     - Mạch mở rộng cho Yolo:Bit
     - Động cơ Servo MG90S
   * - `Mua sản phẩm <https://ohstem.vn/product/may-tinh-lap-trinh-yolobit/>`_
     - `Mua sản phẩm <https://ohstem.vn/product/grove-shield/>`_
     - `Mua sản phẩm <https://ohstem.vn/product/dong-co-servo-mg90s/>`_


- **Bước 2**: Cắm Yolo:Bit vào mạch mở rộng

- **Bước 3**: Kết nối thiết bị vào **chân P4 trên mạch mở rộng**

.. image:: images/3.2.png
    :scale: 100%
    :align: center 
| 

**3. Hướng dẫn lập trình**
--------
------------

- **Đối với động cơ servo 180 độ:** 

    + Sử dụng khối lệnh sau trong danh mục **CHÂN CẮM**, để điều khiển:

    .. image:: images/2.3.png
        :scale: 100%
        :align: center 
    |

    + Trước khi lập trình, bạn cần xác định vị trí góc của servo để việc lập trình thuận lợi hơn.

    + Gửi chương trình sau xuống Yolo:Bit, để kiểm tra hoạt động của servo:

    .. image:: images/2.4.png
        :scale: 100%
        :align: center 
    |

.. note:: 

   Khi sau khi xác định vị trí góc của servo, bằng câu lệnh trong khối bắt đầu. Bạn hãy nhấn nút để xem sự di chuyển của cánh servo.


- **Đối với động cơ servo 360 độ:** 

    + Sử dụng khối lệnh sau trong danh mục **CHÂN CẮM**, để điều khiển:

    .. image:: images/2.5.png
        :scale: 100%
        :align: center 
    |

    + Động cơ servo 360, sẽ có các chế độ hoạt động như sau: 

        - Tốc độ 0: Đứng yên
        - Tốc độ 100: Tối đa
        - Tốc độ -100 - 0: Động cơ quay ngược chiều kim đồng hồ
        - Tốc độ 0- 100: Động cơ quay cùng chiều kim đồng hồ

    + Gửi chương trình sau xuống Yolo:Bit, để kiểm tra hoạt động của servo:

    .. image:: images/2.6.png
        :scale: 100%
        :align: center 
    |

.. note::

    Chương trình được ứng dụng vào các dự án như sáng tạo bánh xe robot, ròng rọc của cáp treo… 



