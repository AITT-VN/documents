1. Giới thiệu về robot Rover 
============================

**1.1 Robot Rover là gì?**

--------------------------------

Robot Rover là xe lập trình điều khiển thông minh, được thiết kế để ứng dụng vào giảng dạy STEM cho học sinh và người mới bắt đầu học lập trình. Bộ Kit này sẽ là công cụ giúp trẻ phát triển tư duy sáng tạo và trí tuệ hiệu quả. Thông qua phương pháp lập trình kéo thả khối lệnh đơn giản, chúng ta có thể xây dựng nhiều tính năng thú vị và độc đáo cho Robot Rover.

**1.2 Hình ảnh**

--------------------------

    .. image:: images/rover_1.1.png
        :width: 400px
        :align: center 
    |

**1.3 Tham số**

---------------

====================================== =========================== 
    **Tên**                                     **Tham số**
 Điện áp                                    3.3 V
 Kích thước                                 130mm x 140mm x 70mm
 Điều khiển hồng ngoại                      Kết nối với P4 
 Đèn RGB WS2812B                            6 x RGB kết nối với P6
 LED trắng                                  2 Led 5mmm kết nối với I2C 
 Kết nối                                    Cổng IIC (P19, P20), Cổng Servo (S1-P16, S2-P3), Cổng siêu âm (Ultrasonic) (P13-P14), P0, P1 
 Động cơ                                    Động cơ giảm tốc vi bánh răng GA12-N20 DC (145 vòng / phút)
 Cảm biến siêu âm                           HC-SR04 (phát hiện khoảng cách không tiếp xúc 2cm-200cm, độ chính xác ± 1.5mm)
 Cảm biến dò đường                          4 x mắt đọc
====================================== ===========================


**1.4 Giới thiệu các Mô - đun chính của Rover**

------------------------------------

Mắt nhận hồng ngoại kết nối với cổng P4 của Yolo:Bit được đặt ở phần đầu Rover 

    .. image:: images/5_rover.png
        :width: 400px
        :align: center 
    |
Hai đèn LED trắng đầy đủ màu được điều khiển bởi mạch mở rộng robot Rover, được đặt cả hai bên của phần mặt trước 

    .. image:: images/2_rover.png
        :width: 400px
        :align: center 
    |
Sáu đèn LED RGB được đặt ở 2 phía mặt trước của Rover, có thể pha màu và sử dụng làm đèn chiếu sáng. 
   
    .. image:: images/3_rover.png
        :width: 400px
        :align: center 
    |
Kết nối cảm biến khoảng cách và cổng I2C, cổng Servo(S1,S2) được đặt ở phía sau Rover:

    .. image:: images/4_rover.png
        :width: 400px
        :align: center 
    |
Khe cắm pin Lipo 18650 được đặt ở giữa Rover.
  
    .. image:: images/9_rover.png
        :width: 400px
        :align: center 
    |
Công tắc nguồn, được đặt ở bên trái xe.
 
    .. image:: images/10_rover.png
        :width: 400px
        :align: center 
    |
Cảm biến dò đường kết nối với cổng I2C của Yolo:Bit đặt ở phía dưới Rover được sử dụng để phát hiện đường màu đen.  

    .. image:: images/6_rover.png
        :width: 400px
        :align: center 
    |
Bánh xe đa năng được đặt ở phía trước của Rover, có thể đi được mọi hướng với các tốc độ khác nhau
 
    .. image:: images/7_rover.png
        :width: 400px
        :align: center 
    |
Hai bánh xe ở cả hai bên được dẫn bởi động cơ giảm tốc DC vi bánh răng (145 vòng/ phút)

    .. image:: images/8_rover.png
        :width: 400px
        :align: center 
    |
