:mod:`ir_receiver` --- IR Receiver Sensor
=============================================

.. module:: ir_receiver
    :synopsis: IR Receiver Sensor

Chức năng chính và chức năng của ``ir_receiver``

Function
----------------------

ir_rx.get_code() == IR_REMOTE_A
  Trả về chuỗi tương ứng với phím được nhấn trên IR remote. Trên remote có các nút nhấn là A|B|C|D|E|F|lên|xuống|trái|phải|setup|0|1|2|3|4|5|6|7|8|9, tương ứng với các giá trị đã được khai báo sẵn trong thư viện như sau: IR_REMOTE_A, IR_REMOTE_B ... IR_REMOTE_F .. IR_REMOTE_0 .. IR_REMOTE_9, IR_REMOTE_SETUP

ir_rx.get_code()
   Trả về chuỗi giá trị HEX. 

ir_rx.get_raw_code()
   Trả về chuỗi giá trị chưa được xử lý

ir_rx.clear_code()
   Xóa các giá trị đã nhận để tránh trùng lặp với các giá trị mới.

Sample Code：
----------------------
In giá trị nhận được từ IR Remote

.. code-block:: python

  from ir_receiver import *; ir_rx.start();

  while True:
    if ir_rx.get_code() == IR_REMOTE_A:
      print('Nhận giá trị từ nút A trên remote')
      ir_rx.clear_code()
    if ir_rx.get_code() == IR_REMOTE_B:
      print('Nhận giá trị từ nút B trên remote')
      ir_rx.clear_code()
