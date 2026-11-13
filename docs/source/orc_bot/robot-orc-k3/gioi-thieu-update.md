# 1. Giới thiệu về kit ORC K3

Tài liệu này là chuỗi bài hướng dẫn giúp bạn làm quen, lắp ráp và lập trình robot ORC. Toàn bộ các bài phía sau vẫn giữ cùng lộ trình thực hành như bộ tài liệu ORC gốc, để bạn có thể bắt đầu với khối lệnh, Python hoặc Arduino C rồi phát triển robot theo các bài toán sáng tạo và thi đấu nâng cao.

## 1. Bộ kit Robot ORC K3

[Robot ORC K3](https://ohstem.vn/product/robot-orc-k3/) là dòng robot cao cấp của OhStem dành cho học sinh THCS, THPT và sinh viên. Với kích thước lớn, kết cấu kim loại chắc chắn và khả năng triển khai nhiều cơ cấu phức tạp, K3 mang đến một nền tảng mạnh mẽ để học tập, sáng tạo và chinh phục các bài toán Robotics toàn diện trong môi trường thi đấu cường độ cao.

So với K2, ORC K3 nổi bật ở không gian lắp ráp rộng hơn, phần cơ khí mạnh hơn và cấu hình nguồn 12V, nhờ đó thích hợp để triển khai các cơ cấu nâng cao, robot thi đấu nhiều nhiệm vụ hoặc các mô hình cần độ bền và lực tốt hơn.

Sau khi lắp ráp theo hướng dẫn, bạn sẽ có một robot 4 bánh Mecanum cỡ lớn có thể di chuyển đa hướng, gắp thả vật thể và dễ dàng mở rộng thêm nhiều cơ cấu phục vụ dự án hoặc thi đấu.
![1.1](/wiki-assets/images/orc_bot/orc-bot/images/1.1.png)

## 2. Thành phần chính của robot

## 2.1. Mạch điều khiển

Robot ORC K3 sử dụng **ORC Control Hub** làm bộ điều khiển trung tâm. Đây là bo mạch do OhStem phát triển cho giáo dục Robotics, hỗ trợ lập trình bằng khối lệnh, Python và Arduino C, đồng thời kết nối thuận tiện qua USB và Bluetooth.
![orc hub](/wiki-assets/images/orc_bot/orc-bot/images/orc_hub.png)

Bo mạch dùng vi điều khiển ESP32-S3, có Wi-Fi 2.4 GHz, Bluetooth LE và khả năng mở rộng tốt cho các dự án robot phức tạp. ORC Control Hub cho phép bạn điều khiển động cơ, đọc cảm biến và tổ chức chương trình cho nhiều cơ cấu cùng lúc.
![1.3](/wiki-assets/images/orc_bot/orc-bot/images/1.3.png)

Trên ORC Control Hub có **8 cổng Grove** và khả năng điều khiển tối đa **10 động cơ**, đủ để triển khai các robot cỡ lớn với nhiều cơ cấu mở rộng.

- 2 động cơ DC có encoder
- 4 động cơ DC thường
- 4 động cơ servo
![orc hub dong co](/wiki-assets/images/orc_bot/orc-bot/images/orc-hub-dong-co.png)

Hệ cổng chuẩn hóa giúp quá trình lắp đặt cảm biến và phụ kiện ổn định hơn, đặc biệt hữu ích khi bạn cần tháo lắp và tinh chỉnh robot thường xuyên trong quá trình học hoặc thi đấu.
![orc hub grove](/wiki-assets/images/orc_bot/orc-bot/images/orc-hub-grove.png)
![orc hub sensor](/wiki-assets/images/orc_bot/orc-bot/images/orc-hub-sensor.jpg)

## 2.2. Cơ khí và động cơ

ORC K3 có bộ khung kim loại lớn và chắc chắn hơn, cho phép lắp thêm nhiều chi tiết cơ khí và xây dựng các cơ cấu robot phức tạp. Đây là điểm khác biệt quan trọng khiến K3 phù hợp hơn với các bài toán thi đấu cần lực, độ ổn định và không gian lắp ráp lớn.

Trong các bài học của bộ tài liệu này, robot sử dụng chủ yếu hai nhóm động cơ:

- **Động cơ DC** cho hệ di chuyển
- **Động cơ servo** cho các cơ cấu gắp, nâng hoặc thao tác chính xác

![1.7](/wiki-assets/images/orc_bot/orc-bot/images/1.7.png)
![1.8](/wiki-assets/images/orc_bot/orc-bot/images/1.8.png)

ORC K3 đi kèm:

- 2 động cơ DC 12V GA25-370 có encoder
- 2 động cơ DC 12V GA25-370 không encoder
- 2 động cơ servo công suất lớn 20 kg
- 4 bánh Mecanum đa hướng cỡ 80 mm
- 80+ chi tiết lắp ráp bằng kim loại và nhựa

Cấu hình này giúp ORC K3 phù hợp để phát triển robot có cơ cấu phức tạp hơn và thực hiện các nhiệm vụ thi đấu đòi hỏi độ bền, lực kéo và độ chính xác tốt.

## 2.3. Cảm biến

Robot ORC K3 tích hợp và hỗ trợ các cảm biến quen thuộc trong Robotics để bạn xây dựng những thuật toán điều khiển thực tế:

- Cảm biến dò line 4 kênh
- Cảm biến góc xoay 6 trục
- Cảm biến khoảng cách
- Module nút nhấn đôi

Các cảm biến này giúp robot nhận biết môi trường, bám hướng, phát hiện vật cản và phản ứng theo chiến lược bạn lập trình.
![1.10](/wiki-assets/images/orc_bot/orc-bot/images/1.10.png)

## 2.4. Nguồn điện

ORC K3 sử dụng **pin sạc 12V 2500mAh**. Nguồn điện cao hơn giúp K3 đáp ứng tốt hơn cho hệ cơ khí lớn, động cơ mạnh và các cơ cấu thi đấu nâng cao.

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

