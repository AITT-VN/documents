# 3. Cảm biến nhiệt độ & độ ẩm DHT20

## 1. Mục tiêu

Trong bài này, chúng ta sẽ học cách sử dụng cảm biến **DHT20** để đo **nhiệt độ** và **độ ẩm** không khí. Đây là thông số quan trọng nhất trong giám sát môi trường đô thị, ảnh hưởng trực tiếp đến sức khỏe và sinh hoạt của người dân.

![Cảm biến DHT20](/wiki-assets/images/yolo_uno/yolo_uno_khoi_lenh/cam_bien/images/dht20.png)


## 2. Giới thiệu cảm biến DHT20

Cảm biến nhiệt độ và độ ẩm DHT20 sử dụng giao thức đầu ra là **I2C**. Cảm biến có độ chính xác cao, giá thành thấp, thích hợp với các ứng dụng cần đo nhiệt độ, độ ẩm của môi trường.

### Thông số kỹ thuật

| Thông số | Giá trị |
|----------|---------|
| Điện áp đầu vào | 3.3V |
| Tín hiệu đầu ra | I2C |
| Dải đo nhiệt độ | -40°C ~ +80°C |
| Độ chính xác nhiệt độ | ±0.5°C |
| Dải đo độ ẩm | 0 ~ 100% RH |
| Độ chính xác độ ẩm | ±3% RH (25°C) |

### Ứng dụng trong thành phố thông minh

- **Giám sát chất lượng sống:** Đo nhiệt độ, độ ẩm tại các khu dân cư.
- **Quản lý năng lượng:** Khi nhiệt độ cao, hệ thống tự động kích hoạt quạt thông gió hoặc hệ thống làm mát.
- **Bảo vệ sức khỏe:** Cảnh báo khi nhiệt độ quá cao hoặc chỉ số nhiệt (Heat Index) đạt mức nguy hiểm.


## 3. Kết nối

Kết nối cảm biến DHT20 vào cổng **I2C2** trên Yolo UNO:

![Kết nối DHT20 với Yolo UNO](/wiki-assets/images/yolo_uno/yolo_uno_khoi_lenh/cam_bien/images/dht20_1.png)

> **Lưu ý:** Tránh đặt cảm biến DHT20 gần nguồn nhiệt (mạch điện, động cơ...) để đảm bảo kết quả đo chính xác.


## 4. Giới thiệu khối lệnh

Để lập trình DHT20, bạn cần tải thư viện mở rộng từ liên kết sau:
> `https://github.com/AITT-VN/yolouno_extension_smartcity.git`

*(Xem hướng dẫn thêm thư viện mở rộng [tại đây](https://docs.ohstem.vn/en/latest/module/thu-vien-yolobit.html) hoặc dán đường link trên vào ô tìm kiếm thư viện mở rộng như hình dưới)*

![minh họa tải thư viện](/wiki-assets/images/yolo_uno/yolo_uno_khoi_lenh/cam_bien/images/acd1100_04.png)

Sau khi tải thư viện, các khối lệnh đọc DHT20 sẽ xuất hiện:

![Khối lệnh DHT20](/wiki-assets/images/yolo_uno/yolo_uno_khoi_lenh/cam_bien/images/dht20_2.png)


## 5. Viết chương trình

### Chương trình cơ bản: Hiển thị nhiệt độ và độ ẩm

Đọc dữ liệu từ cảm biến DHT20 và hiển thị lên màn hình LCD:

![Chương trình DHT20](/wiki-assets/images/yolo_uno/yolo_uno_khoi_lenh/cam_bien/images/dht20_3.png)

### Bảng phân loại mức độ thoải mái

| Nhiệt độ | Độ ẩm | Mức độ |
|-----------|-------|--------|
| 20–25°C | 40–60% | 😊 Rất thoải mái |
| 25–30°C | 40–70% | 🙂 Thoải mái |
| 30–35°C | > 60% | 😓 Nóng, oi bức |
| > 35°C | > 70% | 🥵 Rất nóng, nguy hiểm |
| < 18°C | < 30% | 🥶 Lạnh, khô |

### Chương trình nâng cao: Chỉ số nhiệt (Heat Index)

Chỉ số nhiệt (Heat Index) kết hợp nhiệt độ và độ ẩm để cho biết cảm giác nhiệt thực tế. Ví dụ: khi nhiệt độ 32°C và độ ẩm 70%, cảm giác thực tế có thể lên đến 41°C!

**Cách tính đơn giản:**

Nếu nhiệt độ ≥ 27°C và độ ẩm ≥ 40%:

**Heat Index ≈ Nhiệt độ + (Độ ẩm × 0.1)**

Thêm tính năng cảnh báo:
1. Heat Index **< 32°C** → Hiển thị **"An toan"** (đèn LED xanh)
2. Heat Index **32–40°C** → Hiển thị **"Than trong!"** (đèn LED vàng)
3. Heat Index **> 40°C** → Hiển thị **"Nguy hiem!"** (đèn LED đỏ)


## 6. Kiến thức mở rộng

### Điểm sương (Dew Point)

Điểm sương là nhiệt độ mà tại đó hơi nước trong không khí bắt đầu ngưng tụ thành sương. Công thức ước lượng:

**Điểm sương ≈ Nhiệt độ - ((100 - Độ ẩm) / 5)**

| Điểm sương | Cảm giác |
|------------|----------|
| < 10°C | Khô ráo, dễ chịu |
| 10–15°C | Thoải mái |
| 16–18°C | Hơi ẩm |
| 19–21°C | Ẩm, khó chịu |
| > 21°C | Rất ẩm, ngột ngạt |

> **Thử thách:** Em hãy đặt cảm biến DHT20 ở các vị trí khác nhau (trong nhà, ngoài trời, gần cửa sổ) và so sánh nhiệt độ, độ ẩm. Ghi nhận kết quả trong 1 ngày và vẽ biểu đồ thay đổi!
