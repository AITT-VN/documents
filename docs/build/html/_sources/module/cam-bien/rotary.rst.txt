22. Cảm biến góc xoay - Rotary Encoder 
==============

.. image:: images/23.1.png
    :width: 400px
    :align: center 
| 

- Rotary Encoder (hoặc gọi tắt là Encoder) là loại cảm biến có khả năng biến đổi chuyển động (chuyển động tịnh tiến, chuyển động quay của trục, ...) thành tín hiệu đầu ra thành xung hoặc tín hiệu số

- Ta cần phân biệt Rotary Encoder và Analog Rotary có sự khác nhau như sau: 

    - **Rotary Encoder:**

        + Không giới hạn góc xoay, xoay được 360 độ vô hạn
        + Có thể xoay được 1 khoảng chính xác theo từng nấc
        + Giá trị đọc được là số nấc đã xoay qua trái hoặc qua phải

    - **Rotary Analog:**

        + Góc xoay bị giới hạn trong 1 khoảng nhất định
        + Không thể xoay được 1 khoảng chính xác
        + Giá trị đọc được là dạng analog (từ 0 đến 4095 đối với Yolo:Bit)

- Rotary Encoder thường ứng dụng vào những dự án như: điều khiển tốc độ quạt, điều khiển tốc độ xe, điều khiển độ sáng đèn, điều khiển âm lượng, …

- **Trong hướng dẫn này, OhStem sẽ hướng dẫn bạn lập trình điều khiển tốc độ quạt bằng module Rotary Encoder.**

**1. Mua sản phẩm**
-----------
----------

..  image:: images/gio.png
    :alt: some image
    :target: https://shop.ohstem.vn/san-pham/rotary-encoder/
    :class: with-shadow
    :scale: 100%
    :align: center
|

**2. Thông số kỹ thuật**
---------
------------

- **Thông số kỹ thuật:**

    + Điện áp sử dụng: 3.3V
    + Độ phân giải 20 xung/vòng
    + Tín hiệu cảm biến: 2 pha
    + Kích thước của mạch: 24mm x 48mm x 16mm

- **Pinout của cảm biến:**

Cảm biến có 4 chân, mỗi chân có chức năng như sau:

..  csv-table:: 
    :header: "STT", "Chân", "Chức năng"
    :widths: 10, 15, 30

    1, "GND", "Nối đất"
    2, "VCC", "Cấp nguồn (3.3V)"
    3, "SIGA (CLK)", "Pha A"
    4, "SIGB (DT)", "Pha B"



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
     - .. image:: images/quat_mini.png
          :width: 200px
          :align: center
   * - Máy tính lập trình Yolo:Bit
     - Mạch mở rộng cho Yolo:Bit
     - Module Rotary Encoder (kèm dây Grove)
     - Quạt mini (kèm dây Grove)
   * - `Mua sản phẩm <https://shop.ohstem.vn/san-pham/may-tinh-lap-trinh-yolobit/>`_
     - `Mua sản phẩm <https://shop.ohstem.vn/san-pham/grove-shield/>`_
     - `Mua sản phẩm <https://shop.ohstem.vn/san-pham/rotary-encoder/>`_
     - `Mua sản phẩm <https://shop.ohstem.vn/san-pham/dong-co-quat-mini/>`_


- **Bước 2**: Cắm Yolo:Bit vào mạch mở rộng
- **Bước 3**: Sử dụng dây Grove cắm vào cảm biến
- **Bước 4**: Kết nối Rotary Encoder và quạt mini với mạch mở rộng như sau: 

..  figure:: images/23.2.png
    :scale: 100%
    :align: center 

    Vì module Rotary Encoder có 2 chân tín hiệu là chân CLK và chân DT do đó ta phải kết nối module Rotary Encoder vào các port có 2 chân tín hiệu của mạch mở rộng Yolo:Bit , không được kết nối module Rotary Encoder vào các port có 1 chân tín hiệu như port P0, port P1 hoặc port P2.



**4. Hướng dẫn lập trình với OhStem App**
--------
------------

- **Bước 1:** Tải thư viện **Rotary Encoder**, bằng cách dán đường link sau vào phần tìm kiếm thư viện: `https://github.com/AITT-VN/yolobit_rotary_encoder.git <https://github.com/AITT-VN/yolobit_rotary_encoder.git>`_
    
    Xem hướng dẫn tải thư viện `tại đây <https://docs.ohstem.vn/en/latest/module/thu-vien-yolobit.html>`_


    .. image:: images/rotary.png
        :scale: 80%
        :align: center 
    |

    Sau khi tải thư viện, trong danh mục khối lệnh sẽ xuất hiện các khối lệnh tương ứng:

    .. image:: images/lenh_rotary.png
        :scale: 90%
        :align: center 
    |


- **Bước 2:** **Để làm việc với quạt mini** bạn hãy tải thư viện **AIOT KIT** ,  xem hướng dẫn `tại đây <https://docs.ohstem.vn/en/latest/module/dong-co/quat-mini.html>`_


- **Bước 3:** Lập trình điều khiển quạt bằng Rotary Encoder

    + Trước tiên chúng ta sẽ khởi tạo các chân, chế độ xoay và khoảng giá trị cho Rotary, như sau: 

    .. image:: images/23.3.png
        :scale: 90%
        :align: center 
    |  

    + Tiếp theo, gửi chương trình sau xuống Yolo:Bit: 

    ..  figure:: images/23.4.png
        :scale: 80%
        :align: center 

        Câu lệnh **bật quạt chân P14 với tốc độ (0 -100)** nằm trong danh mục khối lệnh **AIOT KIT**


.. note::
    
    **Giải thích chương trình**: Chúng ta sẽ lập trình các mức độ của quạt khi xoay Encoder: 

    - Đặt điều kiện "**nếu đọc giá trị của rotary = 3**" thì quạt sẽ quay ở mức độ cao nhất tương ứng với tốc độ 100% và hiển thị ra màn hình LED Yolo:Bit mức độ quạt đang hoạt động. 

    - Tương tự như vậy ta sẽ tạo ra thêm các điều kiện để quạt quay ở mức độ 2 và mức độ 1 và mức 0 tương ứng với 50% và 25% và 0%.


5. **Chương trình mẫu:** 
------
----------

- Xem chương trình: `Tại đây <https://app.ohstem.vn/#!/share/yolobit/2H4YlGJ8lAd8DUExjFdCg2XfiqC>`_

.. image:: images/23.5.png
    :width: 200px
    :align: center 


**6. Hướng dẫn lập trình Arduino**
--------
------------

- Mở phần mềm Arduino IDE. Xem hướng dẫn lập trình với Arduino `tại đây <https://docs.ohstem.vn/en/latest/module/cai-dat-arduino.html>`_. 

- Copy đoạn code sau, click vào nút ``Verify`` để kiểm tra lỗi chương trình. Sau khi biên dịch không báo lỗi, bạn có thể nạp đoạn code vào board. 

.. code-block:: guess

    // Định nghĩa cấu hình mắcro của cảm biến góc xoay và chân LED
    
    #include "YoloBit.h"

    Yolobit yolobit;
    
    #define ROTARY_ANGLE_SENSOR P10 
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