# 7. Bài 5: Hệ thống tưới cây tự động

## Mục tiêu
Ở dự án này, sẽ thiết lập một hệ thống tưới cây tự động dựa trên độ ẩm của đất nhằm tiết kiệm thời gian chăm sóc cây trồng trong đô thị.

Khi đất trở nên khô (độ ẩm thấp), máy bơm sẽ tự động bật lên để tưới nước cho đến khi đạt độ ẩm tiêu chuẩn thì tắt máy bơm.

## Thiết bị cần dùng
Yolo:Bit, cảm biến độ ẩm đất, máy bơm mini.

## Kết nối
- Cảm biến độ ẩm đất (cổng A)
- Máy bơm mini (cổng M2)

![Kết nối bài 5](/wiki-assets/images/citybit_v2/bai5-ket-noi.jpg)

## Lắp ráp mô hình
1. Lắp vòi vào máy bơm.
2. Đặt máy bơm vào bồn chứa nước.
3. Cắm cảm biến độ ẩm đất và vòi nước của máy bơm vào chậu cây.
4. Lắp Yolo:Bit vào mô hình.

![Lắp ráp bài 5](/wiki-assets/images/citybit_v2/bai5-lap-rap-1.jpg)

## Giới thiệu khối lệnh
Bài này sử dụng lại các khối lệnh **độ ẩm đất (%)** và **máy bơm ... bật ... %** đã học ở [Bài 4](/citybit_v2/bai-4.md).

## Viết chương trình
1. Kéo khối **hiện hình ảnh** vào phần bắt đầu.
2. **Xóa thông tin** trên màn hình trước đó và **hiện thông tin** độ ẩm đất lên màn hình.
3. **Tạo điều kiện**:
   - Khi độ ẩm của đất thấp hơn 30%, phát cảnh báo và kích hoạt máy bơm để tưới nước cho cây.
   - Nếu không, thông báo an toàn và máy bơm sẽ không hoạt động!
4. **Cập nhật thông tin độ ẩm đất** sau mỗi giây.

![Viết chương trình bài 5](/wiki-assets/images/citybit_v2/bai5-chuong-trinh-1.jpg)
