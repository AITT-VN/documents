# 1. Giới thiệu về kit ORC K2

Tài liệu này là chuỗi bài hướng dẫn giúp bạn làm quen, lắp ráp và lập trình robot ORC. Toàn bộ các bài phía sau vẫn giữ cùng lộ trình thực hành như bộ tài liệu ORC gốc, để bạn có thể bắt đầu nhanh với khối lệnh, Python hoặc Arduino C rồi tiếp tục mở rộng robot theo nhu cầu học tập và thi đấu.

## 1. Bộ kit Robot ORC K2

[Robot ORC K2](https://ohstem.vn/product/robot-orc-k2/) là phiên bản phù hợp cho học sinh từ THCS trở lên, phục vụ dạy học và thi đấu Robotics. Với kích thước gọn gàng, cách lắp ráp đơn giản và bộ động cơ DC, servo được tối ưu riêng, K2 giúp người học nhanh chóng làm quen với robot, dễ triển khai bài học và vẫn đủ linh hoạt cho nhiều nhiệm vụ thực hành, sáng tạo và thi đấu.

Điểm mạnh của ORC K2 là giúp người học tiếp cận Robotics theo hướng thực hành: tự lắp ráp khung kim loại chuẩn hóa, làm quen với cơ cấu di chuyển đa hướng, lập trình cảm biến và phát triển các bài toán điều khiển robot từ cơ bản đến nâng cao.

Sau khi lắp ráp theo hướng dẫn, bạn sẽ có một robot 4 bánh Mecanum có thể di chuyển đa hướng, gắp thả vật thể và tiếp tục nâng cấp thêm các cơ cấu khác.
![Robot ORC K2](/wiki-assets/images/orc_bot/orc-bot/images/orc-k2.PNG)

## 2. Thành phần chính của robot

## 2.1. Mạch điều khiển

Robot ORC K2 sử dụng **ORC Control Hub** làm bộ điều khiển trung tâm. Đây là bo mạch do OhStem thiết kế cho giáo dục Robotics, hỗ trợ lập trình bằng khối lệnh, Python và Arduino C, đồng thời hỗ trợ cả kết nối USB lẫn Bluetooth.
![orc hub](/wiki-assets/images/orc_bot/orc-bot/images/orc_hub.png)

Bo mạch dùng vi điều khiển ESP32-S3, cho hiệu năng xử lý tốt, tích hợp Wi-Fi 2.4 GHz và Bluetooth LE. ORC Control Hub hỗ trợ nhiều cổng kết nối để bạn dễ dàng gắn thêm cảm biến, động cơ và các cơ cấu mở rộng.
![1.3](/wiki-assets/images/orc_bot/orc-bot/images/1.3.png)

Trên ORC Control Hub có **8 cổng Grove** và khả năng điều khiển tối đa **10 động cơ**, phù hợp cho cả robot cơ bản lẫn những mô hình thi đấu cần thêm cơ cấu nâng cao.

- 2 động cơ DC có encoder
- 4 động cơ DC thường
- 4 động cơ servo
![orc hub dong co](/wiki-assets/images/orc_bot/orc-bot/images/orc-hub-dong-co.png)

Các cổng Grove giúp việc kết nối cảm biến trở nên nhanh và an toàn hơn, giảm lỗi cắm nhầm dây trong quá trình học và thử nghiệm.
![orc hub grove](/wiki-assets/images/orc_bot/orc-bot/images/orc-hub-grove.png)
![orc hub sensor](/wiki-assets/images/orc_bot/orc-bot/images/orc-hub-sensor.jpg)

## 2.2. Cơ khí và động cơ

ORC K2 được lắp từ các thanh kim loại chuẩn hóa nên dễ lắp, dễ thay đổi thiết kế và phù hợp để học sinh sáng tạo nhiều cơ cấu robot khác nhau. Bộ kit đi kèm các động cơ phù hợp với kích thước nhỏ gọn của robot, giúp cân bằng giữa độ bền, khả năng điều khiển và mức độ dễ tiếp cận cho người mới.

Trong các bài học của bộ tài liệu này, robot sử dụng chủ yếu hai nhóm động cơ:

- **Động cơ DC** cho hệ di chuyển
- **Động cơ servo** cho các cơ cấu gắp, nâng hoặc thao tác chính xác

![1.7](/wiki-assets/images/orc_bot/orc-bot/images/1.7.png)
![1.8](/wiki-assets/images/orc_bot/orc-bot/images/1.8.png)

ORC K2 đi kèm:

- 2 động cơ DC 6V có encoder
- 2 động cơ DC 6V không encoder
- 2 động cơ servo công suất cao
- 4 bánh Mecanum đa hướng cỡ 60 mm

Nhờ cấu hình này, ORC K2 rất phù hợp để học cách điều khiển robot di chuyển chính xác, gắp vật và thực hiện các nhiệm vụ thi đấu ở quy mô vừa.

## 2.3. Cảm biến

Robot ORC K2 tích hợp và hỗ trợ nhiều cảm biến quen thuộc trong Robotics để bạn xây dựng các bài toán điều khiển thực tế:

- Cảm biến dò line 4 kênh
- Cảm biến góc xoay 6 trục
- Cảm biến khoảng cách
- Module nút nhấn đôi

Các cảm biến này giúp robot nhận biết môi trường, giữ hướng di chuyển, phát hiện vật cản và phản hồi theo chương trình bạn lập trình.
![1.10](/wiki-assets/images/orc_bot/orc-bot/images/1.10.png)

## 2.4. Nguồn điện

ORC K2 sử dụng **pin sạc 2S 8.4V 2500mAh**. Mức điện áp này phù hợp với kích thước và hệ động cơ của K2, giúp robot hoạt động ổn định trong quá trình học tập và thi đấu.

Khi sử dụng pin cho robot, bạn vẫn nên chú ý:

- Sạc đúng bộ sạc đi kèm
- Kiểm tra dây nguồn trước khi vận hành
- Ngắt nguồn khi không sử dụng
- Tránh để pin cạn quá sâu hoặc va đập mạnh

![1.11](/wiki-assets/images/orc_bot/orc-bot/images/1.11.png)
![1.12](/wiki-assets/images/orc_bot/orc-bot/images/1.12.png)

## 3. Thư viện Robotics Open Platform

Khi làm các dự án Robotics, chúng ta thường phải xử lý nhiều bài toán nền tảng như điều khiển động cơ, đọc cảm biến, điều khiển từ xa, giữ hướng hoặc tổ chức chương trình theo từng cơ cấu của robot.

Thư viện **Robotics Open Platform** giúp đơn giản hóa các tác vụ đó để bạn tập trung hơn vào ý tưởng, chiến thuật thi đấu và cách mở rộng robot theo mục tiêu của mình.



