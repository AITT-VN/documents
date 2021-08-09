:mod:`ir_sender` --- IR Sender
=============================================

.. module:: ir_sender
    :synopsis: IR Sender

Chức năng chính và chức năng của ``ir_sender``

Function
----------------------

ir_tx.send(data)
   Gửi giá trị IR từ xController đến một hoặc nhiều thiết bi có hỗ trợ mắt đọc hồng ngoại.

ir_tx.send(data, address)
   Gửi giá trị IR từ xController đến một thiết bi có địa chỉ cụ thể có hỗ trợ mắt đọc hồng ngoại.

Sample Code：
----------------------
Gửi giá trị IR từ xController khi nhấn nút nhấn trên board.

.. code-block:: python

  from ir_sender import *

  while True:
    if btn_onboard.is_pressed():
      ir_tx.send(69)
