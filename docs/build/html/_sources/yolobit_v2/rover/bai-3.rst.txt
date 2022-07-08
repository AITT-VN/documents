7. Bài 3: Thắp sáng 
==================================

*Trời đã xế chiều, Rover cần đi qua một đường hầm tối để đến thành phố bên kia. Hãy giúp Rover bật đèn chiếu sáng khi trời tối để đi qua đường hầm.*


Mục tiêu 
----------------
-----------------------

1. Điều khiển đèn pha trên Rover
2. Hiểu biết và ứng dụng cảm biến ánh sáng trên Yolo:Bit
3. Biết cách sử dụng câu lệnh điều kiện
4. Làm quen với phép toán tử so sánh

Bộ phận điện tử
-----------------
-------------------------

- Cảm biến ánh sáng có thể cảm nhận cường độ ánh sáng của môi trường, cụ thể là sáng hoặc tối

.. image:: images/bai_3.1.png
    :width: 400px
    :align: center
|   
- Đèn LED có tác dụng phát sáng, Rover sử dụng đèn LED với chức năng là đèn pha

.. image:: images/bai_3.2.png
    :width: 200px
    :align: center
|

Giới thiệu khối lệnh 
-------------------------
-----------------------

- Khối lệnh điều kiện:

.. image:: images/bai_3.3.png
    :width: 1000px
    :align: center
|
- Khối lệnh so sánh:

.. image:: images/bai_3.4.png
    :width: 400px
    :align: center
|
- Khối lệnh độ sáng:

    Giá trị độ sáng được giới hạn trong khoảng từ 0-100.Trong đó: 80-100 là ánh sáng ngoài trời, 30-79 là ánh sáng trong phòng, 10-29 là ánh sáng tối, 0-9 là trời tối

.. image:: images/bai_3.5.png
    :width: 400px
    :align: center
|
- Khối lệnh bật đèn pha:

.. image:: images/bai_3.6.png
    :width: 400px
    :align: center
|
- Khối lệnh số: 

.. image:: images/bai_3.7.png
    :width: 400px
    :align: center
|

Viết chương trình
---------------------
------------------------

1. Tạo điều kiện: kiểm tra độ sáng môi trường, nếu trời tối (giá trị < 5)

.. image:: images/bai_3.8.png
    :width: 800px
    :align: center
|
2. Bật đèn khi điều kiện đúng, tắt đèn khi điều kiện sai, cho thời gian tạm dừng là 0,1s (100 milli giây)

.. image:: images/bai_3.9.png
    :width: 400px
    :align: center




