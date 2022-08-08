Project 5: Cửa thông minh
====================

Mục tiêu
-----------

Mỗi khi về đến nhà, nếu trong tay đang phải xách rất nhiều đồ đạc mà lại phải dùng chìa khóa để mở cửa thì cũng phiền bạn nhỉ? Chúng ta hãy làm một giải pháp khóa cửa thông minh như sau:

  - Nhấn nút A trên remote để khóa cửa.
  - Nhấn nút B trên remote để bắt đầu nhập mật mã và nút C để kết thúc quá trình nhập.
  - Trong khi nhập mật mã, thông tin sẽ được hiển thị lên màn hình LCD.
  - Nếu mật mã nhập đúng, cửa sẽ mở ra.

Chúng ta sẽ dùng động cơ Servo để đóng và mở cửa ngôi nhà.


Thiết bị cần sử dụng
-----------

.. image:: images/project-5-1.png
  :width: 600
  :align: center

Kết nối phần cứng
-----------

.. image:: images/project-5-2.png
  :width: 600
  :align: center


Viết chương trình
--------------

Mở phần mềm Arduino IDE.

Copy đoạn code sau, click vào nút ``Verify`` để kiểm tra lỗi chương trình. Sau khi biên dịch không báo lỗi, bạn có thể nạp đoạn code vào board.

.. code-block:: guess

  #include <xcontroller.h>
  #include <IRremote.h>
  #include <Servos.h>
  #include <LCD_1602.h>

  #define PASSCODE "1234"

  XController xcon;
  IRrecv irrecv(IR_RX);
  LCD_1602 lcd(0x21);
  Servos s;

  int irCommand;

  void setup()
  {
    Serial.begin(9600);
    irrecv.begin();
    s.init();
    s.position(0, 0);
    lcd.begin(D1_1, D1_2);
    lcd.backlight();
  }

  void loop() {
    if (irrecv.decode()) {
      irCommand = irrecv.decodedIRData.command;
      Serial.println(irCommand);
      irrecv.resume();
      if (irCommand == IR_REMOTE_A){
        // khóa cửa lại
        s.position(0, 0);
      } else if (irCommand == IR_REMOTE_B){
        // bắt đầu nhập mật mã
        lcd.clear();
        lcd.setCursor(0, 0);
        lcd.print("Hay nhap mat ma:");
        String passcode = "";
        while (irCommand != IR_REMOTE_C) {
          // liên tục đọc tín hiệu remote để nhập
          // mật mã cho đến khi phím C được nhấn
          if (irrecv.decode()) {
            irCommand = irrecv.decodedIRData.command;
            Serial.println(irCommand);
            char input;
            switch (irCommand) {
              case IR_REMOTE_0:
                passcode += "0";
                break;
              case IR_REMOTE_1:
                passcode += "1";
                break;
              case IR_REMOTE_2:
                passcode += "2";
                break;
              case IR_REMOTE_3:
                passcode += "3";
                break;
              case IR_REMOTE_4:
                passcode += "4";
                break;
              case IR_REMOTE_5:
                passcode += "5";
                break;
              case IR_REMOTE_6:
                passcode += "6";
                break;
              case IR_REMOTE_7:
                passcode += "7";
                break;
              case IR_REMOTE_8:
                passcode += "8";
                break;
              case IR_REMOTE_9:
                passcode += "9";
                break;
            }
            lcd.setCursor(0, 1);
            lcd.print(passcode);
            delay(500);
            irrecv.resume();
          }
        }

        // nhập mật mã đã xong, cần kiểm tra
        if (passcode == PASSCODE) {
          lcd.setCursor(0, 1);
          lcd.print("Mat ma dung");
          s.position(0, 90);
        } else {
          lcd.setCursor(0, 1);
          lcd.print("Mat ma sai");
        }
      }
    }
  }


Giải thích chương trình
--------------

.. code-block:: guess

  #define PASSCODE "1234"

Khai báo mật mã của ngôi nhà là 4 số “1234”.

.. code-block:: guess

  s.position(0, 0);

Trong hàm ``setup()``, ta cho Servo quay về góc ``0`` độ (vị trí mà cửa được khóa).

.. code-block:: guess

  if (irCommand == IR_REMOTE_A){
    // khóa cửa lại
    s.position(0, 0);
  }

Trong hàm ``loop()``, chúng ta liên tục kiểm tra tín hiệu từ remote. 

Nếu phím A được nhấn thì sẽ khóa cửa lại bằng cách cho Servo quay về góc ``0`` độ (nếu đang mở).

.. code-block:: guess

  } else if (irCommand == IR_REMOTE_B){
        // bắt đầu nhập mật mã
        lcd.clear();
        lcd.setCursor(0, 0);
        lcd.print("Hay nhap mat ma:");
        String passcode = "";

Nếu phím B được nhấn, ta sẽ xóa trắng màn hình LCD và hiển thị thông báo: “bắt đầu nhập mật mã”. Biến ``passcode`` có chức năng lưu mật mã đang nhập để kiểm tra sau khi nhập xong.

.. code-block:: guess

  while (irCommand != IR_REMOTE_C) {
    // liên tục đọc tín hiệu remote để nhập
    // mật mã cho đến khi phím C được nhấn
    if (irrecv.decode()) {
      irCommand = irrecv.decodedIRData.command;
      Serial.println(irCommand);
      char input;
      switch (irCommand) {
      case IR_REMOTE_0:
        passcode += "0";
        break;
      case IR_REMOTE_1:
        passcode += "1";
        break;
      case IR_REMOTE_2:
        passcode += "2";
        break;
      case IR_REMOTE_3:
        passcode += "3";
        break;
      case IR_REMOTE_4:
        passcode += "4";
        break;
      case IR_REMOTE_5:
        passcode += "5";
        break;
      case IR_REMOTE_6:
        passcode += "6";
        break;
      case IR_REMOTE_7:
        passcode += "7";
        break;
      case IR_REMOTE_8:
        passcode += "8";
        break;
      case IR_REMOTE_9:
        passcode += "9";
        break;
      }
      lcd.setCursor(0, 1);
      lcd.print(passcode);
      delay(500);
      irrecv.resume();
    }
  }

Đây là đoạn code chính để xử lý phần nhập mật mã. Nếu phím được nhấn chưa phải là phím C thì sẽ tiếp tục lưu nút được nhấn vào biến ``passcode`` và hiện lên màn hình LCD.

.. code-block:: guess

  // nhập mật mã đã xong, cần kiểm tra
  if (passcode == PASSCODE) {
    lcd.setCursor(0, 1);
    lcd.print("Mat ma dung");
    s.position(0, 90);
  } else {
    lcd.setCursor(0, 1);
    lcd.print("Mat ma sai");
  }

Nếu phím C được nhấn, vòng lặp nhập mật mã sẽ kết thúc. Đến đây, chương trình sẽ kiểm tra mật mã đã nhập (được lưu trong biến ``passcode``) có giống mật mã ta đã khai báo ban đầu không (là ``1234``). 

Nếu giống thì sẽ mở khóa bằng cách cho Servo quay đến góc ``90`` độ. Ngược lại, nếu mật mã sai thì sẽ thông báo cho người dùng biết.

Như vậy, các bạn đã hoàn thành 5 project để hoàn thiện 5 chức năng khá thú vị của một ngôi nhà thông minh và hiện đại rồi. Bài tập dành cho bạn là hãy tìm cách tổng hợp code của cả 5 project thành một chương trình hoàn chỉnh cho ngôi nhà nhé.

Bạn có thể tham khảo chương trình mẫu có sẵn trên đường link chứa toàn bộ code mẫu của tài liệu Arduino này nhé.

* :download:`Arduino Tutorial Code <https://github.com/AITT-VN/xbuild_creator_kit/tree/main/Arduino>`
