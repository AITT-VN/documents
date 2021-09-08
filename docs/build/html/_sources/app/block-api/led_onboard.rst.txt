LED RGB tích hợp trên board
=============================================

Chức năng chính của LED RGB tích hợp trên board

xController được tích hợp sẵn 2 đèn LED đa màu RGB trên board. Đèn LED RGB là đèn LED đặc biệt, có thể phát sáng với nhiều màu khác nhau (lên đến 16 triệu màu). Màu của đèn LED được tổng hợp từ 3 đèn màu đỏ (Red), xanh lục (Green), xanh lam (Blue) bên trong. 

Các LED màu này có độ sáng từ 0 đến 255. Để thay đổi màu đèn LED RGB, chúng ta sẽ thay đổi độ sáng của 3 LED màu này.

.. image:: images/led_RGB.jpg
    :width: 400
    :align: center

led_onboard.show(index, color, time)
----------------------

.. image:: images/led-onboard-1.png
    :width: 320
    :align: center

Hiển thị cả 2 đèn led trên mạch xController với màu sắc như bảng lựa chọn trong khoảng thời gian ``time`` (Tính theo giây).

led_onboard.show(index, color)
----------------------

.. image:: images/led-onboard-2.png
    :width: 320
    :align: center

Hiển thị đèn led trên mạch xController tùy chọn từng màu sắc cho đèn bên trái hoặc đèn bên phải.


led_onboard.show(0, (50, 50, 50))
----------------------

.. image:: images/led-onboard-3.png
    :width: 320
    :align: center

Hiển thị đèn led trên mạch xController tùy chọn từng thông số ``R|G|B`` màu sắc cho đèn bên trái, đèn bên phải, hoặc cả hai.


led_onboard.show(0, (0, 0, 0))
----------------------

.. image:: images/led-onboard-4.png
    :width: 320
    :align: center

Tắt toàn bộ LED.


Ví dụ
----------------------
Bật tắt hai LED Onboard

.. image:: images/led-onboard-5.png
    :width: 480
    :align: center

