1. Hướng Dẫn Cài Đặt Arduino và xController
====================

Cài đặt Arduino IDE
-----------

Bạn có thể tải phiên bản Arduino IDE mới nhất, phù hợp với hệ điều hành của máy tính của bạn tại trang chủ của Arduino (Đường dẫn: https://www.arduino.cc/en/Main/Software)

.. image:: images/P1-1.png
  :width: 600
  :align: center


Cài đặt board xController trong Arduino IDE
--------------

Phần mềm Arduino có thể lập trình cho rất nhiều loại board mạch khác nhau. Tuy nhiên, bạn cần làm thêm một vài bước sau để có thể làm việc với xController:

  1. `Mở phần mềm Arduino đã cài đặt.

  2. Vào menu ``File > Preferences``. Trong tab ``Settings``, mục ``Additional Boards Manager``, thêm địa chỉ đường dẫn mô tả thông tin xController như hình và nhấn “OK”
  ``https://raw.githubusercontent.com/AITT-VN/ohstem_arduino_board/main/package_xcon_index.json ``

    .. image:: images/P1-2.png
      :width: 480
      :align: center

    Sau này, để hỗ trợ nhiều loại board khác, bạn có thể nhập nhiều dòng bằng cách nhấn Enter để xuống dòng cho từng link.

  3. Mở menu ``Tools > Board [tên board đang được chọn] > Boards Manager…``, nhập Ohstem vào thanh search và chọn board ``OhStem Boards by OhStem Education`` được tìm thấy như hình dưới, nhấn vào ``Install``, chờ đến khi board được cài đặt hoàn tất. Sau khi cài đặt xong, nhấn vào ``Close``.

    .. image:: images/P1-3.png
      :width: 480
      :align: center

  4. Vào menu ``Tools > Board``, chọn loại board là ``OhStem Boards > xController`` vừa được cài đặt:

    .. image:: images/P1-4.png
      :width: 480
      :align: center

  5. Vào menu ``Tools > Port`` để chọn Cổng kết nối đến xController (chính là COM Port hiện ra trong ``Device Manager`` chúng ta đã thấy lúc nãy) 

    Ví dụ: Trong máy tính Windows của tác giả, cổng trên Device Manager là ``COM12``:

      .. image:: images/P1-2.png
      :width: 480
      :align: center
 
    Đối với người dùng hệ điều hành macOS, cổng kết nối sẽ được hiển thị là: ``/dev/cu.SLAB_USBtoUART``.

Chương trình mẫu
+++++++++++++++++

* :download:`Arduino Tutorial Code <https://github.com/AITT-VN/xbuild_creator_kit/tree/main/Arduino>`

