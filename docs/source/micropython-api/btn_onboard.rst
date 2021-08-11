:mod:`btn_onboard` --- Onboard Button
=============================================

.. module:: btn_onboard
    :synopsis: Onboard Button

Chức năng chính và chức năng của ``btn_onboard``

Function
----------------------

.. function::  btn_onboard.is_pressed()

  Lấy giá trị hiện tại của nút nhấn trên board.
  Kết quả trả về là ``True``: Khi nút được nhấn, hoặc là ``False``: Khi nút không được nhấn.

Sample Code
----------------------

.. code-block:: python

  while True:
    if btn_onboard.is_pressed():
        print("Button Onboard is pressed")