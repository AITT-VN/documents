6. Module điều khiển động cơ
================

.. image:: images/6.1.png
    :width: 400px
    :align: center 

Sản phẩm được sử dụng để điều khiển chuyển động của các thiết bị điện như động cơ DC giảm tốc hoặc động cơ servo. Mạch này cho phép kiểm soát hướng quay và độ mạnh yếu của động cơ, tính năng này sẽ bảo vệ sự an toàn cho vi điều khiển của bạn không bị chập nguồn.


**1. Mua sản phẩm**
-----------
----------

..  image:: images/gio.png
    :alt: some image
    :target: https://ohstem.vn/product/module-dieu-khien-dong-co/
    :class: with-shadow
    :scale: 100%
    :align: center
|

**2. Thông số kỹ thuật**
------
---------

    + Kích thước 48x60mm, chuẩn 4 dây tín hiệu
    + Giao tiếp: I2C
    + Cùng một lúc có thể điều khiển được 4 động cơ DC hoặc 2 động cơ bước
    + Điện áp 5-12V 2A (Được cấp thông qua Jack DC cái) 
    

**3. Kết nối**
------------
------------

Kết nối module điều khiển động cơ với Yolo:Bit thông qua **cổng I2C** trên mạch mở rộng. 

.. image:: images/6.7.png
    :scale: 70%
    :align: center 
|

**4. Hướng dẫn lập trình với OhStem App**
--------
------------

    **4.1. Tải thư viện**
    ---------

Để điều khiển được module, chúng ta phải cần thêm thư viện mở rộng **MOTORS DRIVER**, bạn hãy copy đường dẫn sau: `<https://github.com/AITT-VN/yolobit_extension_motor_driver.git>`_ và dán vào mục mở rộng để tải thư viện mở rộng.

    Xem hướng dẫn tải thư viện `tại đây <https://docs.ohstem.vn/en/latest/module/cai-dat-thu-vien.html>`_.

    .. image:: images/6.2.png
        :width: 300px
        :align: center 
    |

    Sau khi tải thư viện, trong danh mục khối lệnh sẽ xuất hiện các khối lệnh tương ứng:

    .. image:: images/6.3.png
        :scale: 100%
        :align: center 
    |   

.. note::

    Với các lệnh cơ bản này, bạn có thể xây dựng 1 mô hình robot 4 bánh xe hoặc các mô hình khác theo ý thích. Module hỗ trợ cả 2 loại động cơ bước và động cơ 1 chiều (DC), tuy nhiên khi sử dụng, chúng ta chỉ được phép sử dụng 1 trong 2 loại cùng lúc. 


    **4.2 Viết chương trình**
    --------

**Dự án mẫu: Robot Mecanum 4 bánh** sử dụng module điều khiển động cơ:

.. image:: images/6.4.png
    :scale: 100%
    :align: center 

Với các cổng gắn động cơ như sau: 

+ Bánh trước bên phải : cổng M1
+ Bánh trước bên trái : cổng M2
+ Bánh sau bên trái: cổng M3
+ Bánh sau bên phải: cổng M4

Gửi chương trình sau vào Yolo:Bit: 

.. image:: images/6.6.png
    :scale: 100%
    :align: center 
| 

Sau đó, vào giao diện điều khiển của gamepad Yolo:Bit, kết nối Bluetooth và bắt đầu điều khiển robot: 

.. image:: images/6.5.png
    :scale: 40%
    :align: center 
| 
**Chương trình mẫu:** Bạn có thể tải chương trình `tại đây <https://app.ohstem.vn/#!/share/yolobit/2T0hIh2U4JbeIzs7sVJdBNehDSR>`_. 