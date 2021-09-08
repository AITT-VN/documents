Cảm biến gia tốc góc
=============================================

Chức năng chính của cảm biến gia tốc góc.

.. function:: motion.get_accel(x|y|z)
----------------------

.. image:: images/motion-1.png
    :width: 480
    :align: center

Trả về giá trị góc nghiêng của xController và cho ta biết xController đang nghiêng về hướng nào.
Tầm giá trị lý thuyết: ``-16384 ~ 16384``

    - *x* : nghiêng về sau hay trước.
    - *y* : nghiêng sang trái hay phải.
    - *z* : xController đang úp hay ngửa.

.. function:: motion.get_gyro_roll|pitch|yaw()
----------------------

.. image:: images/motion-2.png
    :width: 480
    :align: center

Trả về giá trị ``roll|pitch|yaw`` của cảm biến gyroscope.
Tầm giá trị lý thuyết: ``-16 ~ 16``

.. function:: motion.is_shaked()
----------------------

.. image:: images/motion-3.png
    :width: 150
    :align: center

Trả về giá trị ``TRUE`` khi xController bị lắc.

ví dụ
----------------------
Xác định xController nghiêng qua trái hay phải

.. image:: images/motion-4.png
    :width: 500
    :align: center