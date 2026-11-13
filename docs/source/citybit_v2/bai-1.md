# 3. Bài 1: Đèn công cộng thông minh

## Mục tiêu
Trong bài này, chúng ta sẽ cùng lập trình một chiếc đèn thông minh có thể tự sáng khi có người lại gần. Các đèn này có thể gắn vào các khu vui chơi hoặc công viên tùy thích.

## Thiết bị cần dùng
Yolo:Bit, đèn LED RGB, cảm biến khoảng cách.

## Kết nối
- Cảm biến khoảng cách (cổng A)
- Đèn LED RGB (cổng B)

![Kết nối bài 1](/wiki-assets/images/citybit_v2/bai1-ket-noi.jpg)

## Lắp ráp mô hình
![Lắp ráp bài 1 - 1](/wiki-assets/images/citybit_v2/bai1-lap-rap-1.jpg)

![Lắp ráp bài 1 - 2](/wiki-assets/images/citybit_v2/bai1-lap-rap-2.jpg)

![Lắp ráp bài 1 - 3](/wiki-assets/images/citybit_v2/bai1-lap-rap-3.jpg)

## Giới thiệu khối lệnh
- **Khối lệnh điều kiện** (mục LÔGIC): kiểm tra một điều kiện để thực hiện chương trình. Nếu điều kiện đúng, chạy các lệnh trong phần *thực hiện*; nếu sai, chạy phần *nếu không*.
- **LED màu ... đổi ... thành ...** (mục STEM KIT): điều khiển đèn LED RGB bằng cách chọn đúng chân kết nối và màu đèn trong chương trình (màu đen - tắt đèn).
- **khoảng cách ... < ... cm** (mục STEM KIT): so sánh kết quả đọc được từ cảm biến siêu âm.
- **tạm dừng ... mili giây**: tạm dừng với thời gian tùy chỉnh.
- **hiện hình ảnh** (mục CƠ BẢN): hiện hình ảnh tùy chọn lên màn hình LED của Yolo:Bit.

![Giới thiệu khối lệnh bài 1](/wiki-assets/images/citybit_v2/bai1-khoi-lenh-1.jpg)

## Viết chương trình
1. Kéo khối **hiện hình ảnh** vào phần bắt đầu (dùng để kiểm tra chương trình đã được gửi thành công đến thiết bị hay chưa).
2. Sử dụng khối LED đổi màu thành màu đen, để tắt đèn ngay khi chương trình bắt đầu.
3. Kéo **khối lệnh điều kiện** vào phần lặp lại mãi.

![Viết chương trình bài 1 (1)](/wiki-assets/images/citybit_v2/bai1-chuong-trinh-1.jpg)

4. Nếu phát hiện vật ở khoảng cách < 10cm, thì **bật đèn** (khối tạm dừng 3000 mili giây giữ đèn sáng trước khi kiểm tra lại).
5. Nếu không, tắt đèn.

![Viết chương trình bài 1 (2)](/wiki-assets/images/citybit_v2/bai1-chuong-trinh-2.jpg)
