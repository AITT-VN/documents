# 3. Bài 2: Bãi đậu xe thông minh

## 1. Mục tiêu
Trong bài này, chúng ta sẽ cùng lập trình một bãi đậu xe thông minh có thể tự động mở thanh chắn để xe vào (nếu chỗ đậu xe còn trống). Nếu bãi xe đầy, đèn LED trên Yolo UNO sẽ đổi thành màu đỏ để báo hiệu và hiển thị số lượng chỗ trống trên màn hình OLED.

## 2. Kết nối
- Cảm biến vật cản (D9-D10)
![cityuno1 1](/wiki-assets/images/yolo_uno/thanh_pho_thong_minhyolouno/images/cityuno1_1.png)


- Cảm biến khoảng cách (D5-D6)
![cityuno1 2](/wiki-assets/images/yolo_uno/thanh_pho_thong_minhyolouno/images/cityuno1_2.png)


- Động cơ Servo (D11)
![cityuno1 3](/wiki-assets/images/yolo_uno/thanh_pho_thong_minhyolouno/images/cityuno1_3.png)


- Màn hình LCD OLED (I2C)
![cityuno4 2](/wiki-assets/images/yolo_uno/thanh_pho_thong_minhyolouno/images/cityuno4_2.png)


- **Kết nối:**
![bai 2.4](/wiki-assets/images/yolo_uno/thanh_pho_thong_minhyolouno/images/bai_2.4.png)


## 3. Lắp ráp mô hình
- Trước khi lắp ráp, bạn cần căn chỉnh Servo về góc 90 để hoạt động chính xác. Thực hiện như sau:

    1. Kết nối Servo vào chân D11 trên mạch Yolo UNO
    
    2. Kết nối Yolo UNO với Ohstem App và tiến hành lập trình.
    
    3. Tạo chương trình như hình minh họa
![cityuno1 4](/wiki-assets/images/yolo_uno/thanh_pho_thong_minhyolouno/images/cityuno1_4.png)


    4.  Nhấn nút chạy chương trình
    
    5. Ngắt kết nối Servo với nguồn điện (tránh vừa cắm điện vừa gắn làm quay Servo gây hư hại thiết bị)
    
    
- **Tiến hành lắp ráp**:
![bai 2.6](/wiki-assets/images/yolo_uno/thanh_pho_thong_minhyolouno/images/bai_2.6.png)


## 4. Giới thiệu khối lệnh
- Vào mục **Mở rộng**, tải thư viện **Màn hình OLED**:
![cityuno4 11](/wiki-assets/images/yolo_uno/thanh_pho_thong_minhyolouno/images/cityuno4_11.png)


- Khối lệnh kiểm tra khoảng cách:
![cityuno1 5](/wiki-assets/images/yolo_uno/thanh_pho_thong_minhyolouno/images/cityuno1_5.png)


- Khối lệnh điều khiển chân servo 180 độ:
![cityuno1 6](/wiki-assets/images/yolo_uno/thanh_pho_thong_minhyolouno/images/cityuno1_6.png)


- Khối lệnh xác định trạng thái cảm biến vật cản
![cityuno3 3](/wiki-assets/images/yolo_uno/thanh_pho_thong_minhyolouno/images/cityuno3_3.png)


- Khối lệnh tạm dừng (chờ):
![cityuno1 7](/wiki-assets/images/yolo_uno/thanh_pho_thong_minhyolouno/images/cityuno1_7.png)


## 5.  Giới thiệu về biến
- Để kiểm tra số chỗ đỗ xe còn lại, chúng ta cần sử dụng đến biến. Có thể hiểu, biến như một chiếc hộp, nơi chứa giá trị mà ta cần sử dụng.

- Mỗi hộp chỉ có thể chứa duy nhất một giá trị (chữ, số, chuỗi, dữ liệu) tại một thời điểm. Trong trường hợp này, biến sẽ chứa giá  trị số, đại diện cho số chỗ đậu xe còn lại.
![bai 2.14](/wiki-assets/images/yolo_uno/thanh_pho_thong_minhyolouno/images/bai_2.14.png)


**Cách tạo và sử dụng biến:**


    1. Bạn cần vào mục Biến và chọn Tạo biến. Sau đó, điền tên cho biến mới để tạo.
![bai 2.15](/wiki-assets/images/yolo_uno/thanh_pho_thong_minhyolouno/images/bai_2.15.png)


    2. Khi tạo biến thành công, trong mục Biến sẽ xuất hiện những khối lệnh liên quan để làm việc với biến.
![bai 2.16](/wiki-assets/images/yolo_uno/thanh_pho_thong_minhyolouno/images/bai_2.16.png)


## 6. Viết chương trình
1. Tạo một biến mới tên **“Số chỗ đậu xe”** và gán giá trị 2 vào biến (đồng nghĩa với bãi xe vẫn còn 2 chỗ trống):
![cityuno1 8](/wiki-assets/images/yolo_uno/thanh_pho_thong_minhyolouno/images/cityuno1_8.png)

    |
    
2. Tạo điều kiện: nếu bãi xe còn trống (cảm biến vật cản không bị che đi), biến số chỗ đậu xe > 0
![cityuno1 9](/wiki-assets/images/yolo_uno/thanh_pho_thong_minhyolouno/images/cityuno1_9.png)


        Khi bãi xe còn chỗ trống thì servo sẽ mở cánh barrier trong 3s để xe vào
    |
    
3. Tạo thêm 1 điều kiện lồng ghép: nếu phát hiện có xe (khoảng cách đến xe < 5cm)
![cityuno1 10](/wiki-assets/images/yolo_uno/thanh_pho_thong_minhyolouno/images/cityuno1_10.png)

    |
    
    Trong trường hợp bãi xe còn chỗ trống (biến số chỗ đậu xe > 0): quay Servo đến góc 20 độ để mở thanh chắn, tạm dừng 500 mili giây:
    
4. Trong trường hợp bãi xe đã đầy chỗ (biến = 0): servo sẽ không mở barrier cho xe khác vào.
![cityuno1 11](/wiki-assets/images/yolo_uno/thanh_pho_thong_minhyolouno/images/cityuno1_11.png)

    |
    
    
5. Sử dụng khối lệnh sau mỗi 1 giây kiểm tra cảm biến vật cản. Nếu trạng thái chân D9 là bật, tức là không có vật cản. Nếu trạng thái chân là TẮT, tức là có vật cản phía trên cảm biến biến số chỗ đậu xe sẽ thay đổi như sau:
![cityuno1 12](/wiki-assets/images/yolo_uno/thanh_pho_thong_minhyolouno/images/cityuno1_12.png)

    |
    
## 8. Chương trình mẫu
- Bãi đậu xe thông minh:
![cityuno1 13](/wiki-assets/images/yolo_uno/thanh_pho_thong_minhyolouno/images/cityuno1_13.png)


- Link chương trình: [https://app.ohstem.vn/#!/share/yolouno/2eImTbJnX7OTcXuia2a6kNi2i7O](https://app.ohstem.vn/#!/share/yolouno/2eImTbJnX7OTcXuia2a6kNi2i7O)