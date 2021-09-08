:mod:`motor` --- Motor
=============================================

Chức năng chính và chức năng của ``motor``

Function
----------------------

.. function:: speed(m1,m2)

    - Điều chỉnh tốc độ quay của động cơ ``M1`` hoặc ``M2``
    
    - ``m1`` và ``m2`` tương ứng với 2 port động cơ ``M1`` và ``M2``, là giá trị tốc độ ``-100 ~ 100`, số âm và số dương biểu thị chiều quay của động cơ.

.. function:: move(dir, speed)

    Di chuyển xController dựa trên chuyển động của 2 động cơ M1 và M2

        - ``dir`` là tham số hướng di chuyển xủa xController với dải giá trị ``1~8``

        - ``speed`` là tham số tốc độ di chuyển với dải giá trị ``0-100``.

        /*
            calculate direction based on angle
                *         90(3)
                *   135(4) |  45(2)
                * 180(5)---+----Angle=0(dir=1)
                *   225(6) |  315(8)
                *         270(7)
        */

.. function:: stop()

    Dừng quay cả 2 động cơ ``M1`` và ``M2``

Sample Code
----------------------
Xoay M1 và M2 ngược chiều nhau với tốc độ tối đa.

.. code-block:: guess

    #include "Motors.h"

    Motors m;

    // the setup function runs once when you press reset or power the board
    void setup() {
    
    }

    // the loop function runs over and over again forever
    void loop() {
    m.speed(100, 100);
    delay(1000);
    m.speed(0, 0);
    delay(1000);
    m.speed(-100, -100);
    delay(1000);
    }