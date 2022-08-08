12. Bài học 9: Cảm biến gia tốc góc nghiêng
====================

Mục tiêu
-----------

Các bạn sử dụng điện thoại ắt hẳn đã từng chơi qua những game như đua xe, lắc banh… mà trong đó, các bạn phải nghiêng, xoay điện thoại phải không? Làm sao điện thoại có thể biết chính nó bị nghiêng hay xoay về hướng nào? Câu trả lời là dựa vào cảm biến gia tốc.

Trong bài học này, chúng ta sẽ cùng tìm hiểu về cảm biến gia tốc, góc nghiêng và một phương thức giao tiếp mới là I2C.

Kiến thức mới
-----------

*IMU*

IMU (``Inertial Measurement Unit``) là một con chip để đo những chuyển động như đã giới thiệu ở trên. Một module IMU thường gồm 2 loại cảm biến: cảm biến gia tốc (Accelerometer) và cảm biến quay (Gyroscope).

  - ``Accelerometer`` (gọi tắt là ``accel``): như tên gọi của nó, accel đơn giản là một cảm biến đo gia tốc của chính nó. Thông thường, một cảm biến accel sẽ có 3 trục xyz tương ứng với 3 chiều không gian, giúp ta biết được module đang bị nghiêng về hướng nào (trục x và y) hoặc đang bị lật hay úp (trục z).
  - ``Gyroscope`` (gọi tắt là ``gyro``): đo tốc độ quay của nó quanh một trục. Tương tự với cảm biến gia tốc, thông thường, gyro sẽ có 3 trục xyz. 

*Lưu ý*: ``gyro`` chỉ đo tốc độ quay chứ không đo trực tiếp góc quay, nên khi bạn quay module một góc nào đó rồi dừng, giá trị của gyro sẽ tăng lên rồi hạ xuống về 0.

Trên board xController đã tích hợp sẵn một module IMU tên là ``MPU6050``.

*Giao tiếp I2C*

Ở các bài trước, chúng ta đã tìm hiểu về các loại tín hiệu đơn giản là ``Digital`` và ``Analog``. Tuy nhiên, để mạch điều khiển có thể làm việc được với các thiết bị phức tạp, chúng cần sử dụng các chuẩn giao tiếp phức tạp hơn. Một trong số đó là giao tiếp I2C (``Inter-Integrated Circuit``) rất phổ biến mà ``MPU6050`` cũng sử dụng.

Giao tiếp I2C chia thiết bị làm 2 loại: ``Master`` (điều phối toàn bộ cách thức giao tiếp và truyền dữ liệu, ví dụ xController) và ``Slave`` (các cảm biến, module nối với chip điều khiển).

Có thể có nhiều kênh I2C trong một hệ thống, gọi là I2C bus. Mỗi I2C bus sử dụng hai đường truyền tín hiệu:

  - Một đường xung nhịp đồng hồ (``SCL``) chỉ do thiết bị Master phát đi.
  - Một đường truyền dữ liệu (``SDA``) theo 2 hướng.

Nhiều thiết bị có thể được kết nối vào cùng một bus I2C, tuy nhiên điều này sẽ không gây xung đột bởi mỗi thiết bị đều được nhận diện bởi một địa chỉ I2C duy nhất.


Thiết bị cần sử dụng
-----------

.. image:: images/device-1.png
  :width: 600
  :align: center


Viết chương trình
--------------

  - Mở phần mềm uPyCraft.
  - Tạo một file chương trình mới (``File > New``) và lưu với tên main.py bằng cách chọn menu ``File > Save…``.
  - Copy đoạn code sau, click vào nút ``DownloadAndRun`` để chạy chương trình.

.. code-block:: python

  while True:
    tmp1 = translate((motion.get_accel('x')), (-16384), 16384, (-90), 90)
    print('AccelX: ' + tmp1)
    tmp2 = translate((motion.get_accel('y')), (-16384), 16384, (-90), 90)
    print('AccelY: ' + tmp2)
    tmp3 = translate((motion.get_accel('z')), (-16384), 16384, (-90), 90)
    print('AccelZ: ' + tmp3)
    print('GyroX:' + motion.get_gyro_roll())
    print('GyroY:' + motion.get_gyro_pitch())
    print('GyroZ:' + motion.get_gyro_yaw())

Sau khi nạp chương trình, Bạn có thể xem các giá trị đọc được từ cảm biến gia tốc góc nghiêng trong cửa sổ Terminal.

Giải thích chương trình
--------------

Chương trình trên liên tục đọc và in ra giá trị tất cả các trục xyz của cảm biến gia tốc và cảm biến quay.

.. code-block:: python

  tmp1 = translate((motion.get_accel('x')), (-16384), 16384, (-90), 90)
  print('AccelX: ' + tmp1)

Đọc giá trị trục X của cảm biến gia tốc. Do cảm biến gia tốc trả về giá trị từ ``-16384 đến 16384`` nên ta dùng hàm ``translate()`` để chuyển sang dải giá trị góc từ ``-90 đến 90`` (để dễ hiểu hơn). Sau đó, dùng hàm ``print()`` để in ra giá trị này.

.. code-block:: python

  tmp2 = translate((motion.get_accel('y')), (-16384), 16384, (-90), 90)
  print('AccelY: ' + tmp2)
  tmp3 = translate((motion.get_accel('z')), (-16384), 16384, (-90), 90)
  print('AccelZ: ' + tmp3)

Áp dụng tương tự để đọc và in ra trục Y và Z của cảm biến gia tốc.

.. code-block:: python

  print('GyroX:' + motion.get_gyro_roll())
  print('GyroY:' + motion.get_gyro_pitch())
  print('GyroZ:' + motion.get_gyro_yaw())

Đọc và in ra giá trị 3 trục XYZ của cảm biến quay Gyroscope.

Khi chương trình chạy, giá trị các trục XYZ của 2 cảm biến sẽ được hiển thị lên cửa sổ Terminal.

Ngoài ra, bạn có thể sử dụng thêm hàm ``motion.is_shaked()`` để xác định xController có đang bị lắc hay không.