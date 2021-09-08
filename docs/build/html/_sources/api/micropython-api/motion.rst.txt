:mod:`motion` --- Motion
=============================================

.. module:: motion
    :synopsis: Motion

Chức năng chính và chức năng của ``motion``

Function
----------------------

.. function:: motion.get_accel(x|y|z)

    Trả về giá trị góc nghiêng của xController và cho ta biết xController đang nghiêng về hướng nào.
    Tầm giá trị lý thuyết: ``-16384 ~ 16384``

        - *x* : nghiêng về sau hay trước.
        - *y* : nghiêng sang trái hay phải.
        - *z* : xController đang úp hay ngửa.

.. function:: motion.get_gyro_roll()

    Trả về giá trị ``roll`` của cảm biến gyroscope.
    Tầm giá trị lý thuyết: ``-16 ~ 16``

        - Hàm: motion.get_gyro_roll() 
        - Tham số: ``None``

.. function:: motion.get_gyro_pitch()

    Trả về giá trị pitch của cảm biến gyroscope.
    Tầm giá trị lý thuyết: ``-16 ~ 16``

        - Hàm: motion.get_gyro_pitch() 
        - Tham số: ``None``
	
.. function:: motion.get_gyro_yaw()

    Trả về giá trị ``yaw`` của cảm biến gyroscope.
    Tầm giá trị lý thuyết: ``-16 ~ 16``

        - Hàm: motion.get_gyro_yaw() 
        - Tham số: ``None``

.. function:: motion.is_shaked()

    Trả về giá trị ``TRUE`` khi xController bị lắc.

Sample Code
----------------------
Xác định xController nghiêng qua trái hay phải

.. code-block:: python

    while True:
        if (motion.get_accel('y')) <= 0:
            print('xController nghiêng sang trái')
        else:
            print('xController nghiêng sang phải')
