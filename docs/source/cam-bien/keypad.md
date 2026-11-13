# 20. Keypad - Bàn phím cảm ứng điện dung
![22.1](/wiki-assets/images/module/cam-bien/images/22.1.png)


- Bàn phím cảm ứng điện sử dụng IC chuyên dụng MPR121 có khả năng nhận biết điện dung từ tay người qua 12 vị trí cảm ứng với độ chính xác và độ nhạy cao, bàn phím phù hợp với các ứng dụng cần độ bền, tạo sự độc đáo và chuyên nghiệp trong các ứng dụng điều khiển cảm ứng, bàn phím sử dụng giao tiếp I2C rất dễ kết nối và giao tiếp chỉ với 2 chân GPIO.


## **1. Mua sản phẩm**
![gio](/wiki-assets/images/module/cam-bien/images/gio.png)


## **2. Thông số kỹ thuật**
- **Thông số kỹ thuật**

    + IC chính: MPR121
    + Điện áp sử dụng: 3.3VDC
    + Giao tiếp: I2C
    + Mức logic giao tiếp: TTL 3.3V
    
    
## **3. Kết nối**
- **Bước 1**: Chuẩn bị các thiết bị như sau:


| Hình ảnh | Sản phẩm | Mua hàng |
|:--------:|:---------|:--------:|
| ![yolo](/wiki-assets/images/module/cam-bien/images/yolo.png) | Máy tính lập trình Yolo:Bit | [Mua sản phẩm ](https://shop.ohstem.vn/san-pham/may-tinh-lap-trinh-yolobit/) |
| ![mmr](/wiki-assets/images/module/cam-bien/images/mmr.png) | Mạch mở rộng cho Yolo:Bit | [Mua sản phẩm ](https://shop.ohstem.vn/san-pham/grove-shield/) |
| ![22.1](/wiki-assets/images/module/cam-bien/images/22.1.png) | Keypad (kèm dây Grove) | [Mua sản phẩm ](https://shop.ohstem.vn/san-pham/keypad-ban-phim-cam-ung-dien-dung/) |
    
    
- **Bước 2**: Cắm Yolo:Bit vào mạch mở rộng
- **Bước 3**: Sử dụng dây Grove cắm vào cảm biến
- **Bước 4**: Kết nối cảm biến với **I2C trên mạch mở rộng**.
![22.2](/wiki-assets/images/module/cam-bien/images/22.2.png)


    Bạn có thể kết nối cảm biến vào 1 trong 2 chân I2C trên mạch mở rộng
    
    
## **4. Hướng dẫn lập trình**
- **Bước 1:** Tải thư viện **Bàn phím cảm ứng**, xem hướng dẫn tải thư viện [tại đây ](https://docs.ohstem.vn/en/latest/module/thu-vien-yolobit.html)
![banphim](/wiki-assets/images/module/cam-bien/images/banphim.png)

    |
    
    Sau khi tải thư viện, trong danh mục khối lệnh sẽ xuất hiện các khối lệnh tương ứng:
![lenh banphim](/wiki-assets/images/module/cam-bien/images/lenh_banphim.png)

    |
    
- **Bước 2**: Gửi chương trình sau xuống Yolo:Bit
![22.3](/wiki-assets/images/module/cam-bien/images/22.3.png)

    |
    
> **Ghi chú:** **Giải thích chương trình:** Khi nút trên bàn phím được nhấn, Yolo:Bit sẽ hiển thị thông tin ra màn hình LED tương ứng.