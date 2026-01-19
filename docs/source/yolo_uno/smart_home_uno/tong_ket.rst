9. Tổng kết
============

1. Mục tiêu
-----
--------

Ở các phần trước, bạn đã làm quen với các module và cách lập trình điều khiển chúng một cách đơn giản. Trong phần này, chúng ta sẽ ứng dụng những kiến thức đã học để xây dựng một mô hình nhà thông minh hoàn chỉnh, tích hợp nhiều chức năng tự động hóa, bao gồm:

- **Hệ thống chiếu sáng thông minh**

    - Bật/tắt đèn bằng **nút nhấn đôi**

    - **Đèn thông minh** – tự động bật/tắt dựa vào **cảm biến ánh sáng**

- **Hệ thống làm mát tự động**

    - **Quạt thông minh** – tự động điều chỉnh theo **nhiệt độ và độ ẩm** môi trường

- **Hệ thống kiểm soát ra vào**

    - **Cửa thông minh** – sử dụng **thẻ từ** để đóng/mở cửa an toàn

- **Kết nối và điều khiển từ xa**

    - **Nhận và gửi dữ liệu** lên **server IoT** để giám sát và điều khiển thiết bị từ xa

Với những chức năng này, mô hình sẽ mô phỏng một hệ thống Smart Home cơ bản, giúp bạn hiểu cách ứng dụng lập trình và cảm biến trong thực tế.


2. Kết nối phần cứng
-------
--------

Bảng tổng hợp các chân kết nối như sau: 

..  figure:: images/tong_ket_2.png
    :scale: 100%
    :align: center 
|

..  figure:: images/tong_ket_1.png
    :scale: 60%
    :align: center 
|

3. Chương trình lập trình
------
------

Link chương trình tổng thể cho dự án Smarthome với IoT :

`<https://app.ohstem.vn/#!/share/yolouno/2vFjbxeAluaGYAmf7bg32U4OO7X>`_

4. Nạp chương trình tham khảo:
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
