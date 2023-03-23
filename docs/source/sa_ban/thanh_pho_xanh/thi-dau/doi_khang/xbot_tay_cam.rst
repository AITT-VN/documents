7. 2. Lập trình robot xBot với tay cầm điều khiển
=================

Chúng ta sẽ lập trình GamePad để điều khiển cho xBot, sao cho:

    - Khi kéo cần gạt Joystick sang trái, phải, trên, dưới thì xBot sẽ di chuyển theo hướng tương ứng.
    - Nhấn nút A để tiến hành tìm và kết nối Bluetooth đến xBot
    - Nhấn nút B để ngắt kết nối
    - Nhấn nút C để mở tay gắp (cho Servo nối với cổng S1 quay đến góc 0 độ)
    - Nút E để mở tay gắp (cho Servo nối với cổng S1 quay đến góc 90 độ)

..  figure:: images/7.24.png
    :scale: 80%
    :align: center 


Chương trình mặc định khi khởi động của xBot (trong Firmware mới nhất) đã hỗ trợ điều khiển từ Bluetooth nếu nhận được các ký tự sau:

    - “F = xx” với xx là số từ 0-100: xBot di chuyển về phía trước (F=Forward) với tốc độ xx
    - “B = xx” với xx là số từ 0-100: xBot di chuyển về phía sau (B=Backward) với tốc độ xx
    - “L = xx” với xx là số từ 0-100: xBot quay về bên trái (L=Left) với tốc độ xx
    - “R = xx” với xx là số từ 0-100: xBot di chuyển về bên phải (R=Right) với tốc độ xx
    - “S1=xx” với S1 là tên cổng Servo cần điều khiển (bạn có thể chọn từ S1 đến S8 tùy thích), xx là góc quay (0-180 độ) muốn điều khiển
    - “S=0”: xBot đứng yên tại chỗ (S=Stop)


Ví dụ: Khi bạn sử dụng khối lệnh sau, robot xBot sẽ di chuyển tới với tốc độ 50:

..  figure:: images/7.25.jpg
    :scale: 80%
    :align: center 


**Nạp chương trình hoàn chỉnh**
---------
-------

Trước khi tìm hiểu cách lập trình, bạn có thể sử dụng trực tiếp chương trình mẫu chúng tôi đã lập trình sẵn cho bạn: 

* :download:`Tại đây <https://app.ohstem.vn/#!/share/yolobit/22dWk3SIq1dSrdaHTbd3O7Eip2J>`


**Hướng dẫn lập trình**
---------
------------

1. Xóa màn hình trước đó:

..  figure:: images/7.26.jpg
    :scale: 80%
    :align: center 


2. Khi nút A được nhấn, Yolo:Bit sẽ hiển thị hình ảnh trái tim, đồng thời bắt đầu kết nối Bluetooth với xBot:

..  figure:: images/7.27.jpg
    :scale: 80%
    :align: center 

**Giải thích thêm:**

“ohstem-xbot-83fc” là tên của robot xBot, mỗi một thiết bị xBot sẽ có cái tên khác nhau.

Để biết tên robot của mình, bạn có thể bật Bluetooth (và cả vị trí đối với Android) và quét, tên của xBot sẽ hiển thị dưới dạng “ohstem-xbot-………” như hình:

..  figure:: images/7.28.jpg
    :scale: 80%
    :align: center 


Bạn cũng có thể đổi tên xBot thành tên mình thích để dễ nhớ và phân biệt chúng với các thiết bị xBot khác. Thực hiện như sau:

Nhấn vào icon Hướng dẫn lập trình Game Pad và chọn mục Đổi tên thiết bị như hình dưới:

..  figure:: images/7.29.jpg
    :scale: 80%
    :align: center 

Nhập tên bạn thích và nhấn lưu:

..  figure:: images/7.30.jpg
    :scale: 80%
    :align: center 

3. Nếu nút B được nhấn, tiến hành ngắt kết nối với xBot:

..  figure:: images/7.31.jpg
    :scale: 80%
    :align: center 

4. Khi kết nối / ngắt kết nối với xBot thành công, màn hình LED của Yolo:Bit sẽ hiển thị dòng chữ YES hoặc NO để báo hiệu:

..  figure:: images/7.32.jpg
    :scale: 80%
    :align: center 

5. Đặt điều kiện: Nếu Joystick được kéo sang phải:

..  figure:: images/7.33.jpg
    :scale: 80%
    :align: center 


**Lưu ý:** Bạn sử dụng khối lệnh Nếu / thực hiện / Nếu không nhé!

..  figure:: images/7.34.jpg
    :scale: 80%
    :align: center 

6. Khi đó, thông tin “R” sẽ được hiển thị lên cửa sổ thông tin, đồng thời robot sẽ xoay sang phải với tốc độ bằng khoảng cách kéo chia 2:

..  figure:: images/7.35.jpg
    :scale: 80%
    :align: center 

7. Nhấn vào icon hình bánh răng và tạo thêm 3 nhánh điều kiện **Nếu không nếu** như hình:

..  figure:: images/7.36.jpg
    :scale: 80%
    :align: center 

8. Thực hiện tương tự với các hướng quay khác của Joystick:

..  figure:: images/7.37.jpg
    :scale: 80%
    :align: center 

9. Nếu không có trường hợp nào phía trên đúng, ta cho xBot dừng lại:

..  figure:: images/7.38.jpg
    :scale: 80%
    :align: center 

10. Khi nút C được nhấn, tay gắp sẽ mở (Servo chân S1 quay về góc 0 độ):

..  figure:: images/7.39.jpg
    :scale: 80%
    :align: center 

11. Tạo thêm khối Nếu không nếu và lập trình khi nút E được nhấn, tay gắp sẽ đóng lại (quay Servo đến góc 90 độ):

..  figure:: images/7.40.png
    :scale: 60%
    :align: center 

12. Tạm dừng toàn chương trình trong 50ms (1 giây = 1000ms)

..  figure:: images/7.41.png
    :scale: 60%
    :align: center 
