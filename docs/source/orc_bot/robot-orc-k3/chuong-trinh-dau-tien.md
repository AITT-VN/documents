# 3. Hướng dẫn lập trình

Phần này hướng dẫn thao tác trên OhStem App để kết nối ORC Control Hub, nạp chương trình mẫu và điều khiển Robot ORC K3 bằng Gamepad. Phần sơ đồ nối dây đã có trong tài liệu hướng dẫn lắp ráp (HDLR).

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




## 3. Nạp chương trình mẫu

- **Code tham khảo cho Robot ORC K2 và K3 (mới nhất)**: [Mở chương trình trên OhStem App](https://app.ohstem.vn/#!/share/yolouno/3JOjsTiKo2Q1u3f089XSY5W7kR1)
- Mở link ở trên, chọn **Import project** để nạp chương trình vào giao diện lập trình.
- Hoặc quét mã QR / mở đường link hiển thị trong ảnh bên dưới để lấy chương trình mẫu.
- Kiểm tra lại các khối lệnh trước khi gửi xuống thiết bị.
- Chương trình mẫu của ORC K3 tương tự ORC K2, có thể xem thêm tại [Hướng dẫn lập trình ORC K2](/orc_bot/robot-orc-k2/chuong-trinh-dau-tien.md).


  

![Nạp chương trình mẫu cho ORC K3](/wiki-assets/images/orc_bot/orc-bot/images/k3-laptrinh4.PNG)

Quét QR hoặc mở link trong ảnh, sau đó chọn Import project.




## 4. Lưu chương trình vào Flash và chạy thử

- Nhấn **Lưu project vào thiết bị** để ghi chương trình vào bộ nhớ Flash.
- Sau khi lưu thành công, tắt và bật lại công tắc nguồn để robot chạy chương trình đã lưu.
- Nếu chỉ muốn chạy thử nhanh, có thể nhấn nút **Play** mà không cần lưu vào Flash.
- Có thể nhấn **Stop** để dừng chương trình đang chạy.


  

![Lưu chương trình vào Flash cho ORC K3](/wiki-assets/images/orc_bot/orc-bot/images/k3-luucode.PNG)

Lưu chương trình vào Flash, hoặc chạy thử nhanh bằng nút Play.




## 5. Kết nối robot với Gamepad

- Nhấn nút `P` trên Gamepad để khởi động.
- Đưa Gamepad lại gần robot để ghép nối.
- Khi kết nối thành công, module `Gamepad Receiver` trên robot sẽ sáng đèn xanh lá.


  

![Kết nối Gamepad với ORC K3](/wiki-assets/images/orc_bot/orc-bot/images/k3-ketnoitaycam.PNG)

Nhấn nút P, đưa tay cầm lại gần robot và chờ đèn receiver sáng xanh.




## 6. Gợi ý kiểm tra khi chạy thử

- Nếu robot đi ngược chiều, hãy kiểm tra lại thứ tự các cổng cắm động cơ.
- Nếu robot không di chuyển, hãy kiểm tra chiều lắp bánh Mecanum và thử nâng robot lên để xem bánh có quay hay không.
- Nếu không điều khiển được bằng Gamepad, hãy kiểm tra lại kết nối receiver và xác nhận chương trình đã thực sự chạy.


  

![Các lỗi thường gặp khi chạy ORC K3](/wiki-assets/images/orc_bot/orc-bot/images/k3-chuy1.PNG)

Các lỗi thường gặp khi robot đi ngược chiều, không di chuyển hoặc không nhận Gamepad.




## 7. Tham khảo thêm

- Nếu bạn cần hướng dẫn chi tiết hơn về ORC Control Hub và các bài tập nền tảng, có thể xem tại:
  [Làm quen với Control Hub](/orc_bot/lam-quen-control-hub/chuong-trinh-dau-tien.md)

