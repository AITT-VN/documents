# 3. Theo dõi đối tượng

## **Giới thiệu**

Chức năng theo dõi đối tượng cho phép camera liên tục bám theo một vật thể được chỉ định trước, trả về tọa độ và kích thước của vật thể trong khung hình theo thời gian thực.

**Ứng dụng tiêu biểu:**
- Robot tự động bám theo người hoặc vật thể
- Hệ thống camera xoay theo mục tiêu
- Điều khiển robot tránh vật cản thông minh

## **Hướng dẫn dạy camera theo dõi đối tượng**

1. Nhấn nút **Learning** trên camera
2. Đưa vật thể cần theo dõi vào giữa khung hình
3. Camera sẽ ghi nhớ màu sắc và hình dạng của vật thể đó
4. Sau khi lưu, camera sẽ tự động bám theo vật thể trong khung hình

## **Các khối lệnh**

| Khối lệnh | Mô tả |
|-----------|-------|
| `tọa độ X của đối tượng theo dõi` | Trả về tọa độ X của vật thể trong khung hình (0–320) |
| `tọa độ Y của đối tượng theo dõi` | Trả về tọa độ Y của vật thể trong khung hình (0–240) |
| `chiều rộng của đối tượng theo dõi` | Trả về chiều rộng vùng bao quanh vật thể (pixel) |
| `chiều cao của đối tượng theo dõi` | Trả về chiều cao vùng bao quanh vật thể (pixel) |
| `đang theo dõi đối tượng` | Trả về `True` nếu camera đang nhìn thấy vật thể cần theo dõi |

## **Ví dụ chương trình**

**Mô tả:** Robot điều chỉnh hướng di chuyển để bám theo vật thể, căn chỉnh dựa vào tọa độ X của đối tượng so với tâm màn hình (160).

```
khi bắt đầu:
    khởi tạo ai vision camera chân RX [D3] TX [D4]

lặp mãi mãi:
    nếu [đang theo dõi đối tượng] thì:
        nếu [tọa độ X của đối tượng theo dõi] < 140 thì:
            rẽ trái
        ngược lại nếu [tọa độ X của đối tượng theo dõi] > 180 thì:
            rẽ phải
        ngược lại:
            đi thẳng
    ngược lại:
        dừng lại
```

> **Lưu ý:** Tọa độ trung tâm màn hình là X=160, Y=120. Khoảng "chết" (140–180) giúp robot không rung lắc khi vật thể gần trung tâm.
