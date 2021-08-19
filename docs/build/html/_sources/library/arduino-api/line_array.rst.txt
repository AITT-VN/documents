:mod:`line_array` --- Line Array Module
=============================================

Chức năng chính và chức năng của ``line_array``

Function
----------------------

.. function:: LineArray(scl, sda)

    Khởi tạo module Line Array và khai báo 2 chân IO (sử dụng cho giao tiếp I2C) để kết nối với module.
     
    Ví dụ: Nếu chúng ta sử dụng PORT số 1 thì 2 chân IO tín hiệu tương ứng sẽ là D1_1 và D1_2.

.. function:: read()

    Đọc trạng thái của line finder array.

    Trong đó:

        - Kết quả trả về ``TUPLE`` 4 giá trị tương ứng với trạng thái của 4 mắt S1 đến S4, ví dụ: ``(0, 1, 1, 0)`` với ``0`` là đọc được line trắng còn ``1`` là line đen.

.. function:: read(TUPLE)

    Đọc trạng thái từng mắt đọc của Module.

    *TUPLE* : Có giá trị từ ``0 ~ 3`` tương ứng với 4 mắt đọc của Module.

Sample Code
----------------------

.. code-block:: guess

    #include "LineArray.h"

    line_array LineArray(D1_1, D1_2;

    void setup() {
        Serial.begin(9600); 
    }

    void loop(){
        Serial.println(line_array.read());
        delay(1000)
    }
