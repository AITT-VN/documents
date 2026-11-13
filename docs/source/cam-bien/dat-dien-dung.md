# 4. Cảm biến độ ẩm đất điện dung
![4.1](/wiki-assets/images/module/cam-bien/images/4.1.png)


- Cảm biến độ ẩm đất điện dung sẽ sử dụng cảm biến điện dung để phát hiện độ ẩm của đất và phản hồi tín hiệu về. Bạn có thể ứng dụng cảm biến này vào các dự án như đo độ ẩm của đất để chăm sóc cây trồng,…

- Sản phẩm có độ bền cao, ít bị ăn mòn và có thể sử dụng lâu dài.

## **1. Mua sản phẩm**
![gio](/wiki-assets/images/module/cam-bien/images/gio.png)


## **2. Thông số kỹ thuật**
- **Thông số kỹ thuật của cảm biến:**

    + Điện áp hoạt động: 3.3V
    + Tín hiệu đầu ra: Analog
    + Chiều dài: 92,1mm
    + Bề rộng: 23,5mm
    + Chiều cao: 6,5mm
    + kích thước: L: 40mm W: 20mm H: 13mm
    
    
## **3. Kết nối**
- **Bước 1**: Chuẩn bị các thiết bị như sau:


| Hình ảnh | Sản phẩm | Mua hàng |
|:--------:|:---------|:--------:|
| ![yolo](/wiki-assets/images/module/cam-bien/images/yolo.png) | Máy tính lập trình Yolo:Bit | [Mua sản phẩm ](https://shop.ohstem.vn/san-pham/may-tinh-lap-trinh-yolobit/) |
| ![mmr](/wiki-assets/images/module/cam-bien/images/mmr.png) | Mạch mở rộng cho Yolo:Bit | [Mua sản phẩm ](https://shop.ohstem.vn/san-pham/grove-shield/) |
| ![4.1](/wiki-assets/images/module/cam-bien/images/4.1.png) | Cảm biến độ ẩm đất điện dung (kèm dây Grove) | [Mua sản phẩm ](https://shop.ohstem.vn/san-pham/cam-bien-do-am-dat-dien-dung/) |
    
- **Bước 2**: Cắm Yolo:Bit vào mạch mở rộng
- **Bước 3**: Sử dụng dây Grove cắm vào cảm biến
- **Bước 4**: Kết nối cảm biến độ ẩm đất vào **chân P1 trên mạch mở rộng**
![4.2](/wiki-assets/images/module/cam-bien/images/4.2.png)


## **4. Hướng dẫn lập trình với OhStem App**
- **Bước 1:** Tải thư viện **AIOT KIT**, xem hướng dẫn tải thư viện [tại đây ](https://docs.ohstem.vn/en/latest/module/thu-vien-yolobit.html)
![aiot](/wiki-assets/images/module/cam-bien/images/aiot.png)

    |
    
    Sau khi tải thư viện, trong danh mục khối lệnh sẽ xuất hiện các khối lệnh tương ứng:
![lenh aiot](/wiki-assets/images/module/cam-bien/images/lenh_aiot.png)

    |
    
    
- **Bước 2**: Gửi chương trình sau xuống Yolo:Bit
![3.3](/wiki-assets/images/module/cam-bien/images/3.3.png)


> **Ghi chú:** **Giải thích chương trình:** Phần trăm độ ẩm đất sẽ được hiển thị lên màn hình LED của Yolo:Bit sau mỗi giây.


## **5. Hướng dẫn lập trình Arduino**
- Mở phần mềm Arduino IDE. Xem hướng dẫn lập trình với Arduino [tại đây ](https://docs.ohstem.vn/en/latest/module/cai-dat-arduino.html).

- Copy đoạn code sau, click vào nút `Verify` để kiểm tra lỗi chương trình. Sau khi biên dịch không báo lỗi, bạn có thể nạp đoạn code vào board.

```guess
#include "YoloBit.h"

 YoloBit yolobit;

 int sensorPin = P1_ADC;
 int sensorValue = 0;

 void setup() {
   Serial.begin(115200);
 }

 void loop() {
   // đọc giá trị cảm biến
   sensorValue = analogRead(sensorPin);
   Serial.println(sensorValue);
   delay(200);
 }
```

> **Ghi chú:** **Giải thích chương trình:** Sau khi nạp chương trình và mở cửa sổ Serial, bạn sẽ thấy giá trị đọc được từ cảm biến được in ra. Bạn hãy thử đặt cảm biến vào ly nước hay chậu đất để thấy được sự thay đổi.