# Câu hỏi thường gặp

## Câu hỏi thường gặp

Tổng hợp các lưu ý và câu hỏi thường gặp khi thực hiện dự án **Nhà kính thông minh Green House với Yolo UNO**.

---

### 1. Nối dây thiết bị với Relay đúng cách

Khi nối quạt, đèn hoặc máy bơm vào Relay 4 kênh, bạn cần chú ý:

- Relay có **2 đầu kết nối** cho mỗi kênh — phải nối đúng **chiều dây + (dương)** và **− (âm)** của thiết bị.
- Dây **+ (đỏ)** của thiết bị nối vào **cổng COM** hoặc **NO** trên Relay.
- Dây **− (đen)** của thiết bị nối vào **cực âm** của nguồn điện.

> ⚠️ **Quan trọng**: Nếu nối ngược chiều + − của relay, thiết bị (quạt, đèn, máy bơm) **sẽ không hoạt động** hoặc có thể gây hư hỏng. Hãy kiểm tra kỹ **ký hiệu + −** trên relay và thiết bị trước khi cấp nguồn.

**Sơ đồ nối dây tham khảo:**

| Relay kênh | Thiết bị | Ghi chú |
|-----------|---------|---------|
| Relay 3 | Quạt | Đảm bảo nối đúng chiều + − |
| Relay 2 | Đèn kích thích sinh trưởng | Đảm bảo nối đúng chiều + − |
| Relay 4 | Máy bơm nước | Nối đúng chiều + −, kiểm tra IN/OUT máy bơm |

---

### 2. Máy bơm nước không bơm hoặc bơm ngược?

Máy bơm nước có 2 đầu **IN** và **OUT**:

- **IN**: nối ống nước đến **nguồn nước** (hút nước vào)
- **OUT**: đầu **bơm nước ra** từ máy bơm

Nếu nối ngược IN/OUT, nước sẽ bơm ngược hướng. Hãy kiểm tra ký hiệu trên thân máy bơm.

---

### 3. Đèn LED trên mạch Yolo UNO báo hiệu gì?

| Trạng thái đèn | Ý nghĩa |
|----------------|---------|
| 🔴 **Đỏ** | Mạch đang khởi động |
| 🟢 **Xanh lá** | Mạch đã sẵn sàng hoạt động |

Nếu đèn vẫn **đỏ** sau khi nạp chương trình:
- Kiểm tra cáp USB-C kết nối chắc chắn
- Thử nhấn nút **Reset** trên mạch
- Thử rút và cắm lại cáp USB

---

### 4. Cảm biến DHT20 không hiển thị nhiệt độ, độ ẩm?

- Kiểm tra cảm biến đã cắm vào khe mở rộng **I2C** trên Yolo UNO chưa
- Kiểm tra dây tín hiệu có chắc chắn không (thử rút và cắm lại)
- Đảm bảo đã tải đúng thư viện cảm biến trong chương trình

---

### 5. Cảm biến ánh sáng VEML6040 đọc sai giá trị?

- Đảm bảo cảm biến cắm vào khe **I2C** (không cắm vào cổng Analog)
- Không che cảm biến bằng tay khi đang test
- Giá trị ánh sáng dao động từ 0 (tối) đến vài nghìn (sáng) — nên đặt ngưỡng bật/tắt đèn phù hợp với môi trường thực tế

---

### 6. Cảm biến độ ẩm đất cho giá trị ngược?

Cảm biến độ ẩm đất **điện dung** hoạt động ngược so với cảm biến điện trở:

| Giá trị % | Trạng thái đất |
|-----------|---------------|
| **Cao** (trên 70%) | Đất **khô** |
| **Thấp** (dưới 30%) | Đất **ướt** |

> ⚠️ Nên cắm cổng **A0** và kiểm tra giá trị trên Cửa sổ nhập lệnh (Serial Monitor)  hoặc LCD trước khi đặt ngưỡng bật/tắt máy bơm.

---

### 7. Relay 4 kênh không hoạt động?

Kiểm tra theo thứ tự:

1. Relay đã cắm vào khe mở rộng **I2C3** trên Yolo UNO chưa?
2. Đã tải thư viện **Relay 4 kênh** trong OhStem App chưa?
   - Link thư viện: `https://github.com/AITT-VN/yolouno_extension_relay4ch`
3. Nghe tiếng **"tách"** khi relay đóng/mở? Nếu có tiếng nhưng thiết bị không chạy → **kiểm tra lại chiều nối dây + −**
4. Nếu không có tiếng → relay chưa nhận tín hiệu, kiểm tra lại kết nối I2C

---

### 8. Màn hình LCD1602 không hiển thị hoặc mờ?

- Kiểm tra đã cắm vào khe **I2C** chưa
- Thử chỉnh **biến trở** (ốc nhỏ phía sau LCD) để thay đổi độ tương phản
- Nếu màn hình sáng nhưng không hiện chữ → kiểm tra chương trình có khối lệnh ghi dữ liệu lên LCD không

---

### 9. Thiết bị không hoạt động sau khi nạp chương trình?

- Kiểm tra cáp USB-C kết nối chắc chắn
- Đảm bảo đã chọn đúng thiết bị **Yolo UNO** trên OhStem App
- Thử nhấn nút **Reset** trên mạch sau khi nạp
- Kiểm tra nguồn điện đủ cho tất cả module (relay, cảm biến, LCD)
