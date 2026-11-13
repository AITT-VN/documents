# 6. Đèn LED đơn
![6.1](/wiki-assets/images/module/hien-thi/images/6.1.png)


- LED đơn là một tín hiệu ngõ ra, khi được cấp nguồn điện vào thì đèn LED sẽ bật. Đèn LED đơn thường được sử dụng để thông báo trạng thái (ví dụ như làm đèn giao thông) hoặc dùng làm đèn cửa, đèn chiếu sáng,…

## **1. Mua sản phẩm**
![gio](/wiki-assets/images/module/hien-thi/images/gio.png)


## **2. Thông số kỹ thuật**
- **Thông số kỹ thuật**

    + Hỗ trợ cả 3.3V
    + Đèn LED đơn thường có 3 màu: đỏ, xanh lá, vàng
    + Kích thước của mạch: 24mm x 24mm x 8mm
    
    
- **Pinout của module LED đơn**

Module LED có 3 chân, và mỗi chân có chức năng như sau:


    :widths: 10, 15, 30
    
    1, "GND", "Nối đất"
    2, "VCC", "Cấp nguồn (3.3V)"
    3, "NC", "Không sử dụng"
    4, "SIG", "Tín hiệu điều khiển LED"
    
## **3. Kết nối**
- **Bước 1**: Chuẩn bị các thiết bị như sau:


| Hình ảnh | Sản phẩm | Mua hàng |
|:--------:|:---------|:--------:|
| ![yolo](/wiki-assets/images/module/hien-thi/images/yolo.png) | Máy tính lập trình Yolo:Bit | [Mua sản phẩm ](https://shop.ohstem.vn/san-pham/may-tinh-lap-trinh-yolobit/) |
| ![mmr](/wiki-assets/images/module/hien-thi/images/mmr.png) | Mạch mở rộng cho Yolo:Bit | [Mua sản phẩm ](https://shop.ohstem.vn/san-pham/grove-shield/) |
| ![6.1](/wiki-assets/images/module/hien-thi/images/6.1.png) | Module LED đơn (kèm dây Grove) | [Mua sản phẩm ](https://shop.ohstem.vn/san-pham/den-led-don/) |
    
    
- **Bước 2**: Cắm Yolo:Bit vào mạch mở rộng
- **Bước 3**: Sử dụng dây Grove cắm vào module
- **Bước 4**: Kết nối thiết bị vào **P14/P15 trên mạch mở rộng**
![6.2](/wiki-assets/images/module/hien-thi/images/6.2.png)


    Bạn có thể kết nối LED đơn vào bất kỳ chân nào trên mạch mở rộng.
    
## **4. Hướng dẫn lập trình**
- Sử dụng các khối lệnh trong danh mục **CHÂN CẮM** để làm việc với đèn LED đơn

- Gửi chương trình sau vào Yolo:Bit:
![6.3](/wiki-assets/images/module/hien-thi/images/6.3.png)


> **Ghi chú:** **Giải thích chương trình:** Đèn LED sẽ bật tắt liên tục sau mỗi giây, tạo nên hiệu ứng nhấp nháy của đèn.


## **5. Hướng dẫn lập trình Arduino**
- Mở phần mềm Arduino IDE. Xem hướng dẫn lập trình với Arduino [tại đây ](https://docs.ohstem.vn/en/latest/module/thu-vien-yolobit.html)

- Copy đoạn code sau, click vào nút `Verify` để kiểm tra lỗi chương trình. Sau khi biên dịch không báo lỗi, bạn có thể nạp đoạn code vào board.

```guess
#include "YoloBit.h"

 YoloBit yolobit;

 int ledPin = P14;

 // Bật tắt Relay sau mỗi 2 giây

 void setup() {
   pinMode(relayPin, OUTPUT);
 }

 void loop() {
   digitalWrite(ledPin, HIGH);
   delay(2000);
   digitalWrite(ledPin, LOW);
   delay(2000);
 }
```

> **Ghi chú:** **Giải thích chương trình:** Sau khi nạp chương trình và mở cửa sổ Serial, bạn sẽ thấy giá trị đọc được từ cảm biến được in ra. Bạn hãy thử lấy tay che cảm biến để thấy được sự thay đổi.