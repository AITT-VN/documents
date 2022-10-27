23. Cảm biến vân tay AS608
==============

.. image:: images/22.1.png
    :width: 400px
    :align: center 
| 

- Cảm biến vân tay sử dụng cổng giao tiếp UART TTL để giao tiếp với các loại Vi điều khiển, hoặc là kết nối trực tiếp với máy tính thông qua cáp USB.

- Cảm biến vân tay này được tích hợp một nhân dùng để xử lý và nhận dạng vân tay ở phía trong. Thiết bị này sẽ tự động gán vân tay với một chuỗi dữ liệu và truyền ra ngoài qua giao tiếp UART. Điều này có nghĩa là gì? Nghĩa là bạn hoàn toàn không cần các thao tác phức tạp như xử lý hình ảnh, … Bạn chỉ cần phát lệnh đọc/ghi và so sánh chuỗi UART một cách đơn giản. Đây là thiết bị cảm biến vân tay arduino rất dễ sử dụng và lập trình.


**1. Mua sản phẩm**
-----------
----------

..  image:: images/gio.png
    :alt: some image
    :target: https://ohstem.vn/product/cam-bien-van-tay/
    :class: with-shadow
    :scale: 100%
    :align: center
|

**2. Thông số kỹ thuật**
---------
------------

- **Thông số kỹ thuật**

    + Điện áp: 3.3V 
    + Dòng điện tiêu thụ:  nhỏ hơn 120mA
    + Phương thức giao tiếp: UART
    + Độ an toàn: 5
    + Tỉ lệ chấp nhận sai (FAR):  dưới 0.001% (mức bảo mật 3)
    + Tỉ lệ từ chối sai (FRR): dưới 1.0% (mức bảo mật 3)
    + Sản phẩm này có thể lưu giữ lên đến 127 dấu vân tay khác nhau

- **Sơ đồ chân cảm biến vân tay**



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
     - .. image:: images/22.1.png
          :width: 200px
          :align: center
   * - Máy tính lập trình Yolo:Bit
     - Mạch mở rộng cho Yolo:Bit
     - Cảm biến vân tay (kèm dây Grove)
   * - `Mua sản phẩm <https://ohstem.vn/product/may-tinh-lap-trinh-yolobit/>`_
     - `Mua sản phẩm <https://ohstem.vn/product/grove-shield/>`_
     - `Mua sản phẩm <https://ohstem.vn/product/cam-bien-van-tay/>`_


- **Bước 2**: Cắm Yolo:Bit vào mạch mở rộng
- **Bước 3**: Sử dụng dây Grove cắm vào cảm biến
- **Bước 4**: Kết nối cảm biến với **P3/P6 trên mạch mở rộng**.

..  figure:: images/22.3.png
    :scale: 100%
    :align: center 

**4. Cách làm việc với cảm biến**
--------
------------

- Bước 1: Cài đặt thư viện 

