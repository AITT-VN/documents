OLED I2C Module
=============================================

Chức năng chính của Module OLED I2C 

.. function:: oled = OledI2C(PORT)
----------------------

.. image:: images/oled-1.png
    :width: 400
    :align: center

Khai báo PORT đã được kết nối với module.

PORT: Có giá trị từ 1 đến 6 tương ứng từ PORT 1 đến PORT 6 của xController.

.. function::
      oled.text(TEXT, [X], [Y]);
      oled.show()
----------------------

.. image:: images/oled-2.png
    :width: 400
    :align: center

Thiết lập nội dung (TEXT) lên màn hình tại vị trí muốn xuất hiện kí tự, trong đó:

      X: Tọa độ theo chiều ngang. (0 <= X <= 128)
      Y: Tọa độ theo chiều dọc. (0 <= Y <= 64)


.. function:: 
      oled.fill(0)
      oled.show()
----------------------

.. image:: images/oled-3.png
    :width: 300
    :align: center

Xóa nội dung trên màn hình.

Ví dụ:
----------------------
Hiển thị kí tự trên màn hình OLED

.. image:: images/oled-4.png
    :width: 480
    :align: center
