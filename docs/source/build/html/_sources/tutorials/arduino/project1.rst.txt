Project 1: Đèn điều khiển từ xa
====================

Mục tiêu
-----------

Bạn vừa lên giường trùm chăn ấm và chợt nhận ra là quên chưa tắt đèn, hay bạn băn khoăn không biết vừa nãy đã tắt điện phòng tắm chưa. Nếu ở trong những tình huống này, bạn sẽ làm gì? 

Sẽ rất thuận tiện nếu bạn có thể bật tắt đèn từ xa bằng remote phải không nào? Ngoài ra, không chỉ là bật tắt, chúng ta sẽ dùng remote để điều chỉnh độ sáng đèn phù hợp cho nhiều hoàn cảnh sử dụng như đọc sách, xem phim hay khi chuẩn bị đi ngủ.

Trong dự án này, chúng ta sẽ dùng đèn LED RGB có trên hộp điều khiển xController để mô phỏng đèn trong nhà và sử dụng remote hồng ngoại để có thể:

  - Tăng giảm độ sáng bằng 2 phím ``lên`` và ``xuống``. Mỗi lần tăng giảm 25% độ sáng.
  - Bật hoặc tắt đèn LED bằng phím ``Setup``

.. image:: images/project-1-1.png
  :width: 320
  :align: center

Thiết bị cần sử dụng
-----------

.. image:: images/project-1-2.png
  :width: 420
  :align: center


Viết chương trình
--------------

Mở phần mềm Arduino IDE.

Copy đoạn code sau, click vào nút ``Verify`` để kiểm tra lỗi chương trình. Sau khi biên dịch không báo lỗi, bạn có thể nạp đoạn code vào board.

.. code-block:: guess

  #include <xcontroller.h>
  #include <IRremote.h>

  XController xcon;
  IRrecv irrecv(IR_RX);
  int irCommand;
  int lightLevel = 0;

  void setup()
  {
    irrecv.begin();
    Serial.begin(9600);   
  }

  void loop() {
    if (irrecv.decode()) {
      irCommand = irrecv.decodedIRData.command;
      Serial.println(irCommand);
      if (irCommand == IR_REMOTE_UP){
        lightLevel += 50; // tăng độ sáng 25%
        if (lightLevel > 255) {
          lightLevel = 255;
        }
      } else if (irCommand == IR_REMOTE_DOWN){
        lightLevel -= 50; // giảm độ sáng 25%
        if (lightLevel < 0) {
          lightLevel = 0;
        }
      } else if (irCommand == IR_REMOTE_SETUP){
        if (lightLevel > 0) { // đèn đang bật thì tắt
          lightLevel = 0;
        } else { // đèn đang tắt thì bật
          lightLevel = 255;
        }
      }
      xcon.showLED(0, lightLevel, 0, 0);
      irrecv.resume();
      delay(200);
    }
  }

Giải thích chương trình
--------------

Chương trình sử dụng các lệnh đã học ở những bài học trước về remote và đèn LED RGB. Chúng ta dùng biến tên ``lightLevel`` có kiểu là ``int`` để lưu độ sáng hiện tại của đèn LED và thay đổi độ sáng tùy vào phím được nhấn.