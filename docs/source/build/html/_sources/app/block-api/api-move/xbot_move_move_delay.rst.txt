robot.forward|backward|turn_left|turn_right(speed, t)
==========

.. image:: images/robot-2.png
    :scale: 100 %
    :align: center

Điều khiển xController di chuyển lui về trước/sau/trái/phải trong khoảng thời gian ``time``, trong đó:

    - *speed* tốc độ quay của động cơ với phạm vi tham số là ``0 ~ 100``.
    - *t* Giá trị của thời gian chuyển động, tính bằng ``giây``. Nếu thông số này không được thiết lập, trạng thái tiến được duy trì cho đến khi có lệnh dừng chuyển động hoặc lệnh chuyển động mới.


Ví dụ
----------------------

.. image:: images/move-vd-1.png
    :scale: 100 %
    :align: center
