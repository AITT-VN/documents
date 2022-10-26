2. Động cơ Servo SG90S
===============

.. image:: images/2.1.png
    :width: 400px
    :align: center 
| 

- Động cơ Servo SG90S có thể được điều khiển và ứng dụng vào các dự án như lái robot, di chuyển các khớp cánh tay robot lên xuống,…

- Sản phẩm có 2 loại: động cơ xoay được 180 độ và động cơ xoay được 360 độ.

**1. Mua sản phẩm**
-----------
----------

..  image:: images/gio.png
    :alt: some image
    :target: https://ohstem.vn/product/dong-co-servo-sg90s/
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
     - .. image:: images/2.1.png
          :width: 200px
          :align: center
   * - Máy tính lập trình Yolo:Bit
     - Mạch mở rộng cho Yolo:Bit
     - Động cơ Servo SG90S
   * - `Mua sản phẩm <https://ohstem.vn/product/may-tinh-lap-trinh-yolobit/>`_
     - `Mua sản phẩm <https://ohstem.vn/product/grove-shield/>`_
     - `Mua sản phẩm <https://ohstem.vn/product/dong-co-servo-sg90s/>`_


- **Bước 2**: Cắm Yolo:Bit vào mạch mở rộng

- **Bước 3**: Kết nối thiết bị vào **chân P4 trên mạch mở rộng**

.. image:: images/2.2.png
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

