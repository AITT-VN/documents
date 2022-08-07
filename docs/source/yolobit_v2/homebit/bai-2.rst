5. Bài 2: Điều chỉnh độ sáng đèn
===================================

Mục tiêu
-------------------------
-------------------------

Ở bài đầu tiên, chúng ta biết cách bật tắt đèn LED trên Yolo:Bit bằng remote. Bây giờ, chúng ta hãy cùng tìm hiểu thêm cách điều chỉnh độ sáng đèn bằng remote và kết hợp chúng với bài 1 nhé!

- Nhấn nút ↑ trên remote để tăng độ sáng

- Nhấn nút ↓ trên remote để giảm độ sáng

Thiết bị cần dùng
--------------------------
--------------------------

- Mắt đọc IR

.. image:: images/homebit_23.1.png
    :width: 200px
    :align: center
|   
- Remote điều khiển 

.. image:: images/homebit_23.png
    :width: 200px
    :align: center
| 

Kết nối
------------
--------------

Kết nối **mắt đọc IR** vào cổng P1

.. image:: images/homebit_24.png
    :width: 500px
    :align: center
|    

  
Giới thiệu khối lệnh 
--------------------------
--------------------------

.. image:: images/homebit_29.png
    :width: 600px
    :align: center
|

Giới thiệu về biến
--------------------------
--------------------------

Để thay đổi độ sáng đèn LED tương ứng với điều khiển từ remote, chúng ta cần sử dụng đến biến. Có thể hiểu, biến như một chiếc hộp, nơi chứa giá trị mà ta cần sử dụng.

Mỗi hộp chỉ có thể chứa duy nhất một giá trị (chữ, số, chuỗi, dữ liệu) tại một thời điểm. Trong trường hợp này, biến sẽ chứa giá trị số, đại diện cho mức độ sáng của đèn. 

.. image:: images/homebit_30.png
    :width: 400px
    :align: center
|    


Cách tạo và sử dụng biến
---------------------------
---------------------------

1. Bạn cần vào mục Biến và chọn Tạo biến. Sau đó, điền tên cho biến mới để Tạo.

.. image:: images/homebit_31.png
    :width: 400px
    :align: center
|    
2. Khi tạo biến thành công, trong mục Biến sẽ xuất hiện những khối lệnh liên quan để làm việc với biến.

.. image:: images/homebit_32.png
    :width: 400px
    :align: center
|   


Viết chương trình
----------------------------
----------------------------

1. Tạo biến tên **độ sáng** để chứa giá trị độ sáng. Cho giá trị là 50

.. image:: images/homebit_33.png
    :width: 400px
    :align: center
|    
2. Tạo điều kiện: Nếu nút ↑ được nhấn, tăng giá trị độ sáng lên 25

.. image:: images/homebit_34.png
    :width: 600px
    :align: center
|    
3. Thay đổi giá trị độ sáng theo giá trị biến. Sau đó chọn màu đèn sáng là đỏ. Xóa tín hiệu ở cuối chương trình

.. image:: images/homebit_35.png
    :width: 600px
    :align: center
|    
4. Thực hiện tương tự. Nếu nút ↓ được nhấn, giảm giá trị độ sáng xuống 25 (-25)

.. image:: images/homebit_36.png
    :width: 600px
    :align: center
|    
5. Kết hợp với chương trình của bài 1 để hoàn thiện chương trình

.. image:: images/homebit_37.png
    :width: 600px
    :align: center
|    

Chương trình mẫu
---------------------
---------------------

- Điều chỉnh độ sáng đèn: `Tại đây <https://app.ohstem.vn/#!/share/yolobit/2Cvih3zEB0mBPESubn8On8NihS7>`_

.. image:: images/homebit_37.1.png
    :width: 200px
    :align: center
| 