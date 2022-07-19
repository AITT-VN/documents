4. Bật nảy khi nhân vật gặp tường 
===========================

    .. image:: images/4.1.png
        :width: 600px
        :align: center 
    |

**Giới thiệu**

Một sprite có thể tự do di chuyển trên màn hình? Tất nhiên rối, trong bài này chúng ta sẽ tạo một sprite là một chiếc hăm-bơ-gơ nảy xung quanh màn hình.

Link chương trình mẫu: `Tại đây <https://arcade.makecode.com/57094-19039-40123-56950>`_

**Bước 1**

Tìm ``set mySprite to`` trong ``Sprite``. Kéo thả vào khối ``on start``.

    .. image:: images/4.2.png
        :width: 600px
        :align: center 
    |
**Bước 2**
Click vào hộp màu xám trong ``set mySprite to`` để mở trình chỉnh sửa hình ảnh. Mở thư viện ảnh **Gallery** tìm tìm một chiếc **burger** hay một chiếc bánh tùy thích.

    .. image:: images/4.3.png
        :width: 600px
        :align: center 
    |
**Bước 3**

Tìm ``set mySprite x to 0`` trong ``Sprite`` và đặt nó sau khối ``set mySprite to`` và thay đổi **x** thành **vx**, thay đổi 0 thành 40.

Với v là tốc độ di chuyển, vx là tốc độ di chuyển theo phương ngang. Nếu **vx** bằng 0 thì nhân vật được chọn sẽ đứng yên, nếu lớn hơn 0 thì sẽ nhân vật sẽ di chuyển sang phải, nhỏ hơn 0 sẽ di chuyển sang trái.

Điều này sẽ làm cho sprite di chuyển sang **phải** trên màn hình.

    .. image:: images/4.4.png
        :width: 600px
        :align: center 
    |
**Bước 4**

Tìm ``set mySprite x to 0`` trong ``Sprite`` và đặt nó sau khối ``set mySprite x to 0`` và thay đổi **y** thành **vy**, thay đổi 0 thành 60.

Tương tự như **vx**, **vy** là tốc độ di chuyển theo chiều dọc. Nếu **vy** bằng 0 thì nhân vật được chọn sẽ đứng yên, nếu lớn hơn 0 thì sẽ nhân vật sẽ di chuyển xuống dưới, còn nhỏ hơn 0 sẽ di chuyển lên trên.

Điều này sẽ làm cho sprite di chuyển xuống dưới màn hình, bạn có thể quan sát nó bên phần mô phỏng.

    .. image:: images/4.5.png
        :width: 600px
        :align: center 
    |
**Bước 5**

Tìm ``set mySprite stay in screen``  trong ``Sprite`` và đặt nó sau khối ``set mySprite x to 0``

    .. image:: images/4.6.png
        :width: 600px
        :align: center 
    |
**Bước 6**

Thay đổi ``stay in screen``  thành ``bounce on wall`` và chuyển sang chế độ ``on``.

Điều này sẽ làm cho chiếc hăm-bơ-gơ nảy ra khi va vào tường, thay đổi lại vx hoặc vy.

    .. image:: images/4.7.png
        :width: 600px
        :align: center 
    |
**Hoàn thành**

Nạp chương trình vào Game Kit và quan sát chiếc hăm-bơ-gơ di chuyển như một quả bóng nảy khi va vào tường.

