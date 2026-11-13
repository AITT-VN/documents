# AI Camera

OhStem hiện có 2 dòng camera AI, bạn chọn loại phù hợp với dự án của mình:

| | [Camera AI](/ai-camera/camera-ai.md) | [AI Vision Camera](/ai-camera/ai-vision-camera/gioi-thieu.md) |
|---|---|---|
| Mô hình AI | Tự huấn luyện trên Google Teachable Machine | 8 chức năng AI có sẵn trên module |
| Cần WiFi | Có (xử lý mô hình qua trình duyệt) | Không, xử lý ngay trên camera |
| Chức năng | Nhận dạng theo mô hình bạn tự huấn luyện | Khuôn mặt, đối tượng, màu sắc, dò đường, April Tag, mã QR |
| Giao tiếp với board | UART hoặc server IoT | UART |
| Phù hợp với | Dự án phân loại, nhận dạng vật thể tùy ý | Robot dò đường, bám vật thể, đọc mã |

Nếu bạn **chưa có module Camera AI** mà muốn thử nghiệm mô hình AI ngay, hãy xem [Camera AI với OhStem App](/ai-camera/camera-ai-ohstem-app.md) — dùng webcam của laptop/điện thoại, cách huấn luyện mô hình giống hệt module Camera AI.

```{toctree}
:maxdepth: 2

ai-vision-camera/index
camera-ai
camera-ai-ohstem-app
```
