# 8. Đọc mã QR

## **Giới thiệu**

Chức năng đọc mã QR cho phép camera quét và giải mã nội dung văn bản chứa trong mã QR. Camera trả về chuỗi ký tự được mã hóa trong mã QR theo thời gian thực.

**Ứng dụng tiêu biểu:**
- Hệ thống điểm danh bằng QR code
- Kiểm tra thông tin sản phẩm, hàng hóa
- Mở khóa thiết bị bằng QR code
- Trò chơi tương tác với mã QR

## **Các khối lệnh**

| Khối lệnh | Mô tả |
|-----------|-------|
| `mã QR đọc được` | Trả về chuỗi văn bản chứa trong mã QR vừa quét được |
| `đang nhìn thấy mã QR` | Trả về `True` nếu camera phát hiện mã QR trong khung hình |

## **Ví dụ chương trình**

**Mô tả:** Hệ thống kiểm tra mật khẩu bằng QR — nếu mã QR chứa đúng mật khẩu "OHSTEM2024" thì mở khóa, ngược lại hiển thị thông báo từ chối.

```
khi bắt đầu:
    khởi tạo ai vision camera chân RX [D3] TX [D4]

lặp mãi mãi:
    nếu [đang nhìn thấy mã QR] thì:
        nếu [mã QR đọc được] = "OHSTEM2026" thì:
            hiển thị "Mở khóa!"
            bật relay (mở cửa)
            đợi 3 giây
            tắt relay
        ngược lại:
            hiển thị "Từ chối!"
```

> **Lưu ý:** Giữ mã QR thẳng, đủ ánh sáng và khoảng cách 10–30cm để camera đọc chính xác. Mã QR quá nhỏ hoặc bị nhăn, mờ sẽ không đọc được.
