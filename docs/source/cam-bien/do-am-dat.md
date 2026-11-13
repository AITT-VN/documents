# 3. Cảm biến độ ẩm đất
![3.1](/wiki-assets/images/module/cam-bien/images/3.1.png)


- Cảm biến độ ẩm đất Soil Moisture Sensor thường được sử dụng trong các mô hình tưới nước tự động, vườn thông minh,…, Đây là cảm biến giúp xác định độ ẩm của đất và trả về giá trị Analog.


## **1. Mua sản phẩm**
![gio](/wiki-assets/images/module/cam-bien/images/gio.png)


## **2. Thông số kỹ thuật**
- **Thông số kỹ thuật của cảm biến độ ẩm đất**

    + Điện áp làm việc 3.3V
    + Sử dụng chip LM393 để so sánh, ổn định làm việc
    + Kích thước module: 48mm x 24 mm x 18mm (DxRxC)
    
- **Pinout của cảm biến độ ẩm đất**

Module cảm biến độ ẩm đất có 4 chân, và mỗi chân có chức năng như sau:


    :widths: 10, 15, 30
    
    1, "GND", "Nối đất"
    2, "VCC", "Cấp nguồn (3.3V)"
    3, "NC", "Không sử dụng"
    4, "SIG", "Tín hiệu cảm biến"
    
## **3. Kết nối**
- **Bước 1**: Chuẩn bị các thiết bị như sau:


| Hình ảnh | Sản phẩm | Mua hàng |
|:--------:|:---------|:--------:|
| ![yolo](/wiki-assets/images/module/cam-bien/images/yolo.png) | Máy tính lập trình Yolo:Bit | [Mua sản phẩm ](https://shop.ohstem.vn/san-pham/may-tinh-lap-trinh-yolobit/) |
| ![mmr](/wiki-assets/images/module/cam-bien/images/mmr.png) | Mạch mở rộng cho Yolo:Bit | [Mua sản phẩm ](https://shop.ohstem.vn/san-pham/grove-shield/) |
| ![3.1](/wiki-assets/images/module/cam-bien/images/3.1.png) | Cảm biến độ ẩm đất (kèm dây Grove) | [Mua sản phẩm ](https://shop.ohstem.vn/san-pham/cam-bien-do-am-dat/) |
    
- **Bước 2**: Cắm Yolo:Bit vào mạch mở rộng
- **Bước 3**: Sử dụng dây Grove cắm vào cảm biến
- **Bước 4**: Kết nối cảm biến độ ẩm đất vào **chân P0 trên mạch mở rộng**
![3.2](/wiki-assets/images/module/cam-bien/images/3.2.png)


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

 int sensorPin = P0_ADC;
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