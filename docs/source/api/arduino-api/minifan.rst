:mod:`minifan` --- Minifan
=============================================

Chức năng chính và chức năng của ``minifan``

Động cơ là một thiết bị điện tử rất phổ biến trong cuộc sống của chúng ta (như quạt, động cơ xe, máy bơm nước...). Động cơ khi được cung cấp điện sẽ làm xoay trục động cơ, từ đó tạo nên nhiều ứng dụng khác nhau. 

Các hàm này sẽ giúp bạn làm quen với 1 module Output mới là động cơ mini.


Function
----------------------

.. function:: MiniFan(pin)

    Khởi tạo động cơ mini với IO ``pin``. Trong ``pin`` là pin 1 của 6 PORT mở rộng.
     
    Ví dụ: Nếu chúng ta sử dụng PORT số 1 thì 2 chân IO tín hiệu tương ứng sẽ là D1_1.
        
.. function:: on()

    Bật quạt.

.. function:: off()

    Tắt quạt


Sample Code
----------------------

.. code-block:: guess

    minifan MiniFan(D1_1);

    void setup() { 

    }

    void loop() {
    minifan.on()
    delay(3000);
    minifan.off()
    delay(3000);
    }