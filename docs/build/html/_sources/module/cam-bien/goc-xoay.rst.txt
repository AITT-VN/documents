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
    :target: https://shop.ohstem.vn/san-pham/cam-bien-goc-xoay/
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
   * - `Mua sản phẩm <https://shop.ohstem.vn/san-pham/may-tinh-lap-trinh-yolobit/>`_
     - `Mua sản phẩm <https://shop.ohstem.vn/san-pham/grove-shield/>`_
     - `Mua sản phẩm <https://shop.ohstem.vn/san-pham/cam-bien-goc-xoay/>`_


- **Bước 2**: Cắm Yolo:Bit vào mạch mở rộng
- **Bước 3**: Sử dụng dây Grove cắm vào cảm biến
- **Bước 4**: Kết nối cảm biến với **P0 trên mạch mở rộng**.

..  figure:: images/16.2.png
    :scale: 100%
    :align: center 

    Đây cũng là một cảm biến có giá trị trả về là analog, do đó bạn có thể kết nối với các chân P0, P1, P2 trên mạch mở rộng

**4. Hướng dẫn lập trình với OhStem App**
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


**5. Hướng dẫn lập trình Arduino**
--------
------------

- Mở phần mềm Arduino IDE. Xem hướng dẫn lập trình với Arduino `tại đây <https://docs.ohstem.vn/en/latest/module/cai-dat-arduino.html>`_. 

- Copy đoạn code sau, click vào nút ``Verify`` để kiểm tra lỗi chương trình. Sau khi biên dịch không báo lỗi, bạn có thể nạp đoạn code vào board. 

.. code-block:: guess

    // Định nghĩa cấu hình mắcro của cảm biến góc xoay và chân LED
    
    #include "YoloBit.h"

    Yolobit yolobit;
    
    #define ROTARY_ANGLE_SENSOR P0 
    #define LED P13  // Chân LED được kết nối đến chân PWM P13 của YoloBit
    #define ADC_REF 3.3 // YoloBit sử dụng 3V3, ADC_REF nên là 3,3
    #define GROVE_VCC 3.3 // Cấp nguồn VCC của giao diện Grove thường là 3,3V
    #define FULL_ANGLE 300 // Giá trị đầy đủ của góc quay là 300 độ

    void setup()
    {
      yolobit.serialBegin(9600); // Khởi tạo UART với tốc độ baud rate 9600
      yolobit.pinMode(ROTARY_ANGLE_SENSOR, INPUT); // Thiết lập chân cảm biến góc xoay là chế độ đầu vào
      yolobit.pinMode(LED, OUTPUT); // Thiết lập chân LED là chế độ đầu ra
    }

    void loop()
    {   
      float voltage;
      int sensor_value = yolobit.analogRead(ROTARY_ANGLE_SENSOR); // Đọc giá trị của cảm biến
      voltage = (float)sensor_value*ADC_REF/4095; // Chuyển đổi giá trị analog sang giá trị điện áp
      float degrees = (voltage*FULL_ANGLE)/GROVE_VCC; // Tính góc quay dựa trên giá trị điện áp đọc được
      yolobit.println("The angle between the mark and the starting position:"); // In thông báo lên serial monitor
      yolobit.println(degrees); // In giá trị góc quay lên serial monitor

      int brightness;
      brightness = map(degrees, 0, FULL_ANGLE, 0, 1023); // Chuyển đổi giá trị góc quay sang giá trị độ sáng của LED
      yolobit.analogWrite(LED, brightness); // Điều khiển độ sáng của LED thông qua kết nối PWM
      yolobit.delay(500); // Chờ 500ms
    }
    
.. note:: 
    
    **Giải thích chương trình:** Sau khi chạy chương trình, giá trị của độ sáng sẽ được chuyển từ giá trị analog 0- 4095 thành 0 - 100%. Khi núm xoay của cảm biến được vặn, độ sáng sẽ được thay đổi.