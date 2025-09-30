6. Cảm biến khí gas MQ2
==========

.. image:: images/6.1.png
    :width: 400px
    :align: center 
| 

- Cảm biến khí gas MQ2 được dùng để phát hiện các loại khí gas, khí dễ cháy trong không khí, từ đó trả về giá trị tương ứng để thông báo. Sản phẩm có độ nhạy cao và chi phí thấp, phù hợp với những bạn mới tiếp xúc và học về lập trình các dự án sáng tạo như cảnh báo cháy trong nhà thông minh.

- Đặc điểm: 
    
    + Có độ bền cao, có thể sử dụng trong thời gian dài 
    + Thời gian phản hồi nhanh 
    + Nguồn hoạt động: 5V


**1. Mua sản phẩm**
-----------
----------

..  image:: images/gio.png
    :alt: some image
    :target: https://shop.ohstem.vn/san-pham/cam-bien-khi-gas-mq2/
    :class: with-shadow
    :scale: 100%
    :align: center
|

**2. Thông số kỹ thuật**
------------
-------------

- **Thông số kỹ thuật của cảm biến:**

..  csv-table:: 
    :header: "Mục", "Thông số", "Min", "Trung bình", "Max", "Đơn vị"
    :widths: 10, 30, 10, 15, 10, 10

    "VCC", "Điện áp làm việc", "", 3.3, "", "V"
    "PH", "Hệ thống sưởi tiêu thụ", 0.5, "", 800, "mW"
    "RL", "Chịu tải", "", "Có thể điều chỉnh", "", ""
    "RH", "Chống nóng", "", 33, "", "Ω"
    "RS", "Cảm biến kháng", 3, "", 30, "kΩ"


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
     - .. image:: images/6.1.png
          :width: 200px
          :align: center
   * - Máy tính lập trình Yolo:Bit
     - Mạch mở rộng cho Yolo:Bit
     - Cảm biến khí gas MQ2 (kèm dây Grove)
   * - `Mua sản phẩm <https://shop.ohstem.vn/san-pham/may-tinh-lap-trinh-yolobit/>`_
     - `Mua sản phẩm <https://shop.ohstem.vn/san-pham/grove-shield/>`_
     - `Mua sản phẩm <https://shop.ohstem.vn/san-pham/cam-bien-khi-gas-mq2/>`_


- **Bước 2**: Cắm Yolo:Bit vào mạch mở rộng
- **Bước 3**: Sử dụng dây Grove cắm vào cảm biến
- **Bước 4**: Kết nối thiết bị vào **chân P1 trên mạch mở rộng**

..  figure:: images/6.2.png
    :scale: 100%
    :align: center 

    Đây cũng là một cảm biến có giá trị trả về là analog, do đó bạn có thể kết nối với các chân P0, P1, P2 trên mạch mở rộng


**4. Hướng dẫn lập trình với OhStem App**
--------
------------

- **Bước 1:** Tải thư viện **Cảm biến MQx**, bằng cách dán đường link sau vào phần tìm kiếm thư viện: `https://github.com/AITT-VN/yolobit_extension_mqx.git <https://github.com/AITT-VN/yolobit_extension_mqx.git>`_
    
    Xem hướng dẫn tải thư viện `tại đây <https://docs.ohstem.vn/en/latest/module/thu-vien-yolobit.html>`_


    .. image:: images/6.3.png
        :scale: 80%
        :align: center 
    |

    Sau khi tải thư viện, trong danh mục khối lệnh sẽ xuất hiện các khối lệnh tương ứng:

    .. image:: images/6.4.png
        :scale: 100%
        :align: center 
    |   

- **Bước 2:** Hãy gửi chương trình sau đến Yolo:Bit của bạn:      

    .. image:: images/6.5.png
        :scale: 100%
        :align: center 
    |  

.. note::

    **Giải thích chương trình**: 

    Chương trình cảnh báo nếu xung quanh bạn đang có sự rò rỉ của khí gas. 

    - Đọc giá trị của khí gas bằng câu lệnh đọc giá trị mg/l cảm biến cổng P1 trong thư viện cảm biến MQx. 
    - Màn hình LED của Yolo:Bit sẽ hiện thị kết quả mà cảm biến đọc được. Nếu vượt trên 5 thì sẽ phát âm cảnh báo cho bạn. Nếu không, màn hình hiện chữ OK, nghĩa là không khí xung quanh bạn đang tốt. 

    **Lưu ý:** *Bạn có thể sử dụng các đơn vị đo như analog và ppm trong chương trình*


**5. Hướng dẫn lập trình Arduino**
--------
------------

- Mở phần mềm Arduino IDE. Xem hướng dẫn lập trình với Arduino `tại đây <https://docs.ohstem.vn/en/latest/module/cai-dat-arduino.html>`_. 

- Copy đoạn code sau, click vào nút ``Verify`` để kiểm tra lỗi chương trình. Sau khi biên dịch không báo lỗi, bạn có thể nạp đoạn code vào board. 

.. code-block:: guess

    #include "YoloBit.h"

    YoloBit yolobit;

    int sensorPin = P1_ADC;
    int sensorValue = 0;

    void setup() {
      Serial.begin(115200);
    }

    void loop() {
      // đọc giá trị cảm biến
      sensorValue = analogRead(sensorPin);
      Serial.println(sensorValue);
      delay(200);
    }

.. note:: 
    
    **Giải thích chương trình:** Sau khi nạp chương trình và mở cửa sổ Serial, bạn sẽ thấy giá trị đọc được từ cảm biến được in ra.

    