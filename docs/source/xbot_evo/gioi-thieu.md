# 1. Làm quen với xBot Evo

**Mục tiêu:**

Giúp người mới làm quen với robot xBot Evo, hiểu được các thành phần của robot, mạch điều khiển ORC Control Hub và lộ trình các bài học trong tài liệu này.

## 1. xBot Evo là gì?
xBot Evo là phiên bản nâng cấp của robot giáo dục [xBot](/xbot/xbot/gioi-thieu.rst). Robot vẫn giữ các chức năng cơ bản quen thuộc của xBot như di chuyển, đổi màu đèn LED, né vật cản, dò đường và điều khiển từ xa, nhưng được chuyển sang sử dụng **mạch điều khiển ORC Control Hub** - cùng loại mạch với bộ [KIT Robot Giáo dục ORC](/orc_bot/lam-quen-control-hub/chuong-trinh-dau-tien.md).

Nhờ đó, các kiến thức bạn học được với xBot Evo có thể dùng tiếp khi chuyển lên các robot thi đấu lớn hơn như Robot ORC K1, K2, K3 mà không cần làm quen lại từ đầu.

**So sánh xBot và xBot Evo**

| | **xBot** | **xBot Evo** |
|---|---|---|
| Mạch điều khiển | xController | ORC Control Hub (ESP32-S3) |
| Thiết bị chọn trên OhStem App | xBot | Yolo UNO |
| Thư viện khối lệnh | Có sẵn | Thư viện mở rộng **ROBOTICS** |
| Kết nối lập trình | USB, Bluetooth | USB Type C, Bluetooth |
| Cảm biến góc | Có | Có (MPU6050 tích hợp trên mạch) |
| Ngôn ngữ lập trình | Khối lệnh, MicroPython, Arduino | Khối lệnh, Python, Arduino C |
| Mở rộng | Cổng mở rộng của xController | 4 động cơ DC, 2 động cơ encoder, 4 servo, 8 cổng Grove |

## 2. Thành phần của xBot Evo

- **Mạch điều khiển ORC Control Hub**

Mạch điều khiển đóng vai trò như bộ não của robot, là bộ phận thực thi chương trình và xử lý giúp robot hoạt động theo thiết kế.
![ORC Control Hub](/wiki-assets/images/orc_bot/orc-bot/images/orc_hub.png)


Mạch sử dụng chip ESP32-S3 lõi kép 32-bit, tốc độ lên đến 240MHz, hỗ trợ WiFi 2.4 GHz và Bluetooth (BLE). Trên mạch có sẵn:

    - Nút nhấn **BOOT** dùng để lập trình các hành động khi nhấn nút
    - Đèn **LED RGB** có thể đổi màu theo chương trình
    - **Cảm biến góc MPU6050** giúp robot đi thẳng và quay góc chính xác
    - Cổng **USB Type C** để kết nối máy tính và nạp chương trình
![Thông tin mạch ORC Control Hub](/wiki-assets/images/orc_bot/orc-bot/images/1.3.png)


- **Các cổng kết nối động cơ**

ORC Control Hub điều khiển được tối đa 10 động cơ: 4 động cơ DC thường (M1 - M4), 2 động cơ DC có encoder (E1, E2) và 4 động cơ servo (S1 - S4).
![Cổng động cơ trên ORC Control Hub](/wiki-assets/images/orc_bot/orc-bot/images/orc-hub-dong-co.png)


- **Các cổng mở rộng Grove**

8 cổng mở rộng chuẩn Grove dùng để kết nối cảm biến và module. Dây Grove chỉ cắm được một chiều, hạn chế tối đa việc cắm ngược gây hư hỏng thiết bị.

    - Cổng **màu đỏ (I2C)**: cảm biến dò line 5 mắt, module nhận tín hiệu tay cầm,...
    - Cổng **màu trắng (D3-D4,...)**: cảm biến khoảng cách (siêu âm),...
![Cổng Grove trên ORC Control Hub](/wiki-assets/images/orc_bot/orc-bot/images/orc-hub-grove.png)


- **Động cơ di chuyển**

xBot Evo di chuyển nhờ 2 động cơ DC bên trái và bên phải. Trong tài liệu này, chúng ta quy ước **động cơ bên trái nối vào cổng M1** và **động cơ bên phải nối vào cổng M2**. Nếu robot của bạn được nối dây khác, hãy làm theo sơ đồ nối dây trong tài liệu hướng dẫn lắp ráp và chỉnh lại cổng trong chương trình cho phù hợp.

- **Cảm biến**

Bộ kit đi kèm **cảm biến khoảng cách (siêu âm)** để phát hiện vật cản phía trước và **cảm biến dò line 5 mắt** để phát hiện vạch đen trên sa bàn.
![Cảm biến khoảng cách và cảm biến dò line](/wiki-assets/images/orc_bot/orc-bot/images/1.10.png)


## 3. Cấp nguồn cho xBot Evo

- **Cổng USB Type C**

Dùng để kết nối máy tính với mạch điều khiển và nạp chương trình. Nguồn từ cổng USB chỉ đủ để chạy mạch, **không đủ để chạy động cơ**.

- **Nguồn pin**

ORC Control Hub hỗ trợ 3 loại đầu cắm nguồn: chuẩn chữ T, XH 2P và Jack DC 5521, điện áp vào tối đa 12V. Để động cơ hoạt động, bạn cần cắm pin và bật công tắc nguồn.

> **Lưu ý:** Không sạc pin qua đêm. Khi robot chạy yếu, di chuyển chậm hoặc không quay được góc chính xác như trước, hãy sạc lại pin.

## 4. Các chế độ hoạt động mặc định
Giống như xBot, xBot Evo có sẵn **4 chế độ hoạt động mặc định**, giúp bạn chơi với robot ngay sau khi lắp ráp xong mà chưa cần lập trình.

Bạn **nhấn nút BOOT** trên mạch ORC Control Hub nhiều lần để chuyển qua lại giữa các chế độ. **Đèn LED trên mạch** sẽ đổi màu để cho biết robot đang ở chế độ nào:

| **Số lần nhấn nút BOOT** | **Trạng thái xBot Evo** | **Màu đèn LED** |
|---|---|---|
| Nhấn lần 1 | Đứng yên và chờ lệnh điều khiển từ OhStem App hoặc tay cầm | Đỏ |
| Nhấn lần 2 | Di chuyển và tự né vật cản | Xanh dương |
| Nhấn lần 3 | Giữ khoảng cách và đi theo vật thể trước mặt | Tím |
| Nhấn lần 4 | Đi theo vạch kẻ sẵn (dò đường) | Trắng |

Sau chế độ thứ 4, nhấn nút BOOT thêm một lần nữa để quay lại chế độ đầu tiên.

> **Lưu ý:**
> - Chế độ né vật cản và đi theo vật thể cần **cảm biến khoảng cách** được cắm đúng cổng. Chế độ dò đường cần **cảm biến dò line** và một sa bàn có vạch đen.
> - Đặt robot xuống sàn trước khi chuyển sang các chế độ tự di chuyển (lần 2, 3, 4) để robot không bị rơi khỏi bàn.

## 5. Robot xBot Evo làm được gì?

Sau khi hoàn thành tài liệu này, bạn sẽ lập trình được cho xBot Evo:

1. Đổi màu đèn LED và xử lý khi nhấn nút trên mạch
2. Di chuyển tới, lùi, rẽ trái, rẽ phải theo thời gian
3. Đi thẳng và quay góc chính xác nhờ cảm biến góc
4. Tự động phát hiện và né vật cản
5. Di chuyển theo đường kẻ đen trên sa bàn
6. Điều khiển từ xa bằng OhStem App hoặc tay cầm Gamepad

Tất cả bài học đều dùng phần mềm [OhStem App](https://app.ohstem.vn) với giao diện khối lệnh kéo thả. Một số bài có kèm thêm chương trình Python cho bạn nào muốn tìm hiểu nâng cao.
