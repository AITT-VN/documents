# 1. Giới thiệu & Kết nối

## **Giới thiệu**

**AI Vision Camera** là module camera thông minh tích hợp chip AI Kendryte K210, cho phép thực hiện các tác vụ nhận diện hình ảnh trực tiếp trên thiết bị mà không cần kết nối internet. Module tích hợp sẵn 8 chức năng AI:

- Nhận dạng khuôn mặt
- Theo dõi đối tượng
- Nhận dạng đối tượng
- Theo dõi đường thẳng
- Nhận dạng màu sắc
- Nhận dạng thẻ (April Tag)
- Đọc mã QR

Module giao tiếp với bo mạch chủ qua giao thức **UART (TX/RX)**, dễ dàng tích hợp với Yolo:Bit, Yolo UNO và các bo mạch khác.

## **Thông số kỹ thuật**

| Thông số | Giá trị |
|----------|---------|
| Chip xử lý | Esp32s3 N16R8 |
| Cảm biến hình ảnh | OV2640 |
| Điện áp hoạt động | 3.3V – 5.0V |
| Tiêu thụ dòng điện | 320mA @ 3.3V / 230mA @ 5.0V |
| Màn hình tích hợp | OLED 2.0 inch, 320×240 |
| Giao tiếp | UART |
| Kết nối | Cổng Grove (4 chân) |
| Kích thước | 52mm × 44.5mm |

## **Kết nối phần cứng**

Kết nối AI Vision Camera với bo mạch chủ qua cổng **UART**:

- Chân **RX** của camera → chân **TX** của bo mạch
- Chân **TX** của camera → chân **RX** của bo mạch

Ví dụ kết nối với Yolo:Bit (chân D3/D4):

| Camera | Yolo:Bit |
|--------|----------|
| RX | D4 |
| TX | D3 |
| VCC | 3.3V |
| GND | GND |

## **Khởi tạo trong chương trình**

Trước khi sử dụng bất kỳ chức năng nào, cần khởi tạo kết nối với camera bằng khối lệnh:

```
khởi tạo ai vision camera chân RX [D3] TX [D4]
```

| Tham số | Mô tả |
|---------|-------|
| RX | Chân nhận dữ liệu của bo mạch (ví dụ: D3) |
| TX | Chân gửi dữ liệu của bo mạch (ví dụ: D4) |

> **Lưu ý:** Đặt khối khởi tạo này ở đầu chương trình, trong khối `khi bắt đầu`.
