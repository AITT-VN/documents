Robot
=============================================

Chức năng chính của các khối điều khiển chuyển động của Robot

``Chú ý:`` Vui lòng lắp 2 động cơ DC tại cổng M1 và M2 để triển khai các khối lệnh này.

.. function:: robot.forward|backward|turn_left|turn_right(speed)
----------------------

.. image:: images/robot-1.png
    :width: 400
    :align: center

Điều khiển xBot di chuyển tiến về phía trước/sau/trái/phải, trong đó *speed* là tốc độ quay của động cơ với phạm vi tham số là ``0 ~ 100``.

.. function:: robot.forward|backward|turn_left|turn_right(speed, t = None)
----------------------

.. image:: images/robot-2.png
    :width: 400
    :align: center

Điều khiển xController di chuyển lui về trước/sau/trái/phải trong khoảng thời gian ``time``, trong đó:

    - *speed* tốc độ quay của động cơ với phạm vi tham số là ``0 ~ 100``.
    - *t* Giá trị của thời gian chuyển động, tính bằng ``giây``. Nếu thông số này không được thiết lập, trạng thái tiến được duy trì cho đến khi có lệnh dừng chuyển động hoặc lệnh chuyển động mới.


.. function:: robot.turn_right_angle|turn_left_angle(angle)
----------------------

.. image:: images/robot-3.png
    :width: 320
    :align: center

Điều khiển xBot di chuyển rẽ qua phải/trái một góc ``angle`` với tốc độ ``speed``, trong đó *angle* là góc cần xoay với phạm vi tham số là ``0 ~ 360``.
        
.. function:: robot.set_wheel_speed(speed_1, speed_2)
----------------------

.. image:: images/robot-5.png
    :width: 400
    :align: center

Điều khiển tốc độ độc lập của 2 động cơ M1 và M2, trong đó:

    - *speed_1* là tham số tốc độ của động cơ M1.
    - *speed_2* là tham số tốc độ của động cơ M2.
    - *speed_1* và *speed_2* có phạm vi tham số là ``-100 ~ 100``. Số âm và số dương biểu thị chiều quay của động cơ.

.. function:: robot.stop()
----------------------

.. image:: images/robot-4.png
    :width: 200
    :align: center

Dừng tất cả chuyển động của xBot.

Ví dụ
----------------------
Điều khiển xBot di chuyển

.. image:: images/robot-6.png
    :width: 420
    :align: center