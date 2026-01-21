21. GUVA-S12SD - Cảm biến ánh sáng UV
=================================

Giới thiệu
----------

GUVA-S12SD là cảm biến ánh sáng *UV-A* (315–400 nm), cho phép đo cường độ tia UV ngoài môi trường.
Cảm biến hoạt động dựa trên nguyên lý quang điện và cho ra **tín hiệu analog tuyến tính** (0–1V),
dễ dàng đọc bằng ADC của các vi điều khiển như Yolo UNO, Arduino, ESP32 hoặc MicroPython.

..  image:: images/uv_01.png
    :scale: 100%
    :align: center 
|

Ứng dụng:

- Đo chỉ số UV Index
- Đo cường độ tia UV trong nhà kính
- Hệ thống cảnh báo nắng nóng
- Quan trắc môi trường ngoài trời
- Thiết bị IoT

Đặc điểm kỹ thuật
-----------------

- Dải hoạt động UV-A: **240–370 nm**
- Ngõ ra: **Analog 0–1.0V**
- Điện áp hoạt động: **3.0V – 5.0V**
- Độ nhạy UV cao, ít bị nhiễu ánh sáng khả kiến
- Kích thước nhỏ gọn, dễ lắp đặt vào hệ thống

Sơ đồ chân
----------

.. csv-table::
    :header: "STT", "Chân", "Chức năng"
    :widths: 8, 15, 30

    1, "GND", "GND"
    2, "VCC", "Nguồn 3.3V – 5V"
    3, "NC", "Chân không sử dụng"
    3, "OUT", "Ngõ ra Analog 0–1V"

Kết nối với Yolo UNO
----------------------------

Kết nối đơn giản:

..  image:: images/uv_02.png
    :scale: 100%
    :align: center 
|

Lập trình với Yolo UNO trên OhStem App
------------------------------------
Để lập trình cảm biến GUVA-S12SD với Yolo UNO, bạn có thể sử dụng khối lệnh đọc giá trị UV từ thư viện **Smart City**.
..  image:: images/uv_03.png
    :scale: 100%
    :align: center

Chuong trình mẫu đọc giá trị UV và hiển thị lên màn hình LCD sau mỗi 1 giây.

Lưu ý khi sử dụng
-----------------

- Tránh để bụi hoặc nước che mặt cảm biến
- Đo UV tốt nhất khi cảm biến hướng lên trời
- Nếu dùng ngoài trời lâu dài → nên có nắp bảo vệ xuyên UV
- Tín hiệu analog rất nhỏ → nên dùng dây ngắn để giảm nhiễu
