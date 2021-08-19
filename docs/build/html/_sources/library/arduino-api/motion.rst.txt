:mod:`motion` --- Motion
=============================================

Chức năng chính và chức năng của ``motion``

IMU (Inertial Measurement Unit) là một con chip để đo những chuyển động như đã giới thiệu ở trên. Một module IMU thường gồm 2 loại cảm biến: cảm biến gia tốc (Accelerometer) và cảm biến quay (Gyroscope).

Accelerometer (gọi tắt là accel): như tên gọi của nó, accel đơn giản là một cảm biến đo gia tốc của chính nó. Thông thường, một cảm biến accel sẽ có 3 trục xyz tương ứng với 3 chiều không gian, giúp ta biết được module đang bị nghiêng về hướng nào (trục x và y) hoặc đang bị lật hay úp (trục z).

Gyroscope (gọi tắt là gyro): đo tốc độ quay của nó quanh một trục. Tương tự với cảm biến gia tốc, thông thường, gyro sẽ có 3 trục xyz. 

Lưu ý: gyro chỉ đo tốc độ quay chứ không đo trực tiếp góc quay, nên khi bạn quay module một góc nào đó rồi dừng, giá trị của gyro sẽ tăng lên rồi hạ xuống về 0.

Trên board xController đã tích hợp sẵn một module IMU tên là MPU6050.

Function
----------------------

.. function:: mpu.getAcc[X|Y|Z]()

    Trả về giá trị góc nghiêng của xController và cho ta biết xController đang nghiêng về hướng nào.

    Tầm giá trị lý thuyết: ``-16384 ~ 16384``

        - *X* : nghiêng về sau hay trước.
        - *Y* : nghiêng sang trái hay phải.
        - *Z* : xController đang úp hay ngửa.

.. function:: mpu.getGyro[X|Y|Z]()

    Trả về giá trị ``roll|pitch|yaw`` của cảm biến gyroscope.
    
    Tầm giá trị lý thuyết: ``-16 ~ 16``

        - *X* : roll.
        - *Y* : pitch.
        - *Z* : yaw.

Sample Code
----------------------
Đọc các thông số đo được từ MPU6050

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
    Serial.print("AccelX:  "); Serial.print(mpu.getAccX());
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