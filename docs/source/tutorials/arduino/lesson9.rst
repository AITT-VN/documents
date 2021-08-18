Bài học 9: Cảm biến gia tốc góc nghiêng
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

Mở phần mềm Arduino IDE.

Nếu bạn chưa cài đặt thư viện cho xController thì tham khảo bài học số 4 để tải và cài đặt thư viện vào Arduino IDE.

Copy đoạn code sau, click vào nút ``Verify`` để kiểm tra lỗi chương trình. Sau khi biên dịch không báo lỗi, bạn có thể nạp đoạn code vào board.

Bạn cũng có thể mở chương trình mẫu tương tự bằng cách vào ``File > Examples > xController library``, chọn chương trình ``motion``.

.. code-block:: guess

  #include "mpu6050.h"

  MPU6050 mpu;
  float tmp;

  void setup(){
    Serial.begin(115200);
    mpu.begin();
  }

  void loop(){
    tmp = map(mpu.getAccX(), -16384, 16384, -90, 90);
    Serial.print("	  AccelX:  "); Serial.print(mpu.getAccX());
    tmp = map(mpu.getAccY(), -16384, 16384, -90, 90);
    Serial.print("    AccelY:  "); Serial.print(mpu.getAccY());
    tmp = map(mpu.getAccZ(), -16384, 16384, -90, 90);
    Serial.print("    AccelZ:  "); Serial.print(mpu.getAccZ());
    Serial.print("    GyroX:  "); Serial.print(mpu.getGyroX());
    Serial.print("    GyroY:  "); Serial.print(mpu.getGyroY());
    Serial.print("    GyroZ:  "); Serial.print(mpu.getGyroZ()); 
    Serial.println("   ");
    delay(500);
  }

Giải thích chương trình
--------------

Chương trình trên liên tục đọc và in ra giá trị tất cả các trục xyz của cảm biến gia tốc và cảm biến quay. Sau khi chạy chương trình, bạn hãy mở cửa sổ Serial để quan sát kết quả đọc được.

.. code-block:: guess

  #include "mpu6050.h"

Khai báo thư viện để làm việc với mpu6050.

Tạo biến để lưu giá trị đọc được từ cảm biến MPU6050. 

.. code-block:: guess
  
  Serial.print("AccelX:  "); Serial.print(mpu.getAccX());  

Đọc giá trị trục X của cảm biến gia tốc. Do cảm biến gia tốc trả về giá trị từ ``-16384 ~ 16384`` nên ta dùng hàm ``map()`` để chuyển sang dải giá trị góc từ ``-90 ~ 90`` (để dễ hiểu hơn). Sau đó, dùng hàm ``Serial.print()`` để in ra giá trị này.

.. code-block:: guess

  tmp = map(mpu.getAccY(), -16384, 16384, -90, 90);
  Serial.print("    AccelY:  "); Serial.print(mpu.getAccY());
  tmp = map(mpu.getAccZ(), -16384, 16384, -90, 90);
  Serial.print("    AccelZ:  "); Serial.print(mpu.getAccZ());

Áp dụng tương tự để đọc và in ra trục Y và Z của cảm biến gia tốc.

.. code-block:: guess

  Serial.print("    GyroX:  "); Serial.print(mpu.getGyroX());
  Serial.print("    GyroY:  "); Serial.print(mpu.getGyroY());
  Serial.print("    GyroZ:  "); Serial.print(mpu.getGyroZ());

Đọc và in ra giá trị 3 trục XYZ của cảm biến quay Gyroscope.

*Khi chương trình chạy, giá trị các trục XYZ của 2 cảm biến sẽ được hiển thị lên cửa sổ Serial.*
