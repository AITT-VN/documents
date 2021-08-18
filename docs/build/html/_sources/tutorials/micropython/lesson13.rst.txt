Bài học 13: Giao tiếp Bluetooth Low Energy
====================

Mục tiêu
-----------

Tìm hiểu về giao tiếp bằng tín hiệu Bluetooth Low Energy (BLE) và viết chương trình để điều khiển động cơ Servo bằng phần mềm trên điện thoại thông qua BLE.

Kiến thức mới
-----------

*Bluetooth Low Energy (BLE)*

xController sử dụng chip điều khiển ESP32, tích hợp nhiều kết nối không dây bao gồm Wi-Fi và Bluetooth Low Energy (BLE). BLE là một công nghệ Bluetooth tiết kiệm năng lượng, chủ yếu được dùng để truyền lượng dữ liệu nhỏ (băng thông thấp) với khoảng cách ngắn. 

Khác với chuẩn Bluetooth classic luôn được bật, BLE ngủ liên tục trừ khi bắt đầu kết nối. Đây là lý do BLE tiêu thụ năng lượng thấp: lượng tiêu thụ ít hơn 100 lần so với Bluetooth classic (tùy vào môi trường sử dụng). Hơn nữa, BLE không chỉ hỗ trợ giao tiếp Point-to-Point mà còn hỗ trợ Broadcast và Mesh Network.

.. image:: images/ls-13-1.png
  :width: 480
  :align: center

Do tính chất của nó, BLE phù hợp với các ứng dụng cần trao đổi một lượng nhỏ dữ liệu định kỳ, chỉ chạy trên một viên Pin. Ví dụ, BLE được sử dụng rất nhiều trong chăm sóc sức khỏe, thể dục, theo dõi, Beacons, an ninh và nhà thông minh.

.. image:: images/ls-13-2.png
  :width: 480
  :align: center

*Động cơ Servo*

Servo là một dạng động cơ điện đặc biệt. Không giống như động cơ thông thường, cứ cắm điện vào là quay liên tục, Servo chỉ quay khi được điều khiển (bằng xung PPM) với góc quay nằm trong khoảng bất kì từ 0o - 180o. Mỗi loại Servo có kích thước, khối lượng và cấu tạo khác nhau, phù hợp với nhiều ứng dụng khác nhau. 

Bộ xBuild Creator Kit cung cấp sẵn một động cơ Servo loại nhỏ là SG92R.

.. image:: images/ls-13-3.png
  :width: 480
  :align: center

Thiết bị cần sử dụng
-----------

.. image:: images/device-13.png
  :width: 600
  :align: center

Lưu ý: Để sử dụng động cơ Servo thì bộ điều khiển xController cần phải được cấp nguồn từ nguồn ngoài (như từ pin) vì nguồn từ USB không đủ điện năng để chạy động cơ. 

Kết nối phần cứng
-----------

.. image:: images/ls-13-4.png
  :width: 600
  :align: center

Viết chương trình
--------------

Mở phần mềm Arduino IDE.

Copy đoạn code sau, click vào nút ``Verify`` để kiểm tra lỗi chương trình. Sau khi biên dịch không báo lỗi, bạn có thể nạp đoạn code vào board.

.. code-block:: guess

  #include <xcontroller.h>
  #include <esp32BLEUtilities.h>
  #include <Servos.h>

  #define LEFT_PRESSED "!B714" // sự kiện nút left được nhấn
  #define RIGHT_PRESSED "!B813" // sự kiện nút right được nhấn

  Servos s;

  String cmd = "";
  int angle = 90;

  void setup() {
    Serial.begin(9600);
    s.init();
    s.position(0, 90);
    BLE.begin("OhStem-xController");
    delay(10);
    Serial.println("Setup Done!");
  }

  void loop() {
    if(BLE.isConnected()) {
      if (BLE.available()) {
        cmd = "";
        while(BLE.available()) {
          char data = BLE.read();
          cmd += data;
        }
        Serial.println(cmd);
      }
      
      if (cmd == LEFT_PRESSED) {
        if (angle > 0) {
          angle -= 5;
          s.position(0, angle);
        }      
      } else if (cmd == RIGHT_PRESSED) {
        if (angle < 180) {
          angle += 5;
          s.position(0, angle);
        }      
      }
    }
    delay(10); 
  }


Giải thích chương trình
--------------

Chương trình trên sẽ kiểm tra xem có nhận được dữ liệu gửi qua giao thức BLE hay không. Nếu tín hiệu tương ứng với nút sang trái trên phần mềm điều khiển (được giới thiệu bên dưới) thì cho động cơ Servo quay về 0 độ. Ngược lại, nếu tín hiệu nhận được tương ứng với nút sang phải thì cho động cơ xoay về 180 độ.

.. code-block:: guess

  #include <esp32BLEUtilities.h>
  #include <Servos.h>

Khai báo sử dụng thư viện để làm việc với BLE và động cơ Servo.

.. code-block:: guess

  Servos s;

Khai báo đối tượng ``Servos`` để điều khiển động cơ Servo.

.. code-block:: guess
  
  s.init();
  s.position(0, 90);

Khởi tạo đối tượng làm việc với Servo và quay Servo gắn vào cổng S1 đến trị trí chính giữa là góc 90 độ bằng hàm ``position`` của thư viện Servos.

Hàm ``position()`` có cấu trúc như sau:

.. code-block:: guess

  position(index, angle)

Các tham số sử dụng:

  - ``index``: Số thứ tự của cổng kết nối đến Servo, từ 0 (S1) đến 7 (S8).
  - ``Angle``: Góc cần quay, từ 0 đến 180 độ.

.. code-block:: guess

  BLE.begin("OhStem-xController");

Phát BLE với tên gọi là “OhStem-xController” để phần mềm có thể quét ra được và kết nối.

.. code-block:: guess

  if(BLE.isConnected()) {
      if (BLE.available()) {
        cmd = "";
        while(BLE.available()) {
          char data = BLE.read();
          cmd += data;
        }
        Serial.println(cmd);
      }

Sử dụng câu lệnh điều kiện: Nếu có phần mềm đang kết nối vào và có dữ liệu được gửi đến thì ta sẽ xóa lệnh cũ lúc trước đã lưu trong biến ``cmd``, đọc dữ liệu mới và lưu lại vào biến ``cmd``. Đồng thời, in ra cửa sổ ``Serial``.

.. code-block:: guess

  if (cmd == LEFT_PRESSED) {
    if (angle > 0) {
      angle -= 5;
      s.position(0, angle);
    }      
  }

Kiểm tra xem lệnh nhận được lúc này có phải đang là nút sang trái không. Nếu điều kiện đúng thì giảm góc quay được lưu trong biến Angle và điều khiển Servo quay đến vị trí góc mới này.

.. code-block:: guess

  } else if (cmd == RIGHT_PRESSED) {
    if (angle < 180) {
      angle += 5;
      s.position(0, angle);
    }      
  }

Tương tự: kiểm tra phím sang phải và tăng góc quay để điều chỉnh Servo.

*Lưu ý*: Ở cả 2 trường hợp, ta cần kiểm tra các góc giới hạn là 0 và 180 độ vì Servo chỉ có thể quay trong khoảng này.

Để kiểm tra chương trình trên, bạn cần cài đặt phần mềm có thể giao tiếp BLE, ví dụ như ``Bluefruit Connect`` của Adafruit.

.. image:: images/ls-13-5.png
  :width: 480
  :align: center

Sau khi cài đặt, bạn chạy app sẽ quét thấy một thiết bị BLE tên là ``OhStem-xController``. Nhấn vào nút ``Connect`` để kết nối và vào mục ``Controller > Control Pad`` để hiển thị giao diện điều khiển như hình bên dưới.

.. image:: images/ls-13-6.png
  :width: 240
  :align: center

*Bạn thử lần lượt nhấn vào nút sang trái và sang phải để điều chỉnh góc quay của động cơ.*
