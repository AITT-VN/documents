:mod:`pins` --- Pins
=============================================

.. module:: pins
    :synopsis: Pins

Chức năng chính và chức năng của ``pins``

Function
----------------------

.. function:: pin[X][Y].write_digital((STATE))
    Đổi trạng thái BẬT|TẮT của 1 PORT, trong đó:
        - *X* Có giá trị từ ``1 ~ 6`` đại diện PORT 1 đến PORT 6 của xController.
        - *Y* Có giá trị là ``1|2`` tương ứng với tín hiệu 1 hoặc tín hiệu 2 đối với mỗi PORT. Đối với một số module thì mặc định là 1.
        - *STATE* Có giá trị là ``0|1`` tương ứng với trạng thái TẮT|BẬT PORT.

.. function:: pin[X][Y].read_digital()
    Trả về giá trị ``0`` hoặc ``1``, trong đó:
        - *X* Có giá trị từ ``1 ~ 6`` đại diện PORT 1 đến PORT 6 của xController.
        - *Y* Có giá trị là ``1|2`` tương ứng với tín hiệu 1 hoặc tín hiệu 2 đối với mỗi PORT. Đối với một số module thì mặc định là 1.

.. function:: pin11.write_analog(STATE)
    Đổi trạng thái BẬT|TẮT của 1 PORT, trong đó:
        - *X* Có giá trị từ ``1 ~ 6`` đại diện PORT 1 đến PORT 6 của xController.
        - *Y* Có giá trị là ``1|2`` tương ứng với tín hiệu 1 hoặc tín hiệu 2 đối với mỗi PORT. Đối với một số module thì mặc định là 1.
        - *STATE* Có giá trị là ``0 ~ 4095`` tương ứng mức điện áp ``0 ~ 3.3`` volt

.. function:: pin[X][Y].read_analog()
    Trả về giá trị ``0 ~ 4095``
        - *X* Có giá trị từ ``1 ~ 6`` đại diện PORT 1 đến PORT 6 của xController.
        - *Y* Có giá trị là ``1|2`` tương ứng với tín hiệu 1 hoặc tín hiệu 2 đối với mỗi PORT. Đối với một số module thì mặc định là 1.

.. function:: pin[X][Y].pulse_in(STATE)
    Trả về độ dài (tính theo micro giây) của một xung ``Bật`` hay ``Tắt`` phát ra từ chân cắm, trong đó:
        - *X* Có giá trị từ ``1 ~ 6`` đại diện PORT 1 đến PORT 6 của xController.
        - *Y* Có giá trị là ``1|2`` tương ứng với tín hiệu 1 hoặc tín hiệu 2 đối với mỗi PORT. Đối với một số module thì mặc định là 1.
        - *STATE* Có giá trị là ``0|1`` tương ứng với trạng thái ``TẮT|BẬT``.

.. function:: pin[X][Y].set_pull(MODE)
    Cấu hình điện nổi trở của chân cắm, trong đó:
        - *X* Có giá trị từ ``1 ~ 6`` đại diện PORT 1 đến PORT 6 của xController.
        - *Y* Có giá trị là ``1|2`` tương ứng với tín hiệu 1 hoặc tín hiệu 2 đối với mỗi PORT. Đối với một số module thì mặc định là 1.
        - *MODE* Có các chế độ ``up`` hoặc ``down`` hoặc ``none``.

Sample Code：
----------------------
Bật tắt PORT 1 - PIN 1 của xController

.. code-block:: python

    while True:
        pin11.write_digital((1))
        time.sleep(1)
        pin11.write_digital((0))
        time.sleep(1)