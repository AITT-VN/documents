Project 2: Quạt thông minh
====================

Mục tiêu
-----------

Chúng ta đã học cách đọc và hiển thị nhiệt độ và độ ẩm của môi trường ở bài học số 9. Dựa vào đó, chúng ta sẽ làm cho quạt trong nhà trở nên thông minh hơn và biết lúc nào cần bật, lúc nào cần tắt. Điều này thật sự hữu ích khi vào ban đêm, lúc đang ngủ, chúng ta có thể tránh bị bệnh do quá lạnh hoặc quá nóng làm mất giấc ngủ.

Ngoài ra, bài học này sẽ giúp bạn làm quen với 1 module Output mới là động cơ mini. Động cơ là một thiết bị điện tử rất phổ biến trong cuộc sống của chúng ta (như quạt, động cơ xe, máy bơm nước...). Động cơ khi được cung cấp điện sẽ làm xoay trục động cơ, từ đó tạo nên nhiều ứng dụng khác nhau. 

Thiết bị cần sử dụng
-----------

.. image:: images/project-2-1.png
  :width: 600
  :align: center

Kết nối phần cứng
-----------

.. image:: images/project-2-2.png
  :width: 600
  :align: center


Viết chương trình
--------------

  - Mở phần mềm uPyCraft.
  - Tạo một file chương trình mới (``File > New``) và lưu với tên main.py bằng cách chọn menu ``File > Save…``.
  - Copy đoạn code sau, click vào nút ``DownloadAndRun`` để chạy chương trình.

.. code-block:: python

  from lcd_1602 import LCD1602
  import dht

  dht11 = dht.DHT11(Pin(PORTS_DIGITAL[1][0]))

  lastchecktemp = 0

  lcd1602 = LCD1602(0)
  while True:
    # lấy thời gian hiện tại
    currentmillis = ticks_ms()
    if currentmillis - lastchecktemp >= 5000:
      # đã quá 5s kể từ lần cập nhật nhiệt độ cuối
      # cần cập nhật lại
      lastchecktemp = currentmillis
      dht11.measure()
      t = dht11.temperature()
      h = dht11.humidity()
      lcd1602.move_to(0, 0)
      lcd1602.putstr((''.join([str(x) for x in ['Nhiet do: ', t, ' C']])))
      lcd1602.move_to(0, 1)
      lcd1602.putstr((''.join([str(x2) for x2 in ['Do am: ', h, ' %']])))
      if t < 32:
        pin31.write_digital((0))
        print('Tắt quạt')
      else:
        pin31.write_digital((1))
        print('Bật quạt')

Giải thích chương trình
--------------

Chương trình trên sẽ tương tự như bài học số 9: Đọc và hiển thị nhiệt độ, độ ẩm lên màn hình LCD. Tuy nhiên, có một sự thay đổi đó là chương trình này không dùng hàm ``time.sleep()`` để chờ 5 giây sau mỗi lần cập nhật, mà chúng ta sẽ dùng một phương pháp hay hơn: lưu thời gian lần cuối cập nhật và liên tục kiểm tra xem đã quá 5 giây kể từ lần cuối cập nhật chưa. Nếu đã quá 5 giây thì sẽ tiến hành cập nhật.

.. code-block:: python

  currentmillis = ticks_ms()
  if currentmillis - lastchecktemp >= 5000:
    # đã quá 5s kể từ lần cập nhật nhiệt độ cuối
    # cần cập nhật lại
    lastchecktemp = currentmillis

Hàm ``ticks_ms()`` trả về tổng số mili giây, tính từ lúc chương trình bắt đầu chạy cho đến hiện tại.

.. code-block:: python

    if t < 32:
      pin31.write_digital((0))
      print('Tắt quạt')
    else:
      pin31.write_digital((1))
      print('Bật quạt')

Đồng thời, chúng ta cũng kiểm tra với nhiệt độ hiện tại thì có nên bật quạt không với ngưỡng là 32 độ. Nếu quá 32 độ thì quạt sẽ được bật và ngược lại.
