# 5. Module servo 8 kênh I2C

## **1. Giới thiệu**
![servo 8 kenh](/wiki-assets/images/module/board-mo-rong/images/servo_8_kenh.png)


**Module servo 8 kênh I2C** là một module cho phép điều khiển **đồng thời tối đa 8 động cơ servo** thông qua kết nối với các bộ vi điều khiển như Yolo:Bit hoặc Yolo UNO. Mạch sử dụng giao tiếp I2C, giúp tiết kiệm chân kết nối và dễ dàng mở rộng khi xây dựng các dự án có nhiều động cơ servo.

Một vài ứng dụng có thể sử dụng module này như: Hệ thống mở cửa tự động với nhiều cửa, mô hình robot nhiều khớp, cánh tay robot... Trong hướng dẫn này, chúng tôi sẽ hướng dẫn bạn kết nối module này với mạch lập trình cơ bản Yolo:Bit và Yolo UNO.

## **2. Thông số kỹ thuật**
- Hỗ trợ nguồn pin ~6 - 12V
- Hỗ trợ điều khiển 8 servo độc lập
- Giao tiếp I2C


## **3. Kết nối phần cứng**
- **Chuẩn bị các thiết bị**, bạn có thể chuẩn bị 1 trong 2 mạch lập trình Yolo:Bit hoặc Yolo UNO và các thiết bị như bên dưới:


| Hình ảnh | Sản phẩm | Mua hàng |
|:--------:|:---------|:--------:|
| ![yolo mmr](/wiki-assets/images/module/board-mo-rong/images/yolo_mmr.png) | Máy tính lập trình Yolo:Bit kèm mạch mở rộng | [Mua sản phẩm ](https://shop.ohstem.vn/san-pham/may-tinh-lap-trinh-yolobit/) |
| ![yolo uno](/wiki-assets/images/module/board-mo-rong/images/yolo_uno.png) | Mạch lập trình Yolo UNO | [Mua sản phẩm ](https://shop.ohstem.vn/san-pham/yolo-uno/) |
| ![servo 8 kenh](/wiki-assets/images/module/board-mo-rong/images/servo_8_kenh.png) | Module Module servo 8 kênh I2C | [Mua sản phẩm ](https://shop.ohstem.vn/san-pham/module-servo-8-kenh-i2c/) |
| ![servo 8 kenh 2](/wiki-assets/images/module/board-mo-rong/images/servo_8_kenh_2.png) | Servo 180 độ | [Mua sản phẩm ](https://shop.ohstem.vn/san-pham/dong-co-servo-mg90s/) |
| ![nut nhan doi](/wiki-assets/images/module/board-mo-rong/images/nut_nhan_doi.png) | Nút nhấn đôi (Dành cho kết nối với Yolo UNO ) | [Mua sản phẩm ](https://shop.ohstem.vn/san-pham/nut-nhan-doi/) |
| ![pin2s](/wiki-assets/images/module/board-mo-rong/images/pin2s.png) | Pin 2S | [Mua sản phẩm ](https://shop.ohstem.vn/san-pham/pin-sac-2s-dung-cho-robot-orc-k2/) |
    
- **Kết nối với Yolo:Bit:**
![servo 8 kenh 3](/wiki-assets/images/module/board-mo-rong/images/servo_8_kenh_3.png)


    *Kết nối vào cổng I2C trên mạch mở rộng Yolo:Bit*
    
- **Kết nối với Yolo UNO:**
![servo 8 kenh 4](/wiki-assets/images/module/board-mo-rong/images/servo_8_kenh_4.png)


    *Kết nối vào cổng I2C trên mạch Yolo UNO*
    
## 4. Lập trình với Yolo:Bit
1. Tải thư viện **SERVO8CHS Kit**, bằng cách dán đường link sau vào phần tìm kiếm thư viện: [https://github.com/AITT-VN/yolobit_extension_servo8chs](https://github.com/AITT-VN/yolobit_extension_servo8chs)

    Xem hướng dẫn tải thư viện `tại đây ](https://docs.ohstem.vn/en/latest/module/thu-vien-yolobit.html)
![servo 8 kenh 5](/wiki-assets/images/module/board-mo-rong/images/servo_8_kenh_5.png)

    |
    
    Thư viện sẽ gồm các câu lệnh điều khiển servo như sau:
![servo 8 kenh 6](/wiki-assets/images/module/board-mo-rong/images/servo_8_kenh_6.png)

    |
    
2. **Viết chương trình:**

**2.1. Điều khiển servo quay đến góc cố định**

    Khối lệnh điều khiển servo quay tới góc chỉ định với tốc độ tùy chỉnh:
![servo 8 kenh 7](/wiki-assets/images/module/board-mo-rong/images/servo_8_kenh_7.png)

    |
    Mỗi servo ứng với tên từ MS1-MS8, chúng ta sẽ thay đổi thông số góc trong khoảng từ 0-180 độ và tốc độ tùy chỉnh từ 1-100
    
    Chương trình điều khiển 3 servo kết nối với 3 chân trên mạch Yolo:Bit được thực hiện như sau:
![servo 8 kenh 8](/wiki-assets/images/module/board-mo-rong/images/servo_8_kenh_8.png)


        Link chương trình: [https://app.ohstem.vn/#!/share/yolobit/2vTU0PDwGd2dhp3N11E8c4aYxMX](https://app.ohstem.vn/#!/share/yolobit/2vTU0PDwGd2dhp3N11E8c4aYxMX)
    
    > **Ghi chú:** Khi nhấn nút A, cả 3 động cơ **servo 180 độ** sẽ quay đồng thời đến **góc 90 độ** với **tốc độ 100**. Ngược lại, khi nhấn nút B, các servo sẽ quay trở lại **góc 0 độ** cũng với tốc độ tương tự.
    
Dựa trên chương trình mẫu này, bạn hoàn toàn có thể **điều khiển từng động cơ servo một cách độc lập**, thiết lập **góc quay và tốc độ phù hợp** với từng nhiệm vụ cụ thể – chẳng hạn như đóng/mở cửa, điều khiển cánh tay robot, hay các chuyển động phức tạp khác trong mô hình của bạn.


**2.2. Quay servo thêm một góc nhỏ**

    Khối lệnh điều khiển servo quay thêm một góc nhỏ tùy chỉnh để tăng độ chính xác trong quá trình thực hiện dự án:
![servo 8 kenh 9](/wiki-assets/images/module/board-mo-rong/images/servo_8_kenh_9.png)

    |
    Chương trình được thực hiện như sau:
![servo 8 kenh 10](/wiki-assets/images/module/board-mo-rong/images/servo_8_kenh_10.png)


        Link chương trình: ](https://app.ohstem.vn/#!/share/yolobit/2vTVJrQI7acWr88uOehuAMd9PYr)
    
    > **Ghi chú:** Với chương trình này, người dùng chỉ cần nhất nút A + B, các servo sẽ quay thêm 1 góc nhỏ là 5 độ.
    
Ngoài ra, người dùng có thể cho servo quay thêm 1 góc nhỏ hoặc quay lùi bằng cách thêm dấu trừ "**-**" trước góc cần quay.
![servo 8 kenh 11](/wiki-assets/images/module/board-mo-rong/images/servo_8_kenh_11.png)
:align: center

Quay lùi một góc 5 độ


**2.3. Điều khiển servo 360 độ**

    Chương trình này chỉ phù hợp với servo 360 độ, người dùng cần lưu ý khi chọn servo để thực hiện. Việc kết nối vào các cổng của mạch lập trình được thực hiện tương tự như phần kết nối.
    
    Câu lệnh điều khiển servo 360 độ:
![servo 8 kenh 12](/wiki-assets/images/module/board-mo-rong/images/servo_8_kenh_12.png)

    |
    Chương trình điều khiển tốc độ quay của servo 360 độ:
![servo 8 kenh 13](/wiki-assets/images/module/board-mo-rong/images/servo_8_kenh_13.png)


        Link chương trình: [https://app.ohstem.vn/#!/share/yolobit/2vTW6i4QbLBFhZ5mYxpogqh2ql7](https://app.ohstem.vn/#!/share/yolobit/2vTW6i4QbLBFhZ5mYxpogqh2ql7)
    
    > **Ghi chú:** Khi nhấn nút A, servo 360 độ quay với tốc độ 100.
Khi nhấn nút B, servo quay lùi tốc độ 100.
Khi nút A + B, servo dừng hoạt động.


## 5. Lập trình với Yolo UNO
1. Tải thư viện **SERVO8CHS Kit**, bằng cách dán đường link sau vào phần tìm kiếm thư viện: ](https://github.com/AITT-VN/yolouno_extension_servo8chs)

    Xem hướng dẫn tải thư viện [tại đây ](https://docs.ohstem.vn/en/latest/module/thu-vien-yolouno.html)
![servo 8 kenh 5](/wiki-assets/images/module/board-mo-rong/images/servo_8_kenh_5.png)

    |
    
    Thư viện sẽ gồm các câu lệnh điều khiển servo như sau:
![servo 8 kenh 6](/wiki-assets/images/module/board-mo-rong/images/servo_8_kenh_6.png)

    |
    
2. **Viết chương trình:**

**2.1. Điều khiển servo quay đến góc cố định**

    Khối lệnh điều khiển servo quay tới góc chỉ định với tốc độ tùy chỉnh:
![servo 8 kenh 14](/wiki-assets/images/module/board-mo-rong/images/servo_8_kenh_14.png)


    Mỗi servo ứng với tên từ MS1-MS8, chúng ta sẽ thay đổi thông số góc trong khoảng từ 0-180 độ và tốc độ tùy chỉnh từ 1-100
    
    Chương trình điều khiển 3 servo kết nối với 3 chân trên mạch Yolo:Bit được thực hiện như sau:
![servo 8 kenh 8](/wiki-assets/images/module/board-mo-rong/images/servo_8_kenh_8.png)


        Link chương trình: [https://app.ohstem.vn/#!/share/yolouno/2vTYp3OUG9U3UakHnH8ZpozoYuj](https://app.ohstem.vn/#!/share/yolouno/2vTYp3OUG9U3UakHnH8ZpozoYuj)
    
    > **Ghi chú:** Khi nhấn nút A tại chân D9, cả 3 động cơ **servo 180 độ** sẽ quay đồng thời đến **góc 90 độ** với **tốc độ 100**. Ngược lại, khi nhấn nút B ở chân D10, các servo sẽ quay trở lại **góc 0 độ** cũng với tốc độ tương tự.
    
Dựa trên chương trình mẫu này, bạn hoàn toàn có thể **điều khiển từng động cơ servo một cách độc lập**, thiết lập **góc quay và tốc độ phù hợp** với từng nhiệm vụ cụ thể – chẳng hạn như đóng/mở cửa, điều khiển cánh tay robot, hay các chuyển động phức tạp khác trong mô hình của bạn.


**2.2. Quay servo thêm một góc nhỏ**

    Khối lệnh điều khiển servo quay thêm một góc nhỏ tùy chỉnh để tăng độ chính xác trong quá trình thực hiện dự án:
![servo 8 kenh 9](/wiki-assets/images/module/board-mo-rong/images/servo_8_kenh_9.png)

    |
    Chương trình được thực hiện như sau:
![servo 8 kenh 16](/wiki-assets/images/module/board-mo-rong/images/servo_8_kenh_16.png)


        Link chương trình: ](https://app.ohstem.vn/#!/share/yolouno/2vTYyjogcyl3m8RIkyLVqDhsSml)
    
    > **Ghi chú:** Với chương trình này, người dùng chỉ cần nhất nút Boot trên Yolo UNO, các servo sẽ quay thêm 1 góc nhỏ là 5 độ.
    
Ngoài ra, người dùng có thể cho servo quay thêm 1 góc nhỏ hoặc quay lùi bằng cách thêm dấu trừ "**-**" trước góc cần quay.
![servo 8 kenh 11](/wiki-assets/images/module/board-mo-rong/images/servo_8_kenh_11.png)
:align: center

Quay lùi một góc 5 độ


**2.3. Điều khiển servo 360 độ**

    Chương trình này chỉ phù hợp với servo 360 độ, người dùng cần lưu ý khi chọn servo để thực hiện. Việc kết nối vào các cổng của mạch lập trình được thực hiện tương tự như phần kết nối.
    
    Câu lệnh điều khiển servo 360 độ:
![servo 8 kenh 12](/wiki-assets/images/module/board-mo-rong/images/servo_8_kenh_12.png)

    |
    Chương trình điều khiển tốc độ quay của servo 360 độ:
![servo 8 kenh 17](/wiki-assets/images/module/board-mo-rong/images/servo_8_kenh_17.png)


        Link chương trình: [https://app.ohstem.vn/#!/share/yolouno/2vTZCgMLoZYTgMxDam3XvhdKE6I](https://app.ohstem.vn/#!/share/yolouno/2vTZCgMLoZYTgMxDam3XvhdKE6I)
    
    > **Ghi chú:** Khi nhấn nút A tại chân D9, servo 360 độ quay với tốc độ 100.
Khi nhấn nút B tại chân D10, servo quay lùi tốc độ 100.
Khi nút Boot trên Yolo UNO, servo dừng hoạt động.