4. Bài 1: Điều khiển đèn bằng Remote
=================================

Mục tiêu
---------------------
---------------------

Trong bài học đầu tiên, chúng ta sẽ sử dụng đèn LED trên Yolo:Bit để mô phỏng đèn chiếu sáng trong nhà, có thể bật tắt bằng remote hồng ngoại điều khiển từ xa:

- Nhấn nút A trên remote để bật đèn

- Nhấn nút C trên remote để tắt đèn
  
Thiết bị cần dùng
----------------------
----------------------

.. image:: images/homebit_23.png
    :width: 300px
    :align: center
|   
Kết nối
----------------------
----------------------

.. image:: images/homebit_24.png
    :width: 300px
    :align: center
|   
Kết nối mắt đọc IR vào cổng P1

Giới thiệu khối lệnh
----------------------
----------------------

.. image:: images/homebit_22.png
    :width: 800px
    :align: center
|    
Viết chương trình
---------------------
---------------------

1. Kéo khối lệnh điều kiện vào phần lặp lại mãi mãi

.. image:: images/homebit_25.png
    :width: 300px
    :align: center
|    
2. Nếu nút A được nhấn, đèn LED sẽ bật màu đỏ
   
**Cách thực hiện:**

- Kéo khối **cảm biến IR đọc được nút A** vào phần Nếu
  
- Kéo khối lệnh **đổi màu tất cả đèn LED** thành màu đỏ vào phần Thực hiện 

.. image:: images/homebit_26.png
    :width: 400px
    :align: center
|    
1. Xóa tín hiệu đã thu được từ remote (để không trùng lặp với tín hiệu sau đó)

.. image:: images/homebit_27.png
    :width: 400px
    :align: center
|    
4. Tương tự, lập trình để khi nút C được nhấn, đèn LED sẽ tắt (chuyển thành màu đen)

.. image:: images/homebit_28.png
    :width: 400px
    :align: center
|    