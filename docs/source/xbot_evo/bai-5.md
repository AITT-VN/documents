# 8. Bài 5: Điều khiển từ xa

**Mục tiêu:**

Biết cách bật chế độ điều khiển từ xa cho xBot Evo bằng giao diện tay cầm trên OhStem App hoặc tay cầm Gamepad, và gán thêm chức năng cho các nút nhấn.

## 1. Các cách điều khiển từ xa
Ngoài di chuyển tự động, xBot Evo có thể được điều khiển từ xa theo 2 cách:

- **Giao diện tay cầm trên OhStem App:** dùng điện thoại hoặc máy tính bảng, kết nối với robot qua Bluetooth. Cách này không cần thêm thiết bị.
![Giao diện tay cầm trên OhStem App](/wiki-assets/images/orc_bot/orc-bot/images/6.4.png)
![Giao diện tay cầm trên OhStem App (tiếp)](/wiki-assets/images/orc_bot/orc-bot/images/6.5.png)


- **Tay cầm Gamepad:** tay cầm có kiểu dáng giống tay cầm PS4, giúp điều khiển nhanh và chính xác hơn. Cách này cần thêm **module nhận tín hiệu (receiver)**.
![Tay cầm Gamepad](/wiki-assets/images/orc_bot/orc-bot/images/6.1.png)


## 2. Kết nối tay cầm Gamepad
Nếu dùng tay cầm Gamepad, bạn cắm module nhận tín hiệu vào **cổng Grove màu đỏ (I2C)** bất kỳ trên ORC Control Hub.
![Kết nối module nhận tín hiệu với ORC Control Hub](/wiki-assets/images/orc_bot/orc-bot/images/orc-hub-receiver.jpg)


Để ghép nối tay cầm với robot: bật robot, **nhấn nút P trên tay cầm**, đưa tay cầm lại gần robot và chờ đèn trên module nhận tín hiệu sáng xanh.
![Kết nối tay cầm với robot](/wiki-assets/images/orc_bot/orc-bot/images/k3-ketnoitaycam.PNG)


## 3. Khối lệnh sử dụng
Các khối lệnh điều khiển từ xa nằm trong danh mục **DI CHUYỂN**.
![Khối lệnh điều khiển từ xa](/wiki-assets/images/orc_bot/orc-bot/images/6.6.png)
![Khối lệnh điều khiển từ xa (tiếp)](/wiki-assets/images/orc_bot/orc-bot/images/6.7.png)


- **Bật chế độ điều khiển từ xa:** khi bật chế độ này, thư viện tự động xử lý các nút lên, xuống, trái, phải và joystick trái để robot di chuyển. Bạn không cần lập trình thêm cho việc di chuyển.

    ◼ **Độ nhạy** càng cao thì robot tăng tốc càng nhanh nhưng khó điều khiển chính xác. Độ nhạy thấp giúp robot tăng tốc từ từ và dễ điều khiển hơn.

- **Khi nút được nhấn:** gán các lệnh cần chạy khi một nút trên tay cầm được nhấn, ví dụ: nút vuông, tam giác, X, tròn, L1, R1, L2, R2.
![Khối lệnh khi nút được nhấn](/wiki-assets/images/orc_bot/orc-bot/images/6.8.png)


- **Đọc giá trị joystick:** đọc trục X, trục Y, góc và khoảng cách kéo của joystick trái hoặc phải.
![Khối lệnh đọc joystick](/wiki-assets/images/orc_bot/orc-bot/images/6.9.png)


- **Tắt chế độ điều khiển từ xa:** dùng khi muốn chuyển sang chạy chế độ tự động. Sau khi chạy xong, có thể bật lại chế độ điều khiển từ xa.
![Khối lệnh tắt chế độ điều khiển từ xa](/wiki-assets/images/orc_bot/orc-bot/images/6.10.png)


## 4. Chương trình mẫu
Chương trình khai báo robot và bật chế độ điều khiển từ xa. Bạn dùng các nút mũi tên hoặc joystick trái để điều khiển xBot Evo di chuyển.
![Chương trình điều khiển từ xa](/wiki-assets/images/orc_bot/orc-bot/images/6.11.png)


Chạy chương trình, sau đó mở giao diện tay cầm trên OhStem App (hoặc ghép nối tay cầm Gamepad) và thử điều khiển robot.

> **Mẹo:** Nhấn **Lưu project vào thiết bị** để robot tự vào chế độ điều khiển từ xa mỗi khi bật nguồn, không cần kết nối máy tính.

## 5. Gán thêm chức năng cho các nút
Bạn hãy thêm các chức năng sau vào chương trình bằng khối lệnh **khi nút được nhấn**:

| **Nút trên tay cầm** | **Chức năng** |
|---|---|
| Lên, xuống, trái, phải, joystick trái | Di chuyển robot (thư viện đã xử lý sẵn) |
| Vuông | Đèn LED sáng màu xanh dương |
| Tam giác | Đèn LED sáng màu xanh lá |
| Tròn | Đèn LED sáng màu đỏ |
| X | Tắt đèn LED |
| R1 | Robot quay tại chỗ 1 vòng (360 độ) |

Gợi ý: với nút R1, bạn cần **tắt chế độ điều khiển từ xa**, cho robot quay 360 độ (cần bật cảm biến góc như bài 2), sau đó **bật lại chế độ điều khiển từ xa**.

## 6. Thử thách
Kết hợp các bài đã học, hãy tổ chức một trò chơi cùng bạn bè:

1. **Đua xe:** dán một đường đua bằng băng keo, điều khiển xBot Evo đi hết đường đua trong thời gian ngắn nhất.
2. **Đẩy bóng vào gôn:** dùng xBot Evo đẩy một quả bóng nhỏ vào khung thành làm bằng hộp giấy.
3. **Chế độ tự động:** khi nhấn nút L1, robot tự chạy theo line đến vạch ngang tiếp theo (bài 4), sau đó quay lại chế độ điều khiển từ xa.

## 7. Câu hỏi ôn tập
1. Kể tên 2 cách điều khiển xBot Evo từ xa.
2. Module nhận tín hiệu tay cầm được cắm vào cổng nào trên ORC Control Hub?
3. Vì sao cần tắt chế độ điều khiển từ xa trước khi chạy một hành động tự động?
