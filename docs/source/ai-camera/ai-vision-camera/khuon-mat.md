# 2. Nhận dạng khuôn mặt

## **Giới thiệu**

Chức năng nhận dạng khuôn mặt cho phép camera học và ghi nhớ khuôn mặt của người dùng. Sau khi lưu khuôn mặt, camera có thể phân biệt được khuôn mặt **đã lưu** và khuôn mặt **lạ (chưa lưu)**.

**Ứng dụng tiêu biểu:**
- Khóa cửa thông minh nhận dạng khuôn mặt
- Hệ thống điểm danh tự động
- Cảnh báo khi phát hiện người lạ xâm nhập

## **Hướng dẫn lưu khuôn mặt trên camera**

Trước khi lập trình, cần dạy camera nhận diện khuôn mặt trực tiếp trên thiết bị:

1. Nhấn nút **Learning** trên camera
2. Hướng camera vào khuôn mặt cần lưu trong khoảng cách 30–50cm
3. Giữ nguyên cho đến khi màn hình xác nhận đã lưu thành công
4. Có thể lưu nhiều khuôn mặt khác nhau (mỗi khuôn mặt một ID)

## **Các khối lệnh**

| Khối lệnh | Mô tả |
|-----------|-------|
| `phát hiện khuôn mặt đã lưu` | Trả về `True` nếu camera nhận ra khuôn mặt đã được lưu trước đó |
| `phát hiện khuôn mặt lạ (chưa lưu)` | Trả về `True` nếu camera phát hiện khuôn mặt chưa có trong cơ sở dữ liệu |

## **Ví dụ chương trình**

**Mô tả:** Khi camera nhận ra khuôn mặt đã lưu, hiển thị thông báo "Xin chào!" và bật đèn xanh. Khi phát hiện khuôn mặt lạ, hiển thị "Người lạ!" và bật đèn đỏ.

```
khi bắt đầu:
    khởi tạo ai vision camera chân RX [D3] TX [D4]

lặp mãi mãi:
    nếu [phát hiện khuôn mặt đã lưu] thì:
        hiển thị "Xin chào!"
        bật đèn xanh
    ngược lại nếu [phát hiện khuôn mặt lạ (chưa lưu)] thì:
        hiển thị "Người lạ!"
        bật đèn đỏ
```

> **Lưu ý:** Camera cần được đặt ổn định, ánh sáng đủ để nhận diện chính xác. Tránh ngược sáng hoặc góc nghiêng quá lớn.
