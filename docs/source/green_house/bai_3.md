# 4. Đo và hiển thị độ sáng của ngôi nhà

## 1. Mục tiêu
Đọc thông số độ sáng ngôi nhà từ cảm biến ánh sáng VEML 6040 và hiển thị lên màn hình LCD 1602.

## 2. Thiết bị cần sử dụng
- Mạch Yolo UNO:
![yolouno](/wiki-assets/images/yolo_uno/green_house/images/yolouno.png)


-  Module LCD kèm dây tín hiệu:
![lcd1602](/wiki-assets/images/yolo_uno/green_house/images/lcd1602.png)


- Cảm biến nhiệt ánh sáng và màu sắc VEML 6040 kèm dây tín hiệu:
![6040.1](/wiki-assets/images/yolo_uno/green_house/images/6040.1.png)


## 3. Kết nối phần cứng
- Kết nối LCD 1602 vào cổng I2C1

- Kết nối cảm biến VEML 6040 vào cổng I2C2 của Yolo UNO
![bai 3.1](/wiki-assets/images/yolo_uno/green_house/images/bai_3.1.png)


## 4. Chương trình lập trình
- **Tải thư viện Cảm biến ánh sáng và màu sắc VEML6040**:

    Vào mục **Mở rộng** và dán link sau vào ô tìm kiếm [https://github.com/AITT-VN/yolouno_extension_veml6040](https://github.com/AITT-VN/yolouno_extension_veml6040)
    
    Xem hướng dẫn tải thư viện `tại đây ](https://docs.ohstem.vn/en/latest/module/thu-vien-yolouno.html).
![bai 3.2](/wiki-assets/images/yolo_uno/green_house/images/bai_3.2.png)


- **Giới thiệu khối lệnh:**

    + Khối lệnh đọc giá trị độ sáng môi trường:
![bai 3.3](/wiki-assets/images/yolo_uno/green_house/images/bai_3.3.png)

    |
    
    + Khối lệnh phát hiện màu sắc:
![bai 3.4](/wiki-assets/images/yolo_uno/green_house/images/bai_3.4.png)

    |
    
    
- **Chương trình lập trình:**
![bai 3.5](/wiki-assets/images/yolo_uno/green_house/images/bai_3.5.png)


    Link chương trình [https://app.ohstem.vn/#!/share/yolouno/2s1SyTNuFDFyl5Oxxt5xiXU2aKW](https://app.ohstem.vn/#!/share/yolouno/2s1SyTNuFDFyl5Oxxt5xiXU2aKW)
    
- **Giải thích chương trình:** Sau khi cấp điện, đèn led trên Yolo UNO sẽ chuyển từ đỏ sang xanh lá cây. Sau 3s, màn hình sẽ cập nhật độ sáng và hiển thị trên màn hình LCD