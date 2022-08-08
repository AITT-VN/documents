8. Bài 5: Cảnh báo trộm
=================================

Mục tiêu
-------------------
-------------------

Một ngôi nhà thông minh thì không thể thiếu tính năng cảnh báo trộm. Trong bài học này, chúng ta sẽ cùng lập trình một Smart Home có thể tự động phát ra âm thanh cảnh báo khi có người lạ xuất hiện trước nhà.
Bạn có thể dùng remote để bật, tắt chế độ cảnh báo này.

Thiết bị cần dùng
---------------------
---------------------

- Remote điều khiển 

.. image:: images/homebit_23.png
    :width: 200px
    :align: center
| 
- Cảm biến chuyển động PIR

.. image:: images/homebit_54.png
    :width: 200px
    :align: center
| 

Kết nối
---------------------
---------------------

- Kết nối cảm biến chuyển động PIR vào cổng P16

.. image:: images/homebit_55.png
    :width: 600px
    :align: center
|   


Giới thiệu khối lệnh
----------------------
----------------------

.. image:: images/homebit_56.png
    :width: 900px
    :align: center
|   
.. image:: images/homebit_57.png
    :width: 400px
    :align: center
|   
.. image:: images/homebit_58.png
    :width: 400px
    :align: center
|


Viết chương trình
---------------------
---------------------

1. Tạo một biến mới tên **cảnh báo** và cho giá trị ban đầu của biến cảnh báo là Sai (đồng nghĩa với chế độ cảnh báo đang tắt)

.. image:: images/homebit_59.png
    :width: 400px
    :align: center
|   
2. Khi nút E trên remote được nhấn, chế độ cảnh báo được bật (biến cảnh báo chuyển sang giá trị đúng)

.. image:: images/homebit_60.png
    :width: 600px
    :align: center
|   
3. Tiếp theo, Yolo:Bit hiện hình ảnh báo hiệu và xóa tín hiệu đã thu được từ remote.

.. image:: images/homebit_61.png
    :width: 600px
    :align: center
|   
4. Khi nút F trên remote được nhấn, tắt chế độ cảnh báo (đổi giá trị của biến cảnh báo thành Sai) và tắt toàn bộ đèn LED, đồng thời xóa tín hiệu từ remote:

.. image:: images/homebit_62.png
    :width: 600px
    :align: center
|   
5. Khi chế độ cảnh báo đang bật (cảnh báo = Đúng) và cảm biến PIR phát hiện có người, Yolo:Bit sẽ phát âm thanh cảnh báo

.. image:: images/homebit_63.png
    :width: 1000px
    :align: center
| 

Chương trình mẫu
---------------------
---------------------

- Cảnh báo trộm: `Tại đây <https://app.ohstem.vn/#!/share/yolobit/2CvnzA92HG5Q7ibi3BF2BIeSbAs>`_

.. image:: images/homebit_64.png
    :width: 200px
    :align: center
|

