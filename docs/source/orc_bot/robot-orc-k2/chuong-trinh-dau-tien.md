# 3. Hướng dẫn lập trình

Phần này hướng dẫn thao tác trên OhStem App để kết nối ORC Control Hub và nạp chương trình cho Robot ORC K2 Starter Kit (2025 - 2026). Phần sơ đồ nối dây đã có trong tài liệu hướng dẫn lắp ráp (HDLR).

## 1. Kết nối ORC Control Hub với OhStem App

- **Bước 1:** Truy cập vào link [https://app.ohstem.vn/](https://app.ohstem.vn/):

![Truy cập OhStem App](/wiki-assets/images/orc_bot/orc-bot/images/3.7.png)

- **Bước 2:** Chọn thiết bị lập trình là **Yolo UNO**:

![Chọn thiết bị Yolo UNO](/wiki-assets/images/orc_bot/orc-bot/images/3.8.png)

- **Bước 3:** Chọn vào **Lập trình**:

![Chọn mục Lập trình](/wiki-assets/images/orc_bot/orc-bot/images/3.9.png)

- **Bước 4:** Kết nối ORC Control Hub với máy tính bằng dây USB Type C:

![Kết nối ORC Control Hub với máy tính](/wiki-assets/images/orc_bot/orc-bot/images/app-orc-hub.jpg)

- **Bước 5:** Chọn icon kết nối có dây/Bluetooth → chọn cổng COM có tên gần giống **Espressif CDC Device (COMxx)** → nhấn **Kết nối**. Số thứ tự cổng COM có thể khác nhau trên mỗi máy tính.

![Chọn cổng kết nối](/wiki-assets/images/orc_bot/orc-bot/images/3.11.png)

- **Bước 6:** Kết nối thành công khi biểu tượng USB sáng đèn màu xanh:

![Kết nối thành công](/wiki-assets/images/orc_bot/orc-bot/images/3.12.png)

Nếu mạch chưa kết nối được, hãy cập nhật firmware theo hướng dẫn tại [Chương trình đầu tiên](/orc_bot/lam-quen-control-hub/chuong-trinh-dau-tien.md).

## 2. Cài thư viện ROBOTICS

- **Bước 1:** Trong giao diện lập trình, chọn mục **Mở rộng**.
- **Bước 2:** Tìm và chọn thư viện **ROBOTICS**.
- **Bước 3:** Chọn **OK** khi app hỏi tải thư viện về thiết bị.
- **Bước 4:** Tải thành công, các nhóm khối lệnh **ROBOTICS, ĐỘNG CƠ, DI CHUYỂN, SENSOR, DÒ LINE** sẽ xuất hiện trong danh sách khối lệnh.


  

![Tải thư viện ROBOTICS trong mục Mở rộng](/wiki-assets/images/orc_bot/orc-bot/images/k3-laptrinh3.PNG)

Vào Mở rộng, chọn thư viện ROBOTICS và nhấn OK để tải về thiết bị.




## 3. Nạp chương trình mẫu cho robot ORC K2

- **Code tham khảo cho Robot ORC K2 và K3 (mới nhất)**: [Mở chương trình trên OhStem App](https://app.ohstem.vn/#!/share/yolouno/3JOjsTiKo2Q1u3f089XSY5W7kR1)
- Mở link ở trên, chọn **Import project** để nạp chương trình vào giao diện lập trình.
- Kiểm tra lại các thông số cấu hình robot trong chương trình:
  - đường kính bánh xe `60 mm`
  - tỉ số truyền `1:34`
  - encoder `350 ppr`
- Thiết lập giới hạn góc cho servo `S1` và `S2` để tránh kẹt cơ cấu đẩy trong quá trình vận hành.
- Khi chạy thử:
  - joystick dùng để điều khiển di chuyển robot
  - `L1 / L2` dùng để nâng hoặc hạ cơ cấu
  - `R1 / R2` dùng để mở hoặc gập càng đẩy


  

![Chương trình mẫu cho robot ORC K2](/wiki-assets/images/orc_bot/orc-bot/images/k2-codemau.PNG)

Chương trình mẫu cho robot ORC K2 trên OhStem App.




## 4. Nạp chương trình và xác nhận hoạt động

- Nhấn biểu tượng **Lưu project vào thiết bị** để ghi chương trình vào bộ nhớ Flash của Control Hub.
- Sau khi nạp thành công, đèn LED tại chân `D13` sẽ chớp tắt định kỳ.
- Nếu chương trình không chạy đúng, hãy kiểm tra lại cổng kết nối và tham số cấu hình robot.


  ![Lưu chương trình vào bộ nhớ Flash cho ORC K2](/wiki-assets/images/orc_bot/orc-bot/images/orc-luucode.PNG)


## 5. Điều khiển robot bằng Gamepad

- Nhấn nút `P` để khởi động tay cầm.
- `L1 / L2`: nâng hoặc hạ cơ cấu.
- `R1 / R2`: mở hoặc gập càng đẩy.
- Joystick: điều khiển robot di chuyển.


  ![Kết nối gamepad với ORC K2](/wiki-assets/images/orc_bot/orc-bot/images/k2-ketnoigamepad.PNG)
  ![Chức năng các nút tay cầm cho ORC K2](/wiki-assets/images/orc_bot/orc-bot/images/chucnangtaygame.PNG)


## 6. Gợi ý kiểm tra khi chạy thử

- Nếu robot di chuyển không đúng hướng, hãy kiểm tra lại chiều lắp bánh Mecanum và mapping động cơ.
- Nếu cơ cấu đẩy bị kẹt, hãy giảm giới hạn góc của servo `S1` và `S2`.
- Nếu Gamepad không nhận, hãy kiểm tra lại dây kết nối `I2C 3` và nguồn cấp cho mạch.
- Nên thử robot ở trạng thái không tải trước khi đưa vào vận hành với bóng hoặc vật thể thật.

## 7. Tham khảo thêm

- Nếu bạn cần hướng dẫn chi tiết hơn về cập nhật firmware, kết nối phần mềm hoặc các bài tập nền tảng với ORC Control Hub, có thể xem tại:
  [Làm quen với Control Hub](/orc_bot/lam-quen-control-hub/chuong-trinh-dau-tien.md)
