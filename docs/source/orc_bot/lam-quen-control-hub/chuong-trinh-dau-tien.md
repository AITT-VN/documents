# 1. Chương trình đầu tiên

Trong phần này, bạn sẽ tìm hiểu về cách làm việc với mạch ORC Control Hub bằng phần mềm lập trình OhStem App, sau đó ứng dụng vào viết các chương trình cơ bản đầu tiên:

- Bật tắt đèn LED trên mạch ORC Control Hub.
- Bật tắt đèn LED bằng nút nhấn trên mạch.

## 1. Cập nhật firmware
Phần mềm bên trong ORC Control Hub (firmware) được OhStem nâng cấp và cập nhật thường xuyên. Do đó, khi mới dùng lần đầu, bạn nên cập nhật để đảm bảo thiết bị đang chạy firmware mới nhất, giúp chạy ổn định hơn.

- **Bước 1:** Truy cập vào link [https://fw.ohstem.vn/](https://fw.ohstem.vn/):
![3.1](/wiki-assets/images/orc_bot/orc-bot/images/3.1.png)


- **Bước 2:** Kết nối mạch ORC Control Hub với laptop bằng dây USB Type C:
![fw orc hub](/wiki-assets/images/orc_bot/orc-bot/images/fw-orc-hub.jpg)


- **Bước 3:** **Nhấn và giữ nút Boot** trên ORC Control Hub, **trong lúc đó nhấn nút Reset và thả ra sau 1 giây**, **sau đó mới thả nút Boot** để thiết bị vào trạng thái sẵn sàng cập nhật firmware:
{download}`Video khởi động ORC Control Hub </wiki-assets/images/orc_bot/orc-bot/images/orc-hub-boot.mp4>`


- **Bước 4:** Chọn firmware cần cập nhật là **Yolo UNO v1.x**, chọn cổng kết nối có tên là **USB/JTAG serial…** và nhấn **Cập nhật**.
![3.4](/wiki-assets/images/orc_bot/orc-bot/images/3.4.png)


    Firmware sẽ được cập nhật liên tục, do đó bạn hãy chọn bản cập nhất mới nhất, ví dụ trong hình là v1.1
    
- **Bước 5:** Chọn **Install** để tiếp tục cập nhật firmware
![3.5](/wiki-assets/images/orc_bot/orc-bot/images/3.5.png)


- **Bước 6:** Chờ khoảng 2 phút để cập nhật. Màn hình hiển thị cập nhật thành công như hình:
![3.6](/wiki-assets/images/orc_bot/orc-bot/images/3.6.png)


- **Bước 7:** Nhấn nút Reset và thoát khỏi trang web cập nhật firmware và tiến hành lập trình.

## 2. Kết nối ORC Control Hub với OhStem App
- **Bước 1:** Truy cập vào link [https://app.ohstem.vn/](https://app.ohstem.vn/):
![3.7](/wiki-assets/images/orc_bot/orc-bot/images/3.7.png)


- **Bước 2:** Chọn thiết bị lập trình là Yolo UNO
![3.8](/wiki-assets/images/orc_bot/orc-bot/images/3.8.png)


- **Bước 3:** Chọn vào **Lập trình**:
![3.9](/wiki-assets/images/orc_bot/orc-bot/images/3.9.png)


- **Bước 4:**

    + Kết nối ORC Control Hub vào máy tính và phần mềm lập trình
    + Kết nối dây USB type C với Máy tính và ORC Control Hub.
![app orc hub](/wiki-assets/images/orc_bot/orc-bot/images/app-orc-hub.jpg)


    + Chọn icon kết nối có dây/ Bluetooth → chọn cổng COM/ thiết bị có tên gần giống là **Espressif CDC Device (COMxx)** → nhấn nút Kết nối. (Số thứ tự của cổng COM có thể là khác nhau trên mỗi máy tính.)
![3.11](/wiki-assets/images/orc_bot/orc-bot/images/3.11.png)


    + Khi kết nối thành công biểu tượng USB sẽ sáng đèn màu xanh:
![3.12](/wiki-assets/images/orc_bot/orc-bot/images/3.12.png)


## 3. Chương trình 1: Nháy đèn LED trên mạch
Trong bài này, chúng ta sẽ viết chương trình đầu tiên, lập trình cho ORC Control Hub bật tắt đèn LED màu trên board sau mỗi giây.

- **Giới thiệu khối lệnh lập trình:**
![3.13](/wiki-assets/images/orc_bot/orc-bot/images/3.13.png)


Câu lệnh dùng để thay đổi màu đèn led RGB trên board, màu đen dùng để tắt đèn.

- **Chương trình lập trình:**
![3.14](/wiki-assets/images/orc_bot/orc-bot/images/3.14.png)


- **Link chương trình mẫu:**

Bật tắt đèn LED trên board: [Xem code mẫu tại đây ](https://app.ohstem.vn/#!/share/yolouno/2aLcEMEIMJYYvq47M7660i2djBN) hoặc quét mã QR bên dưới:
![3.15](/wiki-assets/images/orc_bot/orc-bot/images/3.15.png)
