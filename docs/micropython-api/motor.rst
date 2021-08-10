:mod:`motor` --- Motor
=============================================

.. module:: motor
    :synopsis: Motor

Chức năng chính và chức năng của ``motor``

Function
----------------------

.. function:: motor.speed(index, value=None)
    Điều chỉnh tốc độ quay của động cơ ``M1`` hoặc ``M2``, speed là từ -4095 đến 4095, âm là quay ngược, dương là quay tới.
        - *value* là giá trị tốc độ ``-4095 ~ 4095`, số âm và số dương biểu thị chiều quay của động cơ. Nếu ``value`` k truyền vào (None) thì trả về ``value`` hiện tại.
        - *index* có giá trị ``0|1`` tương ứng ``M1|M2``.


Sample Code：
----------------------
Xoay M1 và M2 ngược chiều nhau với tốc độ tối đa.

.. code-block:: python

    while True:
        motor.speed(0, 4095)
        motor.speed(1, -4095)
