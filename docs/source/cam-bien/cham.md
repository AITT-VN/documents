# 20. Cảm biến chạm
![20.1](/wiki-assets/images/module/cam-bien/images/20.1.png)


- Hiện nay smartphone đã khá thân thuộc với mọi người. Cảm biến chạm cũng sử dụng cùng cơ chế với những chiếc điện thoại cảm ứng, giúp chúng ta có thể thao tác chỉ với việc chạm tay. Cảm biến chạm có thể được ứng dụng trong các chương trình như chạm tay để bật/tắt đèn, chạm tay để khởi động xe,…

## **1. Mua sản phẩm**
![gio](/wiki-assets/images/module/cam-bien/images/gio.png)


## **2. Thông số kỹ thuật**
- **Thông số kỹ thuật**

    + Khi chạm tay, module phát ra một tín hiệu mức thấp (LOW), khi chạm lại lần nữa sẽ tạo ra mức cao (HIGH)
    + Điện áp: 3.3V
    + Dòng định mức : 5mA
    + Ngõ ra: Digital
    + Kích thước của mạch: 24mm x 48mm x 16mm
    
    
- **Pinout của cảm biến**

Cảm biến lửa có 4 chân, và mỗi chân có chức năng như sau:


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
| ![20.1](/wiki-assets/images/module/cam-bien/images/20.1.png) | Cảm biến chạm (kèm dây Grove) | [Mua sản phẩm ](https://shop.ohstem.vn/san-pham/cam-bien-cham/) |
    
    
- **Bước 2**: Cắm Yolo:Bit vào mạch mở rộng
- **Bước 3**: Sử dụng dây Grove cắm vào cảm biến
- **Bước 4**: Kết nối cảm biến với **P16/P12 trên mạch mở rộng**.
![20.2](/wiki-assets/images/module/cam-bien/images/20.2.png)


    Cảm biến chạm có kết quả trả về là digital, trên mạch mở rộng các bạn có thể sử dụng các khe cắm có 2 tín hiệu
    
    
## **4. Hướng dẫn lập trình với OhStem App**
- Hãy gửi chương trình sau đến Yolo:Bit của bạn:
![20.3](/wiki-assets/images/module/cam-bien/images/20.3.png)


> **Ghi chú:** **Giải thích chương trình:** Nếu cảm biến được chạm vào, tức là trạng thái của chân P16 đang bật. Đèn LED sẽ chuyển sang màu trắng. Nếu không được chạm vào, đèn sẽ tắt.

Sử dụng các khối lệnh trong danh mục **CHÂN CẮM**.


## **5. Hướng dẫn lập trình Arduino**
- Mở phần mềm Arduino IDE. Xem hướng dẫn lập trình với Arduino [tại đây ](https://docs.ohstem.vn/en/latest/module/cai-dat-arduino.html).

- Copy đoạn code sau, click vào nút `Verify` để kiểm tra lỗi chương trình. Sau khi biên dịch không báo lỗi, bạn có thể nạp đoạn code vào board.

```guess
#include <Yolobit.h>

 Yolobit yolobit;

 int TOUCH_PIN = P16;

 void setup() {
   Serial.begin(9600);
   pinMode(TOUCH_PIN, INPUT);
 }

 void loop() {
   int touch = digitalRead(TOUCH_PIN);

   if (touch == LOW) {
       Serial.println("Touching"); //chạm vào cảm biến
   }
   else {
       Serial.println("None"); // không chạm
   }

   delay(300);
 }
```

> **Ghi chú:** **Giải thích chương trình:** Sau khi nạp chương trình và mở cửa sổ Serial, bạn sẽ thấy giá trị đọc được từ cảm biến được in ra.