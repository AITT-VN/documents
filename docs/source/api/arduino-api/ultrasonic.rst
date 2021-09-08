:mod:`ultrasonic` --- Ultrasonic Module
=============================================


Chức năng chính và chức năng của ``ultrasonic``

Function
----------------------

.. function:: Ultrasonic(triggerPin, echoPin)

    Khởi tạo cảm biến siêu âm và khai báo 2 chân IO để kết nối với module.
     
    Ví dụ: Nếu chúng ta sử dụng PORT số 1 thì 2 chân IO tín hiệu tương ứng sẽ là D1_1 và D1_2.

.. function:: measureDistanceCm()

    Trả về giá trị khoảng cách đo được từ mắt đọc cảu ultrasonic tới vặt thể đổi diện với đơn vị ``centimet``

.. function:: measureDistanceMm()

    Trả về giá trị khoảng cách đo được từ mắt đọc cảu ultrasonic tới vặt thể đổi diện với đơn vị ``milimet``

Sample Code
----------------------
Hiển thị khoảng cách đo được từ cảm biến siêu âm 

.. code-block:: guess

    #include "Ultrasonic.h"

    ultrasonic Ultrasonic(D1_1, D1_2);

    void setup() {
        Serial.begin(9600); 
    }

    void loop(){
        Serial.println(ultrasonic.measureDistanceCm());
        delay(1000)
    }