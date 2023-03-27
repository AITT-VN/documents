4. Màn hình Oled 0.96”
============

.. image:: images/4.1.png
    :width: 400px
    :align: center 
| 

- Màn hình Oled 0.96 inch cho khả năng hiển thị đẹp, sang trọng, rõ nét vào ban ngày và khả năng tiết kiệm năng lượng tối đa với mức chi phí phù hợp.

- Sản phẩm sử dụng giao tiếp I2C cho chất lượng đường truyền ổn định và rất dễ giao tiếp chỉ với 2 chân GPIO.


**1. Mua sản phẩm**
-----------
----------

..  image:: images/gio.png
    :alt: some image
    :target: https://ohstem.vn/product/man-hinh-oled-0-96/
    :class: with-shadow
    :scale: 100%
    :align: center
|


**2. Thông số kỹ thuật**
------------
-------------

- **Thông số kỹ thuật**

    + Hỗ trợ cả 3.3V 
    + Số điểm hiển thị: 128×64 điểm.
    + Độ rộng màn hình: 0.96 inch
    + Màu hiển thị: Trắng / Xanh Dương.
    + Giao tiếp: I2C
    + Driver: SSD1306
    + Tương thích với chuẩn cắm plug & play 4 pin Blocky Piece


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
     - .. image:: images/4.1.png
          :width: 200px
          :align: center
   * - Máy tính lập trình Yolo:Bit
     - Mạch mở rộng cho Yolo:Bit
     - Màn hình OLED (kèm dây Grove)
   * - `Mua sản phẩm <https://ohstem.vn/product/may-tinh-lap-trinh-yolobit/>`_
     - `Mua sản phẩm <https://ohstem.vn/product/grove-shield/>`_
     - `Mua sản phẩm <https://ohstem.vn/product/man-hinh-oled-0-96/>`_

- **Bước 2**: Cắm Yolo:Bit vào mạch mở rộng
- **Bước 3**: Sử dụng dây Grove kết nối với màn hình
- **Bước 4**: Kết nối thiết bị vào **chân I2C trên mạch mở rộng**


..  figure:: images/4.2.png
    :scale: 100%
    :align: center 

    Bạn có thể kết nối vào 1 trong 2 chân I2C


**4. Hướng dẫn lập trình với OhStem App**
--------
------------

- **Bước 1:** Tải thư viện **Màn hình OLED I2C**, xem hướng dẫn tải thư viện `tại đây <https://docs.ohstem.vn/en/latest/module/cai-dat-thu-vien.html>`_


    .. image:: images/oled.png
        :width: 300px
        :align: center 
    |

    Sau khi tải thư viện, trong danh mục khối lệnh sẽ xuất hiện các khối lệnh tương ứng:

    .. image:: images/lenh_oled.png
        :width: 800px
        :align: center 
    |

    Để làm việc với màn hình Oled LCD, chúng ta cần khởi tạo màn hình bằng câu lệnh như sau: 

    ..  image:: images/4.3.png
        :scale: 100%
        :align: center 

- **Bước 2**: Gửi chương trình sau xuống Yolo:Bit

..  image:: images/4.4.png
    :scale: 100%
    :align: center 

.. note::

    **Giải thích chương trình**

    Câu lệnh đầu tiên sẽ xóa toàn bộ màn hình, trong khi câu lệnh thứ 2 sẽ được dùng để hiển thị thông tin lên màn hình LCD tại tọa độ x và y, tọa độ này bạn có thể căn chỉnh để phù hợp với yêu cầu của bạn 


**5. Hướng dẫn lập trình Arduino**
--------
------------

- Mở phần mềm Arduino IDE. Xem hướng dẫn lập trình với Arduino `tại đây <https://docs.ohstem.vn/en/latest/module/cai-dat-arduino.html>`_. 

- Copy đoạn code sau, click vào nút ``Verify`` để kiểm tra lỗi chương trình. Sau khi biên dịch không báo lỗi, bạn có thể nạp đoạn code vào board. 

.. code-block:: guess

    #include "YoloBit.h"
    #include <SPI.h>
    #include <Wire.h>
    #include <Adafruit_GFX.h>
    #include <Adafruit_SSD1306.h>

    Yolobit yolobit;

    Adafruit_SSD1306 display(128, 32, &Wire);

    void setup() {
      Serial.begin(9600);

      display.begin(SSD1306_SWITCHCAPVCC, 0x3C); // Địa chỉ 0x3C cho màn hình 128x32

      display.display();
      delay(1000);

      // Xóa bộ đệm.
      display.clearDisplay();
      display.display();

      // Thiết lập font chữ và màu sắc
      display.setTextSize(1);
      display.setTextColor(WHITE);
    }

    void loop() {
      display.clearDisplay();
      display.setCursor(0, 0);
      display.println("Hello");
      display.display();
      delay(1000);
    }
    
.. note:: 
    
    **Giải thích chương trình:**  Bạn sẽ thấy dòng chữ **"Hello"** được hiển thị liên tục trên 2 dòng của màn hình OLED (hiển thị trong 1 giây rồi biến mất sau mỗi giây)