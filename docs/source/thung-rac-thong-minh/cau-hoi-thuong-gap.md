# Câu hỏi thường gặp

## Câu hỏi thường gặp

Tổng hợp các lưu ý và câu hỏi thường gặp khi thực hiện dự án **Thùng rác thông minh với Yolo UNO**.

---

### 1. Làm sao để thay đổi thông tin WiFi cho camera AI?

Để thay đổi mạng WiFi:

1. **Xóa WiFi cũ**: Nhấn giữ **nút Boot** trên camera (cạnh đèn LED) trong **5 giây**. Khi đèn chuyển từ **xanh sang đỏ**, WiFi cũ đã được xóa.
2. **Kết nối WiFi mới**: Dùng điện thoại/laptop tìm mạng WiFi có tên `ohstem-ai-camera-xxxxx`, sau đó truy cập `192.168.4.1` và nhập thông tin WiFi mới.

> ⚠️ **Lưu ý**: Camera AI và laptop/điện thoại phải kết nối **chung 1 mạng WiFi**.

---

### 2. Kiểm tra trạng thái WiFi qua đèn LED trên camera

| Màu đèn LED | Trạng thái |
|-------------|-----------|
| 🔴 **Đỏ** | Camera chưa kết nối WiFi |
| 🟢 **Xanh lá** | Camera đã kết nối WiFi thành công |

Nếu đèn vẫn **đỏ** sau khi nhập WiFi, hãy kiểm tra:
- Tên và mật khẩu WiFi có đúng không
- Mạng WiFi có hoạt động bình thường không (thử kết nối bằng thiết bị khác)
- Mạng WiFi có phải băng tần **2.4GHz** (camera không hỗ trợ 5GHz)

---

### 3. Kiểm tra trạng thái đèn LED trên mạch Yolo UNO

Khi lập trình kết nối IoT:

| Trạng thái đèn | Ý nghĩa |
|----------------|---------|
| 🔴 **Đỏ** | Yolo UNO đang khởi động, chưa kết nối WiFi |
| 🟢 **Xanh** | Đã kết nối WiFi và bảng điều khiển IoT thành công |

Nếu đèn vẫn đỏ sau 10-15 giây:
- Kiểm tra tên và mật khẩu WiFi trong chương trình
- Đảm bảo WiFi là băng tần **2.4GHz**
- Kiểm tra username của bảng điều khiển IoT có đúng không

---

### 4. Camera AI không nhận dạng được vật thể?

Kiểm tra các điểm sau:
- Đã bấm **"Bật camera"** trên trang IP của camera chưa?
- **Link mô hình AI** đã được dán đúng vào ô cấu hình chưa?
- **Độ chính xác** có đặt quá cao không? Thử giảm xuống 60-70%
- Tab trình duyệt xử lý camera **không được ẩn** (phải mở song song)

---

### 5. Không lấy được địa chỉ IP của camera?

- Sau khi camera kết nối WiFi (đèn xanh), kiểm tra danh sách WiFi trên laptop — sẽ thấy mạng có tên dạng `192.168.x.xxx - cam - id`
- **Không kết nối** vào mạng WiFi đó, chỉ xem để lấy IP
- Mở Chrome gõ IP này vào thanh địa chỉ để truy cập camera

---

### 6. Cấu hình IoT cho camera gửi kết quả nhận dạng

Trong phần **Cài đặt nâng cao** trên trang IP camera:
- **Server**: chọn OhStem
- **User**: điền username bảng điều khiển IoT
- **Kênh dữ liệu**: chọn kênh V1–V20 phù hợp
- **Tần suất gửi**: nên đặt 5-10 giây

> ⚠️ Đảm bảo **tab camera**  mở cùng khi thiết bị hoạt động.

---

### 7. Thiết bị không hoạt động sau khi nạp chương trình?

- Kiểm tra cáp USB-C có kết nối chắc chắn không
- Thử rút và cắm lại cáp USB
- Kiểm tra nguồn điện cho mạch và các module
- Đảm bảo đã chọn đúng thiết bị **Yolo UNO** trên OhStem App trước khi nạp
