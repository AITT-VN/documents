:mod:`servo` --- Servo
=============================================

.. module:: servo
    :synopsis: Servo

Chức năng chính và chức năng của ``servo``

Function
----------------------

.. function:: servo.position(index, degree)

    Điều khiển động cơ servo 180 độ quay tới một góc nào đó tức thời. Trong đó:

        - *index* là tham số có giá trị ``0 ~ 7`` tương ứng với 8 cổng gắn servo trên board xController.
        - *degree* là tham số góc quay của servo có giá trị ``0 ~ 180`` độ.

.. function:: servo.rotate(index, change, sleep, degree)

    Điều khiển động cơ servo 180 độ quay tới một góc tới hạn ``degree`` với thời gian nghỉ ``sleep`` sau mỗi bước di chuyển ``change``. Trong đó:
        
        - *index* là tham số có giá trị ``0 ~ 7`` tương ứng với 8 cổng gắn servo trên board xController.
        - *change* là tham số 1 bước di chuyển tới góc mới của servo. Là giá trị số cosgias trị từ ``0`` đến ``(degree/change)``. ``change`` có giá trị càng nhỏ thì servo chuyển bước cằng mượt.
        - *sleep* là thời gian nghỉ giữa mỗi bước ``change`` có đơn vị là ``mili giây``.
        - *degree* là tham số góc quay tới hạn của servo có giá trị ``0 ~ 180`` độ.

.. function:: servo.spin(index, speed)

    Điều khiển động cơ servo 360 độ quay với tốc độ ``speed``. Trong đó:

        - *index* là tham số có giá trị ``0 ~ 7`` tương ứng với 8 cổng gắn servo trên board xController.
        - *speed* là tốc độ quay của servo 360 độ với phạm vi tham số là ``-100 ~ 100``. Số âm và số dương biểu thị chiều quay của động cơ.

.. function:: servo.position(index)

    Trả về giá trị góc hiện tại của sero. Trong đó ``index`` là tham số có giá trị ``0 ~ 7`` tương ứng với 8 cổng gắn servo trên board xController.

Sample Code
----------------------
Điều khiển động cơ servo 180 độ

.. code-block:: python

    while True:
        servo.position(0, 0)
        sleep(2)
        servo.position(0,180)
        sleep(2)