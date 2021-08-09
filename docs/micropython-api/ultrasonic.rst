:mod:`ultrasonic` --- Ultrasonic Module
=============================================

.. module:: ultrasonic
    :synopsis: Ultrasonic Module

Chức năng chính và chức năng của ``ultrasonic``

Function
----------------------

ultrasonic.distance_cm(PORT)
       Trả về giá trị khoảng cách (đơn vị centimet)
       PORT: Có giá trị từ 0 đến 5 tương ứng từ PORT 1 đến PORT 6 của xController.

Sample Code：
----------------------
Hiển thị khoảng cách đo được từ cảm biến siêu âm 

.. code-block:: python

      while True:
            print(ultrasonic.distance_cm(1)) # Gắn vào PORT 2

