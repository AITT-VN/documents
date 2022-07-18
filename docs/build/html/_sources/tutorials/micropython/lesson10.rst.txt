13. Bài học 10: Hiển thị thông tin lên màn hình LCD
====================

Mục tiêu
-----------

Trong bài học này, chúng ta cùng tìm hiểu về màn hình LCD và viết chương trình để hiện dòng chữ “Hello World” lên màn hình. 

Kiến thức mới
-----------

Màn hình là một thành phần khá phổ biến trong các thiết bị điện tử, được dùng để thể hiện thông tin cho người dùng. Có nhiều loại màn hình LCD phổ biến như LCD dạng line, OLED, eInk, TFT,…

.. image:: images/ls-10-1.png
  :width: 600
  :align: center

Màn hình LCD dạng line là một loại khá thông dụng và có giá thành rẻ. Bộ kit xBuild cung cấp sẵn một module màn hình LCD 1602 đơn sắc, sử dụng giao tiếp I2C, có thể hiển thị được 2 dòng chữ với tối đa 16 ký tự mỗi dòng.

Thiết bị cần sử dụng
-----------

.. image:: images/ls-10-2.png
  :width: 600
  :align: center

Kết nối phần cứng
-----------

.. image:: images/ls-10-3.png
  :width: 600
  :align: center

Viết chương trình
--------------

  - Mở phần mềm uPyCraft.
  - Tạo một file chương trình mới (``File > New``) và lưu với tên main.py bằng cách chọn menu ``File > Save…``.
  - Copy đoạn code sau, click vào nút ``DownloadAndRun`` để chạy chương trình.

.. code-block:: python

  from lcd_1602 import LCD1602

  lcd1602 = LCD1602(0)
  lcd1602.backlight_on()
  while True:
    lcd1602.move_to(0, 0)
    lcd1602.putstr('OhStem')
    lcd1602.move_to(0, 1)
    lcd1602.putstr('Xin chao ban')
    time.sleep(2)
    lcd1602.clear()
    time.sleep(1)

Sau khi nạp chương trình, bạn có thể xem các nội dung được in ra trên màn hình LCD1602.

Giải thích chương trình
--------------

.. code-block:: python

  from lcd_1602 import LCD1602

Khai báo thư viện để làm việc với màn hình LCD 1602.

.. code-block:: python

  lcd1602 = LCD1602(0)

Tạo một đối tượng tên là ``lcd``. Khởi tạo màn hình LCD Vì module LCD được nối với cổng 1, nên ta sẽ chọn giá trị 0. Ta có các giá trị ``0~5`` tương ứng ``PORT 1 ~ PORT 6``.

.. code-block:: python

  lcd1602.backlight_on()

Bật đèn nền phía sau của màn hình lcd. Để tắt, ta sử dụng lệnh ``lcd1602.backlight_off()``

.. code-block:: python

  lcd1602.move_to(0, 0)

Di chuyển vị trí in ký tự tiếp theo đến vị trí hàng 0 cột 0. Hàm này có cú pháp là 	``lcd1602.move_to(X, Y)`` với x là cột và y là hàng.

.. code-block:: python

  lcd1602.putstr('OhStem')

In ra màn hình dòng chữ “OhStem” tại vị trí đã được cài đặt.
.. code-block:: python

  lcd1602.move_to(0, 1)
    lcd1602.putstr('Xin chao ban!')

Để in ra dòng chữ “Xin chao ban!” trên dòng thứ 2 của màn hình, chúng ta làm tương tự bằng cách thay đổi vị trí in ra và dùng lệnh ``lcd1602.putstr()`` để hiển thị.

.. code-block:: python

  lcd1602.clear()

Câu lệnh này sẽ xóa trắng màn hình. Tất cả những gì đang được hiển thị sẽ bị biến mất..

Sau khi chạy chương trình, bạn sẽ thấy dòng chữ "OhStem Xin chào bạn!" được hiển thị liên tục trên 2 dòng của màn hình LCD (hiển thị trong 2 giây rồi biến mất trong 1 giây)