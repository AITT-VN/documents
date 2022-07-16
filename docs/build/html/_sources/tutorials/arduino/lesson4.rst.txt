5. Bài học 4: Điều khiển tốc độ chớp tắt đèn LED
====================

Mục tiêu
-----------

Trong bài học trước, chúng ta đã tìm hiểu về ``Digital Input`` thông qua nút nhấn với 2 trạng thái là ``HIGH`` và ``LOW``. Tuy nhiên trong thực tế, đôi lúc chúng ta cần nhiều hơn 2 trạng thái như vậy. Một số ví dụ: nút điều chỉnh âm thanh (cho biết âm lượng đang ở mức nào) hay cảm biến ánh sáng (độ sáng là bao nhiêu),…

Trong bài học này, chúng ta sẽ cùng tìm hiểu về tín hiệu Analog và lập trình điều khiển thời gian chớp tắt đèn LED bằng giá trị của cảm biến xoay.

Kiến thức mới
-----------

*Tín hiệu Analog*

Khác với tín hiệu ``Digital Input``, tín hiệu Analog Input giúp đo các giá trị đầu vào theo một dải giá trị thay vì chỉ là ``HIGH`` và ``LOW``. 

Tuy nhiên, xét về bản chất, máy tính chỉ có thể hiểu được tín hiệu ``Digital`` (các giá trị ``0`` và ``1``). Do đó, các chip vi điều khiển đều có 1 bộ chuyển đổi từ tín hiệu ``Analog`` sang ``Digital``, gọi là ``ADC`` (Analog to Digital Converter).

.. image:: images/ls-4-1.png
  :width: 500
  :align: center

Lưu ý: Trong 6 cổng mở rộng của xController, chỉ có cổng 4, 5 và 6 là có bộ ``ADC`` và có thể giao tiếp được với các module sử dụng tín hiệu ``Analog``. Giá trị tín hiệu các chân ``Analog`` này có dải từ ``0`` (tương ứng với 0V) đến ``4095`` (tương ứng với 3.3V).

Ví dụ: Nếu giá trị tín hiệu ``Analog`` xuất ra là ``2047`` thì điện áp sẽ nằm trong khoảng ``1.65V``.

Thiết bị cần sử dụng
-----------

.. image:: images/device-4.png
  :width: 600
  :align: center

Kết nối phần cứng
-----------

.. image:: images/ls-4-2.png
  :width: 500
  :align: center


Viết chương trình
--------------

Mở phần mềm Arduino IDE.

Copy đoạn code sau, click vào nút ``Verify`` để kiểm tra lỗi chương trình. Sau khi biên dịch không báo lỗi, bạn có thể nạp đoạn code vào board.

.. code-block:: guess

  int LEDPin = D1_1; // Module LED nối vào cổng số 1
  int rotaryPin = A4_1; // Module rotary nối vào cổng số 4
  int rotaryValue = 0; 

  void setup() {
    pinMode(LEDPin, OUTPUT);
  }

  void loop() {
    // đọc giá trị cảm biến
    rotaryValue = analogRead(rotaryPin);
    // bật đèn LED
    digitalWrite(LEDPin, HIGH);
    // dừng chương trình trong khoảng thời gian 
    // bằng đúng giá trị cảm biến đọc được (milliseconds)
    delay(rotaryValue);
    // tắt đèn LED
    digitalWrite(LEDPin, LOW);
    // dừng chương trình trong khoảng thời gian 
    // bằng đúng giá trị cảm biến đọc được (milliseconds)
    delay(rotaryValue);
  }


Giải thích chương trình
--------------

.. code-block:: guess

  int rotaryPin = A4_1; 

Khai báo chân IO nối với cảm biến xoay. Do cảm biến xoay trả về tín hiệu ``Analog`` và được kết nối với cổng số 4 trên xController nên ta khai báo là ``A4_1``.

.. code-block:: guess
  
  pinMode(LEDPin, OUTPUT);

Cấu hình module LED là ``OUTPUT`` như đã học trong các bài trước.

.. code-block:: guess
  
  rotaryValue = analogRead(rotaryPin);

Đọc giá trị tín hiệu ``Analog`` ở chân IO được chỉ định, đồng thời trả về giá trị kiểu số nguyên (int) nằm trong khoảng từ ``0`` đến ``4095``.

.. code-block:: guess

  delay(rotaryValue);

Tạm ngừng chương trình một khoảng thời gian bằng với giá trị đọc được từ cảm biến xoay. Do đó, bạn có thể điều chỉnh thời gian tạm ngừng bằng cách xoay cảm biến qua trái (giảm dần) hoặc qua phải (tăng dần).

*Sau khi nạp chương trình vào board, bạn xoay biến trở sẽ thấy sự thay đổi về thời gian bật tắt đèn LED.*

*Nếu xoay về tận cùng bên trái (giá trị là 0) thì LED sẽ chớp liên tục và rất khó để nhận ra trạng thái bật tắt của đèn LED. Ngược lại, nếu xoay về tận cùng bên phải, giá trị đọc được sẽ là 4095 (tương đương với hơn 4 giây), bạn sẽ dễ dàng nhìn thấy LED bật và tắt hơn.*
