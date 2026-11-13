# 10. Cảm biến dò đường 4 mắt
![11.1](/wiki-assets/images/module/cam-bien/images/11.1.png)


- Module cảm biến dò đường là lựa chọn hoàn hảo cho các ứng dụng điều hướng robot. Module dò đường loại 4 mắt có năm cảm biến quang học phản chiếu, được sử dụng để theo dõi chính xác bề mặt màu đen.

- Mạch sử dụng cảm biến hồng ngoại với khoảng cách có thể phát hiện vạch đen, nền trắng từ 1~25mm giúp bạn dễ dàng tùy chỉnh module theo nhu cầu. Dựa vào cách hoạt động này, cảm biến sẽ biết được đâu là vạch đen và đâu là nền trắng.

- Cảm biến dò đường được ứng dụng vào các dự án như robot chạy theo đường vẽ được chỉ định sẵn hoặc khi sử dụng sa bàn, giải mê cung,…


## **1. Mua sản phẩm**
![gio](/wiki-assets/images/module/cam-bien/images/gio.png)


## **2. Thông số kỹ thuật**
- **Thông số kỹ thuật**

    + Nguồn cung cấp: 3.3V
    + Sử dụng 4 cảm biến hồng ngoại.
    + Sử dụng IC mở rộng: PCF8574T
    + Dòng điện tiêu thụ: \<10mA.
    + Dải nhiệt độ hoạt động: 0oC ~ 50oC.
    + Mức tín hiệu ngõ ra: TTL
    + Kích thước: 2.4 x 4.8mm
    
    
- **Pinout của cảm biến dò đường 4 mắt**

Cảm biến dò đường 4 mắt có 4 chân, và mỗi chân có chức năng như sau:


    :widths: 10, 15, 30
    
    1, "GND", "Nối đất"
    2, "VCC", "Cấp nguồn (3.3V)"
    3, "SCL", "Xung tín hiệu"
    4, "SDA", "Truyền tín hiệu"
    
    
## **3. Chuẩn bị thiết bị**
Cảm biến dò đường thường được sử dụng trên Robot Rover hoặc xBot, để làm việc với cảm biến bạn cần có một trong hai thiết bị sau:


| Hình ảnh | Sản phẩm | Mua hàng |
|:--------:|:---------|:--------:|
| ![rover](/wiki-assets/images/module/cam-bien/images/rover.png) | Robot Rover (kèm Yolo:Bit) | [Mua sản phẩm ](https://shop.ohstem.vn/san-pham/robot-stem-rover/) |
| ![xbot](/wiki-assets/images/module/cam-bien/images/xbot.png) | Robot xBot | [Mua sản phẩm ](https://shop.ohstem.vn/san-pham/robot-lap-trinh-xbot-stem-robot-kit/) |
    
    
## **4. Hướng dẫn lập trình**
- **Đối với robot Rover:**

    + **Bước 1:** Chọn thiết bị lập trình là **Yolo:Bit**
![11.2](/wiki-assets/images/module/cam-bien/images/11.2.png)

    |
    
    + **Bước 2:** Tải thư viện Rover cho Yolo:Bit, xem hướng dẫn tải thư viện [tại đây ](https://docs.ohstem.vn/en/latest/module/thu-vien-yolobit.html)
![11.3](/wiki-assets/images/module/cam-bien/images/11.3.png)

    |
    
    + **Bước 3:** Gửi chương trình sau cho Yolo:Bit để kiểm tra các trạng thái của mắt đọc:
![11.4](/wiki-assets/images/module/cam-bien/images/11.4.png)

    |
    
> **Ghi chú:** **Giải thích chương trình:** Ở trong vòng lặp mãi, tương ứng với mỗi trạng thái là: nhận mắt S1, S2, S3, S4, chương trình sẽ in ra cửa sổ Serial các hàng ký tự tương ứng với từng trạng thái đó.


- **Đối với robot xBot::**

    + **Bước 1:** Chọn thiết bị lập trình là **xBot**
![11.5](/wiki-assets/images/module/cam-bien/images/11.5.png)

    |
    
    + **Bước 2:** Gửi chương trình sau lên robot xBot:
![11.6](/wiki-assets/images/module/cam-bien/images/11.6.png)

    |
    
> **Ghi chú:** **Giải thích chương trình:** Chương trình được thực hiện tương tự như Robot Rover.


## **5. Hướng dẫn tinh chỉnh cảm biến dò đường:**


[Xem video](https://www.youtube.com/embed/ARVPbp8W_x4)

