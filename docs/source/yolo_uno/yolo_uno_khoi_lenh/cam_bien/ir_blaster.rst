18. Module IR Blaster (Hồng ngoại phát tín hiệu)
=================================================

.. image:: images/ir_01.png
    :width: 400px
    :align: center 
| 

Module **IR Blaster** là một thiết bị phát tín hiệu hồng ngoại (Infrared) được sử dụng để điều khiển từ xa các thiết bị gia dụng như TV, quạt, đầu DVD,... tương tự như remote truyền thống. Với module này, bạn có thể lập trình để mô phỏng tín hiệu điều khiển và gửi đi từ mạch Yolo UNO.

Module hoạt động bằng cách phát các xung tín hiệu mã hóa ở tần số 38kHz thông qua một diode hồng ngoại, có thể thu nhận được bởi các thiết bị có bộ thu IR tương thích.

**Các tính năng nổi bật:**

+ Phát tín hiệu hồng ngoại điều khiển các thiết bị từ xa
+ Hỗ trợ nhiều loại mã hóa IR (NEC, Sony,…)
+ Giao tiếp điều khiển đơn giản qua tín hiệu digital
+ Tích hợp sẵn transistor khuếch đại tín hiệu
+ Phạm vi phát lên đến 5-10 mét (tùy vào môi trường và thiết bị nhận)

**1. Thông số kỹ thuật**
------------------------

- **Thông số kỹ thuật**

    + Điện áp hoạt động: 3.3V – 5V
    + Tín hiệu điều khiển: Digital (ON/OFF)
    + Tần số phát: 38kHz (chuẩn phổ biến của remote IR)
    + Khoảng cách phát: 5 – 10 mét (tùy điều kiện)
    + Giao tiếp: 1 chân tín hiệu
    + Kích thước: nhỏ gọn, dễ tích hợp

- **Pinout của module**

Module IR có 3 chân, chức năng như sau:

.. csv-table:: 
    :header: "STT", "Chân", "Chức năng"
    :widths: 10, 15, 30

    1, "GND", "Nối đất"
    2, "VCC", "Cấp nguồn (3.3V hoặc 5V)"
    3, "SIG", "Tín hiệu điều khiển phát IR"


**2. Kết nối**
--------------

- **Bước 1**: Chuẩn bị các thiết bị như sau:

.. list-table:: 
   :widths: auto
   :header-rows: 1
     
   * - .. image:: images/yolouno.png
          :width: 200px
          :align: center
     - .. image:: images/ir_01.png
          :width: 200px
          :align: center
   * - Máy tính lập trình Yolo UNO
     - Module IR Blaster
   * - `Mua sản phẩm <https://ohstem.vn/product/may-tinh-lap-trinh-yolobit/>`_
     - `Mua sản phẩm <https://ohstem.vn/product/module-hong-ngoai-phat-ir/>`_

- **Bước 2**: Kết nối module IR Blaster vào **cổng digital bất kỳ** trên khe mở rộng:

.. figure:: images/ir_02.png
    :scale: 100%
    :align: center

    Chân tín hiệu của IR Blaster nên cắm vào cổng D5 hoặc D6 trên Yolo UNO.

**3. Lập trình IR Blaster với Yolo UNO trên OhStem App**
---------------------------------------------------------

Bạn cần cài đặt thư viện mở rộng cho module IR bằng cách vào mục **"Mở rộng"** trong OhStem App và dán liên kết sau:

`https://github.com/AITT-VN/yolouno_extension_irblaster.git`

    Hướng dẫn chi tiết cài thư viện `tại đây <https://docs.ohstem.vn/en/latest/module/thu-vien-yolobit.html>`_

.. image:: images/ir_03.png
    :scale: 100%
    :align: center 
|

**Chương trình cơ bản để gửi tín hiệu hồng ngoại:**

.. figure:: images/ir_04.png
    :scale: 100%
    :align: center

    Gửi mã điều khiển hồng ngoại định dạng NEC đến thiết bị TV.

Thông tin giải thích:

+ **Địa chỉ**: là mã đại diện cho thương hiệu thiết bị (ví dụ: 0x00FF)
+ **Dữ liệu**: là mã điều khiển cụ thể (ví dụ: bật/tắt)

**Lưu ý**

+ Mỗi loại thiết bị điều khiển sẽ dùng một mã địa chỉ và mã dữ liệu khác nhau. Bạn cần tra cứu mã tương ứng.
+ Có thể kết hợp với module **IR Receiver** để học lệnh từ remote gốc.
+ Khoảng cách và hướng phát ảnh hưởng lớn đến độ chính xác.

**Chương trình mẫu** `tại đây <https://app.ohstem.vn/#!/share/yolouno/2irEXAMPLEsendTV>`_
