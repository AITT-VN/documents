3. Bài 2: Robot Chó vẫy đuôi
=================================

.. image:: images/cho_vay_duoi.jpg
    :width: 400px
    :align: center  
|

1.  Hướng dẫn lắp ráp
---------------
-------------------------

.. raw:: html

 <iframe width="560" height="315" src="https://www.youtube.com/embed/o_aZV16-PoE" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
| 

2.  Cách thực hiện
---------------------------
----------------------

- Cho Robot đi thẳng liên tục.

- Khi gặp vật cản sẽ dừng lại, nháy đèn (bật đèn 2 bên và led RGB), vẫy đuôi (quay động cơ servo) và phát nhạc.


3. Viết chương trình 
-----------
------------------

1. Đầu tiên, chúng ta viết hàm thiết lập trạng thái mặc định của robot:

    - Tạo hàm **trở về mặc định**
    - Chọn ảnh mặc định HEART, tắt hết đèn 
    - Quay servo về góc sao cho vị trí đuôi robot là cân bằng. 
    - Cho robot di chuyển thẳng với tốc độ tùy chỉnh (nên chỉnh tốc độ dưới 50 để giảm quán tính khi robot dừng đột ngột). 

.. image:: images/bai_2.1.png
    :width: 500px
    :align: center  
|    

2. Tiếp theo, chúng ta viết hàm để robot có thể vẫy đuổi bao gồm

    - Tạo hàm **vẫy đuôi**
    - Robot dừng di chuyển và hiện hình ảnh Happy
    - Bật đèn và phát nhạc 
    - Thực hiện vãy đuôi liên tục 4 lần bằng cách: 

        + Quay chân servo đến góc 70, trong 600 milli giây. 
        + Tương tự, quay chân servo đến góc 180. 

.. image:: images/bai_2.2.png
    :width: 600px
    :align: center  
|  

3. Ở chương trình chính, ta liên tục đọc cảm biến khoảng cách, nếu: 

    - Nhỏ hơn 10cm: Thực hiện gọi hàm **vẫy đuôi**
    - Lớn hơn 10cm: Thực hiện gọi hàm **trở về mặc định**

.. image:: images/bai_2.3.png
    :width: 500px
    :align: center  
|

4. Chương trình mẫu
--------------
-------------------

- Robot Chó vẫy đuôi: `Tại đây <https://app.ohstem.vn/#!/share/yolobit/2DQ75ii2gyan1bVuXkFL4dktuLd>`_

.. image:: images/bai_2.4.png
    :width: 200px
    :align: center 
| 
