2. 5. Robot tự đậu xe vào bãi xe số 3
=========

Trong dự án xBot này, bạn hãy viết chương trình để robot đậu xe vào đúng vị trí số 3 bằng cách nhận diện các vạch đen nằm ngang.


..  figure:: images/5.1.png
    :scale: 100%
    :align: center 
|

**1. Video minh họa**
------------
-----------


.. raw:: html

    <iframe width="640" height="360" src="https://www.youtube.com/embed/ZVskkC2hLfs" title="Robot tự động đậu xe" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
|

**Cách thực hiện:** 

    1. Cho xBot di chuyển theo đường line màu đen
    2. Dùng biến đếm để đếm số lần nhận vạch ngang
    3. Robot sẽ đến vị trí số 3 khi đếm = 3
    4. Robot cần xoay sang trái và tiến tới để vào đúng vị trí bãi đậu xe

**2. Chương trình hoàn chỉnh:**
------
------

..  figure:: images/5.2.png
    :scale: 100%
    :align: center 
|

**3. Giải thích chương trình:**
-----------
----------

Bạn cần tạo một biến tên là **“đếm“**. Ban đầu biến đếm sẽ được gán giá trị là 0:

..  figure:: images/5.3.png
    :scale: 100%
    :align: center 
|

Bật đèn LED màu xanh và chờ đến khi nút được nhấn, chương trình chính sẽ bắt đầu với khối lệnh lặp lại mãi:

..  figure:: images/5.4.png
    :scale: 100%
    :align: center 
|

Tạo câu lệnh điều kiện như trong chương trình:

..  figure:: images/5.5.png
    :scale: 100%
    :align: center 
|

Chúng ta sẽ lập trình để xBot di chuyển theo line:

    1. Khi vạch đen ở giữa (mắt s2, s3 thấy vạch đen): xBot đi thẳng
    2. Nếu vạch đen ở bên trái (mắt s1, s2 hoặc chỉ mắt s1 phát hiện vạch đen): Cho xBot rẽ trái
    3. Tương tự cho bên phải
    4. Nếu không, cho xBot di chuyển thẳng tới trước

..  figure:: images/5.6.png
    :scale: 60%
    :align: center 
|

Tạo thêm một điều kiện **nếu không nếu** ở giữa như hình:

..  figure:: images/5.7.png
    :scale: 70%
    :align: center 
|

Khi phát hiện vạch đen chắn ngang (4 mắt đọc đều thấy vạch đen), ta cho xBot tiến tới một chút và phát nốt nhạc G3 để báo hiệu, đồng thời cộng thêm 1 vào biến:

..  figure:: images/5.8.png
    :scale: 80%
    :align: center 
|

Nếu đếm = 3 (Xe đã tới vạch đen số 3), ta sẽ cho xBot dừng di chuyển trong 0,5 giây, sau đó đi tới và rẽ trái vào bãi đậu xe, đồng thời phát bài nhạc POWER_DOWN và tắt đèn LED và thoát khỏi chương trình:

..  figure:: images/5.9.png
    :scale: 90%
    :align: center 
|


**4. Tải chương trình mẫu**
---------------
---------

Bạn có thể sử dụng trực tiếp chương trình mẫu chúng tôi đã lập trình sẵn cho bạn tại đây. 


* :download:`Robot tự đậu xe vào bãi xe số 3 <https://app.ohstem.vn/#!/share/xbot/23J7ACsYCllrTZo6dEMfbZO19qw>`
