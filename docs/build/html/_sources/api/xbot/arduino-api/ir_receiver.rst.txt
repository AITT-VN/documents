:mod:`ir_receiver` --- IR Receiver Sensor
=============================================

Chức năng chính và chức năng của ``ir_receiver``

Board xController được tích hợp sẵn 2 đèn LED hồng ngoại, một LED thu và một LED phát.

Trong tài liệu này, ta sẽ làm việc với LED thu hồng ngoại và Remote đi kèm.

Function
----------------------

.. function:: #include <IRremote.h>

  Khai báo sử dụng thư viện để làm việc với remote IR.
  
.. function:: IRrecv irrecv(IR_RX);

  Khai báo đối tượng để thu và xử lý tín hiệu IR cùng với chân IO nối với đèn LED thu IR. IR_RX là số chân IO đã được định nghĩa sẵn trong cài đặt của board xController.

.. function:: begin()

  Khởi tạo và bắt đầu xử lý tín hiệu IR.

.. function:: decode()

  Hàm decode() sẽ giải mã tín hiệu nhận được. Nếu có tín hiệu nhận được và giải mã thành công thì hàm này sẽ trả về true.

  Ta thường dùng hàm này để kiểm tra xem xController có nhận được tín hiệu từ Remote hay không.

.. function:: decodedIRData.command()

  Mã hóa tín hiệu đọc được từ hàm ``decode()``.

.. function:: resume()

  Chạy lại chức năng thu tín hiệu.

.. function:: irCommand == IR_REMOTE_A

  Trả về chuỗi tương ứng với phím được nhấn trên IR remote.
  Trên remote có các nút nhấn là A|B|C|D|E|F|lên|xuống|trái|phải|setup|0|1|2|3|4|5|6|7|8|9, tương ứng với các giá trị đã được khai báo sẵn trong thư viện như sau: IR_REMOTE_A, IR_REMOTE_B ... IR_REMOTE_F .. IR_REMOTE_0 .. IR_REMOTE_9, IR_REMOTE_SETUP


Sample Code
----------------------
Điều khiển led_onboard bằng IR remote.

.. code-block:: guess

  #include <xcontroller.h>
  #include <IRremote.h>

  XController xcon;
  IRrecv irrecv(IR_RX);
  int irCommand;

  void setup()
  {
    irrecv.begin();
    Serial.begin(9600);   
  }

  void loop() {
    if (irrecv.decode()) {
      irCommand = irrecv.decodedIRData.command;
      Serial.println(irCommand);
      irrecv.resume();
      if (irCommand == IR_REMOTE_A){
        xcon.showLed(0, 255, 0, 0);
      } else if (irCommand == IR_REMOTE_B){
        xcon.showLed(0, 0, 255, 0);
      } else if (irCommand == IR_REMOTE_C){
        xcon.showLed(0, 0, 0, 255);
      } else if (irCommand == IR_REMOTE_D){
        xcon.showLed(0, 255, 255, 255);
      } else {
        xcon.showLed(0, 0, 0, 0);
      }
    }
  }