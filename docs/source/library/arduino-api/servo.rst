:mod:`servo` --- Servo
=============================================


Chức năng chính và chức năng của ``servo``

Function
----------------------

.. function:: position(index,degrees);

    Điều khiển động cơ servo 180 độ quay tới một góc nào đó tức thời. Trong đó:

        - *index* là tham số có giá trị ``0 ~ 7`` tương ứng với 8 cổng gắn servo trên board xController.
        - *degree* là tham số góc quay của servo có giá trị ``0 ~ 180`` độ.

.. function:: rotate(index, change, sleep);

    Điều khiển động cơ servo 180 độ quay tới một góc tới hạn ``degree`` với thời gian nghỉ ``sleep`` sau mỗi bước di chuyển ``change``. Trong đó:
        
        - *index* là tham số có giá trị ``0 ~ 7`` tương ứng với 8 cổng gắn servo trên board xController.
        - *change* là tham số 1 bước di chuyển tới góc mới của servo. Là giá trị số có giá trị từ ``0`` đến ``(degree/change)``. ``change`` có giá trị càng nhỏ thì servo chuyển bước cằng mượt.
        - *sleep* là thời gian nghỉ giữa mỗi bước ``change`` có đơn vị là ``mili giây``.
        - *degree* là tham số góc quay tới hạn của servo có giá trị ``0 ~ 180`` độ.

.. function:: spin(index, direction, speed);

    Điều khiển động cơ servo 360 độ quay với tốc độ ``speed``. Trong đó:

        - *index* là tham số có giá trị ``0 ~ 7`` tương ứng với 8 cổng gắn servo trên board xController.
        - *direction* là tham số có giá trị ``0`` hoặc ``1`` chiều quay của động cơ
        - *speed* là tốc độ quay của servo 360 độ với phạm vi tham số là ``0 ~ 100``.

.. function:: release(index);

    Dừng chuyển động servo. Trong đó ``index`` là tham số có giá trị ``0 ~ 7`` tương ứng với 8 cổng gắn servo trên board xController.

Sample Code
----------------------
Điều khiển động cơ servo 180 độ

.. code-block:: guess

    #include "Servos.h"

    Servos s;
    // the setup function runs once when you press reset or power the board
    void setup() {
    s.init();
    }

    // the loop function runs over and over again forever
    void loop() {
    for (int i = 0; i < 180; i++){
        for (uint8_t pwmnum=0; pwmnum < 8; pwmnum++) {
            s.position(pwmnum, i);
        }
    }
    delay(1000); 
    }