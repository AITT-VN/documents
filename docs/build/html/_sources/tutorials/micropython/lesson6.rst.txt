Bài học 6: Đèn LED RGB cảm ứng
====================

Mục tiêu
-----------

Vận dụng kiến thức về tín hiệu Analog Input đã học để làm việc với cảm biến ánh sáng và điều khiển đèn LED đa màu RGB được tích hợp sẵn trên xController.

Tìm hiểu cách sử dụng cửa sổ Terminal để xem và theo dõi kết quả đọc được từ cảm biến, từ đó có thể viết đúng logic hoạt động của chương trình.

Viết chương trình điều chỉnh độ sáng của đèn LED RGB một cách tự động dựa vào ánh sáng môi trường.

Kiến thức mới
-----------

*Cảm biến ánh sáng*

Cảm biến ánh sáng có nhiều loại, trong đó loại dùng quang trở là phổ biến nhất. Quang trở là một loại điện trở mà giá trị của nó thay đổi theo cường độ ánh sáng nó thu được. Nếu đặt ở môi trường có ít ánh sáng, có bóng râm hoặc bóng tối thì điện trở của quang trở sẽ tăng cao. Ngược lại, nếu đặt ở ngoài nắng, hoặc nơi có ánh sáng thì điện trở sẽ giảm. 

  .. image:: images/ls-6-1.png
    :width: 600
    :align: center

Ta có thể sử dụng cảm biến ánh sáng trong rất nhiều ứng dụng thực tế, ví dụ như bật tắt đèn tự động mỗi khi trời tối.

*LED đa màu RGB*

xController được tích hợp sẵn 2 đèn LED đa màu RGB trên board. Đèn LED RGB là đèn LED đặc biệt, có thể phát sáng với nhiều màu khác nhau (lên đến 16 triệu màu). Màu của đèn LED được tổng hợp từ 3 đèn màu đỏ (Red), xanh lục (Green), xanh lam (Blue) bên trong. 

Các LED màu này có độ sáng từ ``0 ~ 255``. Để thay đổi màu đèn LED RGB, chúng ta sẽ thay đổi độ sáng của 3 LED màu này.

  .. image:: images/ls-6-2.png
    :width: 600
    :align: center

Thiết bị cần sử dụng
-----------

.. image:: images/device-6.png
  :width: 600
  :align: center

Kết nối phần cứng
-----------

.. image:: images/ls-6-4.png
  :width: 500
  :align: center


Viết chương trình
--------------

  - Mở phần mềm uPyCraft.
  - Tạo một file chương trình mới (``File > New``) và lưu với tên main.py bằng cách chọn menu ``File > Save…``.
  - Copy đoạn code sau, click vào nút ``DownloadAndRun`` để chạy chương trình.

.. code-block:: python

  light_value = pin41.read_analog()

  while True:
    print(light_value) # In giá trị cảm biến ánh sáng
    led_value = translate(light_value, 0, 4095, 0, 255)
    print(led_value) # In giá trị độ sáng của đèn đã được tính toán
    led_onboard.show(0, (led_value, 0, 0))
    time.sleep_ms(10)


Sau khi nạp chương trình, Bạn có thể xem giá trị của cảm biến ánh sáng và kết quả tính toán độ sáng của đèn LED RGB trong cửa sổ Terminal.

Giải thích chương trình
--------------

.. code-block:: python

  light_value = pin41.read_analog()

Đặt biến ``light_value`` là giá trị tín hiệu Analog ở chân IO được chỉ định. Do cảm biến ánh sáng trả về tín hiệu Analog và được kết nối với cổng số 4 trên xController nên ta dùng ``pin41.read_analog()``. Lúc này biến ``light_value`` sẽ trả về giá trị kiểu số nguyên (``int``) nằm trong khoảng từ 0 đến 4095.

Dùng hàm ``print`` để in giá trị ra cửa sổ Terminal trên phần mềm uPyCraft

.. code-block:: python

  print(light_value)

.. image:: images/ls-1-7.png
  :width: 500
  :align: center

.. code-block:: python

  >>>
  Ready to download this file,please wait!
  .
  download ok
  0
  0
  4095
  4095

Nếu cửa sổ Terminal in ra các giá trị trong khoảng 0 đến 4095 một cách ngẫu nhiên khi bạn di chuyển cảm biến ánh sáng vào những vùng sáng tối khác nhau thì cảm biến đã hoạt động tốt.

Như ta đã biết, cảm biến xuất ra tín hiệu Analog có giá trị từ 0 đến 4095, trong khi độ sáng của 3 đèn LED trong đèn LED RGB tích hợp nhận giá trị từ 0 đến 255. Vậy nên, ta cần quy đổi hai thang đo này thành một: 

  - Khi giá trị cảm biến là 0 thì độ sáng của LED đỏ trong LED RGB là 0. 
  - Khi giá trị cảm biến là 4095 thì độ sáng LED đỏ trong LED RGB là 255.

.. code-block:: python

  led_value = translate(light_value, 0, 4095, 0, 255)

Bạn có thể xem lại bài trước để hiểu rõ hơn về hàm ``translate``.

.. code-block:: python

  led_onboard.show(0, (led_value, 0, 0))

Để thay đổi màu và độ sáng của đèn LED RGB trên xController, chúng ta sử dụng hàm ``led_onboard.show(index, color)``. Hàm này có cú pháp như sau: 

.. code-block:: python

  led_onboard.show(index, color)

Các tham số bao gồm:

  - ``index`` : 0-Cả hai LED, 1-LED bên trái, 2-LED bên phải.
  - ``color`` : Có thể sử dụng 2 hệ màu là RGB hoặc HEX:

    - ``RGB`` : (Red,Green,Blue) với phạm vi mỗi tham số là 0 ~ 255. Nếu bằng 0 tương ứng không có thành phần màu và nếu bằng 255 trương ứng thành phần màu cao nhất.
    - ``HEX`` : hex_to_rgb(‘#0000ff’)

Ở đây chúng ta đang sử dụng hệ màu RGB. Và trong ví dụ này, chúng ta chỉ cần thay đổi độ sáng của LED đỏ và tắt các LED xanh lục, xanh lam nên ta có hệ màu RGB như sau :

.. code-block:: python

  (led_value, 0, 0)

Với ``led_value`` là giá trị ``0~255`` sau khi đã quy đổi từ việc phân tích giá trị xuất ra từ cảm biến ánh sáng.

.. code-block:: python

    time.sleep_ms(10)

Dừng chương trình trong một khoảng thời gian (đơn vị ``mili giây``).

Câu lệnh ``sleep_ms()`` có cú pháp như sau:

.. code-block:: python

  time.sleep_ms(s)

Tham số truyền vào:

  ``s``: số mili giây chương trình tạm dừng. (1 giây = 1000 mili giây)

Chúng ta cần tạm dừng chương trình trong khoảng thời gian 10 mili giây để cảm biến ánh sáng được cập nhật liên tục và độ sáng của đèn thay đổi mượt hơn. Tuy nhiên bạn có thể tăng hoặc giảm tham số này đề so sánh sự khác biệt.

Sau khi nạp chương trình, bạn thử lấy tay che cảm biến ánh sáng và quan sát sự thay đổi độ sáng của cả 2 đèn LED RGB trên xController.
