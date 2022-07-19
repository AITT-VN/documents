5. Thiết lập vị trí của nhân vật 
==============================

    .. image:: images/2.1.png
        :width: 600px
        :align: center 
    |
**Giới thiệu**

``Sprites`` có thể được đặt ở các vị trí khác nhau trên màn hình. Điều này được thực hiện bằng cách thiết lập tọa độ x và y tương ứng với vị trí của chúng trên màn hình GameKit.

Với x = 0, y = 0 sẽ cho vị trí góc trên cùng, bên trái màn hình.

**Bước 1**

Tìm ``set mySprite to`` trong ``Sprite``. Kéo thả vào khối ``on start``. Nhấp vào ``mySprite`` , chọn ``rename variable...`` và thay đổi tên từ ``mySprite`` thành ``cherry``.

    .. image:: images/2.2.png
        :width: 600px
        :align: center 
    |
**Bước 2**

Mở trình chỉnh sửa hình ảnh cho ``cherry``. Bạn có thể vẽ hình ảnh tùy thích của riêng mình hoặc mở **Gallery** và chọn một mẫu có sẵn trong đó. Đừng quên nhấn **Done** để lưu lại lựa chọn của mình.

    .. image:: images/2.3.png
        :width: 600px
        :align: center 
    |

**Bước 3**

Tìm ``set mySprite position to x 0 y 0`` trong ``Sprite``. Thay đổi ``mySprite`` thành ``cherry`` và thay đổi giá trị x thành 25.

Điều này sẽ đặt sprites quả táo lên phía trên màn hình, cách xa bên trái một khoảng 25 pixel.

    .. image:: images/2.4.png
        :width: 600px
        :align: center 
    |

**Bước 4**

Trong set ``mySprite position to x 0 y 0`` trong ``Sprite``. Thay đổi tiếp giá trị y thành 45.

Điều này sẽ di chuyển sprites quả táo xuống phía dưới một khoảng 45 pixel nữa.

    .. image:: images/2.5.png
        :width: 600px
        :align: center 
    |
**Hoàn thành**

Bạn hãy tải chương trình xuống GameKit và quan sát vị trí của sprite. Bằng cách xác định vị trí của các nhân vật trong trò chơi, bạn hoàn toàn có thể tự tay tạo ra một khung cảnh với cây cối, nhà cửa, cảnh vật trong trò chơi của mình.





















