1. 1. Lỗi bật Rover lên nhưng không có tín hiệu hoạt động 
==================
Khi bật nguồn robot Rover, chúng ta chờ robot khởi động nhưng sau 1 thời gian chờ robot vẫn không hoạt động.

Nguyên nhân:
    - Do robot chưa có chương trình hoạt động
    - Do có 1 chương trình khác không liên quan đến robot đang chạy bên trong mạch Yolo:Bit.
    - Do code robot có lỗi.

Cách xử lý:
    - Nếu như lần đầu tiên sử dụng robot, bạn cần tải thư viện robot Rover cho app lập trình và thiết bị. Tham khảo hướng dẫn tại đây https://docs.ohstem.vn/en/latest/robot_rover/rover/cai-dat-thu-vien.html
    - Nếu robot đang được dùng trước đó, chúng ta cũng sẽ thao tác tải lại thư viện **Robot Rover** cho thiết bị.
    - Sau khi đã tải lại xong thư viện, chúng ta khởi động lại robot, chờ robot có tín hiệu hoạt động (có đèn đỏ và tiếng chuông) thì đã khôi phục thành công robot.
