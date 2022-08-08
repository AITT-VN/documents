:mod:`speaker` --- Speaker
=============================================


Chức năng chính và chức năng của ``speaker``

Function
----------------------

.. function:: noTone(channel);

    Dừng chơi nhạc. Với ``channel`` là kênh PWM dùng để phát (nhận giá trị từ 0-15) và phải trùng ``channel`` trong hàm ``tone``.

.. function:: tone(frequency, duration, channel);

    Phát 1 bài nhạc hoặc 1 nốt nhạc. Trong đó:
    
        - ``frequency``: Tần số hoặc tên nốt nhạc cần phát
        - ``duration``: Thời gian kéo dài
        - ``channel``: kênh PWM dùng để phát (nhận giá trị từ 0-15)

Sample Code
----------------------
Phát bài Happy Birthday khi nhấn giữ nút trên xController

.. code-block:: guess

    #include <xcontroller.h>

    #define BUZZER_CHANNEL 0 // any from 0-15

    XController xcon;
    // the setup function runs once when you press reset or power the board
    void setup() {
    }

    // the loop function runs over and over again forever
    void loop() {
    xcon.tone(NOTE_C4, 500, BUZZER_CHANNEL);
    xcon.noTone(BUZZER_CHANNEL);
    xcon.tone(NOTE_D4, 500, BUZZER_CHANNEL);
    xcon.noTone(BUZZER_CHANNEL);
    xcon.tone(NOTE_E4, 500, BUZZER_CHANNEL);
    xcon.noTone(BUZZER_CHANNEL);
    xcon.tone(NOTE_F4, 500, BUZZER_CHANNEL);
    xcon.noTone(BUZZER_CHANNEL);
    xcon.tone(NOTE_G4, 500, BUZZER_CHANNEL);
    xcon.noTone(BUZZER_CHANNEL);
    xcon.tone(NOTE_A4, 500, BUZZER_CHANNEL);
    xcon.noTone(BUZZER_CHANNEL);
    xcon.tone(NOTE_B4, 500, BUZZER_CHANNEL);
    xcon.noTone(BUZZER_CHANNEL);
    }
