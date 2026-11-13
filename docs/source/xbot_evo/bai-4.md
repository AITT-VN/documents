# 7. Bài 4: Robot dò đường

**Mục tiêu:**

Hiểu về cảm biến dò line 5 mắt và cách lập trình cho xBot Evo di chuyển theo đường kẻ đen trên sa bàn.

## 1. Cảm biến dò line
Cảm biến dò line dùng tia hồng ngoại để phát hiện màu đen và màu trắng trên mặt sàn. Cảm biến **phát tia hồng ngoại xuống bề mặt và đo lượng tia phản xạ trở lại**:

| **Màu sắc bề mặt** | **Đặc tính phản xạ** |
|---|---|
| Trắng | Phản xạ lại gần như toàn bộ tia hồng ngoại. Cảm biến nhận tia hồng ngoại ở mức tối đa. |
| Đen | Hấp thụ hầu hết tia hồng ngoại. Cảm biến nhận tia hồng ngoại ở mức tối thiểu. |

![Nguyên lý phản xạ hồng ngoại](/wiki-assets/images/orc_bot/orc-bot/images/9.1.png)


Nhờ đó, robot có thể:

- Di chuyển theo đường kẻ đen trên nền trắng, giống như đoàn tàu chạy trên đường ray.
- Né vạch đen để không đi ra khỏi một khu vực, vạch đen đóng vai trò như "đường bảo vệ".
- Đếm số vạch đen đã đi qua để dừng lại hoặc rẽ hướng ở đúng vị trí.

xBot Evo sử dụng **cảm biến dò line 5 mắt**, giúp robot bám line ổn định hơn và nhận biết được các ngã rẽ, vạch ngang trên sa bàn.
![Cảm biến dò line 5 mắt](/wiki-assets/images/xbot_evo/do-line-5-mat.png)


## 2. Kết nối phần cứng
Cảm biến dò line giao tiếp theo chuẩn I2C, bạn cắm vào **cổng Grove màu đỏ bất kỳ** trên ORC Control Hub.
![Kết nối cảm biến dò line với ORC Control Hub](/wiki-assets/images/orc_bot/orc-bot/images/orc-hub-do-line.jpg)


## 3. Chuẩn bị sa bàn
Bạn có thể in sa bàn dò đường có sẵn hoặc dùng **băng keo đen** (bản rộng khoảng 2 cm) dán lên mặt sàn sáng màu hoặc tờ giấy trắng khổ lớn.
![Sa bàn dò đường](/wiki-assets/images/orc_bot/orc-bot/images/9.4.png)


## 4. Cách robot bám theo đường
Tùy vào mắt nào của cảm biến đang nhìn thấy vạch đen, robot sẽ biết mình đang lệch sang trái hay sang phải để điều chỉnh lại:
![Các trường hợp di chuyển của robot](/wiki-assets/images/orc_bot/orc-bot/images/9.5.png)


Các trường hợp này **đã được thư viện ROBOTICS xử lý sẵn**, nên bạn không cần tự viết lại. Bạn chỉ cần dùng các khối lệnh trong danh mục **DÒ LINE** và tập trung xây dựng nhiệm vụ cho robot.

## 5. Chương trình mẫu
Mỗi khi nhấn nút BOOT, xBot Evo đi theo đường line đen cho đến khi gặp **vạch đen ngang** tiếp theo thì dừng lại.
![Chương trình dò line](/wiki-assets/images/orc_bot/orc-bot/images/9.6.png)


Ngoài ra còn có các khối lệnh di chuyển đến cuối vạch đen, quay cho đến khi gặp vạch đen,... dùng cho các tình huống khác nhau trên sa bàn:
![Các khối lệnh dò line khác](/wiki-assets/images/orc_bot/orc-bot/images/9.7.png)


> **Lưu ý:**
> - Cảm biến phải được cắm vào đúng cổng I2C màu đỏ.
> - Cảm biến phải được tinh chỉnh để phân biệt được nền trắng và vạch đen của sa bàn bạn đang dùng. Nếu đổi sang sa bàn khác hoặc điều kiện ánh sáng thay đổi, hãy tinh chỉnh lại.
> - Nên chạy với tốc độ vừa phải. Tốc độ quá cao khiến robot dễ văng ra khỏi line ở các khúc cua.

## 6. Bài tập mở rộng
1. Lập trình cho robot đi theo line qua **2 vạch ngang** rồi dừng lại và nháy đèn LED màu xanh lá 3 lần.
2. Tại vạch ngang thứ nhất, cho robot **quay phải cho đến khi gặp vạch đen** rồi tiếp tục đi theo line.
3. **Robot không ra khỏi sân:** dán một vòng tròn bằng băng keo đen. Lập trình cho robot đi lung tung bên trong vòng tròn, khi cảm biến thấy vạch đen thì lùi lại và quay hướng khác.

## 7. Câu hỏi ôn tập
1. Vì sao cảm biến dò line phân biệt được màu đen và màu trắng?
2. Cảm biến dò line được cắm vào loại cổng nào trên ORC Control Hub? Vì sao?
3. Kể tên 3 ứng dụng của cảm biến dò line cho robot.
