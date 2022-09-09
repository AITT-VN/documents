11. Mở cửa bằng mật khẩu
=============

1. Mục tiêu 
----------
---------------

Trong bài học này, chúng ta sẽ cùng làm một hệ thống cửa mở được bằng mật mã, tương tự các hệ thống khóa của trong thực tế nhé. Bạn sẽ dùng nút A và B trên Yolo:Bit để nhập mật khẩu, nếu đúng thì cửa sẽ mở thông qua động cơ Servo. Ngược lại, nếu mật khẩu sai thì hệ thống sẽ thông báo sai mật khẩu để nhập lại.

2. Thiết bị cần dùng 
-------
-------------

- Mạch Yolo:Bit
- Mạch mở rộng Yolo:Bit.

.. image:: images/4.1.jpg
    :width: 300px
    :align: center
|

- Màn hình LCD1602

.. image:: images/7.1.jpg
    :scale: 40 %
    :align: center
|
- Động cơ Servo 

.. image:: images/11.1.jpg
    :scale: 40 %
    :align: center
|

3. Kết nối 
-------
------------

- Kết nối màn hình vào cổng I2C
- Kết nối Servo vào cổng chân cắm P6 (Lưu ý: Nối dây Servo với đúng với thứ tự màu trên dãy chân cắm như hình minh họa)

.. image:: images/11.2.png
    :width: 450px
    :align: center
| 

- **Giới thiệu đôi nét về động cơ Servo:**

Servo là một dạng động cơ điện đặc biệt, chỉ quay khi được điều khiển (bằng tín hiệu xung) với góc quay nằm trong khoảng bất kỳ. Có 3 loại Servo quen thuộc là:
    
    - Servo quay 180 độ
    - Servo quay 270 độ
    - Servo quay 360 độ

**Ở dự án này, chúng ta sẽ sử dụng Servo 180 độ.**

4. Lập trình 
-------
----------

- **Giới thiệu khối lệnh**

Trong danh mục **CHỮ VIẾT** sử dụng các khối lệnh sau: 

    - Tạo ra văn bản từ các khối lệnh thông tin được gắn ở phía sau:

.. image:: images/11.3.png
    :scale: 80 %
    :align: center
|

    - Khối lệnh trả về giá trị tổng số lượng các ký tự đằng sau nó

.. image:: images/11.4.png
    :scale: 100 %
    :align: center
|

    - Khối lệnh nội dung: tạo một nội dung tùy ý (chữ, số, ký tự...) để sử dụng trong chương trình.

.. image:: images/11.4.1.png
    :scale: 100 %
    :align: center
|

Trong danh mục **CHÂN CẮM** sử dụng các khối lệnh sau để làm việc với Servo: 

    - Điều khiển Servo quay một góc nhất định

.. image:: images/11.4.2.png
    :scale: 80 %
    :align: center
|

    - Tắt điều khiển chân Servo 

.. image:: images/11.4.3.png
    :scale: 80 %
    :align: center
|

Giới thiệu về biến 
----------------------
----------------------

Để chương trình không cần phải đọc khoảng cách và xử lý giá trị liên tục, chúng ta cần sử dụng biến. Có thể hiểu, biến như một chiếc hộp, nơi chứa giá trị mà ta cần sử dụng.

Mỗi hộp chỉ có thể chứa duy nhất một giá trị (chữ, số, chuỗi, dữ liệu) tại một thời điểm. Trong bài này, biến sẽ chứa giá trị số, đại diện cho khoảng cách từ Rover đến vật thể trước mặt.

    .. image:: images/bai_7.2.png
        :width: 400px
        :align: center 
|
**Cách tạo và sử dụng biến**

    1. Bạn cần vào mục Biến và chọn Tạo biến. Sau đó, điền tên cho biến mới để tạo

        .. image:: images/bai_7.3.png
            :width: 400px
            :align: center 
    

    2. Khi tạo biến thành công, trong mục Biến sẽ xuất hiện những khối lệnh liên quan để làm việc với biến.

        .. image:: images/bai_7.4.png
            :width: 400px
            :align: center 



- **Lập trình**

Đầu tiên, chúng ta sẽ tạo 2 biến:

    - Mật khẩu cài đặt (Mật khẩu đúng để mở cửa)
    - Mật khẩu đã nhập (Mật khẩu khi nhập vào)

Chúng ta sẽ quy định mật khẩu đúng để mở cửa là AABB. Để làm điều này, bạn hãy gán giá trị AABB cho biến **mật khẩu cài đặt**.

Lúc ban đầu, chúng ta chưa nhập mật khẩu nên ta cần gán giá trị rỗng cho biến **mật khẩu đã nhập** 

.. image:: images/11.5.png
    :scale: 100 %
    :align: center
|
Chúng ta sẽ lập trình khi nút A được nhấn, chương trình sẽ phát ra một nốt nhạc và thêm 1 kí tự A vào chuỗi mật khẩu đã nhập trước đó.

Ví dụ: Nếu bạn đã nhập AAB trước đó, sau khi nhấn A lần nữa, mật khẩu đã nhập sẽ là AABA

.. image:: images/11.6.png
    :scale: 80 %
    :align: center
|
Sau đó, bạn hãy xóa màn hình LCD trước đó và hiển thị mật khẩu đã nhập lên màn hình LCD trong vòng 300 ms (0.3 giây) để quan sát:

.. image:: images/11.7.png
    :scale: 80 %
    :align: center
|
Bạn tiến hành lập trình tương tự với nút B: Nếu nút B được nhấn thì Yolo:Bit sẽ phát nốt nhạc G3 để báo hiệu, đồng thời lưu thông tin vào mật khẩu đã nhập và hiển thị chúng ra màn hình LCD trong 300 ms:

.. image:: images/11.8.png
    :scale: 80 %
    :align: center
|
Kiểm tra độ dài của mật khẩu đã nhập đủ 4 ký tự chưa, nếu đủ thì xóa màn hình LCD:

.. image:: images/11.9.png
    :scale: 100 %
    :align: center
|
Cuối cùng, chúng ta sẽ kiểm tra mật khẩu. Có 2 trường hợp xảy ra:

    - **Trường hợp 1: Mật khẩu đúng**

    Nếu mật khẩu đúng (mật khẩu đã nhập bằng mật khẩu cài đặt) thì màn hình LCD hiển thị dòng chữ “Xin moi vao” và phát bài nhạc POWER_UP, đồng thời quay Servo để mở cửa trong 3 giây, sau đó đóng cửa và tắt Servo (Bạn nhớ đổi cổng của Servo thành cổng P6 nhé):

.. image:: images/11.10.png
    :scale: 80 %
    :align: center
|

    - **Trường hợp 2: Mật khẩu sai**

    Nếu mật khẩu sai, màn hình LCD hiển thị “Sai mat khau” và phát bài nhạc POWER_DOWN, đồng thời xóa mật khẩu đã nhập tại cuối chương trình (Cho biến mật khẩu đã nhập bằng giá trị rỗng)

.. image:: images/11.11.png
    :scale: 80 %
    :align: center
|
Xem chương trình đầy đủ bên dưới nhé!

5. Chương trình mẫu 
-------
------------

- Mở cửa bằng mật khẩu: `Tại đây <https://app.ohstem.vn/#!/share/yolobit/2EWTBwBtCbYAHEUk2BebalMe0kI>`_

.. image:: images/11.13.png
    :width: 200px
    :align: center 