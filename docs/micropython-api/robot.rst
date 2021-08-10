:mod:`robot` --- Robot
=============================================

.. module:: robot
    :synopsis: Robot

Chức năng chính và chức năng của ``robot``

Function
----------------------

.. function:: robot.forward(speed, t = None)
    Điều khiển xBot di chuyển tiến về phía trước, trong đó:
        - *speed* tốc độ quay của động cơ với phạm vi tham số là ``0 ~ 100``.
        - *t* Giá trị của thời gian chuyển động, tính bằng ``giây``. Nếu thông số này không được thiết lập, trạng thái tiến được duy trì cho đến khi có lệnh dừng chuyển động hoặc lệnh chuyển động mới.

.. function:: robot.backward(speed, t = None)
    Điều khiển xBot di chuyển lui về phía sau, trong đó:
        - *speed* tốc độ quay của động cơ với phạm vi tham số là ``0 ~ 100``.
        - *t* Giá trị của thời gian chuyển động, tính bằng ``giây``. Nếu thông số này không được thiết lập, trạng thái tiến được duy trì cho đến khi có lệnh dừng chuyển động hoặc lệnh chuyển động mới.

.. function:: robot.turn_right(speed, t = None)
    Điều khiển xBot di chuyển rẽ qua phải, trong đó:
        - *speed* tốc độ quay của động cơ với phạm vi tham số là ``0 ~ 100``.
        - *t* Giá trị của thời gian chuyển động, tính bằng ``giây``. Nếu thông số này không được thiết lập, trạng thái tiến được duy trì cho đến khi có lệnh dừng chuyển động hoặc lệnh chuyển động mới.

.. function:: robot.turn_left(speed, t = None)
    Điều khiển xBot di chuyển rẽ qua trái, trong đó:
        - *speed* tốc độ quay của động cơ với phạm vi tham số là ``0 ~ 100``.
        - *t* Giá trị của thời gian chuyển động, tính bằng ``giây``. Nếu thông số này không được thiết lập, trạng thái tiến được duy trì cho đến khi có lệnh dừng chuyển động hoặc lệnh chuyển động mới.

.. function:: robot.turn_right_angle(angle,speed)
    Điều khiển xBot di chuyển rẽ qua phải một góc ``angle`` với tốc độ ``speed``, trong đó:
        - *angle* là góc cần xoay với phạm vi tham số là ``0 ~ 360``.
        - *speed* tốc độ quay của động cơ với phạm vi tham số là ``0 ~ 100``.

.. function:: robot.turn_left_angle(angle,speed)
    Điều khiển xBot di chuyển rẽ qua trái một góc ``angle`` với tốc độ ``speed``, trong đó:
        - *angle* là góc cần xoay với phạm vi tham số là ``0 ~ 360``.
        - *speed* tốc độ quay của động cơ với phạm vi tham số là ``0 ~ 100``.
        
.. function:: robot.set_wheel_speed(speed_1, speed_2)
    Điều khiển tốc độ độc lập của 2 động cơ M1 và M2, trong đó:
        - *speed_1* là tham số tốc độ của động cơ M1.
        - *speed_2* là tham số tốc độ của động cơ M2.
        - *speed_1* và *speed_2* có phạm vi tham số là ``-100 ~ 100``. Số âm và số dương biểu thị chiều quay của động cơ.

.. function:: robot.stop()
    Dừng tất cả chuyển động của xBot.


Sample Code：
----------------------
Điều khiển xBot di chuyển

.. code-block:: python

    while True:
        robot.forward(80, 3)
        robot.backward(50,3)
        robot.turn_left_angle(90,50)
        robot.stop()