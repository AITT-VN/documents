# 2. Module đóng ngắt 2 kênh
![2.1](/wiki-assets/images/module/dieu-khien-dong-ngat/images/2.1.png)


- Module đóng ngắt 2 kênh thường được dùng để điều khiển bật tắt các thiết bị sử dụng cổng USB như máy bơm, đèn LED màu,…

- Module này có chức năng chuyển đổi từ cổng tín hiệu Grove sang cổng cắm USB, để bạn dễ dàng kết nối với các module điện tử phù hợp


## **1. Mua sản phẩm**
![gio](/wiki-assets/images/module/dieu-khien-dong-ngat/images/gio.png)


## **2. Kết nối**
- **Bước 1**: Chuẩn bị các thiết bị như sau:


| Hình ảnh | Sản phẩm | Mua hàng |
|:--------:|:---------|:--------:|
| ![yolo](/wiki-assets/images/module/dieu-khien-dong-ngat/images/yolo.png) | Máy tính lập trình Yolo:Bit | [Mua sản phẩm ](https://shop.ohstem.vn/san-pham/may-tinh-lap-trinh-yolobit/) |
| ![mmr](/wiki-assets/images/module/dieu-khien-dong-ngat/images/mmr.png) | Mạch mở rộng cho Yolo:Bit | [Mua sản phẩm ](https://shop.ohstem.vn/san-pham/grove-shield/) |
| ![2.1](/wiki-assets/images/module/dieu-khien-dong-ngat/images/2.1.png) | Module đóng ngắt (kèm dây Grove) | [Mua sản phẩm ](https://shop.ohstem.vn/san-pham/module-dong-ngat-2-kenh/) |
| ![may bom](/wiki-assets/images/module/dieu-khien-dong-ngat/images/may_bom.png) | Máy bơm mini | [Mua sản phẩm ](https://shop.ohstem.vn/san-pham/may-bom-mini/) |
    
    
- **Bước 2**: Cắm Yolo:Bit vào mạch mở rộng

- **Bước 3**: Kết nối máy bơm mini với module đóng ngắt 2 kênh

- **Bước 4**: Kết nối thiết bị vào **chân P14/P15 trên mạch mở rộng**
![2.2](/wiki-assets/images/module/dieu-khien-dong-ngat/images/2.2.png)


    Để làm việc với module đóng ngắt 2 kênh, bạn sẽ kết nối vào cổng có 2 chân kết nối.
    
## **3. Hướng dẫn lập trình**
- Sử dụng các khối lệnh trong danh mục **CHÂN CẮM** để làm việc với đèn module đóng ngắt 2 kênh.

- Gửi chương trình sau vào Yolo:Bit:
![2.3](/wiki-assets/images/module/dieu-khien-dong-ngat/images/2.3.png)


    Chương trình bật tắt máy bơm kết nối với cổng USB thứ hai.
    
> **Ghi chú:** Trong trường hợp muốn điều khiển đồng thời 2 máy bơm, trong chương trình sẽ thêm câu lệnh điều khiển bật tắt trạng thái chân P14. Và máy bơm còn lại sẽ kết nối với cổng USB thứ 1.


- **Hoặc có thể sử dụng câu lệnh sau trong thư viện AIoT KIT để điều khiển module đóng ngắt 2 kênh:**
![2.4](/wiki-assets/images/module/dieu-khien-dong-ngat/images/2.4.png)
