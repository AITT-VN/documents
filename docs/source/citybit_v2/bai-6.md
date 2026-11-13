# 8. Bài 6: Hệ thống theo dõi thời tiết

## Mục tiêu
Chất lượng không khí là mối quan tâm lớn ở thành phố. Chúng ta sẽ lập trình một hệ thống theo dõi chất lượng không khí và thời tiết, có hiển thị trên màn hình LCD.

Nếu chất lượng không khí kém, hệ thống sẽ cảnh báo bằng màn hình LED 5 x 5 trên Yolo:Bit.

## Thiết bị cần dùng
Cảm biến DHT20, màn hình LCD OLED, cảm biến MQ135.

## Kết nối
- Cảm biến MQ135 (cổng A)
- Màn hình OLED (cổng C)
- Cảm biến DHT20 (cổng D)

**Lưu ý:** Cảm biến MQ135 sẽ ấm lên khi được cấp điện, đây là đặc tính đốt nóng không khí của thiết bị.

![Kết nối bài 6](/wiki-assets/images/citybit_v2/bai6-ket-noi.jpg)

## Lắp ráp mô hình
![Lắp ráp bài 6 - 1](/wiki-assets/images/citybit_v2/bai6-lap-rap-1.jpg)

![Lắp ráp bài 6 - 2](/wiki-assets/images/citybit_v2/bai6-lap-rap-2.jpg)

## Giới thiệu khối lệnh
- **nồng độ khí Gas** (mục STEM KIT): đọc giá trị nồng độ khí Gas từ cảm biến MQ135.
- **đọc nhiệt độ DHT20**: đọc giá trị nhiệt độ từ cảm biến DHT20.
- **đọc độ ẩm DHT20**: đọc giá trị độ ẩm từ cảm biến DHT20.
- **cập nhật cảm biến DHT20**: cập nhật dữ liệu mới cho cảm biến DHT20 trước khi đọc giá trị.
- **đổi màu tất cả các led thành màu ...** (mục LED): điều khiển màu đèn LED trên Yolo:Bit.

![Giới thiệu khối lệnh bài 6](/wiki-assets/images/citybit_v2/bai6-khoi-lenh-1.jpg)

## Viết chương trình
1. Khi bắt đầu, **hiện hình ảnh** Smile.
2. **Cập nhật thông tin** từ cảm biến nhiệt độ độ ẩm DHT20.
3. **Xóa thông tin** trên màn hình trước đó.

![Viết chương trình bài 6 (1)](/wiki-assets/images/citybit_v2/bai6-chuong-trinh-1.jpg)

4. **Hiển thị thông tin** mới từ các cảm biến ra màn hình:
   - Đọc cảm biến DHT20 để lấy nhiệt độ và độ ẩm.
   - Đọc cảm biến Gas để lấy nồng độ khí.

![Viết chương trình bài 6 (2)](/wiki-assets/images/citybit_v2/bai6-chuong-trinh-2.jpg)

5. **Tạo điều kiện** để kiểm tra nồng độ khí gas trong không khí:
   - Nếu nồng độ khí gas > 1000ppm thì đổi màu LED sang đỏ và hiển thị chất lượng không khí xấu.
   - Ngược lại, đèn LED chuyển sang xanh và hiển thị chất lượng không khí bình thường.
6. **Cập nhật thông tin** của cảm biến sau mỗi giây. Chương trình hoàn thiện:

![Chương trình hoàn thiện bài 6](/wiki-assets/images/citybit_v2/bai6-chuong-trinh-3.jpg)
