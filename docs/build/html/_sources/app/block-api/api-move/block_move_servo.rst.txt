servo.rotate(index, change, sleep, degree)
==========

.. image:: images/servo-2.png
    :scale: 100 %
    :align: center

Điều khiển động cơ servo 180 độ quay tới một góc tới hạn ``degree`` với thời gian nghỉ ``sleep`` sau mỗi bước di chuyển ``change``. Trong đó:
        
    - *index* là tham số có giá trị ``0 ~ 7`` tương ứng với 8 cổng gắn servo trên board xController.
    - *change* là tham số 1 bước di chuyển tới góc mới của servo. Là giá trị số có giá trị từ ``0`` đến ``(degree/change)``. ``change`` có giá trị càng nhỏ thì servo chuyển bước cằng mượt.
    - *sleep* là thời gian nghỉ giữa mỗi bước ``change`` có đơn vị là ``mili giây``.
    - *degree* là tham số góc quay tới hạn của servo có giá trị ``0 ~ 180`` độ.

Ví dụ
----------------------

.. image:: images/move-vd-7.png
    :scale: 100 %
    :align: center
