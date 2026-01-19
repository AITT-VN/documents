20. SHT30 - Cảm biến nhiệt độ và độ ẩm
=================================

Giới thiệu
----------

SHT30 là cảm biến nhiệt độ và độ ẩm kỹ thuật số độ chính xác cao của hãng Sensirion.
Module sử dụng giao tiếp **I2C**, cho phép đọc dữ liệu nhanh, ổn định và dễ dàng sử dụng
với Yolo UNO, Arduino, ESP32 hoặc MicroPython.

Ứng dụng:

- Trạm thời tiết mini
- Quan trắc môi trường
- Nhà thông minh
- Hệ thống nông nghiệp IoT
- Đo nhiệt độ – độ ẩm trong phòng học/lớp học STEM

Đặc điểm kỹ thuật
-----------------

- Đo **đồng thời** nhiệt độ và độ ẩm
- Độ chính xác:
  - Nhiệt độ: ±0.3°C
  - Độ ẩm: ±2% RH
- Giao tiếp: **I2C**
- Điện áp hoạt động: **3.3V – 5V**
- Địa chỉ I2C: **0x44** (mặc định)
- Dải đo:
  - Nhiệt độ: –40°C → +85°C
  - Độ ẩm: 0% → 100% RH
- Tốc độ lấy mẫu nhanh, độ ổn định cao

Pinout của module
-----------------

.. csv-table::
    :header: "STT", "Chân", "Chức năng"
    :widths: 10, 15, 30

    1, "GND", "Nối đất"
    2, "VCC", "Nguồn 3.3V – 5V"
    3, "SDA", "Dữ liệu I2C"
    4, "SCL", "Xung nhịp I2C"

Kết nối
-------

**Kết nối module SHT30 vào Yolo UNO:**


Module sử dụng bất kỳ cổng **I2C** nào của Yolo UNO hoặc Yolo:Bit.

Lập trình trên OhStem App
-------------------------

Để lập trình SHT30, bạn cần thêm thư viện mở rộng:

Vào **Mở rộng (Extensions)** → dán link:

::

    https://github.com/ohstem/extensions_sht30.git

Sau khi tải thư viện, bạn sẽ thấy các khối lệnh mới:

- Khối đọc **nhiệt độ (°C)**
- Khối đọc **độ ẩm (%)**

Ví dụ chương trình:

- Đọc nhiệt độ và độ ẩm mỗi giây
- Hiển thị lên màn hình hoặc gửi dữ liệu qua IoT

Lưu ý khi sử dụng
-----------------

- Tránh để module tiếp xúc trực tiếp với hơi nước hoặc mồ hôi tay
- Khi lắp ngoài trời → cần hộp bảo vệ nhưng vẫn đảm bảo thoáng khí
- Không đặt gần nguồn nhiệt (động cơ, pin, bo mạch công suất)
- Đặt cảm biến nơi có luồng gió nhẹ để đo chính xác hơn
