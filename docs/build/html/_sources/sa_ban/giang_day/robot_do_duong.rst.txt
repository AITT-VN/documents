2. 3. Robot dò đường
=============

Bài viết này sẽ hướng dẫn lập trình robot dò đường chi tiết cho bạn, dựa trên cảm biến 4 mắt hồng ngoại của robot xBot.


**1. Video hướng dẫn lập trình:**
------------
-----------

.. raw:: html

    <iframe width="560" height="315" src="https://www.youtube.com/embed/vqmaeJPxfxE" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

|


**2. Chương trình hoàn chỉnh:**
------
------

..  figure:: images/3.2.png
    :scale: 100%
    :align: center 
|

**Lưu ý:** Để robot chạy ổn định và không bị chệch khỏi đường vạch, bạn nên giảm tốc độ di chuyển và thử nghiệm cho đến khi đạt được kết quả tốt nhất.


**3. Giải thích chương trình:**
-----------
----------

Chúng ta sẽ thêm phần khối lệnh chờ nút nhấn được nhấn để bắt đầu chương trình:

..  figure:: images/1.3.png
    :scale: 100%
    :align: center 
|

Ở bài học này ta sẽ sử dụng khối chức năng chính là đọc trạng thái của 2 trong 4 mắt đọc của cảm biến dò line (2 mắt ngoài cùng là S1 và S4).

..  figure:: images/3.3.png
    :scale: 100%
    :align: center 
|

Dựa vào yêu cầu, xBot sẽ hoạt động theo bảng phân tích sau:

..  figure:: images/3.4.png
    :scale: 100%
    :align: center 
|

Từ đó, ta có khối lệnh tương ứng:

..  figure:: images/3.5.png
    :scale: 90%
    :align: center 
|

Khối lệnh điều kiện như trên được tạo thêm bằng cách nhấn vào biểu tượng Cài đặt màu xanh dương đậm ngay góc trái của khối lệnh:

..  figure:: images/3.6.png
    :scale: 100%
    :align: center 
|


**4. Tải chương trình mẫu**
---------------
---------

Bạn có thể sử dụng trực tiếp chương trình mẫu chúng tôi đã lập trình sẵn cho bạn tại đây. 


* :download:`Robot dò đường <https://app.ohstem.vn/#!/share/xbot/1yX3o0Exnmm0hrnyvRbJEFRGp8B>`