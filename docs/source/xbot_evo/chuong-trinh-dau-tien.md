# 3. Kết nối và chương trình đầu tiên

**Mục tiêu:**

Biết cách cập nhật firmware, kết nối xBot Evo với phần mềm OhStem App, cài thư viện ROBOTICS và viết chương trình đầu tiên để làm việc với đèn LED RGB và nút nhấn trên mạch ORC Control Hub.

## 1. Cập nhật firmware
Phần mềm bên trong ORC Control Hub (firmware) được OhStem cập nhật thường xuyên. Khi dùng lần đầu, bạn nên cập nhật để mạch chạy firmware mới nhất.

- **Bước 1:** Truy cập vào link [https://fw.ohstem.vn/](https://fw.ohstem.vn/):
![Trang cập nhật firmware](/wiki-assets/images/orc_bot/orc-bot/images/3.1.png)


- **Bước 2:** Kết nối mạch ORC Control Hub với máy tính bằng dây USB Type C:
![Kết nối ORC Control Hub với máy tính](/wiki-assets/images/orc_bot/orc-bot/images/fw-orc-hub.jpg)


- **Bước 3:** **Nhấn và giữ nút Boot**, **trong lúc đó nhấn nút Reset và thả ra sau 1 giây**, **sau đó mới thả nút Boot** để mạch vào chế độ cập nhật firmware:
{download}`Video khởi động ORC Control Hub </wiki-assets/images/orc_bot/orc-bot/images/orc-hub-boot.mp4>`


- **Bước 4:** Chọn firmware **Yolo UNO** phiên bản mới nhất, chọn cổng kết nối có tên **USB/JTAG serial…** và nhấn **Cập nhật**.
![Chọn firmware](/wiki-assets/images/orc_bot/orc-bot/images/3.4.png)


- **Bước 5:** Chọn **Install** để tiếp tục:
![Cài đặt firmware](/wiki-assets/images/orc_bot/orc-bot/images/3.5.png)


- **Bước 6:** Chờ khoảng 2 phút đến khi màn hình báo cập nhật thành công:
![Cập nhật thành công](/wiki-assets/images/orc_bot/orc-bot/images/3.6.png)


- **Bước 7:** Nhấn nút Reset trên mạch và đóng trang cập nhật firmware.

## 2. Kết nối xBot Evo với OhStem App

- **Bước 1:** Truy cập vào link [https://app.ohstem.vn/](https://app.ohstem.vn/):
![Truy cập OhStem App](/wiki-assets/images/orc_bot/orc-bot/images/3.7.png)


- **Bước 2:** Chọn thiết bị lập trình là **Yolo UNO** (xBot Evo dùng mạch ORC Control Hub, chạy cùng firmware với Yolo UNO):
![Chọn thiết bị Yolo UNO](/wiki-assets/images/orc_bot/orc-bot/images/3.8.png)


- **Bước 3:** Chọn vào **Lập trình**:
![Chọn mục Lập trình](/wiki-assets/images/orc_bot/orc-bot/images/3.9.png)


- **Bước 4:** Kết nối mạch với máy tính bằng dây USB Type C, chọn icon kết nối có dây/Bluetooth → chọn cổng có tên gần giống **Espressif CDC Device (COMxx)** → nhấn **Kết nối**. Số thứ tự cổng COM có thể khác nhau trên mỗi máy tính.
![Chọn cổng kết nối](/wiki-assets/images/orc_bot/orc-bot/images/3.11.png)


- **Bước 5:** Kết nối thành công khi biểu tượng kết nối sáng màu xanh:
![Kết nối thành công](/wiki-assets/images/orc_bot/orc-bot/images/3.12.png)


> Trên điện thoại hoặc máy tính bảng, bạn cài ứng dụng **OhStem App** từ Play Store / App Store và kết nối với robot qua **Bluetooth**.

## 3. Cài thư viện ROBOTICS
Các khối lệnh điều khiển động cơ, di chuyển và cảm biến của xBot Evo nằm trong thư viện mở rộng **ROBOTICS**. Bạn chỉ cần cài một lần cho mỗi mạch.

- **Bước 1:** Trong giao diện lập trình, chọn mục **Mở rộng** và tìm thư viện **ROBOTICS**:
![Tìm thư viện ROBOTICS](/wiki-assets/images/orc_bot/orc-bot/images/4.1.png)


- **Bước 2:** Chọn **OK** khi app hỏi tải thư viện về thiết bị.

- **Bước 3:** Tải thành công, các nhóm khối lệnh **ROBOTICS, ĐỘNG CƠ, DI CHUYỂN, SENSOR, DÒ LINE** sẽ xuất hiện trong danh mục khối lệnh bên trái:
![Danh mục khối lệnh ROBOTICS](/wiki-assets/images/orc_bot/orc-bot/images/4.2.png)


## 4. Chương trình 1: Nháy đèn LED trên mạch
Chúng ta sẽ viết chương trình đầu tiên: cho đèn LED RGB trên mạch bật và tắt sau mỗi giây.

- **Khối lệnh sử dụng:**
![Khối lệnh đổi màu đèn LED](/wiki-assets/images/orc_bot/orc-bot/images/3.13.png)


Khối lệnh này dùng để thay đổi màu đèn LED RGB trên mạch. Chọn **màu đen** để tắt đèn.

- **Chương trình:**
![Chương trình nháy đèn LED](/wiki-assets/images/orc_bot/orc-bot/images/3.14.png)


- **Chương trình mẫu:** [Xem code mẫu tại đây](https://app.ohstem.vn/#!/share/yolouno/2aLcEMEIMJYYvq47M7660i2djBN)

Nhấn nút **Chạy** và quan sát đèn LED trên mạch ORC Control Hub nhấp nháy.

## 5. Chương trình 2: Đổi màu đèn khi nhấn nút
Trên mạch ORC Control Hub có sẵn nút **BOOT**. Bạn hãy viết chương trình: **mỗi khi nhấn nút BOOT, đèn LED lần lượt sáng màu đỏ, xanh lá, xanh dương, mỗi màu 1 giây rồi tắt.**

Gợi ý: dùng khối lệnh **khi nút BOOT được nhấn** trong danh mục **Nút nhấn**, bên trong đặt các khối lệnh đổi màu đèn và khối lệnh **chờ 1 giây**.

## 6. Lưu chương trình vào robot
Khi nhấn **Chạy**, chương trình chỉ chạy tạm thời trong lúc robot đang kết nối. Để robot tự chạy chương trình mỗi khi bật nguồn, bạn nhấn biểu tượng **Lưu project vào thiết bị** để ghi chương trình vào bộ nhớ của ORC Control Hub.
![Lưu chương trình vào thiết bị](/wiki-assets/images/orc_bot/orc-bot/images/orc-luucode.PNG)


## 7. Câu hỏi ôn tập
1. xBot Evo được chọn là thiết bị gì khi lập trình trên OhStem App?
2. Thư viện nào cần cài đặt để có các khối lệnh điều khiển động cơ và cảm biến?
3. Sự khác nhau giữa nút **Chạy** và nút **Lưu project vào thiết bị** là gì?
