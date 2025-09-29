**Mạch mở rộng Motion Kit**
=========


**1. Giới thiệu**
---------
------------

.. image:: images/motion-kit.1.png
    :width: 400px
    :align: center
|

Mạch mở rộng Motion Kit là một công cụ giúp nâng cao khả năng của robot Rover, cho phép mở rộng cổng kết nối động cơ một cách dễ dàng. Nhờ có Motion Kit, robot Rover có thể tích hợp thêm các cơ cấu như cuộn bóng hay bắn bóng và nhiều cơ cấu sáng tạo khác từ bạn.

Ngoài ra, Motion Kit còn tương thích với Grove Shield – mạch mở rộng cho Yolo:Bit, giúp bạn tạo ra những sản phẩm robot độc đáo thông qua các cổng mở rộng có sẵn.

Với 4 cổng động cơ servo, 2 cổng động cơ XH 2.54, 1 cổng cấp nguồn và 1 cổng Grove, Motion Kit mang đến sự linh hoạt tối ưu trong việc kết nối và điều khiển nhiều loại động cơ khác nhau.

.. image:: images/motion-kit.2.png
    :width: 600px
    :align: center
|

Trong hướng dẫn này, chúng tôi sẽ hướng dẫn bạn cách kết nối thêm 1 động cơ DC và 1 động cơ servo với robot Rover, giúp bạn mở rộng thêm cơ cấu robot của mình. 


**2. Thông số kỹ thuật**
---------
------------

- Hỗ trợ nguồn pin 3.7V
- Tích hợp mạch sạc
- Hỗ trợ động cơ DC dưới 6V

 
**3. Kết nối phần cứng**
---------
------------   

- **Bước 1**: Chuẩn bị các thiết bị như sau: 

.. list-table:: 
   :widths: auto
   :header-rows: 1
     
   * - .. image:: images/motion-kit.1.png
          :width: 150px
          :align: center
     - .. image:: images/robot-rover.png
          :width: 400px
          :align: center
     - .. image:: images/servo.png
          :width: 400px
          :align: center
     - .. image:: images/dong-co-dc.png
          :width: 200px
          :align: center
   * - Motion Kit (kèm dây tín hiệu)
     - Robot Rover
     - Động cơ servo
     - Động cơ DC giảm tốc 6V
   * - `Mua sản phẩm <https://shop.ohstem.vn/san-pham/mach-mo-rong-motion-kit/>`_
     - `Mua sản phẩm <https://shop.ohstem.vn/san-pham/robot-stem-rover-v2/>`_
     - `Mua sản phẩm <https://shop.ohstem.vn/san-pham/dong-co-servo-mg90s/>`_
     - `Mua sản phẩm <https://shop.ohstem.vn/san-pham/dong-co-dc-giam-toc-6v/>`_

- **Bước 2**: Kết nối các thiết bị như hình
    
    + Kết nối Motion Kit vào cổng I2C trên Rover
    + Trên Motion Kit kết nối: 
        - Servo vào cổng S4
        - Động cơ DC vào cổng M1 
        - Pin vào cổng nguồn

..  figure:: images/motion-kit.3.png
    :scale: 70%
    :align: center 
|


**5. Hướng dẫn lập trình**
--------
------------

1. Tải thư viện **Motion Kit**, bằng cách dán đường link sau vào phần tìm kiếm thư viện: `<https://github.com/AITT-VN/yolobit_extension_motion_kit.git>`_

    Xem hướng dẫn tải thư viện `tại đây <https://docs.ohstem.vn/en/latest/module/thu-vien-yolobit.html>`_

    ..  figure:: images/motion-kit.4.png
        :scale: 80%
        :align: center 
    |

    Thư viện sẽ gồm các câu lệnh điều khiển 2 động cơ và 4 servo:

    ..  figure:: images/motion-kit.5.png
        :scale: 80%
        :align: center 
    |   

2. **Viết chương trình:**

**2.1. Chương trình kiểm tra hoạt động của Motion Kit và các động cơ mở rộng:**

    Với chương trình mẫu sau, bạn có thể dùng nút A và B trên Yolobit module mở rộng Motion Kit:

..  figure:: images/motion-kit.6.png
    :scale: 50%
    :align: center 

    Link chương trình: `<https://app.ohstem.vn/#!/share/yolobit/2nAKUw7EB6fGpnf5r7rfvBX4LaR>`_      

.. note:: 
    Khi nhấn nút A, động cơ M1 và M2 sẽ quay với tốc độ 50, đồng thời 4 cổng servo sẽ quay đến vị trí 90. Khi ấn nút B thì động cơ M1, M2 sẽ quay ngược chiều với tốc độ 50 và 4 servo sẽ quay về vị trí 0. Khi ấn nút A+B thì 2 động cơ M1 và M2 sẽ dừng quay.


**2.2. Chương trình kết hợp robot Rover với Motion Kit cùng các động cơ để tạo nên phần cuộn bóng cho robot và được điều khiển từ Gamepad**

..  figure:: images/motion-kit.7.png
    :scale: 60%
    :align: center 

    Link chương trình: `<https://app.ohstem.vn/#!/share/yolobit/2n8sxBbVkdPzc1mnY9iua5mtOkw>`_

.. note:: 
    Trong phần lặp mãi mãi, chúng ta sẽ kiểm tra điều kiện joystick phải được kéo theo trục x (phương ngang). Nếu kéo về phía bên phải thì giá trị joystick sẽ là giá trị dương và ngược lại. Khi so sánh với 50 để đảm bảo rằng joystick được kéo theo đúng chiều và không bị ảnh hưởng bởi giá trị nhiễu khi joystick đứng. Lúc này động cơ cổng M1 của Motion kit sẽ hoạt động và tiến hành cuộn - thả theo thiết kế cơ khí. Khi ấn nút joystick phải, động cơ sẽ quay tốc độ 0 (tức là dừng quay).
