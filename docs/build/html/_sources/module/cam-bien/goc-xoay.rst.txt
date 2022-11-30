15. Cảm biến góc xoay
==============

.. image:: images/16.1.png
    :width: 400px
    :align: center 
| 

- Module cảm biến góc xoay là một điện trở có ba chân tín hiệu. Điện trở của nó có thể được điều chỉnh bằng cách xoay núm xoay.

- Phạm vi điều chỉnh của module có điện trở cao nhất là 10 KΩ. Bạn có thể sử dụng cảm biến góc xoay để điều chỉnh tốc độ quay của động cơ, độ sáng của đèn LED.

**1. Mua sản phẩm**
-----------
----------

..  image:: images/gio.png
    :alt: some image
    :target: https://ohstem.vn/product/cam-bien-goc-xoay/
    :class: with-shadow
    :scale: 100%
    :align: center
|

**2. Thông số kỹ thuật**
---------
------------

- **Thông số kỹ thuật**

    + Điện áp hoạt động: 3.3V
    + Dòng điện tối đa: 30 mA
    + Công suất: 0.1 W
    + Góc xoay: 280°
    + Tổng trở resistance: 10 KΩ
    + Kiểu tính hiệu: tín hiệu analog (0~4095)
    + Kích thước module: 48mm x 24mm x 18mm (DxRxC)


- **Pinout của cảm biến**

Cảm biến góc xoay có 4 chân, và mỗi chân có chức năng như sau:

..  csv-table:: 
    :header: "STT", "Chân", "Chức năng"
    :widths: 10, 15, 30

    1, "GND", "Nối đất"
    2, "VCC", "Cấp nguồn (3.3V)"
    3, "NC", "Không sử dụng"
    4, "SIG", "Tín hiệu ngõ ra của cảm biến"


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
     - .. image:: images/16.1.png
          :width: 200px
          :align: center
   * - Máy tính lập trình Yolo:Bit
     - Mạch mở rộng cho Yolo:Bit
     - Cảm biến góc xoay (kèm dây Grove)
   * - `Mua sản phẩm <https://ohstem.vn/product/may-tinh-lap-trinh-yolobit/>`_
     - `Mua sản phẩm <https://ohstem.vn/product/grove-shield/>`_
     - `Mua sản phẩm <https://ohstem.vn/product/cam-bien-goc-xoay/>`_


- **Bước 2**: Cắm Yolo:Bit vào mạch mở rộng
- **Bước 3**: Sử dụng dây Grove cắm vào cảm biến
- **Bước 4**: Kết nối cảm biến với **P0 trên mạch mở rộng**.

..  figure:: images/16.2.png
    :scale: 100%
    :align: center 

    Đây cũng là một cảm biến có giá trị trả về là analog, do đó bạn có thể kết nối với các chân P0, P1, P2 trên mạch mở rộng

**4. Hướng dẫn lập trình**
--------
------------

- Sử dụng các khối lệnh trong danh mục **CHÂN CẮM** để thực hiện chương trình sau: 

..  image:: images/16.3.png
    :scale: 100%
    :align: center 
|

.. note::

    **Giải thích chương trình:** 
    
    Tạo biến một độ sáng, giá trị của độ sáng sẽ được chuyển từ giá trị analog 0- 4095 thành 0 - 100%. Khi núm xoay của cảm biến được vặn, độ sáng sẽ được thay đổi. 

**Hướng dẫn tạo biến:**

    1. Bạn cần vào mục **Biến và chọn Tạo biến.** Sau đó, điền tên cho biến mới để Tạo.

    ..  image:: images/16.4.png
        :scale: 100%
        :align: center 
    |
   
    2. Khi tạo biến thành công, trong mục Biến sẽ xuất hiện những khối lệnh liên quan để làm việc với biến.

    ..  image:: images/16.5.png
        :scale: 100%
        :align: center 
    |