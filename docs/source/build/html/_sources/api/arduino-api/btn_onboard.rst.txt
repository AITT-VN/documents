:mod:`btn_onboard` --- Onboard Button
=============================================

Chức năng chính và chức năng của ``btn_onboard``

Function
----------------------

.. function:: digitalRead(D2_1)

  Nút nhấn trên board được nối với Pin 1 của PORT mở rộng 2 trên xController, nên ta chỉ cần đọc giá trị digitalRead() của D2_1.

Sample Code
----------------------

.. code-block:: guess
 
  int buttonPin = D2_1;
  int buttonState = 0;

  void setup() {
    Serial.begin(9600);
    pinMode(buttonPin, INPUT);
  }

  void loop() {
    // đọc trạng thái của nút nhấn
    buttonState = digitalRead(buttonPin);

    // kiểm tra xem nút có được nhấn không
    // nếu nút được nhấn thì giá trị là LOW
    if (buttonState == LOW) {
      Serial.println("Nút trên board đang được nhấn");
    } else {
      Serial.println("Nút trên board đang không được nhấn");
    }
  }