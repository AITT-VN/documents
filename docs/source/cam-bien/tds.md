# 37. Cảm biến TDS

- Cảm biến TDS (Total Dissolved Solids - tổng chất rắn hòa tan) dùng để ước lượng lượng chất hòa tan trong nước, với đơn vị **ppm** (phần triệu). Giá trị TDS càng cao thì nước càng chứa nhiều muối khoáng và tạp chất.

- Cảm biến trả về tín hiệu điện áp Analog, sau đó thư viện sẽ quy đổi thành giá trị TDS (có bù trừ theo nhiệt độ nước). Bạn có thể áp dụng cảm biến vào các dự án như kiểm tra chất lượng nước uống, máy lọc nước, hồ cá, thủy canh,…

## **1. Kết nối**
Cảm biến dùng cho **Yolo UNO**. Kết nối cảm biến TDS vào chân **Analog A0** trên Yolo UNO (đây cũng là chân mặc định của khối lệnh khởi tạo cảm biến).

> **Lưu ý:** Nếu kết nối vào chân Analog khác trên Yolo UNO, hãy chọn đúng chân đó trong khối lệnh **khởi tạo cảm biến TDS chân**.

## **2. Các khối lệnh**
![Khối lệnh cảm biến TDS](/wiki-assets/images/module/cam-bien/images/tds-khoi-lenh.png)

| Khối lệnh | Chức năng |
|:----------|:----------|
| **khởi tạo cảm biến TDS chân A0** | Khai báo chân kết nối của cảm biến TDS. Đặt khối lệnh này trong phần **bắt đầu** của chương trình. |
| **đặt nhiệt độ nước TDS ... °C** | Cài đặt nhiệt độ nước hiện tại (mặc định 25 °C) để bù trừ nhiệt độ cho kết quả đo. |
| **đọc giá trị TDS (ppm)** | Trả về giá trị TDS đo được, đơn vị ppm. |
| **đọc giá trị điện áp TDS (V)** | Trả về điện áp thô của cảm biến, đơn vị Vôn (V). |
| **hiệu chỉnh TDS: thêm điểm với TDS chuẩn ... ppm** | Thêm một điểm hiệu chỉnh bằng dung dịch TDS chuẩn (ví dụ 100 ppm). |
| **đặt lại hiệu chỉnh TDS** | Xóa các điểm đã hiệu chỉnh để quay về trạng thái ban đầu. |

## **3. Hiệu chỉnh cảm biến**
Để kết quả đo chính xác, bạn nên hiệu chỉnh cảm biến bằng dung dịch TDS chuẩn.

1. Rửa đầu dò bằng nước sạch rồi thấm khô nhẹ.
2. Dùng khối **đặt nhiệt độ nước TDS** để nhập nhiệt độ thực tế của dung dịch (nếu khác 25 °C).
3. Nhúng đầu dò vào dung dịch TDS chuẩn (ví dụ **100 ppm**), chờ vài chục giây cho giá trị ổn định.
4. Chạy chương trình có khối **hiệu chỉnh TDS: thêm điểm với TDS chuẩn** và nhập giá trị của dung dịch đang dùng (ví dụ `100`).
5. Nếu hiệu chỉnh sai hoặc muốn làm lại từ đầu, dùng khối **đặt lại hiệu chỉnh TDS** rồi hiệu chỉnh lại.

## **4. Hướng dẫn lập trình Yolo UNO với OhStem App**
Chọn thiết bị **Yolo UNO** trong OhStem App, rồi tạo chương trình đọc và hiển thị giá trị TDS như sau:

1. Trong phần **bắt đầu**, thêm khối **khởi tạo cảm biến TDS chân A0**.
2. Thêm khối **đặt nhiệt độ nước TDS 25 °C** (hoặc nhiệt độ nước thực tế).
3. Trong phần **lặp lại mãi**, dùng khối hiển thị (hoặc gửi dữ liệu lên máy tính) với giá trị lấy từ khối **đọc giá trị TDS (ppm)**.
4. Thêm khối **tạm dừng 1000 mili giây** để cập nhật giá trị mỗi giây.

Nếu có cảm biến nhiệt độ nước (ví dụ DS18B20), bạn có thể đưa giá trị đo được vào khối **đặt nhiệt độ nước TDS** để kết quả chính xác hơn.

## **5. Lưu ý khi sử dụng**
- Chỉ nhúng phần đầu dò vào nước, giữ các linh kiện điện tử và mối nối khô ráo.
- Rửa đầu dò bằng nước sạch sau mỗi lần đo.
- Cảm biến TDS chỉ ước lượng tổng chất hòa tan, không dùng để kết luận nước có an toàn để uống hay không.
