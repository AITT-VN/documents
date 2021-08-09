:mod:`color_sensor` --- Color Sensor
=============================================

.. module:: color_sensor
    :synopsis: Color Sensor

Chức năng chính và chức năng của ``color_sensor``

Function
----------------------

color_sensor.read(port, 'r|g|b')
   Đọc giá trị R, G, B của cảm biến màu sắc

color_sensor.detect(port, 'w|b|r|g|b')
   Kiểm tra xem cảm biến có phát hiện được 1 trong các màu: w: White, b: black, r: Red, g: Green, b: Blue.
   Kết quả trả về là ``True``: Khi cảm biến đọc được màu trùng với màu cho trước, hoặc là ``False``: Khi cảm biến đọc được màu không trùng khớp với màu cho trước..


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

  color_val = color_sensor.detect(0, 'w')
  if color_val == 'w':
    print('Đúng')
  else:
    print('Sai')