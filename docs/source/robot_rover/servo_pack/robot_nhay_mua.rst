4. Bài 3: Robot nhảy múa
=================================

.. image:: images/nhay_mua.jpg
    :width: 400px
    :align: center  
|

1.  Hướng dẫn lắp ráp
---------------
-------------------------

.. raw:: html

 <iframe width="560" height="315" src="https://www.youtube.com/embed/cH7bInUPFHE" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
| 

2.  Cách thực hiện
---------------------------
----------------------

- Cho Robot đi thẳng liên tục

- Khi gặp vật cản sẽ dừng lại, nháy đèn (bật đèn 2 bên và led RGB), nhảy múa (quay động cơ servo) và phát nhạc.


3. Viết chương trình 
-----------
------------------

1. Đầu tiên, chúng ta viết hàm thiết lập trang thái mặc định của robot: 

    - Tạo hàm **trở về mặc định**
    - Chọn ảnh mặc định HEART, tắt hết đèn. 
    - Quay servo về góc sao cho vị trí tay robot là cân bằng
    - Cho Robot di chuyển thẳng với tốc độ tùy chỉnh (nên chỉnh tốc độ dưới 50 để giảm quán tính khi robot dừng đột ngột).

.. image:: images/bai_3.1.png
    :width: 500px
    :align: center  
|

2. Tiếp theo, chúng ta viết hàm để Robot có thể nhảy múa bao gồm:

    - Tạo hàm **Nhảy múa**.
    - Dừng di chuyển và hiện hình ảnh Happy
    - Bật đèn và phát nhạc
    - Nhảy múa:

        + Quay chân servo đến góc 80, trong 500 milli giây. 
        + Tương tự, quay chân servo đến góc 160.  

.. image:: images/bai_3.2.png
    :width: 600px
    :align: center  
|

3. Ở chương trình chính, ta liên tục đọc cảm biến khoảng cách, nếu:

    - Nhỏ hơn 15cm: Thực hiện gọi hàm **Nhảy múa**
    - Lớn hơn 15cm: Thực hiện gọi hàm **trở về mặc định**

.. image:: images/bai_3.3.png
    :width: 500px
    :align: center  
|

4. Chương trình mẫu
--------------
-------------------

- Robot nhảy múa: `Tại đây <https://app.ohstem.vn/#!/share/yolobit/2DQ9JeugR4waQ0cVqWtE9UQu6YL>`_

.. image:: images/bai_3.4.png
    :width: 200px
    :align: center 
| 
