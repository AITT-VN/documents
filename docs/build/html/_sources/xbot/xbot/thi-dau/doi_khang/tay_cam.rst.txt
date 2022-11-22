7. 1. Lập trình tay cầm điều khiển 
==================

..  figure:: images/7.png
    :scale: 50%
    :align: center 

GamePad shield là bộ Kit mở rộng cho Yolo:Bit. Bộ kit này sẽ biến Yolo:Bit thành một tay cầm điều khiển Bluetooth. GamePad gồm Joystick và 7 nút nhấn có thể lập trình, được dùng để tạo ra các chức năng tùy biến theo ý của người dùng.

Ngoài ra, cùng với pin sạc và chức năng sạc được tích hợp sẵn trên board, GamePad shield có thể được sử dụng để điều khiển các robot của OhStem như robot xBot (thông qua Bluetooth) hoặc biến Yolo:Bit thành một chiếc máy chơi game hoàn chỉnh. 


**Thông số kỹ thuật của GamePad**
---------------
-----------

- **Nguồn:** Pin sạc Li-Ion 3.7V 14500
- **Joystick:** 2 axis analog (X: P0 Y: P1), 1 axis digital (Z: P2)
- **7 nút nhấn**: A (tương ứng với nút A trên Yolo:Bit), B (tương ứng với nút B trên Yolo:Bit), C (P13), D (P14), E (P15), F (P16), Z (nút nhấn của Joystick, P2)
- **Kích thước:** 154 × 56 mm

**Hướng dẫn lập trình cho GamePad shield**
----------
------


GamePad shield được dùng với Yolo:Bit. Bạn có thể tham khảo hướng dẫn lập trình cho Yolo:Bit `ở đây <https://docs.ohstem.vn/en/latest/yolobit_v2/lam-quen.html>`_ nếu chưa từng làm việc với Yolo:Bit trước đó.


**1. Cài đặt thư viện mở rộng cho GamePad**
--------------
-------


    1. Chọn thiết bị lập trình là Yolo:Bit trong OhStem App, tại địa chỉ `<https://app.ohstem.vn/>`_ hoặc ứng dụng OhStem App trên mobile (Tải trên Google Play / App Store với tên tìm kiếm là  “OhStem App”)

    ..  figure:: images/7.1.png
        :scale: 60%
        :align: center 

    2. Nhấn vào mục **Mở Rộng** ở danh sách bên trái:

    ..  figure:: images/7.2.png
        :scale: 80%
        :align: center 

    3. Chọn GamePad trong danh sách các mục mở rộng có sẵn (hoặc nhập tên GamePad vào ô tìm kiếm nếu bạn không thấy):

    ..  figure:: images/7.3.jpg
        :scale: 60%
        :align: center 

    Chọn tải thư viện:

    ..  figure:: images/7.4.png
        :scale: 80%
        :align: center 

    4. Chọn thiết bị Yolo:Bit để kết nối (nếu chưa kết nối) và phải đảm bảo đã cài đặt thư viện thành công (bên trái giao diện **xuất hiện danh mục GamePad** như hình):

    ..  figure:: images/7.5.png
        :scale: 80%
        :align: center 

**2. Giới thiệu khối lệnh**
----------
------

    Bên trong danh mục GamePad, bạn sẽ thấy có 3 khối lệnh: 

    ..  figure:: images/7.6.png
        :scale: 80%
        :align: center 

    - Joystick ở hướng -> : Trả về giá trị đúng khi hướng của cần gạt Joystick xoay sang phải (tương tự với các lựa chọn khác)
    - Đọc Joystick ___: Đọc thông tin từ cần gạt Joystick gửi đến
    - Nút ___ được nhấn: Đọc thông tin từ các nút trên GamePad gửi đến (nút nào được nhấn)


**Joystick ở hướng ->**

    Bạn có thể chọn vào icon hình tam giác ngược trong khối lệnh để hiển thị các lựa chọn khác:

    ..  figure:: images/7.7.png
            :scale: 80%
            :align: center 

    Khối lệnh trên sẽ trả về giá trị đúng khi cần gạt Joystick xoay về đúng hướng như trong khối lệnh. 

**Đọc Joystick**

    Bạn có thể chọn vào icon hình tam giác ngược trong khối lệnh để hiển thị các lựa chọn khác:

    ..  figure:: images/7.8.png
            :scale: 80%
            :align: center 

    - X: Trả về giá trị Analog cho **trục X (trục ngang)** của Joystick theo thang giá trị từ -100 đến 100

    ..  figure:: images/7.9.jpg
            :scale: 80%
            :align: center 

    - Y: Trả về giá trị Analog cho trục Y (trục dọc) của Joystick theo thang giá trị từ -100 đến 100. 

    ..  figure:: images/7.10.jpg
            :scale: 80%
            :align: center 

    - Góc quay: Trả về giá trị góc xoay của cần gạt Joystick theo thang đo từ 0 đến 359 độ:

    ..  figure:: images/7.11.jpg
            :scale: 80%
            :align: center 

    - Khoảng cách kéo: Mức độ kéo Joystick ra ngoài so với tâm của cần gạt (từ 0 – 100%)

    ..  figure:: images/7.12.jpg
            :scale: 80%
            :align: center 


**Nút ____ được nhấn**

    Bạn có thể chọn vào icon hình tam giác ngược trong khối lệnh để hiển thị các lựa chọn khác:

    ..  figure:: images/7.13.jpg
            :scale: 80%
            :align: center 

    Khối lệnh trên sẽ trả về giá trị đúng khi nút Joystick được nhấn (bạn nhấn mạnh vào cần gạt Joystick để thực hiện). Tương tự với các nút nhấn khác.

    **Lưu ý:** Nút nhấn A và B trên GamePad sẽ tương ứng với nút A, B trên Yolo:Bit.
    

**3. Lập trình cơ bản với Yolo:Bit**
-----------
--------

Để làm quen với GamePad, chúng ta sẽ lập trình một chương trình đơn giản với Yolo:Bit:

    - Khi nút bất kỳ được nhấn, tên nút đó sẽ được hiển thị ra màn hình ma trận LED 5×5 trên Yolo:Bit
    
    - Khi cần gạt Joystick được xoay về hướng nào, ma trận LED sẽ hiển thị mũi tên chỉ về hướng đó. Đồng thời, trên cửa sổ thông tin sẽ hiển thị ra giá trị góc quay của cần gạt.

Để thực hiện điều này, chúng ta sẽ sử dụng khối lệnh Nút ____ được nhấn và khối lệnh Joystick ở hướng ___ 


**4. Nạp chương trình hoàn chỉnh**
--------------
-------

Bạn có thể sử dụng trực tiếp chương trình mẫu chúng tôi đã lập trình sẵn cho bạn: 

* :download:`Tại đây <https://app.ohstem.vn/#!/share/yolobit/22dRxWKg7y1vRI2y73DEKXygbyd>`


**Hướng dẫn lập trình**
------------


1. Đầu tiên, chúng ta xóa màn hình trước đó:

..  figure:: images/7.14.jpg
    :scale: 80%
    :align: center 

2. Nếu nút A được nhấn, màn hình Yolo:Bit sẽ hiển thị chữ A:

..  figure:: images/7.15.jpg
    :scale: 80%
    :align: center 

3. Ta thực hiện tương tự với các nút còn lại:

..  figure:: images/7.16.png
    :scale: 80%
    :align: center 

4. Đặt điều kiện: Nếu Joystick xoay về hướng bên phải:

..  figure:: images/7.17.jpg
    :scale: 80%
    :align: center 

5. Lúc này, Yolo:Bit sẽ hiển thị hình ảnh mũi tên chỉ sang phải:

..  figure:: images/7.18.jpg
    :scale: 80%
    :align: center 

6. Nhấn vào icon hình bánh răng và tạo thêm 3 nhánh điều kiện **Nếu không nếu** như hình:

..  figure:: images/7.19.jpg
    :scale: 80%
    :align: center 

**Giải thích thêm:**

Điều kiện “nếu không nếu” là một điều kiện gộp giữa “nếu không” và “nếu”:

..  figure:: images/7.20.jpg
    :scale: 80%
    :align: center 

7. Tương tự, ta cho Yolo:Bit hiển thị mũi tên tương ứng với từng hướng xoay của Joystick trong thuật toán:

..  figure:: images/7.21.png
    :scale: 80%
    :align: center 

8. Hiển thị thông tin góc xoay ra cửa sổ thông tin và cập nhật liên tục sau mỗi 200ms (1 giây = 1000ms):

..  figure:: images/7.22.jpg
    :scale: 80%
    :align: center 

.. note:: 

    Để hiển thị cửa sổ thông tin, bạn hãy nhấn vào nút chức năng nâng cao (biểu tưởng bánh răng), chọn Hiển thị cửa sổ thông tin để mở cửa sổ hiển thị thông tin như sau: 

    ..  figure:: images/7.23.png
        :scale: 80%
        :align: center 

