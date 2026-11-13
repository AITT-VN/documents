# 2. Hướng dẫn lập trình

Trang này hướng dẫn thao tác trên OhStem App để kết nối ORC Control Hub và nạp chương trình tham khảo cho Robot ORC K1. Phần sơ đồ nối dây đã có sẵn trong tài liệu hướng dẫn lắp ráp (HDLR), bạn lắp theo tài liệu đó trước khi lập trình.

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

## 3. Mở chương trình tham khảo

- **Code tham khảo cho Robot ORC K1**: [Mở chương trình trên OhStem App](https://app.ohstem.vn/#!/share/yolouno/3JOYSfjakXvQzOfUgrhbi6rnAeI)

- Mở link ở trên, chọn **Import project** để nạp chương trình vào giao diện lập trình.
- Kiểm tra lại các khối lệnh, chỉnh sửa thông số và thao tác điều khiển theo nhu cầu của đội thi.

## 4. Nạp chương trình vào robot

- Nhấn biểu tượng **Lưu project vào thiết bị** để ghi chương trình vào bộ nhớ Flash của ORC Control Hub.
- Sau khi nạp xong, chương trình sẽ tự chạy mỗi khi bật nguồn robot, không cần kết nối máy tính.

![Lưu chương trình vào bộ nhớ Flash](/wiki-assets/images/orc_bot/orc-bot/images/orc-luucode.PNG)
