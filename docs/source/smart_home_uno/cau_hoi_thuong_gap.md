# Câu hỏi thường gặp

## Câu hỏi thường gặp

Tổng hợp các lưu ý và câu hỏi thường gặp khi thực hiện dự án **Nhà thông minh với Yolo UNO**.

---

### 1. Làm sao để thay đổi thông tin WiFi trong chương trình?

Trong khối lệnh kết nối WiFi trên OhStem App, bạn cần thay đổi:

- **Tên WiFi**: nhập đúng tên mạng WiFi (phân biệt hoa thường)
- **Mật khẩu WiFi**: nhập đúng mật khẩu

> ⚠️ **Lưu ý quan trọng**:
> - WiFi phải là băng tần **2.4GHz** (Yolo UNO không hỗ trợ 5GHz)
> - Tên WiFi **không nên có ký tự đặc biệt** hoặc khoảng trắng
> - Máy tính/điện thoại và Yolo UNO phải kết nối **cùng 1 mạng WiFi**

---

### 2. Kiểm tra kết nối WiFi qua đèn LED trên mạch

Khi chương trình được nạp và Yolo UNO khởi động:

| Trạng thái đèn LED trên board | Ý nghĩa |
|-------------------------------|---------|
| 🔴 **Đỏ** | Đang khởi động, chưa kết nối WiFi |
| 🟢 **Xanh** | Đã kết nối WiFi và bảng điều khiển IoT thành công |

**Nếu đèn vẫn đỏ sau 10-15 giây**, hãy kiểm tra:
1. Tên và mật khẩu WiFi có đúng chính xác không
2. Mạng WiFi có hoạt động bình thường không
3. Thử đưa mạch lại gần router WiFi hơn
4. Kiểm tra **username** của bảng điều khiển IoT

---

### 3. Kiểm tra mạng WiFi có phù hợp không?

Yolo UNO chỉ hỗ trợ **WiFi 2.4GHz**. Để kiểm tra:

- Nếu router phát cả 2.4GHz và 5GHz, đảm bảo bạn đang kết nối vào mạng **2.4GHz**
- Nếu dùng điểm phát sóng từ điện thoại (hotspot), mặc định sẽ là 2.4GHz
- Tránh dùng mạng WiFi công cộng (captive portal) vì Yolo UNO không thể xác thực qua trang web

---

### 4. Cảm biến DHT20 không hiển thị giá trị?

- Kiểm tra cảm biến đã cắm vào cổng **I2C** trên Yolo UNO chưa
- Kiểm tra dây tín hiệu có chắc chắn không (thử rút và cắm lại)
- Đảm bảo đã chọn đúng loại cảm biến **DHT20** trong khối lệnh (không phải DHT11 hay DHT22)

---

### 5. Đèn LED RGB không sáng?

- Kiểm tra module 4 LED RGB đã cắm vào đúng chân **D9-D10** chưa
- Kiểm tra chương trình đã có khối lệnh điều khiển LED chưa
- Thử đổi dây kết nối hoặc đổi cổng khác trên Yolo UNO

---

### 6. Quạt mini không hoạt động?

- Kiểm tra module quạt đã cắm vào đúng chân **D7-D8** chưa
- Quạt mini cần nguồn điện đủ — đảm bảo cáp USB kết nối ổn định
- Thử nạp chương trình đơn giản để kiểm tra quạt riêng trước khi kết hợp IoT

---

### 7. Bảng điều khiển IoT không nhận dữ liệu?

Kiểm tra theo thứ tự:

1. **Đèn LED xanh** trên Yolo UNO → WiFi và IoT đã kết nối
2. **Username** trong chương trình khớp với username trên bảng điều khiển
3. **Kênh thông tin** (V1, V2, V3...) phải đúng giữa chương trình và bảng điều khiển
4. Mở bảng điều khiển và đợi ít nhất **5-10 giây** để dữ liệu đầu tiên xuất hiện

---

### 8. Không thể điều khiển thiết bị từ bảng điều khiển IoT?

- Kiểm tra widget trên bảng điều khiển đã gán đúng **kênh thông tin** (V3 cho đèn, V4 cho quạt...)
- Đảm bảo chương trình có khối lệnh **nhận thông tin từ kênh dữ liệu**
- Thử tắt/bật lại widget và quan sát Serial Monitor để debug

---

### 9. Thiết bị không hoạt động sau khi nạp chương trình?

- Kiểm tra cáp USB-C có kết nối chắc chắn không
- Thử rút và cắm lại cáp USB
- Kiểm tra nguồn điện cho mạch và các module
- Đảm bảo đã chọn đúng thiết bị **Yolo UNO** trên OhStem App trước khi nạp
- Thử nhấn nút Reset trên mạch
