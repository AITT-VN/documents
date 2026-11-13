# 3. Đèn LED màu kích thích cây trồng
![3.1](/wiki-assets/images/module/dieu-khien-dong-ngat/images/3.1.png)


- Đèn LED màu kích thích cây trồng được ứng dụng trong các dự án như kích thích cây sinh trưởng trong môi trường thiếu sáng. Nếu bạn mới tiếp xúc và làm quen với các dự án IoT, đây sẽ là module phù hợp với bạn.


## **1. Mua sản phẩm**
![gio](/wiki-assets/images/module/dieu-khien-dong-ngat/images/gio.png)


## **2. Kết nối**
- **Bước 1**: Chuẩn bị các thiết bị như sau:


| Hình ảnh | Sản phẩm | Mua hàng |
|:--------:|:---------|:--------:|
| ![yolo](/wiki-assets/images/module/dieu-khien-dong-ngat/images/yolo.png) | Máy tính lập trình Yolo:Bit | [Mua sản phẩm ](https://shop.ohstem.vn/san-pham/may-tinh-lap-trinh-yolobit/) |
| ![mmr](/wiki-assets/images/module/dieu-khien-dong-ngat/images/mmr.png) | Mạch mở rộng cho Yolo:Bit | [Mua sản phẩm ](https://shop.ohstem.vn/san-pham/grove-shield/) |
| ![2.1](/wiki-assets/images/module/dieu-khien-dong-ngat/images/2.1.png) | Module đóng ngắt 2 kênh (kèm dây Grove) | [Mua sản phẩm ](https://shop.ohstem.vn/san-pham/module-dong-ngat-2-kenh/) |
| ![3.1](/wiki-assets/images/module/dieu-khien-dong-ngat/images/3.1.png) | Đèn LED màu kích thích cây trồng | [Mua sản phẩm ](https://shop.ohstem.vn/san-pham/may-bom-mini/) |
    
    
- **Bước 2**: Cắm Yolo:Bit vào mạch mở rộng

- **Bước 3**: Kết nối đèn LED với module đóng ngắt 2 kênh

- **Bước 4**: Kết nối thiết bị vào **chân P14/P15 trên mạch mở rộng**
![3.2](/wiki-assets/images/module/dieu-khien-dong-ngat/images/3.2.png)


    Để làm việc với module đóng ngắt 2 kênh, bạn sẽ kết nối vào cổng có 2 chân kết nối.
    
## **4. Hướng dẫn lập trình**
- **Bước 1:** Tải thư viện **AIOT KIT**, xem hướng dẫn tải thư viện [tại đây ](https://docs.ohstem.vn/en/latest/module/thu-vien-yolobit.html)
![aiot](/wiki-assets/images/module/dieu-khien-dong-ngat/images/aiot.png)

    |
    
    Sau khi tải thư viện, trong danh mục khối lệnh sẽ xuất hiện các khối lệnh tương ứng:
![lenh aiot](/wiki-assets/images/module/dieu-khien-dong-ngat/images/lenh_aiot.png)

    |
    
- **Bước 2:** Hãy gửi chương trình sau đến Yolo:Bit của bạn:
![3.3](/wiki-assets/images/module/dieu-khien-dong-ngat/images/3.3.png)


> **Ghi chú:** **Giải thích chương trình**:

Chúng ta sẽ sử dụng nút A trên mạch Yolo:Bit để bật đèn ở độ sáng 70%. Nút B để chuyển đèn về độ sáng 0% (tắt đèn).

Bạn có thể thay đổi độ sáng của đèn trong chương trình.