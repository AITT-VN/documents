# 5. Theo dõi đường thẳng

## **Giới thiệu**

Chức năng theo dõi đường thẳng giúp camera phát hiện và bám theo một đường kẻ (thường là đường đen trên nền trắng hoặc ngược lại). Camera trả về tọa độ và góc nghiêng của đường trong khung hình.

**Ứng dụng tiêu biểu:**
- Robot dò line tự động
- Xe tự hành đi theo vạch đường
- Hệ thống phân làn trong nhà máy

## **Yêu cầu về đường line**

- Đường có màu tương phản rõ với nền (đen/trắng hoặc trắng/đen)
- Độ rộng đường khuyến nghị: 1–4cm
- Ánh sáng đồng đều, tránh bóng đổ trên đường line

## **Các khối lệnh**

| Khối lệnh | Mô tả |
|-----------|-------|
| `đang nhìn thấy đường line` | Trả về `True` nếu camera phát hiện đường line trong khung hình |
| `tọa độ X của đường line` | Trả về tọa độ X của điểm giữa đường line (0–320) |
| `tọa độ Y của đường line` | Trả về tọa độ Y của điểm giữa đường line (0–240) |
| `góc nghiêng của đường line` | Trả về góc nghiêng của đường so với trục ngang (độ) |

## **Ví dụ chương trình**

**Mô tả:** Robot dò line – điều chỉnh hướng dựa theo tọa độ X của đường line so với tâm màn hình.

```
khi bắt đầu:
    khởi tạo ai vision camera chân RX [D3] TX [D4]

lặp mãi mãi:
    nếu [đang nhìn thấy đường line] thì:
        nếu [tọa độ X của đường line] < 140 thì:
            rẽ trái nhẹ
        ngược lại nếu [tọa độ X của đường line] > 180 thì:
            rẽ phải nhẹ
        ngược lại:
            đi thẳng
    ngược lại:
        dừng lại và tìm đường
```

> **Lưu ý:** Với đường line cong, kết hợp thêm `góc nghiêng của đường line` để điều chỉnh mượt mà hơn.
