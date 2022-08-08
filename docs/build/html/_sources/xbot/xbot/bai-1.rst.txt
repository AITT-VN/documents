5. Bài 1: Cùng di chuyển nào
<<<<<<< HEAD
====================================

**Mục tiêu:**

Hiểu về động cơ và các khối lệnh giúp cho xBot có thể di chuyển theo ý muốn.

5.1 Giới thiệu về động cơ
-----------------
-----------------

Để điều khiển xBot di chuyển, bạn cần hiểu về động cơ và cách hoạt động của chúng. 

Các động cơ này sẽ giúp cho xBot di chuyển tự do nhiều hướng (tiến tới, lùi lại, rẽ trái, rẽ phải) hoặc thực hiện một tác vụ phức tạp nào đó theo yêu cầu.

.. image:: images/xbot_bai_1.1.png
    :width: 600px
    :align: center
|   
**Động cơ có trên xBot**

.. image:: images/xbot_bai_1.2.png
    :width: 700px
    :align: center
| 


5.2 Khối kệnh điều khiển động cơ
---------------------
---------------------

Để điều khiển động cơ, bạn sẽ dùng các khối lệnh theo những cách sau:

- **Cách 1: Điều khiển 2 động cơ cùng lúc**

.. image:: images/xbot_bai_1.3.png
    :width: 700px
    :align: center
|   
Bạn hãy thử đặt xBot xuống nền nhà và chạy thử lệnh trên xem robot di chuyển đúng không nhé.

Ngoài ra, bạn cũng có thể sử dụng khối lệnh di chuyển với thời gian vô hạn sau:

.. image:: images/xbot_bai_1.4.png
    :width: 700px
    :align: center
| 
.. image:: images/xbot_bai_1.5.png
    :width: 700px
    :align: center
| 

- **Cách 2: Điều khiển từng động cơ riêng biệt**

Bạn cũng có thể điều khiển từng động cơ riêng biệt để xBot di chuyển theo ý muốn.

.. image:: images/xbot_bai_1.6.png
    :width: 700px
    :align: center
|   
.. image:: images/xbot_bai_1.7.png
    :width: 700px
    :align: center
| 
.. image:: images/xbot_bai_1.8.png
    :width: 700px
    :align: center
| 

- **Mô tả**

1. Tốc độ quay của mỗi động cơ có giá trị từ -100 đến 100. 

    ◼ Tốc độ > 0: Động cơ quay thuận chiều, xBot đi tới.

    ◼ Tốc độ < 0: Động cơ quay ngược chiều, xBot lùi lại.

2. Giá trị tốc độ càng lớn thì động cơ quay càng nhanh.


5.3 Viết chương trình di chuyển
-----------------------
-----------------------

- **Chương trình 1:** Ở trên xBot có một nút nhấn, khi nút được nhấn, xBot di chuyển về phía trước 1 giây và sau đó lùi lại 1 giây. 

.. image:: images/xbot_bai_1.10.png
    :width: 500px
    :align: center
| 
**Khối lệnh chương trình**

.. image:: images/xbot_bai_1.11.png
    :width: 600px
    :align: center
| 
**Sơ đồ hoạt động**

.. image:: images/xbot_bai_1.12.png
    :width: 500px
    :align: center
|  


- **Chương trình 2:** Khi nút được nhấn, xBot sẽ rẽ sang trái trong 1 giây và sau đó rẽ sang phải trong 1 giây.

**Sơ đồ hoạt động**

.. image:: images/xbot_bai_1.13.png
    :width: 200px
    :align: center
|  
**Khối lệnh chương trình**

.. image:: images/xbot_bai_1.14.png
    :width: 600px
    :align: center
|  
- **Chương trình 3**: Khi nút được nhấn, chương trình hoạt động theo mô tả sau:

1. Quay động cơ trái trong vòng 1 giây (dừng động cơ phải)

2. Quay động cơ phải trong vòng 1 giây (dừng động cơ phải)

3. Dừng cả 2 động cơ

  
**Sơ đồ hoạt động**

.. image:: images/xbot_bai_1.15.png
    :width: 200px
    :align: center
|    
**Khối lệnh chương trình**

.. image:: images/xbot_bai_1.16.png
    :width: 600px
    :align: center
| 


5.4 Chương trình mở rộng
----------------------
----------------------

Trong phần trước, bạn đã biết cách điều khiển xBot di chuyển đơn giản. 

Trong phần này, bạn hãy thử viết một chương trình phức tạp hơn: **Cho xBot di chuyển theo hình vuông sau khi được nhấn** như hình bên cạnh.

**Điều kiện**: *xBot sẽ tiến tới và rẽ sau mỗi 2 giây.*

.. image:: images/xbot_bai_1.17.png
    :width: 200px
    :align: center
|    
**Bước 1**: Cho xBot tiến tới 2 giây vẽ rẽ phải 0.5 giây.

.. image:: images/xbot_bai_1.18.png
    :width: 600px
    :align: center
| 
*Bạn cần thử nghiệm và chỉnh sửa thời gian rẽ phải để xBot có thể rẽ được một góc vuông. Thời gian này sẽ khác nhau tùy thuộc vào địa hình và dung lượng pin của xBot.*

**Bước 2**: Tạo ra 4 bản sao của thao tác di chuyển, ứng với 4 cạnh hình vuông.

.. image:: images/xbot_bai_1.19.png
    :width: 600px
    :align: center
|   
Sau khi chạy chương trình, hãy đặt xBot lên mặt phẳng rộng và nhấn nút để bắt đầu di chuyển.

Do nhiều yếu tố, xBot sẽ không thể chạy hình vuông chính xác. Bạn cần tinh chỉnh tốc độ (càng chậm càng chính xác) và thời gian rẽ để đường đi giống hình vuông nhất.

5.5 Bài tập mở rộng
-------------------
--------------------

Chúng ta thấy chương trình ở phần 3-4 khá dài, có 2 khối lệnh tiến tới và rẽ phải được lặp lại 4 lần. Để rút gọn chương trình, bạn có thể sử dụng khối lệnh lặp lại 4 lần.

Chương trình khi đó sẽ như sau:

**Sơ đồ hoạt động**

.. image:: images/xbot_bai_1.20.png
    :width: 200px
    :align: center
| 
**Khối lệnh chương trình**

.. image:: images/xbot_bai_1.21.png
    :width: 600px
    :align: center
|  


5.6 Câu hỏi ôn tập
-----------------
----------------

1. Công dụng của động cơ trên xBot là gì?

2. Có bao nhiều cách để lập trình điểu khiển động cơ? Liệt kê những khối lệnh cần dùng.
=======
====================================
>>>>>>> main
