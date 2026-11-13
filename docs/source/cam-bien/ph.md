# 36. Cảm biến pH

- Cảm biến pH dùng để đo độ pH (độ axit - kiềm) của dung dịch, với thang đo từ 0 đến 14: pH nhỏ hơn 7 là môi trường axit, pH bằng 7 là trung tính và pH lớn hơn 7 là môi trường kiềm.

- Cảm biến trả về tín hiệu điện áp Analog, sau đó thư viện sẽ quy đổi điện áp này thành giá trị pH. Bạn có thể áp dụng cảm biến vào các dự án như theo dõi chất lượng nước, hồ cá, thủy canh, hệ thống tưới tiêu thông minh,…

## **1. Kết nối**
Cảm biến dùng cho **Yolo UNO**. Kết nối cảm biến pH vào chân **Analog A0** trên Yolo UNO (đây cũng là chân mặc định của khối lệnh khởi tạo cảm biến).

> **Lưu ý:** Nếu kết nối vào chân Analog khác trên Yolo UNO, hãy chọn đúng chân đó trong khối lệnh **khởi tạo cảm biến pH chân**.

## **2. Các khối lệnh**
![Khối lệnh cảm biến pH](/wiki-assets/images/module/cam-bien/images/ph-khoi-lenh.png)

| Khối lệnh | Chức năng |
|:----------|:----------|
| **khởi tạo cảm biến pH chân A0** | Khai báo chân kết nối của cảm biến pH. Đặt khối lệnh này trong phần **bắt đầu** của chương trình. |
| **đọc giá trị pH** | Trả về giá trị pH đo được (thang đo 0 - 14). |
| **đọc điện áp pH (V)** | Trả về điện áp thô của cảm biến, đơn vị Vôn (V). Dùng để kiểm tra cảm biến hoặc khi cần hiệu chỉnh. |
| **hiệu chỉnh pH: thêm điểm với pH chuẩn ...** | Thêm một điểm hiệu chỉnh bằng dung dịch pH chuẩn (ví dụ 6.86). |
| **đặt lại hiệu chỉnh pH** | Xóa các điểm đã hiệu chỉnh để quay về trạng thái ban đầu. |

## **3. Hiệu chỉnh cảm biến**
Để kết quả đo chính xác, bạn nên hiệu chỉnh cảm biến bằng dung dịch pH chuẩn trước khi sử dụng, và hiệu chỉnh lại định kỳ.

1. Rửa đầu dò bằng nước sạch rồi thấm khô nhẹ (không chà xát đầu dò).
2. Nhúng đầu dò vào dung dịch pH chuẩn (ví dụ dung dịch **pH 6.86**), chờ vài chục giây cho giá trị ổn định.
3. Chạy chương trình có khối **hiệu chỉnh pH: thêm điểm với pH chuẩn** và nhập giá trị pH của dung dịch đang dùng (ví dụ `6.86`).
4. Nếu muốn hiệu chỉnh thêm điểm khác, rửa đầu dò, nhúng vào dung dịch chuẩn tiếp theo rồi lặp lại bước 3.
5. Nếu hiệu chỉnh sai hoặc muốn làm lại từ đầu, dùng khối **đặt lại hiệu chỉnh pH** rồi hiệu chỉnh lại.

## **4. Hướng dẫn lập trình Yolo UNO với OhStem App**
Chọn thiết bị **Yolo UNO** trong OhStem App, rồi tạo chương trình đọc và hiển thị giá trị pH như sau:

1. Trong phần **bắt đầu**, thêm khối **khởi tạo cảm biến pH chân A0**.
2. Trong phần **lặp lại mãi**, dùng khối hiển thị (hoặc gửi dữ liệu lên máy tính) với giá trị lấy từ khối **đọc giá trị pH**.
3. Thêm khối **tạm dừng 1000 mili giây** để cập nhật giá trị mỗi giây.

Có thể thêm khối **đọc điện áp pH (V)** vào cùng chương trình để theo dõi điện áp thô khi hiệu chỉnh.

## **5. Lưu ý khi sử dụng**
- Luôn giữ đầu dò ẩm, không để khô; bảo quản trong dung dịch bảo quản theo khuyến cáo của nhà sản xuất.
- Rửa đầu dò bằng nước sạch sau mỗi lần đo.
- Chờ giá trị ổn định vài chục giây trước khi đọc kết quả.
