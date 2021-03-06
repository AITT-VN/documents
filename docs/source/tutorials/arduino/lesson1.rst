2. Bài học 1: Hello world
====================

Mục tiêu
-----------

Để làm quen với Arduino, đầu tiên chúng ta sẽ viết một chương trình cực kỳ đơn giản: in ra dòng chữ ``Hello World``. 


Thiết bị cần sử dụng
-----------

.. image:: images/device-1.png
  :width: 200
  :align: center


Viết chương trình
--------------

Trong Arduino, bạn hãy tạo một file chương trình mới ``(File > New)`` và lưu với tên ``hello.ino`` bằng cách chọn menu ``File > Save As… ``(chọn thư mục để lưu). Sau đó, bạn copy đoạn code này vào:

.. code-block:: guess

  void setup() {
    Serial.begin(9600); // khởi tạo cổng serial xuất ra thông tin
  }

  void loop() {
    Serial.println("Hello World"); // in ra dòng chữ Hello World
    delay(1000); // tạm dừng chương trình 1 giây
  }

*Lưu ý:* Bạn chưa cần hiểu đoạn code ở trên ngay bây giờ nhé. Ở các bài học sau, từng thành phần của một đoạn code trong Arduino sẽ được giải thích kỹ hơn.
Trên góc trái của Arduino IDE, có 2 nút nhấn với chức năng là: ``Verify`` và ``Upload``. 

  Nút ``Verify``  dùng để biên dịch chương trình nhưng không nạp (gọi là compile) vào board, chủ yếu để kiểm tra xem chương trình đã viết có bị lỗi không.

  Nút ``Upload``  dùng để vừa biên dịch vừa nạp chương trình vào board.

  .. image:: images/ls-1-1.png
    :width: 500
    :align: center

Bạn hãy thử nhấn nút Upload và chờ cho đến khi nạp thành công (Bạn nhớ kết nối xController với máy bằng cáp USB trước khi Upload nhé).

.. image:: images/ls-1-2.png
  :width: 500
  :align: center

Để xem thông tin xuất ra cổng ``Serial``, bạn vào menu ``Tools > Serial Monitor``, hoặc click vào nút ``Serial Monitor`` nằm ở góc trên bên phải . 

.. image:: images/ls-1-3.png
  :width: 500
  :align: center

Ở cửa sổ ``Serial Monitor``, bạn sẽ thấy kết quả chương trình đã thực hiện là: dòng chữ ``Hello World`` được in ra sau mỗi 1 giây:

.. image:: images/ls-1-4.png
  :width: 500
  :align: center

Chúc mừng bạn đã hoàn thành chương trình đầu tiên trong chuỗi các bài học. Hãy tiếp tục các bài tiếp theo nhé.

*Lưu ý:* Nếu chương trình không thể biên dịch thành công hoặc không thể nạp vào board xController, bạn cần kiểm tra các yếu tố sau:
  - Đảm bảo bạn chọn đúng loại board là xController và COM port tương ứng với xController. Tên board và COM port được hiển thị ở góc dưới cùng bên phải của Arduino IDE.

  .. image:: images/ls-1-5.png
    :width: 500
    :align: center

  - Code nhập vào đúng như code mẫu, không bị thiếu các dấu như () hay {} hoặc dấu ; sau mỗi dòng. Bạn có thể mở file code mẫu đi kèm tài liệu và copy vào để đảm bảo code không bị sai sót.