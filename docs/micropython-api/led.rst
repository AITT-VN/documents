:mod:`led` --- LED Module
=============================================

.. module:: led
    :synopsis: LED Module

Chức năng chính và chức năng của ``led``

Function
----------------------

pin[X][Y].write_digital((STATE))
     Đổi trạng thái BẬT|TẮT của 1 PORT, trong đó
         X: Có giá trị từ 1 đến 6 đại diện PORT 1 đến PORT 6 của xController.
         Y: Có giá trị là 1|2 tương ứng với tín hiệu 1 hoặc tín hiệu 2 đối với mỗi PORT. Đối với module LED thì mặc định là 1.
         STATE: Có giá trị là 0|1 tương ứng với trạng thái TẮT|BẬT PORT.

Sample Code：
----------------------
Bật tắt đèn ở PORT 1 của xController

.. code-block:: python

    while True:
        pin11.write_digital((1))
        time.sleep(1)
        pin11.write_digital((0))
        time.sleep(1)