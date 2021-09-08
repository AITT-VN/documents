:mod:`pins` --- Pins
=============================================


Chức năng chính và chức năng của ``pins``

Có 2 loại tín hiệu cơ bản mà chúng ta sẽ làm việc với chúng trong lập trình điện tử, đó là tín hiệu Digital và tín hiệu Analog. Chúng ta sẽ tìm hiểu về Analog trong các bài học sau. 

Tín hiệu Digital là tín hiệu chỉ có 2 giá trị là Tắt (còn gọi là LOW, 0V) và Bật (HIGH, 3.3V hay 5V tùy vào điện áp hoạt động của hệ thống, xController sử dụng 3.3V).

Khác với tín hiệu Digital Input, tín hiệu Analog Input giúp đo các giá trị đầu vào theo một dải giá trị thay vì chỉ là HIGH và LOW. 

Tuy nhiên, xét về bản chất, máy tính chỉ có thể hiểu được tín hiệu Digital (các giá trị 0 và 1). Do đó, các chip vi điều khiển đều có 1 bộ chuyển đổi từ tín hiệu Analog sang Digital, gọi là ADC (Analog to Digital Converter).

Lưu ý: Trong 6 cổng mở rộng của xController, chỉ có cổng 4, 5 và 6 là có bộ ADC và có thể giao tiếp được với các module sử dụng tín hiệu Analog. Giá trị tín hiệu các chân Analog này có dải từ 0 (tương ứng với 0V) đến 4095 (tương ứng với 3.3V).

Ví dụ: Nếu giá trị tín hiệu Analog xuất ra là 2047 thì điện áp sẽ nằm trong khoảng 1.65V.


Function
----------------------

Lưu ý: Trên board xController có 6 cổng mở rộng, được đánh số từ 1 đến 6. Mỗi cổng gồm 4 đường tín hiệu:

    - 2 đường tín hiệu dành cho nguồn điện là GND (nguồn âm, 0V) và VCC (nguồn dương, 3.3V)
    - 2 đường tín hiệu logic, có thể sử dụng cho tín hiệu Digital (cả 6 cổng) hoặc Analog (chỉ hỗ trợ trên cổng 4, 5 và 6)

        - ``Digital``: D1_1|D1_2|D2_1|D2_2|D3_1|D3_2|D4_1|D4_2|D5_1|D5_2|D6_1|D6_2
        - ``Analog``: A4_1|A4_2|A5_1|A5_2|A6_1|A6_2|

.. function:: pinMode(pin, mode)

    Cấu hình 1 pin quy định hoạt động như là một đầu vào (INPUT) hoặc đầu ra (OUTPUT). Xem mô tả kỹ thuật số (datasheet) để biết chi tiết về các chức năng của các chân. 

    Như trong phiên bản Arduino 1.0.1, nó có thể kích hoạt các điện trở pullup nội bộ với chế độ INPUT_PULLUP. Ngoài ra, chế độ INPUT vô hiệu hóa một cách rõ ràng điện trở pullups nội bộ.

        - ``pin``: tương ứng với cổng mở rộng trên board. Lưu ý: Trên board xController có 6 cổng mở rộng, được đánh số từ 1 đến 6. Mỗi cổng gồm 4 đường tín hiệu:

        - ``mode``: INPUT, INPUT_PULLUP hoặc OUTPUT
        
.. function:: digitalWrite(pin, value)

    - Xuất tín hiệu ra các chân digital, có 2 giá trị là HIGH hoặc là LOW

    - Nếu một pin được thiết đặt là OUTPUT bởi pinMode(). Và bạn dùng digitalWrite để xuất tín hiệu thì điện thế tại chân này sẽ là 5V (hoặc là 3,3 V trên mạch 3,3 V) nếu được xuất tín hiệu là HIGH, và 0V nếu được xuất tín hiệu là LOW.

    - Nếu một pin được thiết đặt là INPUT bởi pinMode(). Lúc này digitalWrite sẽ bật (HIGH) hoặc tắt (LOW) hệ thống điện trở pullup nội bộ. Chúng tôi khuyên bạn nên dùng INPUT_PULLUP nếu muốn bật hệ thống điện trở pullup nội bộ.

        - ``pin``: chân IO cần xuất tín hiệu
        - ``Value``: giá trị cần xuất, HIGH hoặc LOW .

.. function:: digitalRead(pin)

    - Đọc tín hiệu điện từ một chân digital (được thiết đặt là INPUT). Trả về 2 giá trị HIGH hoặc LOW.

    - ``pin``: giá trị của Digital muốn đọc.

.. function:: analogRead(pin)

    - Đọc giá trị tín hiệu Analog ở chân IO được chỉ định, đồng thời trả về giá trị kiểu số nguyên int (nằm trong khoảng từ 0 đến 4095)

    - ``pin``: giá trị của Analog muốn đọc.


Sample Code
----------------------
Bật tắt PORT 1 - PIN 1 của xController

.. code-block:: guess

    // Blink LED
    // Bật tắt đèn LED sau mỗi 1 giây
    int LEDPin = D1_1; 

    void setup() { 
    pinMode(LEDPin, OUTPUT);
    }

    void loop() {
    digitalWrite(LEDPin, HIGH);
    delay(1000);
    digitalWrite(LEDPin, LOW);
    delay(1000);
    }