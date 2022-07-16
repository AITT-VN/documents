5. Bài học 2: Blink LED
====================

Mục tiêu
-----------

Sau khi hoàn thành chương trình đầu tiên để làm quen với Arduino trong bài trước, bây giờ, chúng ta hãy thử học cách điều khiển module đèn LED. Trong bài tập này, chúng ta sẽ lập trình cho module đèn LED bật và tắt liên tục (còn gọi là ``blink``) sau mỗi giây.

Kiến thức mới
-----------

Các yếu tố cấu thành một hệ thống điều khiển

  3 yếu tố cơ bản cấu thành nên một hệ thống điều khiển là: 
    ``Input``: Thông tin đầu vào
    ``Control`` Unit: Trung tâm xử lý và điều khiển
    ``Output``: Xuất ra thông tin hoặc hành động đã được lập trình sẵn

  Trong chương trình bật/tắt LED, chúng ta sẽ chỉ sử dụng `Output` mà không sử dụng Input. xController chính là Control Unit - sử dụng tín hiệu Digital để điều khiển module Output là đèn LED .

Tín hiệu Digital là gì?

  Có 2 loại tín hiệu cơ bản mà chúng ta sẽ làm việc với chúng trong lập trình điện tử, đó là ``tín hiệu Digital`` và tín hiệu Analog. Chúng ta sẽ tìm hiểu về Analog trong các bài học sau. 
  
  ``Tín hiệu Digital`` là tín hiệu chỉ có 2 giá trị là ``Tắt`` (còn gọi là LOW, 0V) và ``Bật`` (HIGH, 3.3V hay 5V tùy vào điện áp hoạt động của hệ thống, xController sử dụng 3.3V).

  .. image:: images/ls-2-1.png
    :width: 420
    :align: center

  Module LED hoạt động dựa vào tín hiệu Digital:

  .. image:: images/ls-2-2.png
    :width: 420
    :align: center

Kết nối phần cứng
-----------

.. image:: images/ls-2-3.png
  :width: 600
  :align: center

Thiết bị cần sử dụng
-----------

.. image:: images/device-2.png
  :width: 480
  :align: center


Viết chương trình
--------------

  - Mở phần mềm uPyCraft.
  - Tạo một file chương trình mới (``File > New``) và lưu với tên main.py bằng cách chọn menu ``File > Save…``.
  - Copy đoạn code sau, click vào nút ``DownloadAndRun`` để chạy chương trình.

.. code-block:: python

  while True:
    pin11.write_digital(1)
    time.sleep(1)
    pin11.write_digital(0)
    time.sleep(1)

Sau khi chạy chương trình, bạn sẽ thấy đèn LED  phát sáng và tắt liên lục mỗi 1 giây.


Giải thích chương trình
--------------

.. code-block:: python

  pin11.write_digital(1)

Câu lệnh này cấu hình chế độ hoạt động của chân IO (nối với module LED) thành ``DIGITAL OUTPUT`` để có thể điều khiển được. 

Lưu ý: Một chân IO có thể được sử dụng với các chế độ hoạt động khác nhau:

  - Tín hiệu ``Digital`` hoặc ``Analog``
  - Có thể là ``Input`` (nếu nhận thông tin từ các module như module cảm biến) hoặc ``Output`` (nếu dùng để điều khiển bật tắt module gắn vào). 

Do tính đa năng như vậy, nên các chân IO còn được gọi là ``General Purpose Input Output`` (các chân IO đa mục đích), hay gọi tắt là ``GPIO``.

Lệnh khởi tạo một Object Pin Digital đầy đủ như sau:

.. code-block:: python

  pin[X][Y].write_digital((STATE))

  - ``X`` Có giá trị từ ``1 ~ 6`` đại diện PORT 1 đến PORT 6 của xController.
  - ``Y`` Có giá trị là ``1`` hoặc ``2`` tương ứng với 2 đường tín hiệu logic đối với mỗi PORT. Đối với một số module output thì mặc định là 1.

Lưu ý: Trên board xController có 6 cổng mở rộng, được đánh số từ 1 đến 6. Mỗi cổng gồm 4 đường tín hiệu:

  - 2 đường tín hiệu dành cho nguồn điện là GND (nguồn âm, 0V) và VCC (nguồn dương, 3.3V)
  - 2 đường tín hiệu logic, có thể sử dụng cho tín hiệu ``Digital`` (cả 6 cổng) hoặc ``Analog`` (chỉ hỗ trợ trên cổng 4, 5 và 6)

Sau đó, dùng một vòng lặp ``while`` với biểu thức điều kiện luôn luôn trả về ``True``. Điều này tương tự như hàm ``loop ()`` trong Arduino IDE:

.. code-block:: python

  while True:
    # Các lệnh cần thực hiện

Để điều khiển object led, ta dùng value(``state``), với ``state`` là đối số truyền vào giá trị cho led b``ật hoặc ``tắt``.

.. code-block:: python

  pin11.write_digital(1)

Xuất ra tín hiệu mức HIGH cho chân IO nối với module LED.

Nếu chân IO được khai báo mode ``write_digital``, thì điện áp xuất ra sẽ là 3.3V (hoặc 5V trên board sử dụng 5V) đối với mức ``HIGH``, và 0V đối với mức ``LOW``.

Câu lệnh trên sẽ xuất ra tín hiệu mức HIGH (3.3V). Khi đó, LED sẽ được bật do có điện.

.. code-block:: python

  pin11.write_digital(0)

Tương tự, câu lệnh này xuất tín hiệu ``LOW`` cho chân IO nối với module LED, tương ứng với mức điện áp 0V. Khi đó, LED sẽ được tắt.

.. code-block:: python

  time.sleep(1)

Dừng chương trình trong một khoảng thời gian (đơn vị ``giây``).

Câu lệnh sleep() có cú pháp như sau:

.. code-block:: python

  time.sleep(s)

Tham số truyền vào:

  ``s``: số giây chương trình tạm dừng.

Chúng ta cần tạm dừng chương trình trong khoảng thời gian 1 giây để có thể nhìn rõ được hiệu ứng bật và tắt đèn LED. Nếu không, đèn LED sẽ được bật và tắt một cách chớp nhoáng, mắt người không nhìn rõ được.

Vậy là bạn đã làm quen với khái niệm tín hiệu Digital và biết cách điều khiển module LED. Ở bài học sau, bạn sẽ kết hợp thêm các tín hiệu Input khác để làm những bài học nâng cao hơn.
