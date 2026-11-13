# 5. Bài 3: Hệ thống cảnh báo tiếng ồn

## Mục tiêu
Tại các khu vực cần sự yên tĩnh như trường học, bệnh viện, chúng ta sẽ thiết lập một hệ thống đo lường và cảnh báo khi tiếng ồn vượt hạn mức cho phép.

## Thiết bị cần dùng
Yolo:Bit, cảm biến âm thanh, màn hình LCD OLED.

## Kết nối
- Cảm biến âm thanh (cổng A)
- Màn hình LCD OLED (cổng C)

![Kết nối bài 3](/wiki-assets/images/citybit_v2/bai3-ket-noi.jpg)

## Lắp ráp mô hình
![Lắp ráp bài 3 - 1](/wiki-assets/images/citybit_v2/bai3-lap-rap-1.jpg)

![Lắp ráp bài 3 - 2](/wiki-assets/images/citybit_v2/bai3-lap-rap-2.jpg)

## Giới thiệu khối lệnh
- **màn hình OLED hiển thị ... x ... y ...** (mục STEM KIT): hiển thị nhiều thông tin lên màn hình OLED tại vị trí cột (x), hàng (y) tùy chỉnh.
- **màn hình LCD1602 hiển thị ... x ... y ...**: hiển thị ký tự bất kỳ lên màn hình tại vị trí cột (x), hàng (y) tùy chỉnh.
- **xóa màn hình OLED**: xóa nội dung hiển thị trên màn hình.
- **mức độ âm thanh (%)**: đo và trả về giá trị cường độ âm thanh xung quanh.
- **tạo văn bản từ** (mục CHỮ VIẾT): tạo ra văn bản từ các khối lệnh thông tin được gắn phía sau. **Khối lệnh nội dung** tạo một nội dung tùy ý (chữ, số, kí tự,...) để sử dụng trong chương trình.
- **Khối lệnh số** (mục TÍNH TOÁN): tạo một số tùy ý để sử dụng trong chương trình.

![Giới thiệu khối lệnh bài 3](/wiki-assets/images/citybit_v2/bai3-khoi-lenh-1.jpg)

## Viết chương trình
1. Kéo khối **hiện hình ảnh** vào phần bắt đầu.
2. **Xóa thông tin** trên màn hình trước đó.
3. **Hiện thông tin tiếng ồn**: xuất hiện trên màn hình OLED thông tin về "Tiếng ồn" với cường độ âm thanh được đo bằng đơn vị dB (decibel).

![Viết chương trình bài 3 (1)](/wiki-assets/images/citybit_v2/bai3-chuong-trinh-1.jpg)

4. **Tạo điều kiện**:
   - Nếu mức độ âm thanh vượt quá 70dB, thực hiện phát cảnh báo trên màn hình OLED và màn hình LED của Yolo:Bit.
   - Nếu không, hiển thị thông báo bình thường!

![Viết chương trình bài 3 (2)](/wiki-assets/images/citybit_v2/bai3-chuong-trinh-2.jpg)

5. **Cập nhật thông tin tiếng ồn** sau mỗi giây. Chương trình hoàn thiện:

![Chương trình hoàn thiện bài 3](/wiki-assets/images/citybit_v2/bai3-chuong-trinh-3.jpg)
