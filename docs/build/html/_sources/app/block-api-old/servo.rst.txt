Động cơ Servo
=============================================

Chức năng chính động cơ Servo.

.. function:: servo.position(index, degree)
----------------------

.. image:: images/servo-1.png
    :width: 400
    :align: center

Điều khiển động cơ servo 180 độ quay tới một góc nào đó tức thời. Trong đó:

    - *index* là tham số có giá trị ``0 ~ 7`` tương ứng với 8 cổng gắn servo trên board xController.
    - *degree* là tham số góc quay của servo có giá trị ``0 ~ 180`` độ.

.. function:: servo.rotate(index, change, sleep, degree)
----------------------

.. image:: images/servo-2.png
    :width: 480
    :align: center

Điều khiển động cơ servo 180 độ quay tới một góc tới hạn ``degree`` với thời gian nghỉ ``sleep`` sau mỗi bước di chuyển ``change``. Trong đó:
        
    - *index* là tham số có giá trị ``0 ~ 7`` tương ứng với 8 cổng gắn servo trên board xController.
    - *change* là tham số 1 bước di chuyển tới góc mới của servo. Là giá trị số có giá trị từ ``0`` đến ``(degree/change)``. ``change`` có giá trị càng nhỏ thì servo chuyển bước cằng mượt.
    - *sleep* là thời gian nghỉ giữa mỗi bước ``change`` có đơn vị là ``mili giây``.
    - *degree* là tham số góc quay tới hạn của servo có giá trị ``0 ~ 180`` độ.

.. function:: servo.spin(index, speed)
----------------------

.. image:: images/servo-3.png
    :width: 480
    :align: center

Điều khiển động cơ servo 360 độ quay với tốc độ ``speed``. Trong đó:

    - *index* là tham số có giá trị ``0 ~ 7`` tương ứng với 8 cổng gắn servo trên board xController.
    - *speed* là tốc độ quay của servo 360 độ với phạm vi tham số là ``-100 ~ 100``. Số âm và số dương biểu thị chiều quay của động cơ.

.. function:: servo.position(index)
----------------------

.. image:: images/servo-4.png
    :width: 320
    :align: center

Trả về giá trị góc hiện tại của servo. Trong đó ``index`` là tham số có giá trị ``0 ~ 7`` tương ứng với 8 cổng gắn servo trên board xController.

Ví dụ
----------------------
Điều khiển động cơ servo 180 độ

.. image:: images/servo-5.png
    :width: 420
    :align: center