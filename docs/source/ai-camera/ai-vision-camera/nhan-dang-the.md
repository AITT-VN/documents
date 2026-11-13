# 7. Nhận dạng thẻ (April Tag)

## **Giới thiệu**

**April Tag** là loại thẻ mã hóa dạng 2D (tương tự QR code nhưng đơn giản hơn), được thiết kế đặc biệt cho các ứng dụng robot và thị giác máy tính. Camera có thể nhận diện thẻ và trả về **ID của thẻ** cùng với **vị trí** trong khung hình.

**Ứng dụng tiêu biểu:**
- Robot tự định vị và điều hướng theo thẻ
- Hệ thống kho hàng tự động
- Trò chơi tương tác với thẻ vật lý
- Điều khiển robot bằng thẻ giấy in sẵn

## **April Tag là gì?**

April Tag là các hình vuông đen trắng với mã nhị phân bên trong. Mỗi thẻ mang một **ID duy nhất** (từ 0 đến hàng trăm ID tùy họ thẻ). Bạn có thể in thẻ April Tag miễn phí từ các công cụ online.

## **Các khối lệnh**

| Khối lệnh | Mô tả |
|-----------|-------|
| `đang nhìn thấy thẻ April Tag` | Trả về `True` nếu camera phát hiện thẻ trong khung hình |
| `ID của thẻ April Tag` | Trả về số ID của thẻ đang được nhận diện |
| `tọa độ X của thẻ April Tag` | Trả về tọa độ X của tâm thẻ trong khung hình (0–320) |
| `tọa độ Y của thẻ April Tag` | Trả về tọa độ Y của tâm thẻ trong khung hình (0–240) |

## **Ví dụ chương trình**

**Mô tả:** Robot thực hiện hành động khác nhau tùy theo ID thẻ: thẻ ID=1 → tiến, thẻ ID=2 → lùi, thẻ ID=3 → dừng.

```
khi bắt đầu:
    khởi tạo ai vision camera chân RX [D3] TX [D4]

lặp mãi mãi:
    nếu [đang nhìn thấy thẻ April Tag] thì:
        nếu [ID của thẻ April Tag] = 1 thì:
            đi tiến
        ngược lại nếu [ID của thẻ April Tag] = 2 thì:
            đi lùi
        ngược lại nếu [ID của thẻ April Tag] = 3 thì:
            dừng lại
```

> **Lưu ý:** In thẻ April Tag trên giấy trắng, kích thước tối thiểu 3×3cm để camera nhận diện ổn định ở khoảng cách 20–50cm.
