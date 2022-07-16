18. Project 3: Đèn thông minh
====================

Mục tiêu
-----------

Trong một ngôi nhà, nếu đèn có thể tự bật một cách thông minh khi có người hoặc khi trời bắt đầu tối thì sẽ rất thuận tiện đấy. Một số ví dụ phổ biến là đèn ngoài cửa khi ta đi về nhà hoặc đèn cầu thang khi ta đi lên xuống buổi tối.

Trong bài này, chúng ta cùng nhau làm một đèn ngoài cửa nhà thông minh với các tính năng sau:

  - Tự động bật đèn khi phát hiện chuyển động hoặc khi trời đang tối
  - Tự động tắt sau 15 giây

Để phát hiện được có người, chúng ta sẽ dùng một cảm biến mới là cảm biến phát hiện chuyển động bằng hồng ngoại (``Passive Infrared``, gọi tắt là ``PIR``). 

.. image:: images/project-3-1.png
  :width: 320
  :align: center

Khi phát hiện có chuyển động, chân tín hiệu của module sẽ được bật ở mức ``HIGH``. Bình thường, chân tín hiệu này sẽ ở mức ``LOW``.

Thiết bị cần sử dụng
-----------

.. image:: images/project-3-2.png
  :width: 600
  :align: center

Kết nối phần cứng
-----------

.. image:: images/project-3-3.png
  :width: 600
  :align: center


Viết chương trình
--------------

Mở phần mềm Arduino IDE.

Copy đoạn code sau, click vào nút ``Verify`` để kiểm tra lỗi chương trình. Sau khi biên dịch không báo lỗi, bạn có thể nạp đoạn code vào board.

.. code-block:: guess

  #define LIGHT_PIN A4_1
  #define PIR_PIN D5_1
  #define LED_PIN D6_1
  
  int lightSensorValue = 0;
  int pirState = 0;
  int LEDState = 0;

  unsigned long LEDOnTime = 0; // lưu thời gian lúc bật đèn

  void setup() {
    pinMode(LED_PIN, OUTPUT);
    pinMode(PIR_PIN, INPUT);
  }

  void loop() {
    // đọc giá trị cảm biến ánh sáng
    lightSensorValue = analogRead(LIGHT_PIN);
    pirState = digitalRead(PIR_PIN);
    if (pirState == HIGH && lightSensorValue < 200) {
      // trời tối và phát hiện có người => bật đèn
      digitalWrite(LED_PIN, HIGH);
      LEDOnTime = millis();
      LEDState = 1;
    }

    // lấy thời gian hiện tại
    unsigned long currentMillis = millis();
    if (LEDState == 1 && currentMillis - LEDOnTime >= 10000) {
      // đã bật đèn được quá 15s => tắt đèn
      digitalWrite(LED_PIN, LOW);
      LEDOnTime = 0;
      LEDState = 0;
    }
  }


Giải thích chương trình
--------------

Trong chương trình trên, chúng ta sẽ sử dụng các hàm đơn giản đã học là ``digitalRead()`` để đọc tín hiệu Digital từ cảm biến PIR và hàm ``analogRead()`` để đọc giá trị cảm biến ánh sáng. Sau đó, chương trình kiểm tra điều kiện có phát hiện sự chuyển động và trời có đang tối không để bật đèn.

Sau khi bật đèn, chúng ta sử dụng cách thức đo thời gian như trong project 2 để biết đến lúc phải tắt đèn (sau 10 giây tính từ lúc bật đèn).
