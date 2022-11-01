:mod:`ble` --- Bluetooth Low Energy
=============================================

Chức năng chính và chức năng của ``Bluetooth Low Energy``

xController sử dụng chip điều khiển ESP32, tích hợp nhiều kết nối không dây bao gồm Wi-Fi và Bluetooth Low Energy (BLE). BLE là một công nghệ Bluetooth tiết kiệm năng lượng, chủ yếu được dùng để truyền lượng dữ liệu nhỏ (băng thông thấp) với khoảng cách ngắn. 

Khác với chuẩn Bluetooth classic luôn được bật, BLE ngủ liên tục trừ khi bắt đầu kết nối. Đây là lý do BLE tiêu thụ năng lượng thấp: lượng tiêu thụ ít hơn 100 lần so với Bluetooth classic (tùy vào môi trường sử dụng). Hơn nữa, BLE không chỉ hỗ trợ giao tiếp Point-to-Point mà còn hỗ trợ Broadcast và Mesh Network.

Do tính chất của nó, BLE phù hợp với các ứng dụng cần trao đổi một lượng nhỏ dữ liệu định kỳ, chỉ chạy trên một viên Pin.

Ví dụ, BLE được sử dụng rất nhiều trong chăm sóc sức khỏe, thể dục, theo dõi, Beacons, an ninh và nhà thông minh.

Function
----------------------

.. function:: BLE.begin(name)

  Phát BLE với tên gọi là ``name`` để phần mềm có thể quét ra được và kết nối.

.. function:: BLE.available()

  Trả về kết quả thông báo BLE có đang nhận được dữ liệu nào hay không.
  
.. function:: BLE.isConnected();

   Trả về kết quả kiểu ``bool`` thông báo BLE đã được kết nối với thiệt bị khác hay chưa.

.. function:: BLE.read()

  Trả về các kết quả từ thiết bị khác gửi đến qua ``BLE``.

.. function:: BLE.write()

  Gửi thông tin từ xController đến thiết bị hỗ trợ BLE và đã kết nối với xController.

  Các thông tin gửi đi có thể ở các dạng float, string, int, uint8_t.

.. function:: BLE.stop()

  Ngắt kết nối BLE.


Sample Code
----------------------

Xem hướng dẫn cụ thể sử dụng BLE tại Bài 13 - Arduino Smarthome.


