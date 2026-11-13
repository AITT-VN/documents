# 6. Bài 3: Robot né vật cản

**Mục tiêu:**

Hiểu cách hoạt động của cảm biến khoảng cách (cảm biến siêu âm) và lập trình cho xBot Evo tự động phát hiện, né tránh vật cản khi di chuyển.

## 1. Cảm biến khoảng cách
Cảm biến siêu âm dùng để đo khoảng cách tới vật cản phía trước, giúp robot di chuyển an toàn, tránh va chạm. Khi gặp vật cản, robot có thể được lập trình để rẽ hướng khác hoặc quay đầu.
![Cảm biến siêu âm](/wiki-assets/images/orc_bot/orc-bot/images/8.1.png)


Cảm biến có 2 mắt: **mắt phát** tạo ra âm thanh tần số cao mà tai người không nghe được, **mắt thu** nhận tiếng vang phản xạ lại khi âm thanh gặp vật cản. Dựa vào thời gian từ lúc phát đến lúc nhận được tiếng vang, cảm biến tính ra khoảng cách tới vật cản.
![Cách hoạt động của cảm biến siêu âm](/wiki-assets/images/orc_bot/orc-bot/images/8.2.png)


Phạm vi đo tối đa của cảm biến là khoảng **200 cm** và cảm biến chỉ phát hiện được vật cản **ở phía trước**, không phát hiện được vật cản ở bên trái hoặc bên phải.

## 2. Kết nối phần cứng
Cảm biến khoảng cách được nối vào cổng Grove **màu trắng D3-D4** trên mạch ORC Control Hub.
![Kết nối cảm biến siêu âm với ORC Control Hub](/wiki-assets/images/orc_bot/orc-bot/images/orc-hub-ultrasonic.jpg)


Dây Grove gồm 4 sợi:

    + Đỏ: nguồn dương (+)
    + Đen: nguồn âm (GND)
    + Vàng: phát sóng âm (Trigger)
    + Trắng: thu sóng âm phản xạ (Echo)

## 3. Đọc khoảng cách
Trước khi lập trình né vật cản, hãy thử đọc giá trị của cảm biến để hiểu nó hoạt động thế nào.

Bạn hãy viết chương trình **liên tục đọc khoảng cách (cm) từ cảm biến siêu âm ở cổng D3-D4 và in ra màn hình** bằng khối lệnh **in ra** trong danh mục **Serial**. Sau đó, đưa tay lại gần và ra xa cảm biến, quan sát giá trị thay đổi.

Gợi ý: khối lệnh đọc khoảng cách nằm trong danh mục **SENSOR** của thư viện ROBOTICS.

## 4. Chương trình né vật cản
Robot luôn đi tới. Khi khoảng cách tới vật cản phía trước **nhỏ hơn 15 cm**, robot lùi lại 1 giây và quay trái 1 giây rồi tiếp tục đi tới.
![Chương trình né vật cản](/wiki-assets/images/orc_bot/orc-bot/images/8.4.png)


**Sơ đồ hoạt động**

    1. Robot đi tới
    2. Đọc khoảng cách từ cảm biến
    3. Nếu khoảng cách < 15 cm: lùi lại 1 giây, quay trái 1 giây
    4. Quay lại bước 1

**Chương trình Python**

```python
import yolo_uno
from mdv2 import *
from motor import *
from drivebase import *
from ultrasonic import *

md_v2 = MotorDriverV2()
motor1 = DCMotor(md_v2, M1, reversed=False)
motor2 = DCMotor(md_v2, M2, reversed=False)
robot = DriveBase(MODE_2WD, m1=motor1, m2=motor2, m3=None, m4=None)
ultrasonic = Ultrasonic(D3_PIN, D4_PIN)

def deinit():
    robot.stop()

yolo_uno.deinit = deinit

async def task_forever():
    while True:
        robot.forward()
        if ultrasonic.distance_cm() < 15:
            await robot.backward_for(1, unit=SECOND, then=STOP)
            await robot.turn_left_for(1, unit=SECOND, then=STOP)
        await asleep_ms(50)

async def setup():
    robot.speed(60, min_speed=40)
    create_task(task_forever())

async def main():
    await setup()
    while True:
        await asleep_ms(100)

run_loop(main())
```

> **Ghi chú:**
> - Nếu robot đi quá nhanh, robot có thể va vào vật cản trước khi kịp xử lý. Hãy giảm tốc độ hoặc tăng khoảng cách phát hiện (ví dụ 20 cm).
> - Vật cản có bề mặt mềm (vải, bông) hoặc nghiêng sẽ hấp thụ hoặc làm lệch sóng âm, cảm biến có thể đo không chính xác.

## 5. Bài tập mở rộng
1. Khi phát hiện vật cản, cho đèn LED trên mạch chuyển sang **màu đỏ**, khi đường thông thoáng thì chuyển sang **màu xanh lá**.
2. Thay vì luôn quay trái, hãy dùng khối lệnh **số ngẫu nhiên** để robot quay trái hoặc quay phải ngẫu nhiên khi gặp vật cản.
3. Kết hợp cảm biến góc ở bài 2: khi gặp vật cản, robot quay **đúng 90 độ** thay vì quay theo thời gian.
4. **Robot đi theo người:** lập trình cho robot giữ khoảng cách khoảng 20 cm với bàn tay của bạn. Nếu tay ở xa hơn 25 cm thì đi tới, gần hơn 15 cm thì lùi lại, ở giữa thì dừng.

## 6. Câu hỏi ôn tập
1. Cảm biến siêu âm đo khoảng cách dựa trên nguyên lý nào?
2. Cảm biến khoảng cách được nối vào cổng nào trên ORC Control Hub?
3. Vì sao cần thêm khối lệnh chờ ngắn (50ms) trong vòng lặp đọc cảm biến?
