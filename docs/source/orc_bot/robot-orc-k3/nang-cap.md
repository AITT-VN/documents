# 4. Nâng cấp mở rộng

Sau khi hoàn thành phiên bản cơ bản, bạn có thể mở rộng ORC K3 bằng các cơ cấu phụ dùng thêm **Yolo UNO** làm bộ điều khiển mở rộng. Hai hướng phổ biến là mở rộng thêm động cơ và mở rộng thêm nhiều cổng servo.

## 1. Mở rộng động cơ

Phương án này phù hợp khi bạn muốn gắn thêm một động cơ DC hoặc một cơ cấu phụ có dùng động cơ để thử nghiệm riêng ngoài bộ điều khiển chính của robot.

### Kết nối

- Dùng **ORC Control Hub** kết hợp với **mạch điều khiển động cơ** giao tiếp `I2C`.
- Nối mạch điều khiển động cơ vào cổng `I2C` trên Control Hub.
- Cắm động cơ DC cần mở rộng vào cổng `M1` trên mạch điều khiển động cơ.
- Cấp nguồn ngoài `12V` cho mạch điều khiển động cơ trước khi thử cơ cấu.
- Kiểm tra đúng cực nguồn trước khi bật hệ thống.


  ![Kết nối mạch điều khiển động cơ với ORC Control Hub](/wiki-assets/images/orc_bot/orc-bot/images/morongdongco.PNG)


### Lập trình đơn giản

- Truy cập [app.ohstem.vn](https://app.ohstem.vn/), chọn thiết bị **Yolo UNO**.
- Vào mục **Mở rộng** và cài thư viện `Motors Driver V1` bằng link:
  `https://github.com/AITT-VN/yolobit_extension_motor_driver.git`
- Chương trình kiểm tra nhanh có thể dùng để thử động cơ DC ở cổng `M1`.
- Hình code mẫu điều khiển động cơ được minh họa ngay bên dưới.


  ![Tải thư viện Motors Driver V1 cho mở rộng động cơ](/wiki-assets/images/yolo_uno/yolo_uno_khoi_lenh/dong_co/images/dong-co-buoc.4.png)


*Minh họa bước tải thư viện `Motors Driver V1` trong mục **Mở rộng**.*


  ![Chương trình mẫu mở rộng động cơ DC](/wiki-assets/images/yolo_uno/yolo_uno_khoi_lenh/dong_co/images/dongcoDC2.PNG)


## 2. Mở rộng servo

Phương án này phù hợp khi bạn muốn bổ sung thêm nhiều servo cho các cơ cấu như tay gắp, tay đẩy, càng đỡ hoặc các cơ cấu phụ khác.

### Kết nối

- Dùng **ORC Control Hub** kết hợp với **Module servo 8 kênh I2C**.
- Nối module servo 8 kênh vào cổng `I2C` trên ORC Control Hub.
- Cắm các servo vào các cổng `MS1` đến `MS8` trên module.
- Cấp nguồn riêng cho module servo, có thể dùng **pin 2S** như trong tài liệu mẫu.
- Nếu cần làm nút thử nhanh, có thể dùng thêm nút nhấn đôi theo cấu hình trong chương trình mẫu.



![Kết nối module servo 8 kênh với ORC Control Hub](/wiki-assets/images/orc_bot/orc-bot/images/morongservo.PNG)

Kết nối module servo 8 kênh vào cổng I2C của ORC Control Hub.



### Lập trình đơn giản

- Truy cập [app.ohstem.vn](https://app.ohstem.vn/), chọn thiết bị **Yolo UNO**.
- Vào mục **Mở rộng** để thêm thư viện servo 8 kênh.
- Dán link thư viện sau vào ô tìm kiếm:
  `https://github.com/AITT-VN/yolouno_extension_servo8chs`
- Nhấn cài đặt thư viện `SERVO8CHS Kit`.



![Thêm thư viện SERVO8CHS Kit trên Yolo UNO](/wiki-assets/images/yolo_uno/yolo_uno_khoi_lenh/dong_co/images/servo_8_kenh_5.png)

Bước thêm thư viện SERVO8CHS Kit trong mục Mở rộng.



- Sau khi cài xong, bộ lệnh điều khiển servo 8 kênh sẽ xuất hiện để bạn dùng cho các cổng `MS1` đến `MS8`.



![Các khối lệnh của thư viện servo 8 kênh sau khi cài](/wiki-assets/images/yolo_uno/yolo_uno_khoi_lenh/dong_co/images/servo_8_kenh_6.png)

Các khối lệnh điều khiển servo 8 kênh sau khi cài thư viện.



- Mỗi servo trên module sẽ có tên từ `MS1` đến `MS8`.
- Bạn có thể đặt góc quay trong khoảng `0-180` độ và chỉnh tốc độ từ `1-100`.
- Code mẫu tham khảo:
  [Mở chương trình servo 8 kênh trên OhStem App](https://app.ohstem.vn/#!/share/yolouno/2vTYp3OUG9U3UakHnH8ZpozoYuj)



![Chương trình mẫu điều khiển servo 8 kênh với Yolo UNO](/wiki-assets/images/yolo_uno/yolo_uno_khoi_lenh/dong_co/images/servo_8_kenh_15.png)

Chương trình mẫu điều khiển nhiều servo trên các cổng MS1 đến MS8.


