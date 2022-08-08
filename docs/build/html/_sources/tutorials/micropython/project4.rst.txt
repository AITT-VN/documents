21. Project 4: Hệ thống chống trộm và báo động
====================

Mục tiêu
-----------

Ngôi nhà nào cũng cần phải đảm bảo sự an toàn cho chủ nhân của nó, đúng không nào? Trong project này, chúng ta sẽ làm cho ngôi nhà trở nên an toàn hơn bằng cách xây dựng hệ thống an ninh: tự động hú còi báo động và chớp đèn liên tục khi phát hiện có sự xâm nhập trái phép.

Hệ thống này sẽ hoạt động kết với hợp remote điều khiển như sau:

  - Bật chế độ bảo vệ bằng nút nhấn tích hợp trên hộp điều khiển xController
  - Khi chế độ bảo vệ được bật, nếu phát hiện có sự chuyển động thì sẽ tự động hú còi cảnh báo và chớp đèn liên tục trong vòng 5 giây.


Thiết bị cần sử dụng
-----------

.. image:: images/project-4-1.png
  :width: 600
  :align: center

Kết nối phần cứng
-----------

.. image:: images/project-4-2.png
  :width: 600
  :align: center


Viết chương trình
--------------

  - Mở phần mềm uPyCraft.
  - Tạo một file chương trình mới (``File > New``) và lưu với tên main.py bằng cách chọn menu ``File > Save…``.
  - Copy đoạn code sau, click vào nút ``DownloadAndRun`` để chạy chương trình.

.. code-block:: python

  alarmmode = False
  pirstate = 0

  while True:
    if (btn_onboard.is_pressed()) == False:
      alarmmode = not alarmmode
      if alarmmode:
        print('Chế độ bảo vệ được bật')
      else:
        print('Chế độ bảo vệ được tắt')
    pirstate = pin51.read_digital()
    if alarmmode and pirstate == 1:
      print('Phát hiện có người xâm nhập')
      for count in range(5):
        led_onboard.show(0, (255, 0, 0))
        speaker.play(['C4:1'], wait=True)
        time.sleep(1)
        led_onboard.show(0, (0, 0, 0))
        speaker.stop()


Giải thích chương trình
--------------

Trong chương trình trên, chúng ta khai báo biến ``alarmmode`` kiểu bool (có giá trị ``true`` hoặc ``false``) để lưu trạng thái bật tắt của chế độ bảo vệ. Chế độ này sẽ bật/tắt khi nút trên board được nhấn.

Nếu chế độ này đang được bật, đồng thời phát hiện có sự chuyển động thì ngôi nhà sẽ nháy đèn LED RGB và phát âm thanh báo động 5 lần, đủ để cho kẻ trộm chạy mất và chủ nhà thức giấc.
