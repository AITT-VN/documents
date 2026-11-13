# 4. Cảm biến tia UV GUVA-S12SD

## 1. Mục tiêu

Trong bài này, chúng ta sẽ học cách sử dụng cảm biến **GUVA-S12SD** để đo **cường độ tia cực tím (UV)** từ ánh sáng mặt trời. Chỉ số UV là thông tin quan trọng giúp người dân bảo vệ sức khỏe khi ra ngoài trời.

![Cảm biến GUVA-S12SD - Đo cường độ tia UV](/wiki-assets/images/yolo_uno/tram_giam_sat/images/guva_s12sd_sensor.png)


## 2. Giới thiệu cảm biến GUVA-S12SD

### Cảm biến GUVA-S12SD là gì?

**GUVA-S12SD** là cảm biến quang điện chuyên dụng để đo bức xạ tia cực tím (UV) trong dải sóng **240nm - 370nm**. Cảm biến xuất ra tín hiệu analog tỷ lệ thuận với cường độ UV, giúp dễ dàng đo và tính toán chỉ số UV.

### Tia UV là gì?

Tia cực tím (Ultraviolet - UV) là bức xạ điện từ từ mặt trời, chia thành 3 loại:

| Loại | Bước sóng | Đặc điểm |
|------|-----------|----------|
| UVA | 315-400 nm | Xuyên qua mây, gây lão hóa da |
| UVB | 280-315 nm | Gây cháy nắng, ảnh hưởng sức khỏe |
| UVC | 100-280 nm | Bị tầng ozone hấp thụ hoàn toàn |

Cảm biến GUVA-S12SD chủ yếu đo **UVA và UVB**, là hai loại tia cực tím ảnh hưởng trực tiếp đến sức khỏe con người.

### Thông số kỹ thuật

| Thông số | Giá trị |
|----------|---------|
| Điện áp hoạt động | 2.5V - 5V |
| Giao tiếp | Analog |
| Dải sóng nhạy | 240 nm - 370 nm |
| Đỉnh nhạy | 300 nm - 350 nm |
| Tín hiệu đầu ra | 0 - 1V (tương ứng UV Index 0-11+) |
| Dòng tiêu thụ | < 1 mA |
| Thời gian phản hồi | < 0.5 giây |


## 3. Kết nối

Cảm biến GUVA-S12SD sử dụng tín hiệu **Analog**, kết nối vào cổng analog trên Yolo UNO:

| GUVA-S12SD | Yolo UNO |
|------------|----------|
| VCC | 3.3V hoặc 5V |
| GND | GND |
| OUT (Signal) | A0 |

Kết nối cảm biến GUVA-S12SD vào cổng **A0** trên Yolo UNO như hình dưới:
![uv 02](/wiki-assets/images/yolo_uno/yolo_uno_khoi_lenh/cam_bien/images/uv_02.png)

> **Lưu ý:** Đặt cảm biến hướng lên trời để nhận ánh sáng mặt trời trực tiếp. Không che chắn mặt cảm biến.


## 4. Giới thiệu khối lệnh

Để lập trình, bạn cần tải thư viện mở rộng **Smart City** từ liên kết sau:
> `https://github.com/AITT-VN/yolouno_extension_smartcity.git`

*(Xem hướng dẫn thêm thư viện mở rộng [tại đây](https://docs.ohstem.vn/en/latest/module/thu-vien-yolobit.html) hoặc dán đường link trên vào ô tìm kiếm thư viện mở rộng như hình dưới)*
![minh họa tải thư viện](/wiki-assets/images/yolo_uno/yolo_uno_khoi_lenh/cam_bien/images/acd1100_04.png)



## 5. Viết chương trình

### Chương trình cơ bản: Đo và hiển thị chỉ số UV

**Mô tả chương trình:**
- Sử dụng khối lệnh từ thư viện Smart City để đọc chỉ số UV.
- Cập nhật hiển thị lên màn hình LCD mỗi 1 giây (hoặc 3 giây).


![uv 3](/wiki-assets/images/yolo_uno/yolo_uno_khoi_lenh/cam_bien/images/uv_3.png)

### Bảng phân loại mức độ tia UV (theo WHO)

| Chỉ số UV | Mức độ | Khuyến cáo |
|-----------|--------|------------|
| 0-2 | 🟢 Thấp | An toàn, không cần bảo vệ đặc biệt |
| 3-5 | 🟡 Trung bình | Đội mũ, sử dụng kem chống nắng SPF 30+ |
| 6-7 | 🟠 Cao | Hạn chế ra ngoài 10h-14h, dùng kem SPF 50+ |
| 8-10 | 🔴 Rất cao | Tránh ra ngoài khi không cần thiết |
| 11+ | 🟣 Cực cao | Cực kỳ nguy hiểm, ở trong nhà |

### Chương trình nâng cao: Cảnh báo mức UV

Thêm tính năng cảnh báo bằng đèn LED RGB:

1. UV **0-2** → LED **xanh lá** + LCD hiển thị **"UV: Thap - An toan"**
2. UV **3-5** → LED **vàng** + LCD hiển thị **"UV: TB - Doi mu"**
3. UV **6-7** → LED **cam** + LCD hiển thị **"UV: Cao - Han che"**
4. UV **8-10** → LED **đỏ** + LCD hiển thị **"UV: Rat cao!"**
5. UV **11+** → LED **đỏ nhấp nháy** + LCD hiển thị **"UV: NGUY HIEM!"**


## 6. Kiến thức mở rộng

### Tại sao chỉ số UV thay đổi trong ngày?

Cường độ tia UV phụ thuộc vào nhiều yếu tố:

- **Thời gian trong ngày:** UV mạnh nhất từ 10h - 14h khi mặt trời ở đỉnh.
- **Mùa trong năm:** UV mạnh hơn vào mùa hè.
- **Mây:** Mây dày có thể giảm 50-80% UV, nhưng mây mỏng chỉ giảm rất ít.
- **Phản xạ:** Mặt nước, cát và tuyết phản xạ UV, tăng cường tiếp xúc.

### Thí nghiệm thú vị

Đo chỉ số UV vào các thời điểm khác nhau trong ngày (8h, 10h, 12h, 14h, 16h) và lập bảng so sánh:

| Thời gian | Chỉ số UV | Mức độ |
|-----------|-----------|--------|
| 8:00 | ? | ? |
| 10:00 | ? | ? |
| 12:00 | ? | ? |
| 14:00 | ? | ? |
| 16:00 | ? | ? |

> **Thử thách:** Em hãy đo chỉ số UV ở ngoài trời và dưới tán cây. So sánh kết quả để thấy hiệu quả của việc trồng cây xanh trong thành phố!
