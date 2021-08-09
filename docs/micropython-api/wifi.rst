:mod:`wifi` --- Wifi
=============================================

.. module:: wifi
    :synopsis: Wifi

Chức năng chính và chức năng của ``wifi``

Function
----------------------

wifi.start(ssid = "wifi_ssid", password = "password", mode = codey.wifi.STA)
     Bật wifi 

wifi.is_connected()
     Kiểm tra xem wifi đã kết nối chưa


Sample Code：
----------------------
Hiển thị khoảng cách đo được từ cảm biến siêu âm 

.. code-block:: python

      while True:
            print(ultrasonic.distance_cm(1)) # Gắn vào PORT 2

