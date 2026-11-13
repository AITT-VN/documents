# 6. Bài 4: Hệ thống phát hiện ngập nước

## Mục tiêu
Tại các con đường ở vùng trũng trong thành phố thường xuất hiện tình trạng bị ngập nước. Do đó, chúng ta hãy cùng làm một hệ thống theo dõi và báo động tình trạng ngập nước nhé.

Khi bị ngập nước, màn hình LED Yolo:Bit sẽ hiển thị cảnh báo và máy bơm hoạt động để hút nước.

## Thiết bị cần dùng
Yolo:Bit, cảm biến độ ẩm đất, máy bơm mini.

## Kết nối
- Cảm biến độ ẩm đất (cổng A)
- Máy bơm mini (cổng M2)

![Kết nối bài 4](/wiki-assets/images/citybit_v2/bai4-ket-noi.jpg)

## Lắp ráp mô hình
![Lắp ráp bài 4 - 1](/wiki-assets/images/citybit_v2/bai4-lap-rap-1.jpg)

![Lắp ráp bài 4 - 2](/wiki-assets/images/citybit_v2/bai4-lap-rap-2.jpg)

## Giới thiệu khối lệnh
- **độ ẩm đất (%)** (mục STEM KIT): đọc giá trị độ ẩm đất.
- **máy bơm ... bật ... %**: điều khiển hoạt động của máy bơm, với tốc độ bơm từ 0 (tắt) đến 100%.

![Giới thiệu khối lệnh bài 4](/wiki-assets/images/citybit_v2/bai4-khoi-lenh-1.jpg)

## Viết chương trình
1. Kéo khối **hiện hình ảnh** vào phần bắt đầu.
2. **Xóa thông tin** trên màn hình trước đó và **hiện thông tin mực nước** (độ ẩm đất) lên màn hình.
3. **Tạo điều kiện**:
   - Khi mực nước vượt quá 50%, phát cảnh báo và kích hoạt máy bơm để xả nước ra bên ngoài.
   - Nếu không, thông báo an toàn và máy bơm sẽ không hoạt động!
4. **Cập nhật thông tin mực nước** sau mỗi giây.

![Viết chương trình bài 4](/wiki-assets/images/citybit_v2/bai4-chuong-trinh-1.jpg)
