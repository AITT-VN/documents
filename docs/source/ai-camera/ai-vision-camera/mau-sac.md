# 6. Nhận dạng màu sắc

## **Giới thiệu**

Chức năng nhận dạng màu sắc cho phép camera xác định màu sắc chủ đạo của vật thể trong khung hình. Camera hỗ trợ nhận diện các màu cơ bản: **Đỏ, Cam, Vàng, Xanh lá, Xanh lam, Tím, Đen, Trắng**.

**Ứng dụng tiêu biểu:**
- Robot phân loại vật thể theo màu sắc
- Hệ thống kiểm tra màu sơn, bao bì sản phẩm
- Trò chơi nhận màu sắc tương tác

## **Các khối lệnh**

| Khối lệnh | Mô tả |
|-----------|-------|
| `màu sắc nhận dạng được là` | Trả về tên màu sắc đang được nhận diện trong khung hình |
| `phát hiện ra màu [Đỏ]` | Trả về `True` nếu màu được chọn xuất hiện trong khung hình |

**Các màu hỗ trợ:** Đỏ, Cam, Vàng, Xanh lá, Xanh lam, Tím, Đen, Trắng.

## **Ví dụ chương trình**

**Mô tả:** Robot băng chuyền phân loại vật thể — đẩy sang trái nếu màu đỏ, sang phải nếu màu xanh lá, dừng lại nếu màu khác.

```
khi bắt đầu:
    khởi tạo ai vision camera chân RX [D3] TX [D4]

lặp mãi mãi:
    nếu [phát hiện ra màu Đỏ] thì:
        đẩy sang trái
    ngược lại nếu [phát hiện ra màu Xanh lá] thì:
        đẩy sang phải
    ngược lại:
        dừng băng chuyền
```

> **Lưu ý:** Ánh sáng ảnh hưởng lớn đến độ chính xác nhận màu. Sử dụng trong điều kiện ánh sáng ổn định, tránh ánh sáng vàng hoặc màu môi trường chiếu vào vật thể.
