# 4. Bài 2: Thùng rác thông minh

## Mục tiêu
Thùng rác thông minh tự động mở nắp khi có người lại gần, mang lại tiện lợi và giúp thành phố xanh sạch đẹp hơn. Bài viết này sẽ hướng dẫn lập trình thùng rác với tính năng tự mở và phát âm thanh báo hiệu.

## Thiết bị cần dùng
Cảm biến khoảng cách, loa phát nhạc, động cơ Servo.

## Kết nối
- Cảm biến siêu âm (cổng A)
- Loa phát nhạc (cổng B)
- Động cơ Servo (cổng S1)

![Kết nối bài 2](/wiki-assets/images/citybit_v2/bai2-ket-noi.jpg)

## Lắp ráp mô hình
### Bước 1: Hiệu chỉnh góc Servo
Trước khi lắp ráp, bạn cần cân chỉnh Servo về góc 20 để hoạt động chính xác. Thực hiện như sau:

1. Kết nối Servo vào chân S1 trên mạch mở rộng đã gắn Yolo:Bit.
2. Kết nối Yolo:Bit với OhStem App và tiến hành lập trình (xem phần [Cài đặt thư viện STEM KIT](/citybit_v2/cai-dat-thu-vien.md)).
3. Tạo chương trình: khối **xoay servo S1 góc 20** đặt trong phần lặp lại mãi.
4. Nhấn nút chạy.
5. **Ngắt kết nối Servo với nguồn điện.** (Tránh vừa cắm điện và kết nối Servo khi đang gắn lên mô hình, gây hư hại thiết bị.)

![Hiệu chỉnh Servo](/wiki-assets/images/citybit_v2/bai2-lap-rap-1.jpg)

### Bước 2: Lắp ráp mô hình
![Lắp ráp bài 2 - 1](/wiki-assets/images/citybit_v2/bai2-lap-rap-2.jpg)

![Lắp ráp bài 2 - 2](/wiki-assets/images/citybit_v2/bai2-lap-rap-3.jpg)

## Giới thiệu khối lệnh
**loa ... phát bài ... âm lượng ...** (mục STEM KIT): phát những bài nhạc đã lưu trữ trong bộ nhớ của loa.

Mặc định trong thiết bị đã có tập tin MP3 với nội dung "Hãy bỏ rác vào thùng!". Nếu bạn muốn thêm câu nói hoặc bài nhạc vào bộ nhớ của loa, hãy thực hiện như sau:

1. Kết nối loa với máy tính bằng dây USB type C.
2. Bộ nhớ lưu trữ **USB Drive (E:)** của loa sẽ xuất hiện trên máy tính.
3. Chuẩn bị các file MP3 và sao chép vào USB Drive (E:), đặt tên theo thứ tự (01.mp3, 02.mp3, ...). Ngắt kết nối loa khỏi máy tính để tiếp tục lập trình.

![Giới thiệu khối lệnh bài 2](/wiki-assets/images/citybit_v2/bai2-khoi-lenh-1.jpg)

## Viết chương trình
1. Kéo khối **hiện hình ảnh** vào phần bắt đầu.
2. Đặt Servo ở vị trí luôn đóng (góc 20 độ).
3. Kéo khối **điều kiện** vào phần lặp lại mãi.
4. **Tạo điều kiện**: nếu vật cản ở phạm vi nhỏ hơn 10cm.

![Viết chương trình bài 2 (1)](/wiki-assets/images/citybit_v2/bai2-chuong-trinh-1.jpg)

5. **Điều kiện đúng**, thực hiện: phát âm thanh từ loa và mở nắp thùng rác trong 3 giây.
6. **Điều kiện sai**: đóng nắp thùng rác.

![Viết chương trình bài 2 (2)](/wiki-assets/images/citybit_v2/bai2-chuong-trinh-2.jpg)
