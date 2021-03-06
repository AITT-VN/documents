15. Bài học 12: Remote hồng ngoại
====================

Mục tiêu
-----------

Tìm hiểu về tín hiệu hồng ngoại và remote điều khiển từ xa bằng hồng ngoại đi kèm. Viết chương trình để thay đổi màu sắc đèn LED RGB trên board bằng remote.

Kiến thức mới
-----------

Chắc hẳn là bạn cũng đã sử dụng remote hồng ngoại để điều khiển TV, quạt, máy lạnh,.... đúng không nào? Các remote này đều sử dụng tín hiệu hồng ngoại (Infrared, gọi tắt là IR), được hiểu là 1 chùm sóng ánh sáng không thể nhìn thấy bằng mắt thường. Do đó, bạn không thể thấy ánh sáng phát ra khi nhìn vào đèn LED hồng ngoại nhỏ ở đầu của remote.

.. image:: images/ls-12-1.png
  :width: 480
  :align: center

Trên remote có 1 hoặc nhiều LED hồng ngoại được sử dụng để truyền tín hiệu hồng ngoại. Tín hiệu này sẽ được nhận bởi 1 bộ thu hồng ngoại đặc biệt và chuyển thành dạng xung điện, sau đó, các xung điện này được chuyển đổi thành dữ liệu được sử dụng cho các thiết bị điện tử.

Nếu bạn tò mò muốn biết ánh sáng hồng ngoại như thế nào, hãy nhấn 1 nút bất kỳ trên remote rồi nhìn vào đèn LED ở đầu remote thông qua 1 chiếc camera nhé!

.. image:: images/ls-12-2.png
  :width: 480
  :align: center

Board xController được tích hợp sẵn 2 đèn LED hồng ngoại, một LED thu và một LED phát. Bộ xBuild Creator Kit cũng đi kèm một remote hồng ngoại để chúng ta thực hành.

.. image:: images/ls-12-3.png
  :width: 480
  :align: center

Thiết bị cần sử dụng
-----------

.. image:: images/device-12.png
  :width: 600
  :align: center

Viết chương trình
--------------

  - Mở phần mềm uPyCraft.
  - Tạo một file chương trình mới (``File > New``) và lưu với tên main.py bằng cách chọn menu ``File > Save…``.
  - Copy đoạn code sau, click vào nút ``DownloadAndRun`` để chạy chương trình.

.. code-block:: python

  from ir_receiver import *;ir_rx.start();


  while True:
    if ir_rx.get_code() == IR_REMOTE_A:
      led_onboard.show(0, (255, 0, 0))
      ir_rx.clear_code()
    elif ir_rx.get_code() == IR_REMOTE_B:
      led_onboard.show(0, (0, 255, 0))
      ir_rx.clear_code()
    elif ir_rx.get_code() == IR_REMOTE_C:
      led_onboard.show(0, (0, 0, 255))
      ir_rx.clear_code()
    elif ir_rx.get_code() == IR_REMOTE_D:
      led_onboard.show(0, (255, 255, 255))
      ir_rx.clear_code()
    else:
      led_onboard.show(0, (0, 0, 0))
      ir_rx.clear_code()


Giải thích chương trình
--------------

Chương trình trên sẽ liên tục đọc tín hiệu IR (nếu có) và giải mãi. Nếu tín hiệu giải mã trùng với các phím A, B, C hoặc D trên remote hồng ngoại đi kèm, đèn LED RGB sẽ đổi màu tương ứng. Nếu tín hiệu nhận được không phải 1 trong 4 phím đó thì đèn LED sẽ tắt.

.. code-block:: python

  from ir_receiver import *;

Khai báo sử dụng thư viện để làm việc với remote IR.

.. code-block:: python

  ir_rx.start();

Khởi tạo và bắt đầu xử lý tín hiệu IR.

.. code-block:: python

  ir_rx.get_code()

Hàm ``ir_rx.get_code()`` sẽ trả về chuỗi tương ứng với phím được nhấn trên IR remote.

.. code-block:: python

  if ir_rx.get_code() == IR_REMOTE_A:
    led_onboard.show(0, (255, 0, 0))
    ir_rx.clear_code()

Dúng hàm If kiểm tra: Nếu tín hiệu trùng với phím A trên remote thì đổi màu đèn LED RGB thành màu đỏ. ``IR_REMOTE_A`` là giá trị tín hiệu của phím A trên remote đi kèm bộ kit (đã được khai báo trong thư viện IRRemote).

Đồng thời ta sẽ sử dụng thêm hàm ``ir_rx.clear_code()`` để xóa các giá trị đã nhận để tránh trùng lặp với các giá trị mới.

Kiểm tra tương tự với các phím B, C và D bằng đoạn code bên dưới.

Sau khi chạy chương trình, bạn thử hướng remote về phía board và nhấn các phím A, B, C, D. Bạn sẽ thấy màu LED thay đổi theo như logic trong chương trình.
