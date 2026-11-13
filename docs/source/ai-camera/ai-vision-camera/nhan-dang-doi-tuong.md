# 4. Nhận dạng đối tượng

## **Giới thiệu**

Chức năng nhận dạng đối tượng sử dụng mô hình AI được huấn luyện sẵn để phân loại và nhận ra các vật thể trong khung hình. Camera trả về tên đối tượng nhận dạng được cùng với độ tin cậy (%).

**Ứng dụng tiêu biểu:**
- Phân loại sản phẩm trên băng chuyền
- Nhận dạng thú cưng, đồ vật trong nhà
- Hệ thống kiểm soát chất lượng tự động

## **Các khối lệnh**

| Khối lệnh | Mô tả |
|-----------|-------|
| `nhận dạng được là` | Trả về tên đối tượng đang được nhận diện |
| `độ tin cậy nhận dạng (%)` | Trả về độ tin cậy của kết quả nhận dạng (0–100%) |
| `nhận dạng là [tên] và độ tin cậy ≥ [80] %` | Trả về `True` nếu nhận dạng đúng tên với độ tin cậy đạt ngưỡng |

## **Ví dụ chương trình**

**Mô tả:** Hiển thị tên đối tượng và độ tin cậy lên màn hình. Nếu nhận ra "meo" với độ tin cậy ≥ 80%, phát âm thanh thông báo.

```
khi bắt đầu:
    khởi tạo ai vision camera chân RX [D3] TX [D4]

lặp mãi mãi:
    hiển thị [nhận dạng được là] + " " + [độ tin cậy nhận dạng (%)] + "%"

    nếu [nhận dạng là "meo" và độ tin cậy ≥ 80%] thì:
        phát âm thanh thông báo
```

> **Lưu ý:** Ngưỡng độ tin cậy khuyến nghị từ **70–85%**. Đặt quá thấp dễ nhận sai, quá cao có thể bỏ sót đối tượng hợp lệ.
