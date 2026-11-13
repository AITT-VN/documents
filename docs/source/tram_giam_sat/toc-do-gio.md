# 7. Đo tốc độ gió

## 1. Mục tiêu

Trong bài này, chúng ta sẽ học cách đo **tốc độ gió** bằng cảm biến gió (anemometer) kết hợp với Yolo UNO. Tốc độ gió là yếu tố quan trọng trong dự báo thời tiết, đánh giá ô nhiễm không khí và quản lý năng lượng trong thành phố thông minh.

![Cảm biến đo tốc độ gió](/wiki-assets/images/yolo_uno/tram_giam_sat/images/wind_speed_sensor.png)


## 2. Giới thiệu về đo tốc độ gió

### Tại sao cần đo tốc độ gió?

Trong thành phố thông minh, dữ liệu tốc độ gió phục vụ nhiều mục đích:

- **Dự báo thời tiết:** Gió mạnh có thể dự báo mưa bão.
- **Quản lý ô nhiễm:** Gió giúp phân tán bụi mịn và khí ô nhiễm.
- **Năng lượng gió:** Đánh giá tiềm năng lắp đặt tuabin gió mini.
- **An toàn:** Cảnh báo gió mạnh nguy hiểm cho người đi đường.
- **Quy hoạch đô thị:** Thiết kế tòa nhà và đường phố tối ưu luồng gió.

### Các phương pháp đo tốc độ gió

| Phương pháp | Nguyên lý | Phù hợp với |
|-------------|-----------|-------------|
| Cánh quạt (Cup Anemometer) | Đếm vòng quay cánh quạt | Trạm thời tiết chuyên nghiệp |
| Cánh gạt (Vane Anemometer) | Đo lực gió tác động lên cánh | Đo gió trong ống dẫn |
| Siêu âm (Ultrasonic) | Đo thời gian truyền sóng âm | Nghiên cứu chính xác cao |
| Đơn giản (DIY) | Cảm biến analog + cánh quạt tự chế | **Dự án STEM học sinh** |

### Cảm biến gió Analog

Trong dự án này, chúng ta sử dụng cảm biến gió analog (hoặc module đo tốc độ gió) xuất tín hiệu điện áp tỷ lệ thuận với tốc độ gió:

| Thông số | Giá trị |
|----------|---------|
| Điện áp hoạt động | 10-30V |
| Tín hiệu đầu ra | Analog (0 - 5V) |
| Dải đo | 0 - 60 m/s |
| Độ phân giải | 0.1 m/s |
| Giao tiếp | Analog |


## 3. Kết nối

Cảm biến gió kết nối vào mạch chuyển đổi tín hiệu, sau đó nối vào cổng Analog **A1** trên Yolo UNO:


> **Lưu ý:**
> - Đặt cảm biến ở vị trí cao, thoáng gió, không bị che chắn.
> - Cánh quạt cần quay tự do, không bị vướng.
> - Nếu sử dụng cảm biến tự chế, cần hiệu chuẩn trước khi sử dụng.


## 4. Công thức tính tốc độ gió

### Từ giá trị Analog sang tốc độ gió

Với cảm biến gió analog, công thức quy đổi như sau:

**Bước 1:** Đọc giá trị ADC (0-4095 với ESP32)

**Bước 2:** Chuyển sang điện áp:
> **Điện áp (V) = Giá trị ADC × 3.3 / 4095**

**Bước 3:** Chuyển sang tốc độ gió:
> **Tốc độ gió (m/s) = Điện áp × Hệ số quy đổi**

Hệ số quy đổi phụ thuộc vào loại cảm biến, thông thường:
- Với cảm biến 0-5V, dải 0-30 m/s: **Hệ số = 6.0**
- Với cảm biến 0-3.3V, dải 0-30 m/s: **Hệ số = 9.09**

### Quy đổi đơn vị tốc độ gió

| Từ | Sang | Công thức |
|----|------|-----------|
| m/s | km/h | × 3.6 |
| m/s | mph | × 2.237 |
| m/s | knot | × 1.944 |
| km/h | m/s | ÷ 3.6 |


## 5. Giới thiệu khối lệnh

- Sử dụng khối lệnh **đọc chân Analog A1** để đọc giá trị thô từ cảm biến.

- Sử dụng các khối lệnh **tính toán** để quy đổi sang tốc độ gió (m/s) và km/h.

- Có thể tạo **biến** (variable) để lưu giá trị tốc độ gió và sử dụng trong các điều kiện cảnh báo.


## 6. Viết chương trình

### Chương trình cơ bản: Đo và hiển thị tốc độ gió

**Các bước thực hiện:**

1. **Khai báo biến:** Tạo biến `tocDoGio` để lưu giá trị tốc độ gió.

2. **Đọc và tính toán:** Sử dụng khối lệnh **"Sau mỗi 2 giây thực hiện"**:
   - Đọc giá trị Analog từ chân A1
   - Tính điện áp: `dienAp = analogRead(A1) * 3.3 / 4095`
   - Tính tốc độ gió: `tocDoGio = dienAp * 9.09` (m/s)
   - Tính km/h: `tocDoGioKmh = tocDoGio * 3.6`

3. **Hiển thị lên LCD:**
   - Hàng 1: **"Gio: X.X m/s"**
   - Hàng 2: **"(XX.X km/h)"**

### Thang phân loại gió Beaufort

| Cấp | Tốc độ (m/s) | Tốc độ (km/h) | Mô tả | Biểu hiện |
|-----|-------------|---------------|-------|-----------|
| 0 | 0-0.2 | 0-1 | Gió lặng | Khói bay thẳng lên |
| 1 | 0.3-1.5 | 1-5 | Gió rất nhẹ | Khói hơi nghiêng |
| 2 | 1.6-3.3 | 6-11 | Gió nhẹ | Lá cây rung nhẹ |
| 3 | 3.4-5.4 | 12-19 | Gió vừa | Lá và cành nhỏ dao động |
| 4 | 5.5-7.9 | 20-28 | Gió khá mạnh | Bụi bay, cành cây nhỏ dao động |
| 5 | 8.0-10.7 | 29-38 | Gió mạnh | Cây nhỏ dao động |
| 6 | 10.8-13.8 | 39-49 | Gió to | Cành cây lớn dao động, khó cầm ô |
| 7 | 13.9-17.1 | 50-61 | Gió bão | Cây lớn dao động, đi lại khó khăn |
| 8+ | > 17.2 | > 62 | Bão | Gãy cành, tốc mái nhà |

### Chương trình nâng cao: Cảnh báo gió mạnh

Thêm tính năng cảnh báo theo cấp gió:

1. Gió **< 5.5 m/s** (cấp 0-3) → LED **xanh** + LCD: **"Gio nhe"**
2. Gió **5.5-10.7 m/s** (cấp 4-5) → LED **vàng** + LCD: **"Gio manh"**
3. Gió **10.8-17.1 m/s** (cấp 6-7) → LED **cam** + Buzzer + LCD: **"GIO RAT MANH!"**
4. Gió **> 17.2 m/s** (cấp 8+) → LED **đỏ nhấp nháy** + Buzzer liên tục + LCD: **"BAO! CANH BAO!"**


## 7. Kiến thức mở rộng

### Tốc độ gió và ô nhiễm không khí

Tốc độ gió ảnh hưởng trực tiếp đến mức độ ô nhiễm:

| Tốc độ gió | Ảnh hưởng đến ô nhiễm |
|------------|----------------------|
| < 1 m/s | Ô nhiễm tích tụ, PM2.5 tăng cao |
| 1-3 m/s | Ô nhiễm giảm chậm |
| 3-5 m/s | Phân tán tốt, không khí sạch hơn |
| > 5 m/s | Phân tán nhanh nhưng có thể cuốn bụi |

### Năng lượng gió

Công suất gió tỷ lệ với **lũy thừa bậc 3** của tốc độ gió:

**P = 0.5 × ρ × A × V³**

Trong đó:
- **P:** Công suất (Watt)
- **ρ:** Mật độ không khí (≈ 1.225 kg/m³)
- **A:** Diện tích quét cánh quạt (m²)
- **V:** Tốc độ gió (m/s)

Điều này có nghĩa: gió mạnh gấp đôi → năng lượng tăng **8 lần**!

> **Thử thách:** Em hãy đo tốc độ gió tại 3 vị trí khác nhau trong trường (sân trống, hành lang, gần tòa nhà) và giải thích sự khác biệt. Vị trí nào phù hợp nhất để đặt tuabin gió mini?
