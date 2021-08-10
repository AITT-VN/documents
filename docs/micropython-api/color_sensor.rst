:mod:`color_sensor` --- Color Sensor Module
=============================================

.. module:: color_sensor
    :synopsis: Color Sensor Module

Chức năng chính và chức năng của ``color_sensor``

Function
----------------------

.. function:: color_sensor.read(PORT, 'R|G|B')
  Đọc giá trị R, G, B của cảm biến màu sắc, trong đó:
    - *PORT* có giá trị từ ``0 ~ 5`` đại diện PORT 1 đến PORT 6 của xController.
    - Kết quả trả về giá trị ``0 ~ 255`` tương ứng với mức độ màu của màu cần đọc (R hoặc G hoặc B).

.. function:: color_sensor.detect(PORT, 'w|b|r|g|b')
  Kiểm tra xem cảm biến có phát hiện được 1 trong các màu: w: White, b: black, r: Red, g: Green, b: Blue. Trong đó:
    - *PORT* có giá trị từ ``0 ~ 5`` đại diện PORT 1 đến PORT 6 của xController.
    - Kết quả trả về là ``True`` khi cảm biến đọc được màu trùng với màu cho trước, hoặc là ``False`` khi cảm biến đọc được màu không trùng khớp với màu cho trước.


Sample Code：
----------------------
Xác định giá trị màu đỏ của vật thể:

.. code-block:: python

  from color_sensor import color_sensor

  while True:
    red = color_sensor.read(0,'r')
    print(red)

Tìm vật thể có màu trắng:

.. code-block:: python

  from color_sensor import color_sensor

  while True:
    color_val = color_sensor.detect(0, 'w')
    if color_val == 'w':
      print('Đúng')
    else:
      print('Sai')