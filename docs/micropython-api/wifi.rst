:mod:`wifi` --- Wifi
=============================================

.. module:: wifi
    :synopsis: Wifi

Chức năng chính và chức năng của ``wifi``

Function
----------------------

.. function:: connect(ssid, password, name)
  Kết nối xController vào mạng Wifi của bạn. Trong đó:
    - *ssid* là tên mạng Wifi của bạn.
    - *password* là mật khẩu mạng WiFi nhà bạn.
    - *name* là tên bạn đặt cho xController của mình. Khi một xController khác kết nối vào cùng mạng Wifi thì có thể trao đổi với xController của bạn bằng ``name``.

.. function:: isconnected()
  Trả về két quả thông báo xController đã kết nối vào WiFi đã đưuọc thiết lập bằng hàm ``connect()`` chưa.

.. function:: check_message()
  Kiểm tra xem xController của bạn có nhận được tin nhắn nào từ thiết bị khác, hoặc từ server không.

.. function:: send_message(other_name, text)
  Gửi tin nhắn có nội dung ``text`` tới xController có tên ``other_name``.

.. function:: on_receive_message(topic, callback):
  Sự kiện khi có dữ liệu từ server gửi đến

.. function:: send_message(topic, massage)
  Gửi dữ liệu lên server


Sample Code：
----------------------
Hiển thị khoảng cách đo được từ cảm biến siêu âm 

.. code-block:: python

      while True:
            #do something

