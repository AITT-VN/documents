# 5. Bài 2: Di chuyển chính xác với cảm biến góc

**Mục tiêu:**

Làm quen với cảm biến góc MPU6050 có sẵn trên ORC Control Hub, biết cách bật cảm biến góc để xBot Evo đi thẳng và quay đúng góc mong muốn.

## 1. Cảm biến góc là gì?
Ở bài trước, khi quay theo thời gian, robot quay nhiều hay ít phụ thuộc vào mặt sàn và lượng pin, nên rất khó quay đúng một góc vuông.

Mạch ORC Control Hub có sẵn **cảm biến góc MPU6050**, đo được 6 trục: 3 trục gia tốc XYZ và 3 trục con quay hồi chuyển (gyroscope) XYZ. Nhờ cảm biến này, robot biết được mình đang quay về hướng nào và đã quay được bao nhiêu độ.
![Các góc quay của cảm biến](/wiki-assets/images/orc_bot/orc-bot/images/7.5.png)


Trong đó, góc **heading** (còn gọi là **yaw**) cho biết robot đang quay về hướng nào khi đặt trên mặt sàn. Đây là thông số quan trọng nhất khi lập trình robot di chuyển.

## 2. Khối lệnh sử dụng
![Khối lệnh cảm biến góc](/wiki-assets/images/orc_bot/orc-bot/images/7.2.png)
![Khối lệnh cảm biến góc (tiếp)](/wiki-assets/images/orc_bot/orc-bot/images/7.3.png)


- **Bật cảm biến góc:** khởi tạo cảm biến và tinh chỉnh ban đầu với số mẫu chỉ định (ví dụ 500 mẫu). Số mẫu càng cao thì càng chính xác nhưng robot khởi động lâu hơn.

> **Lưu ý:** Trong lúc cảm biến tinh chỉnh, bạn cần **đặt robot đứng yên trên mặt phẳng**, không chạm vào robot.

- **Đọc góc quay:** trả về các góc heading, pitch, roll mà cảm biến đã tính toán.
![Đọc góc quay](/wiki-assets/images/orc_bot/orc-bot/images/7.4.png)


Khi đã bật cảm biến góc cho robot, thư viện sẽ tự động dùng thông tin này để giúp robot **đi thẳng hơn** và **quay đúng góc** khi bạn chọn đơn vị là **độ** trong khối lệnh quay.

## 3. Chương trình: Đi hình vuông chính xác
Khi nhấn nút BOOT, xBot Evo đi tới 2 giây rồi quay phải đúng 90 độ, lặp lại 4 lần.
![Chương trình đi hình vuông với cảm biến góc](/wiki-assets/images/orc_bot/orc-bot/images/7.6.png)


**Chương trình Python**

```python
import yolo_uno
from mdv2 import *
from motor import *
from drivebase import *
from mpu6050 import MPU6050
from angle_sensor import AngleSensor
from abutton import *

md_v2 = MotorDriverV2()
motor1 = DCMotor(md_v2, M1, reversed=False)
motor2 = DCMotor(md_v2, M2, reversed=False)
robot = DriveBase(MODE_2WD, m1=motor1, m2=motor2, m3=None, m4=None)
imu = MPU6050()
angle_sensor = AngleSensor(imu)
btn_BOOT = aButton(BOOT_PIN)

async def on_BOOT_pressed():
    for count in range(4):
        await robot.forward_for(2, unit=SECOND, then=BRAKE)
        await robot.turn_right_for(90, unit=DEGREE, then=BRAKE)

def deinit():
    robot.stop()
    btn_BOOT.deinit()

yolo_uno.deinit = deinit

async def setup():
    robot.speed(90, min_speed=40)
    angle_sensor.calibrate(500)
    create_task(angle_sensor.run())
    robot.angle_sensor(angle_sensor)
    btn_BOOT.pressed(on_BOOT_pressed)

async def main():
    await setup()
    while True:
        await asleep_ms(100)

run_loop(main())
```

So sánh với chương trình đi hình vuông ở bài 1, bạn sẽ thấy robot quay góc đều và chính xác hơn rất nhiều, dù mặt sàn hay lượng pin thay đổi.

> **Mẹo:** Dùng **phanh** (BRAKE) thay vì **dừng** (STOP) sau mỗi lần di chuyển để robot dừng ngay lập tức, giúp góc quay chính xác hơn.

## 4. Bài tập mở rộng
1. Lập trình cho xBot Evo đi theo **hình tam giác đều** (mỗi lần quay 120 độ).
2. Lập trình cho xBot Evo quay đủ 1 vòng (360 độ) tại chỗ, vừa quay vừa đổi màu đèn LED.
3. Lập trình cho xBot Evo "nhảy múa": đi tới, lùi lại, quay trái 45 độ, quay phải 90 độ, quay trái 45 độ, lặp lại 4 lần, mỗi động tác đổi một màu đèn LED.

## 5. Câu hỏi ôn tập
1. Cảm biến góc MPU6050 đo được những thông số nào?
2. Góc heading (yaw) cho biết điều gì?
3. Vì sao cần đặt robot đứng yên khi cảm biến góc đang tinh chỉnh?
