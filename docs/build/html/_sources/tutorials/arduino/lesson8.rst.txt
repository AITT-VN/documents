9. Bài học 8: Phát nhạc với còi báo
====================

Mục tiêu
-----------

Tương tự như module đèn LED, còi báo (buzzer) được tích hợp trên board xController cũng là một module thuộc loại output, có chức năng phát ra âm thanh. Trong bài học này, chúng ta sẽ học cách dùng thư viện xController để buzzer phát ra các nốt nhạc và ghép thành một bài nhạc hoàn chỉnh.


Thiết bị cần sử dụng
-----------

.. image:: images/device-1.png
  :width: 480
  :align: center

Viết chương trình
--------------

Mở phần mềm Arduino IDE.

Nếu bạn chưa cài đặt thư viện cho xController thì tham khảo bài học số 4 để tải và cài đặt thư viện vào Arduino IDE.

Copy đoạn code sau, click vào nút ``Verify`` để kiểm tra lỗi chương trình. Sau khi biên dịch không báo lỗi, bạn có thể nạp đoạn code vào board.

.. code-block:: guess

  #include <xcontroller.h>

  #define BUZZER_CHANNEL 0 // giá trị bất kỳ từ 0 đến 15

  XController xcon;

  void setup() { }

  void loop() {
    // phát bài nhạc Twinkle twinkle little stars
    // đoạn 1: Đồ, Đồ, Son, Son, La, La, Son
    xcon.tone(NOTE_C4, 500, BUZZER_CHANNEL);
    xcon.noTone(BUZZER_CHANNEL);
    xcon.tone(NOTE_C4, 500, BUZZER_CHANNEL);
    xcon.noTone(BUZZER_CHANNEL);
    xcon.tone(NOTE_G4, 500, BUZZER_CHANNEL);
    xcon.noTone(BUZZER_CHANNEL);
    xcon.tone(NOTE_G4, 500, BUZZER_CHANNEL);
    xcon.noTone(BUZZER_CHANNEL);
    xcon.tone(NOTE_A4, 500, BUZZER_CHANNEL);
    xcon.noTone(BUZZER_CHANNEL);
    xcon.tone(NOTE_A4, 500, BUZZER_CHANNEL);
    xcon.noTone(BUZZER_CHANNEL);
    xcon.tone(NOTE_G4, 500, BUZZER_CHANNEL);
    xcon.noTone(BUZZER_CHANNEL);
    delay(500);
    // đoạn 2: Fa, Fa, Mi, Mi, Rê, Rê, Đồ
    xcon.tone(NOTE_F4, 500, BUZZER_CHANNEL);
    xcon.noTone(BUZZER_CHANNEL);
    xcon.tone(NOTE_F4, 500, BUZZER_CHANNEL);
    xcon.noTone(BUZZER_CHANNEL);
    xcon.tone(NOTE_E4, 500, BUZZER_CHANNEL);
    xcon.noTone(BUZZER_CHANNEL);
    xcon.tone(NOTE_E4, 500, BUZZER_CHANNEL);
    xcon.noTone(BUZZER_CHANNEL);
    xcon.tone(NOTE_D4, 500, BUZZER_CHANNEL);
    xcon.noTone(BUZZER_CHANNEL);
    xcon.tone(NOTE_D4, 500, BUZZER_CHANNEL);
    xcon.noTone(BUZZER_CHANNEL);
    xcon.tone(NOTE_C4, 500, BUZZER_CHANNEL);
    xcon.noTone(BUZZER_CHANNEL);
    delay(1000);
  }


Giải thích chương trình
--------------

.. code-block:: guess

  #define BUZZER_CHANNEL 0 // giá trị bất kỳ từ 0 đến 15

Thư viện làm việc với còi báo cũng sử dụng PWM để phát nhạc. Bạn có thể xem lại kiến thức về PWM trong bài học 5. Ở đây, chúng ta khai báo kênh PWM muốn sử dụng là 0.

.. code-block:: guess
  
  xcon.tone(NOTE_C4, 500, BUZZER_CHANNEL);
  xcon.noTone(BUZZER_CHANNEL);

Trong hàm ``loop()`` của chương trình, 2 câu hàm ``tone()`` và ``notone()`` được sử dụng để phát ra nhạc và tắt nhạc. Hai hàm này có cú pháp như sau:

.. code-block:: guess

  tone(frequency, duration, channel);

.. code-block:: guess

  noTone(channel);

Ý nghĩa các tham số:

  - ``frequency``: Tần số hoặc tên nốt nhạc cần phát
  - ``duration``: Thời gian kéo dài
  - ``channel``: kênh PWM dùng để phát (nhận giá trị từ 0-15)

*Sau khi chạy chương trình, còi báo tích hợp trên board xController sẽ liên tục phát ra các nốt nhạc của bài hát quen thuộc “Twinkle Twinkle Little Stars”.*