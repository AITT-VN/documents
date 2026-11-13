# 8. Giám sát năng lượng mặt trời

## 1. Mục tiêu

Trong bài này, chúng ta sẽ học cách sử dụng Yolo UNO để **giám sát hiệu suất của tấm pin năng lượng mặt trời**. Dự án giúp theo dõi điện áp, ước tính công suất và hiểu rõ hơn về năng lượng tái tạo trong thành phố thông minh.

![Giám sát năng lượng mặt trời](/wiki-assets/images/yolo_uno/tram_giam_sat/images/solar_energy_monitor.png)


## 2. Giới thiệu về năng lượng mặt trời

### Năng lượng mặt trời là gì?

Năng lượng mặt trời là năng lượng được chuyển đổi từ ánh sáng mặt trời sang điện năng thông qua **tấm pin quang điện (Solar Panel)**:

- ♻️ **Tái tạo:** Không bao giờ cạn kiệt
- 🌿 **Sạch:** Không phát thải CO2 khi hoạt động
- 🔇 **Im lặng:** Không gây tiếng ồn
- 💰 **Tiết kiệm:** Giảm chi phí điện lâu dài

### Ứng dụng trong thành phố thông minh

- **Đèn đường năng lượng mặt trời:** Tiết kiệm điện chiếu sáng công cộng.
- **Trạm sạc điện thoại:** Cung cấp điện miễn phí tại công viên, bến xe.
- **Giám sát môi trường:** Cấp điện cho các trạm cảm biến IoT ở xa lưới điện.
- **Tòa nhà xanh:** Lắp pin mặt trời trên mái nhà giảm phát thải carbon.


## 3. Thành phần cần chuẩn bị

| STT | Linh kiện | Số lượng | Mô tả |
|-----|-----------|----------|-------|
| 1 | Tấm pin năng lượng mặt trời (5V) | 1 | Loại nhỏ 5V/1W |
| 2 | Module đo điện áp hoặc 2 điện trở 10kΩ | 1 | Tạo mạch chia áp |
| 3 | Yolo UNO | 1 | Bo mạch điều khiển |
| 4 | Màn hình LCD 1602 | 1 | Hiển thị thông số |

### Mạch chia áp (Voltage Divider)

Dùng 2 điện trở 10kΩ tạo bộ chia áp:

```
Pin mặt trời (+) ── R1 (10kΩ) ──┬── R2 (10kΩ) ── GND
                                  │
                                  └── Chân A2 (Yolo UNO)
```

> **V_out = V_in × R2 / (R1 + R2) = V_in / 2**

Nếu pin xuất 5V → chân A2 nhận 2.5V (an toàn cho ESP32).


## 4. Kết nối

| Linh kiện | Chân | Yolo UNO |
|-----------|------|----------|
| Pin mặt trời (qua chia áp) | Signal | A2 |
| Pin mặt trời (-) | GND | GND |
| Màn hình LCD | I2C | I2C1 |

> **⚠️ KHÔNG nối trực tiếp điện áp > 3.3V vào chân Analog. PHẢI dùng bộ chia áp.**


## 5. Công thức tính toán

### Tính điện áp pin mặt trời

> **V_A2 = ADC × 3.3 / 4095**
>
> **V_pin = V_A2 × 2** (qua bộ chia áp 1:2)

### Ước tính hiệu suất

> **Hiệu suất (%) = (V_pin / 5.0) × 100**


## 6. Viết chương trình

### Chương trình cơ bản: Hiển thị điện áp pin mặt trời

1. **Khai báo biến:** `dienApPin`, `hieuSuat`

2. **Đọc và tính toán** (mỗi 3 giây):
   - `dienApPin = analogRead(A2) * 3.3 / 4095 * 2`
   - `hieuSuat = dienApPin / 5.0 * 100`

3. **Hiển thị LCD:**
   - Hàng 1: **"Solar: X.XX V"**
   - Hàng 2: **"Hieu suat: XX%"**

### Bảng hiệu suất và điều kiện ánh sáng

| Điện áp | Hiệu suất | Điều kiện |
|---------|-----------|-----------|
| 4.5-5.0V | 90-100% | ☀️ Nắng gắt |
| 3.5-4.5V | 70-90% | 🌤️ Nắng nhẹ |
| 2.0-3.5V | 40-70% | ⛅ Nhiều mây |
| 1.0-2.0V | 20-40% | 🌥️ Trời âm u |
| < 1.0V | < 20% | 🌧️ Mưa / Tối |

### Chương trình nâng cao: Dashboard năng lượng

Thêm đèn LED chỉ thị:

1. Hiệu suất **> 70%** → LED **xanh** + **"NANG LUONG: TOT"**
2. Hiệu suất **40-70%** → LED **vàng** + **"NANG LUONG: TB"**
3. Hiệu suất **< 40%** → LED **đỏ** + **"NANG LUONG: YEU"**


## 7. Kiến thức mở rộng

### Yếu tố ảnh hưởng hiệu suất

| Yếu tố | Ảnh hưởng | Khắc phục |
|---------|-----------|-----------|
| Góc nghiêng | Pin nên hướng Nam | Điều chỉnh theo mùa |
| Bóng râm | Giảm 30-50% | Tránh cây, tòa nhà |
| Nhiệt độ | +1°C → -0.4% | Thông gió phía sau |
| Bụi bẩn | Giảm 5-25% | Vệ sinh định kỳ |

### So sánh nguồn năng lượng

| Nguồn | CO2 (g/kWh) | Tái tạo |
|-------|------------|---------|
| Than đá | 820 | ❌ |
| Khí tự nhiên | 490 | ❌ |
| Mặt trời | 41 | ✅ |
| Gió | 11 | ✅ |
| Thủy điện | 24 | ✅ |

> **Thử thách:** Đo điện áp pin mặt trời mỗi giờ từ 7h-17h. Vẽ biểu đồ và xác định giờ nào cho hiệu suất cao nhất!
