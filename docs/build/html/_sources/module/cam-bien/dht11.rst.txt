2. Cảm biến nhiệt độ độ ẩm DHT11
============

.. image:: images/2.1.png
    :width: 400px
    :align: center 
| 

- Cảm biến nhiệt độ độ ẩm là cảm biến rất thông dụng hiện nay vì chi phí rẻ và tính dễ dàng khi sử dụng. Bạn có thể dễ dàng lấy dữ liệu thông qua giao tiếp 1-wire (chỉ cần 1 chân digital để truyền dữ liệu) từ cảm biến này. 

- Cảm biến được tích hợp bộ tiền xử lý tín hiệu giúp dữ liệu nhận về được chính xác mà không cần phải qua bất kỳ tính toán nào.

- Cảm biến nhiệt độ và độ ẩm thường được ứng dụng trong các chương trình như hiển thị trạng thái nhiệt độ lên màn hình, tự động bật quạt khi trời nóng,….

- Đặc điểm: 
    
    + Đọc giá trị trực tiếp, không cần phải tính toán lạ
    + Sử dụng duy nhất một cổng tín hiệu ngõ ra
    + Cảm biến độ ẩm điện dung chính xác cao
    + Khoảng cách truyền xa và ổn định
    + Điện năng tiêu thụ thấp
    + Giá thành rẻ


**1. Mua sản phẩm**
-----------
----------

..  image:: images/gio.png
    :alt: some image
    :target: https://ohstem.vn/product/cam-bien-nhiet-do-do-am/
    :class: with-shadow
    :scale: 100%
    :align: center
|

**2. Thông số kỹ thuật**
------------
-------------

- **Thông số kỹ thuật của cảm biến nhiệt độ độ ẩm DHT11**

    + Điện áp đầu vào: 3.3V
    + Khoảng giá trị dòng điện: 1.3 – 2.1 mA
    + Khoảng giá trị độ ẩm: 5% – 95% RH
    + Khoảng giá trị nhiệt độ: -20 – 60 ℃


- **Pinout của DHT11**

Cảm biến nhiệt độ và độ ẩm DHT11 có 4 chân, và mỗi chân có chức năng như sau:

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
     - .. image:: images/2.1.png
          :width: 200px
          :align: center
   * - Máy tính lập trình Yolo:Bit
     - Mạch mở rộng cho Yolo:Bit
     - Cảm biến DHT11 (kèm dây Grove)
   * - `Mua sản phẩm <https://ohstem.vn/product/may-tinh-lap-trinh-yolobit/>`_
     - `Mua sản phẩm <https://ohstem.vn/product/grove-shield/>`_
     - `Mua sản phẩm <https://ohstem.vn/product/cam-bien-nhiet-do-do-am/>`_

- **Bước 2**: Cắm Yolo:Bit vào mạch mở rộng
- **Bước 3**: Sử dụng dây Grove cắm vào cảm biến
- **Bước 4**: Kết nối cảm biến nhiệt độ độ ẩm DHT11 vào **chân P0 trên mạch mở rộng**


..  figure:: images/2.2.png
    :scale: 100%
    :align: center 

..  attention::

    Cảm biến độ DHT11 có giá trị trả về là analog, trên mạch mở rộng có 3 chân có giá trị analog là P0, P1, P2. Bạn có thể kết nối vào 1 trong 3 chân này để làm việc với cảm biến. 


**4. Hướng dẫn lập trình với OhStem App**
--------
------------

- **Bước 1:** Tải thư viện **Cảm biến DHT**, xem hướng dẫn tải thư viện `tại đây <https://docs.ohstem.vn/en/latest/module/thu-vien-yolobit.html>`_


    .. image:: images/2.3.png
        :width: 300px
        :align: center 
    |

    Sau khi tải thư viện, trong danh mục khối lệnh sẽ xuất hiện các khối lệnh tương ứng:

    .. image:: images/2.4.png
        :width: 800px
        :align: center 
    |

    Để làm việc với cảm biến DHT11, bạn cần khai báo chân làm việc của cảm biến ở đầu chương trình bằng câu lệnh: 

    ..  image:: images/2.5.png
        :scale: 100%
        :align: center 
    |

- **Bước 2**: Gửi chương trình sau xuống Yolo:Bit

..  image:: images/2.6.png
    :scale: 100%
    :align: center 
|

.. note::

    **Giải thích chương trình:** Sau khi khai báo chân làm việc của cảm biến, các thông tin về nhiệt độ độ ẩm sẽ được hiển thị lên màn hình LED Yolo:Bit và cập nhật liên tục sau mỗi 5 giây.  


**5. Hướng dẫn lập trình Arduino**
--------
------------

- Mở phần mềm Arduino IDE. Xem hướng dẫn lập trình với Arduino `tại đây <https://docs.ohstem.vn/en/latest/module/cai-dat-arduino.html>`_. 

- Copy đoạn code sau, click vào nút ``Verify`` để kiểm tra lỗi chương trình. Sau khi biên dịch không báo lỗi, bạn có thể nạp đoạn code vào board. 

.. code-block:: guess

    #include "YoloBit.h"
    
    YoloBit yolobit;

    #include "DHT.h"  

    const int DHTPIN = P0;      
    const int DHTTYPE = DHT11;  
    DHT dht(DHTPIN, DHTTYPE);

    void setup() {
      Serial.begin(9600);
      dht.begin();       
    }

    void loop() {
      float h = dht.readHumidity();    
      float t = dht.readTemperature(); 
      Serial.print("Nhiet do: ");
      Serial.println(t);               
      Serial.print("Do am: ");
      Serial.println(h);                
      Serial.println();               
      delay(3000);                     
    }

.. note::

    **Giải thích chương trình:** Thông tin nhiệt độ và độ ẩm sẽ hiển thị ra cửa sổ Serial và được cập nhật liên tục sau mỗi 3 giây.









