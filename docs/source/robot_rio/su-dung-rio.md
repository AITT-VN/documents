# 2. Hướng dẫn sử dụng robot Rio

Trên Rio có sẵn các nút nhấn tương tác ở lưng kèm theo cảm biến nhận diện, giúp các bé từng bước tiếp xúc với tư duy lập trình cơ bản và phát triển kỹ năng giải quyết vấn đề theo hướng vui nhộn mà không cần dùng đến điện thoại di động!

![](/wiki-assets/images/robot_rio/rio3.png)

## 2.1. Khởi động nguồn
- Bấm vào nút phía sau đuôi Rio **một lần** để MỞ NGUỒN.
- Nhấn **hai lần liên tiếp** vào công tắc đuôi để TẮT NGUỒN robot.

![](/wiki-assets/images/robot_rio/rio4.PNG)

## 2.2. Các nút nhấn tương tác
Khi vừa khởi động, Rio sẽ vào chế độ nút nhấn tương tác mặc định. Tại đây, Rio nhận lệnh của bé từ các nút điều khiển màu sắc trên lưng:

| Nút/Màu sắc | Chức năng di chuyển |
|:---:|---|
| 🟢 Xanh lá | Di chuyển tiến lùi về phía trước (khoảng 15cm - tương đương 1 ô trên bản đồ vải) |
| 🔴 Đỏ | Di chuyển lùi lại phía sau (khoảng 15cm) |
| 🔵 Xanh dương | Xoay quay trái 90 độ tại chỗ |
| 🟡 Vàng | Xoay quay phải 90 độ tại chỗ |
| 🎵 Nút âm nhạc | Phát bài nhạc vui nhộn |
| 🔁 Nút vòng lặp | Lặp lại các chuỗi nút lệnh đã chọn trước đó |

## 2.3. Nút chọn chế độ Mode (🔄)
Ngoài lập trình di chuyển cơ bản, Rio còn được tích hợp thêm các chế độ thông minh. Dùng nút Mode (🔄) để chuyển đổi:
- **Bấm 1 lần:** Chuyển sang **Chế độ né vật cản** (đèn sẽ báo sáng màu Xanh).
- **Bấm 2 lần liên tiếp:** Chuyển qua **Chế độ dò đường line** (đèn sẽ báo sáng màu Trắng). Nhấn giữ nút Mode để robot học quét nền line, khi học xong Rio sẽ phát ra âm báo "YES" xác nhận.

## 2.4. Đèn LED chỉ báo trạng thái
- **🔶 Dải đèn phía trên:** Hiển thị các nút lệnh mà bạn đã chọn thiết lập với màu sắc tương ứng (ví dụ: lục = tiến, đỏ = lùi...). Dễ dàng kiểm tra lại chuỗi thuật toán.

![](/wiki-assets/images/robot_rio/rio5.PNG)

- **🔷 Dải đèn phía dưới:** Hiển thị số lượng số lần lặp lại chuỗi nếu bạn đang sử dụng nút vòng lặp 🔁.

![](/wiki-assets/images/robot_rio/rio6.PNG)

**Khởi chạy chương trình:**
Sau khi đã thiết lập lộ trình bằng các thẻ lệnh giấy kết hợp nút nhấn trên lưng, hãy nhấn vào **nút Bắt Đầu (Play) ở vị trí chính giữa** để dứt lệnh và Rio sẽ bắt đầu lần lượt di chuyển mô phỏng theo chương trình bạn đã gõ.

## 2.5. Quy tắc sạc và bảo quản
1. **🔋 Cảnh báo pin yếu:** Khi Rio cạn pin, mắt của nó sẽ sáng lên hiển thị biểu tượng hình cục pin.

![](/wiki-assets/images/robot_rio/rio7.PNG)

   - 👉 Hãy ngay lập tức cắm sạc pin (ở cạnh đuôi). Sạc đầy mất khoảng 3 tiếng hoặc cho đến khi đèn báo hiệu ngừng chớp tắt / sáng ổn định.

![](/wiki-assets/images/robot_rio/rio8.PNG)

2. **⏱️ Định kỳ sạc:** Khuyến cáo sạc bù pin ít nhất 2 tuần/lần (ngay cả khi bạn không sử dụng thường xuyên) để hệ thống pin hoạt động bền và chống chai.
3. **🚫 Lưu ý chống va đập:** Robot tích hợp nhiều board vi mạch điện từ, nên cần tránh làm rơi rớt, đụng đập mạnh gây hỏng.
4. **🌬️ Bảo quản:** Cất chứa robot ở môi trường khô ráo, thoáng mát ở nhiệt độ phòng. Tuyệt đối không để linh kiện tiếp xúc với bề mặt ẩm ướt, nước.
