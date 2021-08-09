:mod:`oled_i2c` --- OLED I2C Module
=============================================

.. module:: oled_i2c
    :synopsis: OLED I2C Module

Chức năng chính và chức năng của ``oled_i2c``

Function
----------------------

oled = OledI2C(PORT)
      Khai báo PORT đã được kết nối với module.
      PORT: Có giá trị từ 0 đến 5 tương ứng từ PORT 1 đến PORT 6 của xController.

oled.text(TEXT, [X], [Y]);
      Thiết lập nội dung (TEXT) lên màn hình tại vị trí muốn xuất hiện kí tự, trong đó:
          X: Tọa độ theo chiều ngang. (0 <= X <= 128)
          Y: Tọa độ theo chiều dọc. (0 <= Y <= 64)

oled.show()
      Lệnh hiển thị nội dung.

oled.fill(0);
     Xóa nội dung trên màn hình.

Sample Code：
----------------------
Hiển thị kí tự trên màn hình OLED

.. code-block:: python

     from oled_i2c import OledI2C

     while True:
          oled = OledI2C(0)
          oled.text('OSTEM', 2, 2);
          oled.show()
          time.sleep(2)
          oled.fill(0);
          oled.show()
