<<<<<<< HEAD
4. Hướng dẫn viết chương trình
=====================

Chúng ta hãy viết một chương trình đơn giản để điều khiển 2 đèn LED đa màu có trên xBot.

Trước tiên bạn cần làm quen với đèn LED RGB và các khối lệnh liên quan sẽ được sử dụng trong chương trình.

.. image:: images/xbot_4.1.png
    :width: 400px
    :align: center
| 

- **Đèn LED RGB trên robot**

xBot được tích hợp sẵn 2 đèn LED RGB. Đèn này được cấu tạo từ 3 đèn màu đỏ (Red), xanh lá (Green), xanh dương (Blue). Bạn có thể lập trình để thay đổi dộ sáng của 3 màu này. 

.. image:: images/xbot_4.2.png
    :width: 400px
    :align: center
| 
   
- **Các khối lệnh dùng trong chương trình**

.. image:: images/xbot_4.3.png
    :width: 800px
    :align: center
| 
  
.. image:: images/xbot_4.4.png
    :width: 800px
    :align: center
| 
  
.. image:: images/xbot_4.5.png
    :width: 800px
    :align: center
| 
   
Sau khi bạn đã nắm được các khối lệnh cần sử dụng, bạn hãy kéo chúng vào vùng viết chương trình và kết nối như hình dưới đây:

.. image:: images/xbot_4.6.png
    :width: 600px
    :align: center
| 
 
- **Chạy chương trình**

1. Bạn cần kết nối với robot bằng cách nhấn vào biểu tượng Bluetooth.

.. image:: images/xbot_4.7.png
    :width: 250px
    :align: center
|   
2. Chọn robot có tên đúng với robot của bạn để kết nối.

.. image:: images/xbot_4.8.png
    :width: 600px
    :align: center
|   
3. Khi kết nối thành công, nhấn vào nút chạy chương trình.

Hãy quan sát xem màu sắc 2 đèn LED RGB trên xBot thay đổi như thế nào nhé.

**Lưu chương trình**

Để lưu một chương trình mới, bạn hãy nhấn **nút Lưu**.

.. image:: images/xbot_4.9.png
    :width: 400px
    :align: center
|    

Để mở lại chương trình đã lưu, vào nút quản lý chương trình và chọn **Project của tôi**. Toàn bộ các chương trình đã lưu sẽ hiện ra và bạn có thể nhấn vào để mở chương trình cần xem lại.

.. image:: images/xbot_4.10.png
    :width: 600px
    :align: center
|   

- **Tạo một chương trình mới**

Để tạo mới một project, bạn chọn nút Quản lý chương trình và chọn Tạo mới Project.

.. image:: images/xbot_4.11.png
    :width: 600px
    :align: center
|  

- **Thay khối lệnh lặp lại mãi mãi bằng khối lệnh lặp lại theo số lần**

Bạn hãy thử thay đổi chương trình để hiệu ứng đèn LED nhấp nháy hấp dẫn hơn bằng cách *nhấp nháy lần lượt từng màu đỏ, xanh lá, xanh dương, mỗi màu nhấp nháy 5 lần*.

Trước tiên, bạn hãy thay khối lệnh *lặp lại mãi mãi* bằng khối lệnh *lặp lại 5 lần* để chỉ nháy đèn LED 5 lần. Các bước như sau:

    1. Kéo các khối lệnh bên trong khối lặp lại mãi mãi ra ngoài.

.. image:: images/xbot_4.12.png
    :width: 600px
    :align: center
|   
    2. Kéo khối lặp lại 10 lần vào, sửa số 10 thành số 5 và kết nối với các khối lệnh cũ. Đồng thời, sửa thời gian chờ từ 1 giây thành 0.1 giây.

.. image:: images/xbot_4.13.png
    :width: 600px
    :align: center
| 
    3. Click chuột phải vào khối lặp lại 5 lần và chọn Tạo bản sao: tạo thêm 2 bản sao.

.. image:: images/xbot_4.14.png
    :width: 600px
    :align: center
|  
    4. Ghép 3 chương trình vào nhau, thay đổi màu cho từng chương trình và đưa vào khối lặp lại mãi mãi.

.. image:: images/xbot_4.15.png
    :width: 600px
    :align: center
| 
Sơ đồ hoạt động của chương trình như sau:

.. image:: images/xbot_4.16.png
    :width: 600px
    :align: center
|
Sau khi hoàn thiện, bạn hãy chạy chương trình để xem đèn LED hoạt động nhưu thế nào. 

Bài tập mở rộng
---------------
---------------

Cùng bật tắt từng đèn LED riêng biệt nào! Bạn hãy thay đổi tùy chọn [tấtcả] thành [trái] hoặc [phải] trong khối lệnh thay đổi màu sắc.

Chương trình tham khảo:

.. image:: images/xbot_4.17.png
    :width: 600px
    :align: center
|  

**Câu hỏi ôn tập**

1. Có bao nhiêu môi trường lập trình cho xBot? Kể tên từng loại!

2. Nêu tên các khu vực trong giao diện lập trình của OhStem App?

3. Có bao nhiêu thao tác với khối lệnh? Kể tên và cách thực hiện từng thao tác.





=======
4. Hướng dẫn viết chương trình 
=======================
>>>>>>> main
