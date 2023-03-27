13. Cảm biến siêu âm
=============

.. image:: images/14.1.png
    :width: 400px
    :align: center 
| 

Module cảm biến siêu âm là một mô-đun điện tử được dùng để đo khoảng cách trong phạm vi từ 3cm đến 200cm. Chúng có thể được sử dụng cho các dự án để giúp xe tự động tránh chướng ngại vật hoặc ứng dụng vào các dự án đo khoảng cách (để tính vận tốc xe),…

**1. Mua sản phẩm**
-----------
----------

..  image:: images/gio.png
    :alt: some image
    :target: https://ohstem.vn/product/cam-bien-sieu-am/
    :class: with-shadow
    :scale: 100%
    :align: center
|

**2. Thông số kỹ thuật**
---------
------------

- **Thông số kỹ thuật**

    + Điện áp hoạt động: 3.3V
    + Góc đo: 30 degree
    + Khoảng cách đo: 3-400cm (with error less than 1cm)
    + Tần số siêu âm: 42 KHz
    + Ngõ ra: Tín hiệu Digital
    + Kích thước module: 48mm x 24mm x 18mm (DxRxC)


- **Pinout của cảm biến siêu âm**

Cảm biến siêu âm có 4 chân, và mỗi chân có chức năng như sau:

..  csv-table:: 
    :header: "STT", "Chân", "Chức năng"
    :widths: 10, 15, 30

    1, "GND", "Nối đất"
    2, "VCC", "Cấp nguồn (3.3V)"
    3, "ECHO", "Thu sóng siêu âm"
    4, "TRIGGER", "Phát sóng siêu âm"


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
     - .. image:: images/14.1.png
          :width: 200px
          :align: center
   * - Máy tính lập trình Yolo:Bit
     - Mạch mở rộng cho Yolo:Bit
     - Cảm biến siêu âm (kèm dây Grove)
   * - `Mua sản phẩm <https://ohstem.vn/product/may-tinh-lap-trinh-yolobit/>`_
     - `Mua sản phẩm <https://ohstem.vn/product/grove-shield/>`_
     - `Mua sản phẩm <https://ohstem.vn/product/cam-bien-sieu-am/>`_


- **Bước 2**: Cắm Yolo:Bit vào mạch mở rộng
- **Bước 3**: Sử dụng dây Grove cắm vào cảm biến
- **Bước 4**: Kết nối cảm biến với **P10/P13 trên mạch mở rộng**.

..  figure:: images/14.2.png
    :scale: 100%
    :align: center 
|


**4. Hướng dẫn lập trình với OhStem App**
--------
------------

- **Bước 1:** Tải thư viện **AIOT KIT**, xem hướng dẫn tải thư viện `tại đây <https://docs.ohstem.vn/en/latest/module/cai-dat-thu-vien.html>`_


    .. image:: images/aiot.png
        :width: 250px
        :align: center 
    |

    Sau khi tải thư viện, trong danh mục khối lệnh sẽ xuất hiện các khối lệnh tương ứng:

    .. image:: images/lenh_aiot.png
        :width: 800px
        :align: center 
    |

    Khi sử dụng cảm biến siêu âm, trước tiên, chúng ta cần khai báo tên cổng mà bạn cắm cảm biến trên mạch mở rộng:

    .. image:: images/14.3.png
        :scale: 80%
        :align: center 
    |

- **Bước 2**: Gửi chương trình sau xuống Yolo:Bit

..  image:: images/14.4.png
    :scale: 100%
    :align: center 
|

.. note::

    **Giải thích chương trình:** 
    
    Sau khi khai báo chân làm việc với cảm biến. Chương trình sẽ hiển thị thông tin cảm biến đo được lên cửa sổ Serial và phát âm cảnh báo nếu phát hiện vật cản trong phạm vi 20cm. 


**5. Hướng dẫn lập trình Arduino**
--------
------------

- Mở phần mềm Arduino IDE. Xem hướng dẫn lập trình với Arduino `tại đây <https://docs.ohstem.vn/en/latest/module/cai-dat-arduino.html>`_.  

- Copy đoạn code sau, click vào nút ``Verify`` để kiểm tra lỗi chương trình. Sau khi biên dịch không báo lỗi, bạn có thể nạp đoạn code vào board. 

.. code-block:: guess

    #include "YoloBit.h"

    YoloBit yolobit;

    #include <Ultrasonic.h>

    int triggerPin = P10;
    int echoPin = P13;

    void setup() {
      Serial.begin(115200);
    }

    void loop() {
      // Chuyển CM làm tham số để có khoảng cách tính bằng CM
      distance = ultrasonic.read();
    
      Serial.print("Distance in CM: ");
      Serial.println(distance);
      delay(200);
    }

.. note:: 
    
    **Giải thích chương trình:** Sau khi chạy chương trình, mở cửa sổ Serial và quan sát kết quả in ra khi bạn đưa ta tới gần hoặc ra xa cảm biến.

..  image:: images/14.5.png
    :scale: 100%
    :align: center 
|