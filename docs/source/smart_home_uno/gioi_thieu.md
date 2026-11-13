# 1. Giới thiệu

## 1. Tổng quan dự án
Smart Home (nhà thông minh) là hệ thống tự động hóa giúp giám sát và điều khiển các thiết bị trong nhà như đèn, quạt, máy lạnh, cửa ra vào… thông qua các phương thức như smartphone, giọng nói hoặc cảm biến. Hệ thống này mang lại sự tiện lợi, tiết kiệm năng lượng và nâng cao chất lượng cuộc sống.
![index 1](/wiki-assets/images/yolo_uno/smart_home_uno/images/index_1.jpg)


Trong dự án này, người học sẽ xây dựng một mô hình **Smart Home** cơ bản bằng cách sử dụng mạch Yolo UNO, các module cảm biến, và kết nối với server IoT của OhStem. Thông qua quá trình thực hành, người học sẽ hiểu cách lập trình, thu thập dữ liệu từ cảm biến và điều khiển thiết bị từ xa, qua đó nắm vững nguyên lý hoạt động của một hệ thống nhà thông minh.

## 2. Các thiết bị cần sử dụng
Các thiết bị và chức năng của từng thiết bị trong dự án này như sau:


    :widths: 10, 15, 30
    
    1, "[Đèn 4 LED RGB ](https://shop.ohstem.vn/san-pham/module-4-led-rgb/)", "Đèn chiếu sáng"
    2, "[Đèn LED đơn ](https://shop.ohstem.vn/san-pham/den-led-don/)", "Bật tắt đèn"
    3, "[Nút nhấn đôi ](https://shop.ohstem.vn/san-pham/nut-nhan-doi/)", "Bật tắt đèn tự động theo độ sáng"
    4, "[Cảm biến ánh sáng ](https://shop.ohstem.vn/san-pham/cam-bien-anh-sang/)", "Theo dõi ánh sáng của môi trường"
    5, "[Cảm biến DHT20 ](https://shop.ohstem.vn/san-pham/cam-bien-dht20/)", "Theo dõi nhiệt độ và độ ẩm của môi trường"
    6, "[Màn hình LCD1602 ](https://shop.ohstem.vn/san-pham/man-hinh-lcd-1602/)", "Hiển thị các thông tin quan trắc môi trường"
    7, "[Quạt mini ](https://shop.ohstem.vn/san-pham/dong-co-quat-mini/)", "Quạt thông minh dựa trên nhiệt độ"
    8, "[Động cơ servo ](https://shop.ohstem.vn/san-pham/servo-micro-9g/)", "Đóng mở cửa"
    9, "RFID", "Khóa cửa thông minh bằng thẻ từ"
    10, "[Yolo UNO ](https://shop.ohstem.vn/san-pham/yolo-uno/)", "Mạch điều khiển các thiết bị hoạt động"
    11, "[Pin ](https://shop.ohstem.vn/san-pham/pin-sac-2s-dung-cho-robot-orc-k2/)", "Cấp nguồn"
    
Ngoài ra bạn đọc có thể tìm hiểu chi tiết hơn về mô hình dự án Smart Home với Yolo UNO [tại đây ](https://shop.ohstem.vn/san-pham/kit-stem-smart-home-tuy-chinh-tu-yolo-uno/).


## 3. Hướng dẫn lắp ráp
Trước khi đi vào phần lắp ráp hoàn thiện mô hình Smart Home, bạn đọc cần hiệu chỉnh servo về góc 0 độ trước khi lắp lên mô hình với các thao tác sau:

- Bước 1: Kết nối Servo 180 độ vào Yolo UNO ở chân D2:
![chinh servo 1](/wiki-assets/images/yolo_uno/smart_home_uno/images/chinh_servo_1.png)


- Bước 2: Gửi chương trình sau vào Yolo UNO để servo quay đến góc 0 độ:
![chinh servo 2](/wiki-assets/images/yolo_uno/smart_home_uno/images/chinh_servo_2.png)


    [https://app.ohstem.vn/#!/share/yolouno/2vQaLMuc5OcJseF3AOc2yUV76FQ](https://app.ohstem.vn/#!/share/yolouno/2vQaLMuc5OcJseF3AOc2yUV76FQ)
    
Sau khi chương trình được tải lên, mạch **Yolo UNO** sẽ nhanh chóng thực hiện các thao tác khởi động: **đèn đỏ bật sáng, servo quay về góc 0 độ**, rồi tiếp theo **đèn xanh được kích hoạt** để báo hiệu hoàn tất. Toàn bộ quá trình diễn ra trong thời gian rất ngắn, vì vậy bạn cần quan sát kỹ để nhận biết rõ từng bước.



[Hướng dẫn lắp ráp Nhà thông minh](https://app.ohstem.vn/#!/aib/view/cloud/arnapv27/)



Hoặc xem video hướng dẫn lắp ráp:



[Xem video](https://www.youtube.com/embed/xEiI1xdeYVc?si=eZJwl5RDQQpC9PgM)


