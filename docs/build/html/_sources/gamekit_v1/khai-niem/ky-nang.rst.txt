6. Tạo kỹ năng cho nhân vật 
=========================

    .. image:: images/6.1.png
        :width: 600px
        :align: center 
    |
**Giới thiệu**

Ở bài này các bạn sẽ học cách tạo kỹ năng bắn đạn từ nhân vật trong trò chơi.

**Bước 1**

Tìm ``set mySprite to`` trong ``Sprites``, kéo thả vào khối ``on start``. Mở trình chỉnh sửa hình ảnh của ``mySprite`` và chọn hình ảnh nhân vật mà bạn thích.

    .. image:: images/6.2.png
        :width: 600px
        :align: center 
    |
**Bước 2**

Tìm ``projectile from mySprite`` trong ``Sprites``, kéo thả vào khối ``on A button pressed``.

Việc này giúp tạo ta một ``Sprite``  có vai trò là đạn xuất hiện cùng vị trí với ``mySprite`` và bắn ra phía nào bất kì. Chúng ta sẽ đặt 2 giá trị **vx** và **vy** lần lượt là 100 và 0 để đạn bắn từ trái sang phải.

Cuối cùng, mở trình chỉnh sửa hình ảnh ``projectile``, và tạo hình ảnh viên đạn mà bạn thích.
  
    .. image:: images/6.3.png
        :width: 600px
        :align: center 
    |
**Hoàn thành**

    .. image:: images/6.4.png
        :width: 600px
        :align: center 
    |
Hãy tải chương trình vào Game Kit của bạn và thử xem trò chơi hoạt động như thế nào nhé.



















