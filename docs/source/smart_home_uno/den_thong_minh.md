# 3. Đèn thông minh

## 1. Mục tiêu
Chúng ta hãy cùng lập trình một chiếc đèn thông minh, có thể bật tắt tự động dựa vào ánh sáng nhé. Cụ thể, khi trời tối (độ sáng < 30%) thì đèn sẽ tự bật. Ngược lại, khi trời sáng thì đèn sẽ tự tắt.

## 2. Thiết bị cần sử dụng
- Mạch Yolo UNO:
![yolo uno](/wiki-assets/images/yolo_uno/smart_home_uno/images/yolo_uno.png)


- Đèn LED đơn kèm dây tín hiệu:
![led don](/wiki-assets/images/yolo_uno/smart_home_uno/images/led_don.png)


- Cảm biến ánh sáng kèm dây tín hiệu:
![cb anh sang](/wiki-assets/images/yolo_uno/smart_home_uno/images/cb_anh_sang.png)


## 3. Kết nối phần cứng
- Module LED đơn kết nối vào cổng D3 - D4

- Module cảm biến ánh sáng kết nối vào cổng A1 - A2
![3.2](/wiki-assets/images/yolo_uno/smart_home_uno/images/3.2.png)


## 4. Chương trình lập trình
- Câu lệnh điều kiện, khối lệnh nằm trong mục **LOGIC**:
![den thong minh 2](/wiki-assets/images/yolo_uno/smart_home_uno/images/den_thong_minh_2.png)


- Câu lệnh đọc kết quả của cảm biến ánh sáng, nằm trong mục **CẢM BIẾN**::
![den thong minh 3](/wiki-assets/images/yolo_uno/smart_home_uno/images/den_thong_minh_3.png)


- Câu lệnh đọc bắt đèn đèn LED đơn, nằm trong mục **HIỂN THỊ**::
![3.4](/wiki-assets/images/yolo_uno/smart_home_uno/images/3.4.png)


- **Chương trình lập trình:**
![3.3](/wiki-assets/images/yolo_uno/smart_home_uno/images/3.3.png)


    [https://app.ohstem.vn/#!/share/yolouno/2vFWXwvS5PbkhKooSzyJ0qrIkU8](https://app.ohstem.vn/#!/share/yolouno/2vFWXwvS5PbkhKooSzyJ0qrIkU8)
    
- **Giải thích chương trình:**  Sau khi thực hiện gửi chương trình lên Yolo UNO, đèn LED trên Yolo UNO sẽ chuyển sang đèn xanh. Hãy thử dùng tay che cảm biến ánh sáng, đèn LED sẽ sáng.
