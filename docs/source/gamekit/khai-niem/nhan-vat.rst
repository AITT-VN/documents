1. Đưa nhân vật vào trò chơi 
===============================

    .. image:: images/1.1.png
        :width: 600px
        :align: center 
    |
**Giới thiệu**

Trong hướng dẫn này bạn sẽ học cách đưa một đối tượng **sprites** vào trò chơi của mình và di chuyển đối tượng này này bằng các nút điều khiển trên Game Kit.


**Bước 1**

Tìm ``set mySprite to`` trong ``Sprite``. Kéo thả vào khối ``on start``.

``Sprites`` này sẽ đại diện cho nhân vật chính trong trò chơi, hiện tại nó vẫn chưa có gì cả, khi bạn click vào biểu tượng sprites sẽ thấy trống rỗng.

    .. image:: images/1.2.png
        :width: 600px
        :align: center 
    |
**Bước 2**

Click vào hộp màu xám trong set ``mySprite to`` để mở trình chỉnh sửa hình ảnh. Sử dụng nó để vẽ một hình ảnh để thể hiện sprite mới của bạn trên màn hình hoặc bạn có thể chọn hình ảnh tương ứng trong **Gallery**.

Khi bạn đóng trình chỉnh sửa hình ảnh bằng cách nhấp vào **Done** bên dưới góc phải màn hình, hình ảnh bạn đã vẽ sẽ hiển thị ở giữa màn hình trong trình giả lập.

    .. image:: images/1.3.png
        :width: 600px
        :align: center 
    |
**Bước 3**

``Sprites`` này đại diện cho nhân vật chính trong trò chơi, vì vậy nó sẽ di chuyển khi người dùng nhấn nút trên GameKit.

Tìm ``move mySprite with buttons`` trong ``Controller``  và đặt nó sau khối set ``mySprite to``.

**Hoàn thành**

Giờ bạn hãy tải chương trình của mình xuống GameKit và thử tận hưởng nó xem như thế nào nhé.




















