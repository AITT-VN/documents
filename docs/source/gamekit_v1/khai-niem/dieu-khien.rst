3. Điều khiển hoạt động nhân vật 
==============================

    .. image:: images/3.1.png
        :width: 600px
        :align: center 
    |
**Giới thiệu**

Một trò chơi không phải là một bức ảnh. trong trò chơi sẽ có các sprite nhân vật di chuyển trên màn hình và sẽ có các sự kiện xảy ra khi có 2 sprite va vào nhau. Trong bài hướng dẫn này mình sẽ tạo ra một cô công chúa đi ăn pizza. Khi sprite công chúa va vào sprite pizza thì trò chơi kết thúc.

Link chương trình mẫu: `Tại đây <https://makecode.com/_RzVeRhFLv58x>`_


**Bước 1**

Tìm ``set mySprite to`` trong ``Sprite``. Kéo thả vào khối ``on start``. Nhấp vào ``mySprite`` , chọn ``rename variable...`` và thay đổi tên từ ``mySprite``  thành ``princess``.

    .. image:: images/3.2.png
        :width: 600px
        :align: center 
    |
**Bước 2**
Mở trình chỉnh sửa hình ảnh cho ``princess``. Bạn có thể tạo hình ảnh tùy thích của riêng mình hoặc mở **Gallery** và chọn một mẫu có sẵn trong đó. Đừng quên nhấn **Done** để lưu lại lựa chọn của mình.

    .. image:: images/3.3.png
        :width: 600px
        :align: center 
    |
**Bước 3**

Tìm ``move mySprite with buttons`` trong ``Controller``  và đặt nó sau khối set ``mySprite to``. Thay đổi tên từ ``mySprite``  thành ``princess``.

    .. image:: images/3.4.png
        :width: 600px
        :align: center 
    |
**Bước 4**

Tìm ``set mySprite to`` trong ``Sprite``. Kéo thả vào khối ``on start``. Đổi tên từ ``mySprite`` thành ``pizza``.

    .. image:: images/3.5.png
        :width: 600px
        :align: center 
    |
**Bước 5**

Thay đổi ``Player`` thành loại ``Food``.

    .. image:: images/3.6.png
        :width: 600px
        :align: center 
    |
**Bước 6**

Tìm ``set mySprite position to x 0 y 0`` trong ``Sprite``. Thay đổi ``mySprite`` thành ``pizza`` và thay đổi giá trị x thành 140, y thành 100.

    .. image:: images/3.7.png
        :width: 600px
        :align: center 
    |
**Bước 7**

Tìm ``on sprite of kind Player overlaps otherSprite of kind Player`` trong ``Sprite`` và kéo nó vào không gian làm việc. Thay đổi ``Player`` thành loại ``Food``.

Sự kiện này sẽ xảy ra bất cứ khi nào hai Sprites va vào nhau.

    .. image:: images/3.8.png
        :width: 600px
        :align: center 
    |
**Bước 8**

Tìm ``game over`` trong ``game`` rồi kéo thả vào ``on sprite``.

Điều này khiến trò chơi kết thú khi công chúa chạm vào chiếc bánh.

    .. image:: images/3.9.png
        :width: 600px
        :align: center 
    |
**Hoàn thành**

Với bài hướng dẫn này bạn có thể, tạo ra nhiều sự kiện khác nhau trong trò chơi theo ý muốn của riêng mình.


















