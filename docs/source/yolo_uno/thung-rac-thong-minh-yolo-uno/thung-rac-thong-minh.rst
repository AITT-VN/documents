4. Thực hiện dự án
=================================

1. Mục tiêu:
------------
-----------------

Trong bài này, chúng ta sẽ cùng lập trình một hệ thống phân loại rác thải qua camera AI.


2. Kết nối 
----------
--------------

- Module camera AI version 2 (Chân D9-D10)

    .. image:: images/trash03.png
        :width: 150px
        :align: center 
    |
- Module SoundPlayer (D3-D4)

    .. image:: images/trash04.png
        :width: 150px
        :align: center 
    |
- Màn hình LCD1602 (I2C)

    .. image:: images/trash05.png
        :width: 150px
        :align: center 
    |
- 3 Servo 180 độ (D2-D11-D12)
    .. image:: images/trash06.png
        :width: 150px
        :align: center 
    |
- **Kết nối:**

    .. image:: images/trash07.png
        :scale: 100%
        :align: center 
|


3. Thực hiện 
-----------
----------------
- Trước khi lắp ráp, bạn cần căn chỉnh Servo về góc 0 (vị trí đóng nắp thùng rác) để hoạt động chính xác. Thực hiện như sau:

    1. Kết nối Servo vào chân D11 trên mạch Yolo UNO(thực hiện tương tự ở 3 chân servo còn lại)

    2. Kết nối Yolo UNO với Ohstem App và tiến hành lập trình.

    3. Tạo chương trình như hình minh họa

.. image:: images/trash08.png
    :scale: 100%
    :align: center 
|

    4.  Nhấn nút chạy chương trình 

    5. Ngắt kết nối Servo với nguồn điện (tránh vừa cắm điện vừa gắn làm quay Servo gây hư hại thiết bị)


4. Giới thiệu khối lệnh
----------
----------------

- Khối lệnh điều khiển loa phát nhạc:

.. image:: images/trash10.png
    :scale: 90%
    :align: center 
|

**Dự án này chúng ta sẽ thống nhất cách nhận kết quả phân loại rác qua IoT server OhStem**



5. Cấu hình cài đặt module camera AI/camera OhStem App:
-----------
----------------

- Bạn xem cách cấu hình/sử dụng tính năng camera AI ở hướng dẫn trước

Viết chương trình
------------
--------------------

1. Đầu tiên sẽ cài đặt góc cho 4 servo về 0 độ (vị trí đóng nắp thùng)

.. image:: images/trash11.png
    :scale: 80%
    :align: center

|

2. Tạo 3 biến cho 3 loại rác thải, 3 biến này sẽ hiển thị trên màn hình lúc phân loại rác.

.. image:: images/trash12.png
    :scale: 100%
    :align: center 
|

3. Khởi tạo Module phát nhạc tại chân D3-D4, mở âm lượng 30 (tối đa)

.. image:: images/trash13.png
    :scale: 100%
    :align: center 
|

4. Kết nối wifi và server để nhận thông tin phân loại AI

.. image:: images/trash14.png
    :scale: 100%
    :align: center 
|

5. Giả sử trong bước thiết lập cài đặt IoT của camera AI bạn gửi lên kênh V1. Vậy để thiết bị nhận thông tin điều khiển bạn cũng sẽ đăng ký kênh V1:

.. image:: images/trash15.png
    :scale: 100%
    :align: center 
|

6. Chúng ta sẽ so sánh thông tin nhận được với loại rác mà mình đã đặt để phân loại, sử dụng câu lệnh Nếu:

.. image:: images/trash16.png
    :scale: 100%
    :align: center 
|
7. Khi kết quả đúng, chúng ta sẽ cho servo quay đến góc mở (có thể là 90 hoặc 1 vị trí khác tùy theo vị trí bạn lắp servo đóng nắp) và phát bài nhạc theo thứ tự âm thanh đã lưu vào loa, âm thanh sẽ được phát ra khi nhận diện đúng loại rác

.. image:: images/trash17.png
    :scale: 100%
    :align: center 
|
8. Chúng ta cũng có thể hiện lên số lần phân loại rác tương ứng  bằng cách cho biến cộng vào 1 khi phân loại đúng và in ra màn hình

.. image:: images/trash18.png
    :scale: 100%
    :align: center 
|

9. Thực hiện tương tự với 3 loại rác còn lại

.. image:: images/trash19.png
    :scale: 80%
    :align: center 
|
.. image:: images/trash20.png
    :scale: 80%
    :align: center 
|

- Link chương trình mẫu: `<https://app.ohstem.vn/#!/share/yolouno/35gNXQ1lHXaS4WeScnFTM1NRrWk>`_


6. Nạp chương trình tham khảo:
---------
-------------

Sau khi ấn vào đường liên kết của chương trình trên, sẽ xuất hiện 1 cửa sổ trang web có chương trình tham khảo hiển thị như hình:

..  figure:: images/napcode_1.png
    :scale: 60%
    :align: center 
|

Sau đó bạn ấn vào nút **IMPORT PROJECT** ở góc trên bên trái phần mềm lập trình như hình minh họa:

..  figure:: images/napcode_2.png
    :scale: 60%
    :align: center 
|

Thay đổi thông tin wifi để mạch Yolo UNO kết nối được Wifi (lưu ý cần đảm bảo kết nối vào mạng wifi băng tầng 2.4Ghz)

..  figure:: images/napcode_3.png
    :scale: 100%
    :align: center 
|

Sau đó bạn kết nối với máy tính và mạch Yolo UNO thông qua kết nối USB như hình minh họa:

..  figure:: images/co_ban_4.png
    :scale: 60%
    :align: center 
|

Chọn vào biểu tượng kết nối USB và kết nối vào thiết bị có tên **Espressif CDC Device (Com X)** với X là 1 số bất kỳ như hướng dẫn:

..  figure:: images/napcode_4.png
    :scale: 100%
    :align: center 
|
..  figure:: images/co_ban_5.png
    :scale: 100%
    :align: center 
|
..  figure:: images/co_ban_6.png
    :scale: 100%
    :align: center 
|

Sau đó chạy thử chương trình bằng cách ấn vào biểu tưởng nút tam giác Play như hình 

..  figure:: images/napcode_5.png
    :scale: 60%
    :align: center 
|

Khi chương trình đã hoạt động, bạn cần lưu chương trình vào thiết bị, sau khi lưu xong chỉ cần khởi động hệ thống, cấp nguồn là hệ thống hoạt động

..  figure:: images/co_ban_10.png
    :scale: 100%
    :align: center 
|
