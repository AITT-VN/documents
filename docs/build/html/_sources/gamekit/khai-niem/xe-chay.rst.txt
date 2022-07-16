7. Tạo hiệu ứng xe chạy
=========================

    .. image:: images/7.1.png
        :width: 600px
        :align: center 
    |
**Giới thiệu**

Trong trò chơi cần có các sự kiện xảy ra liên tục, để tạo bối cảnh trong game. Trong bài hướng dẫn này mình sẽ hướng dẫn các bạn tạo sự kiện các xe chạy ngẫu nhiên trên màn hình.

Link chương trình mẫu: `Tại đây <https://makecode.com/_RwpEYbP7oRWo>`_

**Bước 1**

Tạo khối ``on game update interval 500 ms``, đặt 500ms thành 1000ms (1 giây). Nghĩa là sự kiện này sẽ xảy ra mỗi giây một lần.

    .. image:: images/7.2.png
        :width: 600px
        :align: center 
    |
**Bước 2**

Tìm ``projectile from side`` trong ``Sprites`` và kéo thả nó vào khối ``on game update interval``. Mở trình chỉnh sửa hình ảnh ``projectile`` và chọn hoặc tạo hình ảnh của một chiếc xe.

Trong ``projectile``, đặt **vy** thành 0, để xe chỉ di chuyển sang phải.
 
    .. image:: images/7.3.png
        :width: 600px
        :align: center 
    |
**Bước 3**

Tìm ``set mySprite x to 0`` từ **Sprites** và kéo, thả vào sau khối ``set projectile to``. Thay đổi ``mySprite`` thành ``projectile`` và đổi ``x`` thành ``y``.

    .. image:: images/7.4.png
        :width: 600px
        :align: center 
    |
**Bước 4**

Tìm ``pick random 0 to 10`` trong ``Math`` và đặt vào vị trí 0 trong ``set projectile y to 0``. Điều này sẽ đặt ``projectile`` vào vị trí ngẫu nhiên của ``y`` trong khoảng từ 0 đến 10.

Tìm ``screen height`` trong ``Scene`` và đặt vào vị trí có giá trị là 10 cùa khối ``pick random 0 to 10``.
``screen height`` là chiều cao của màn hình (120), do đó,  ``projectile``  sẽ xuất hiện ở một vị trí ngẫu nhiên phía bên trái màn hình.

    .. image:: images/7.5.png
        :width: 600px
        :align: center 
    |
**Hoàn thành**

Hãy thử tải chương trình xuống kit và quan sát kết quả.




































