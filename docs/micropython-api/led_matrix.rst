:mod:`led_matrix` --- LED Matrix
=============================================

.. module:: led_matrix
    :synopsis: LED Matrix

Chức năng chính và chức năng của ``led_matrix``

Function
----------------------

led_matrix.show(PORT, Image.IMAGE)
     Hiển thị lên màn hình LED Matrix những hình ảnh có sẵn, trong đó:
         PORT: Khai báo PORT đã được kết nối với LED Matrix.
         IMAGE: HEART|SMILE|SAD|CONFUSED|ARROW_N|ARROW_E|ARROW_S|ARROW_W|TRIANGLE|QUARE
      
led_matrix.show(PORT, TEXT)
     Hiển thị lên màn hình LED Matrix những văn bản bất kì, trong đó:
         PORT: Khai báo PORT đã được kết nối với LED Matrix.
         TEXT: Văn bản bạn muốn hiển thị.

Sample Code：
----------------------
Hiển thị hình trái tim và chữ OHSTEM lên màn hình LED Matrix

.. code-block:: python

    while True:
        led_matrix.show(0, Image.HEART)
        time.sleep(2)
        led_matrix.show(0, '')
        time.sleep(0.5)
        led_matrix.show(0, 'OHSTEM')
        time.sleep(2)
        led_matrix.show(0, '')
        time.sleep(0.5)
