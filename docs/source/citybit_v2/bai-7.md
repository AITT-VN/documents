# 9. Bài 7: Bãi đậu xe thông minh

## Mục tiêu
Trong bài này, chúng ta sẽ sử dụng công nghệ RFID để kiểm soát xe ra vào ở các bãi xe và động cơ servo để đóng mở cổng tự động.

## Thiết bị cần dùng
Yolo:Bit, mạch RFID kèm thẻ từ, động cơ Servo.

## Kết nối
- Module RFID (cổng C)
- Động cơ Servo (cổng S1)

**Lưu ý:** Chỉnh Servo về góc 20 độ trước khi lắp (xem cách hiệu chỉnh ở [Bài 2](/citybit_v2/bai-2.md)).

![Kết nối bài 7](/wiki-assets/images/citybit_v2/bai7-ket-noi.jpg)

## Lắp ráp mô hình
![Lắp ráp bài 7 - 1](/wiki-assets/images/citybit_v2/bai7-lap-rap-1.jpg)

![Lắp ráp bài 7 - 2](/wiki-assets/images/citybit_v2/bai7-lap-rap-2.jpg)

## Giới thiệu khối lệnh
- **thẻ có trong danh sách ...** (mục STEM KIT): kiểm tra thẻ RFID đang quét có nằm trong danh sách thẻ hợp lệ hay không.
- **thêm thẻ vào danh sách ...**: lưu thẻ RFID mới vào danh sách.
- **xóa thẻ khỏi danh sách ...**: xóa một thẻ RFID đã lưu ra khỏi danh sách.
- **khi nút A được nhấn** (mục NGÕ VÀO): lập tức thực hiện lệnh bên trong khi nút được nhấn.
- **Khối lệnh so sánh** (mục LÔGIC): thực hiện phép so sánh (`>`, `<`, `=`,...) giữa 2 giá trị bất kì. **Giá trị logic**: đúng hoặc sai.

![Giới thiệu khối lệnh bài 7 (1)](/wiki-assets/images/citybit_v2/bai7-khoi-lenh-1.jpg)

- **phát bài nhạc ... chờ kết thúc** (mục ÂM NHẠC): phát toàn bộ bài nhạc mới và sau đó thực hiện lệnh tiếp theo.
- **phát nốt nhạc ... với độ dài ...**: phát một nốt nhạc.

![Giới thiệu khối lệnh bài 7 (2)](/wiki-assets/images/citybit_v2/bai7-khoi-lenh-2.jpg)

## Viết chương trình
1. **Khởi tạo servo** quay đến góc 20 độ (đóng thanh chắn bãi xe).
2. Thiết lập điều kiện kiểm tra thẻ đã quét. Nếu thẻ đã được quét nằm trong danh sách, thực hiện các bước sau:
   - Bật đèn xanh để báo hiệu.
   - Xoay servo mở thanh chắn trong vòng 3 giây.
   - Phát âm thông báo.
   - Sau đó, bật đèn đỏ.
   - Xoay servo đóng thanh chắn.

![Viết chương trình bài 7 (1)](/wiki-assets/images/citybit_v2/bai7-chuong-trinh-1.jpg)

3. Nếu muốn **thêm một thẻ mới** vào danh sách: nhấn nút A để thêm thẻ mới.
4. Nếu muốn **xóa thẻ đã lưu** ra khỏi danh sách: nhấn nút B để xóa thẻ.

![Viết chương trình bài 7 (2)](/wiki-assets/images/citybit_v2/bai7-chuong-trinh-2.jpg)

5. Chương trình hoàn thiện:

![Chương trình hoàn thiện bài 7](/wiki-assets/images/citybit_v2/bai7-chuong-trinh-3.jpg)
