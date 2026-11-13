# 4. Bài 1: Cùng di chuyển nào

**Mục tiêu:**

Hiểu về động cơ DC, cách khai báo robot di chuyển trên ORC Control Hub và các khối lệnh giúp xBot Evo di chuyển theo ý muốn.

## 1. Động cơ trên xBot Evo
xBot Evo di chuyển được nhờ 2 động cơ DC bên trái và bên phải. Khi 2 động cơ quay cùng chiều, robot đi tới hoặc lùi. Khi 2 động cơ quay ngược chiều nhau, robot quay trái hoặc quay phải.

Theo hướng dẫn lắp ráp, **động cơ bên trái nối vào cổng M1** và **động cơ bên phải nối vào cổng M2** trên ORC Control Hub.
![Cổng động cơ trên ORC Control Hub](/wiki-assets/images/orc_bot/orc-bot/images/orc-hub-dong-co.png)


## 2. Điều khiển từng động cơ
Các khối lệnh làm việc với động cơ nằm trong danh mục **ĐỘNG CƠ**, phần **Động cơ DC**.
![Khối lệnh động cơ DC](/wiki-assets/images/orc_bot/orc-bot/images/4.3.png)


- **Khai báo động cơ:** chọn cổng mà động cơ được nối vào (M1, M2,...). Nếu động cơ quay ngược với mong muốn, bật lựa chọn **đảo chiều quay**.
![Khai báo động cơ](/wiki-assets/images/orc_bot/orc-bot/images/4.4.png)


- **Quay động cơ với tốc độ chỉ định:** tốc độ từ -100 đến 100.

    ◼ Tốc độ > 0: động cơ quay theo chiều kim đồng hồ (nhìn thẳng vào bánh xe).

    ◼ Tốc độ < 0: động cơ quay ngược chiều kim đồng hồ.

    ◼ Giá trị tốc độ càng lớn thì động cơ quay càng nhanh.
![Quay động cơ](/wiki-assets/images/orc_bot/orc-bot/images/4.6.png)


- **Quay động cơ trong một khoảng thời gian:** hết thời gian thì động cơ dừng lại.
![Quay động cơ theo thời gian](/wiki-assets/images/orc_bot/orc-bot/images/4.7.png)


**Chương trình mẫu:** khi nhấn nút BOOT, quay 2 động cơ tới 2 giây, quay ngược 2 giây rồi dừng lại.
![Chương trình điều khiển động cơ](/wiki-assets/images/orc_bot/orc-bot/images/4.15.png)


Bạn sẽ thấy 2 bánh xe quay **ngược chiều nhau** dù cùng tốc độ dương. Đó là vì 2 động cơ được lắp đối xứng ở 2 bên robot. Ở phần tiếp theo, khi khai báo robot di chuyển, thư viện sẽ tự xử lý vấn đề này cho bạn.

## 3. Khai báo robot di chuyển
Thay vì điều khiển từng động cơ, chúng ta khai báo một **robot di chuyển** gồm 2 động cơ, sau đó chỉ cần ra lệnh tới, lùi, trái, phải. Các khối lệnh nằm trong danh mục **DI CHUYỂN**.
![Khối lệnh di chuyển](/wiki-assets/images/orc_bot/orc-bot/images/5.4.png)
![Khối lệnh di chuyển (tiếp)](/wiki-assets/images/orc_bot/orc-bot/images/5.5.png)


- **Khai báo robot:** chọn chế độ **2 động cơ (2WD)**, động cơ bên trái là động cơ gắn ở M1, động cơ bên phải là động cơ gắn ở M2.


- **Di chuyển liên tục:** robot di chuyển tới, lùi, quay trái, quay phải cho đến khi có lệnh mới.
![Di chuyển liên tục](/wiki-assets/images/orc_bot/orc-bot/images/5.7.png)


- **Di chuyển theo thời gian:** robot di chuyển trong số giây chỉ định rồi dừng lại.
![Di chuyển theo thời gian](/wiki-assets/images/orc_bot/orc-bot/images/5.8.png)


- **Quay theo thời gian:**
![Quay theo thời gian](/wiki-assets/images/orc_bot/orc-bot/images/5.9.png)


- **Dừng robot:** dừng theo quán tính (**dừng**) hoặc khóa bánh dừng ngay lập tức (**phanh**).
![Dừng robot](/wiki-assets/images/orc_bot/orc-bot/images/5.10.png)


## 4. Viết chương trình di chuyển

- **Chương trình 1:** Khi nhấn nút BOOT, xBot Evo đi tới 2 giây, lùi lại 2 giây, quay trái 1 giây và quay phải 1 giây.
![Chương trình di chuyển](/wiki-assets/images/orc_bot/orc-bot/images/5.12.png)


**Chương trình Python**

```python
import yolo_uno
from mdv2 import *
from motor import *
from drivebase import *
from abutton import *

md_v2 = MotorDriverV2()
motor1 = DCMotor(md_v2, M1, reversed=False)
motor2 = DCMotor(md_v2, M2, reversed=False)
robot = DriveBase(MODE_2WD, m1=motor1, m2=motor2, m3=None, m4=None)
btn_BOOT = aButton(BOOT_PIN)

async def on_BOOT_pressed():
    await robot.forward_for(2, unit=SECOND, then=STOP)
    await robot.backward_for(2, unit=SECOND, then=STOP)
    await robot.turn_left_for(1, unit=SECOND, then=STOP)
    await robot.turn_right_for(1, unit=SECOND, then=STOP)

def deinit():
    robot.stop()

yolo_uno.deinit = deinit

async def setup():
    robot.speed(70, min_speed=40)
    btn_BOOT.pressed(on_BOOT_pressed)

async def main():
    await setup()
    while True:
        await asleep_ms(100)

run_loop(main())
```

- **Chương trình 2:** Khi nhấn nút BOOT, xBot Evo đi theo **hình vuông**: đi tới 2 giây rồi quay phải, lặp lại 4 lần.

Gợi ý: dùng khối lệnh **lặp lại 4 lần**, bên trong gồm khối lệnh đi tới 2 giây và quay phải. Bạn cần thử và chỉnh thời gian quay phải sao cho robot quay được một góc vuông. Thời gian này phụ thuộc vào mặt sàn và lượng pin còn lại.

> **Ghi chú:**
> - Khi chọn tốc độ quá thấp, lực quay không đủ mạnh, robot sẽ đứng im. Hãy tăng tốc độ lên.
> - Nếu robot di chuyển ngược hướng mong muốn, kiểm tra lại dây động cơ đã cắm đúng cổng M1 (trái), M2 (phải) chưa, hoặc bật **đảo chiều quay** cho động cơ bị ngược.
> - Robot sẽ khó đi hình vuông thật chính xác khi quay theo thời gian. Ở bài sau, chúng ta sẽ dùng **cảm biến góc** để giải quyết vấn đề này.

## 5. Câu hỏi ôn tập
1. Động cơ trái và động cơ phải của xBot Evo được nối vào cổng nào?
2. Tốc độ động cơ nhận giá trị trong khoảng nào? Tốc độ âm có ý nghĩa gì?
3. Sự khác nhau giữa dừng robot bằng **dừng** và bằng **phanh** là gì?
