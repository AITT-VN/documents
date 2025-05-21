1. 2. Lỗi Rover tự hoạt động động cơ khi bật nguồn 
==================
Khi bật nguồn robot Rover, chúng ta thấy có 1 hoặc 2 động cơ chạy ngay lập tức, và robot cũng không khởi động lên.

Nguyên nhân:
    - Do có 1 chương trình khác không liên quan đến robot đang chạy bên trong mạch Yolo:Bit.
    - Do code robot có lỗi.

Cách xử lý:
    - Nếu robot đang được dùng trước đó, chúng ta cũng sẽ thao tác tải lại thư viện **Robot Rover** cho thiết bị (tham khảo hướng dẫn 1.1).
    - Sau khi đã tải lại xong thư viện, chúng ta khởi động lại robot, chờ robot có tín hiệu hoạt động (có đèn đỏ và tiếng chuông) thì đã khôi phục thành công robot.
