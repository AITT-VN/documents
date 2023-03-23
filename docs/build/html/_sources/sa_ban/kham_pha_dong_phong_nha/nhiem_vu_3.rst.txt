4. Nhiệm vụ 3 - Dâng hoa Bác Giáp
========

3.1 Khu vực thi đấu & Yêu cầu 
------------
---------

Robot tiếp tục di chuyển theo vạch đen, khi tới vạch ngang là nơi đặt sẵn mô hình lẵng hoa, robot tiến hành gắp lẵng hoa, di chuyển và đặt lẵng hoa tại vị trí dâng hương hoa tại đền thờ Bác Giáp.

..  figure:: images/nhiem_vu_3.png
    :scale: 100%
    :align: center 

    Nhiệm vụ 3

Cách thức tính điểm gợi ý: 

    - Robot lấy lẵng hoa và đặt đúng lẵng hoa vào vị trí trưng bày: 30 điểm
    - Robot lấy lẵng hoa nhưng đặt sai vị trí lẵng hoa (đặt bên ngoài khu vực vị trí trưng bày): 15 điểm.
    - Robot di chuyển đến điểm checkpoint màu vàng tiếp theo mới tính hoàn thành nhiệm vụ
    - Robot không lấy được lãnh hoa: 0 điểm


3.2 Hướng dẫn viết chương trình
-------
----------

Tương tự như các nhiệm vụ trên, chúng ta cũng tạo 1 hàm mới tên là **bài thi 3**, sau đó gọi tên hàm này trong chương trình chính.

..  figure:: images/nhiem_vu_3.1.png
    :scale: 100%
    :align: center 
|

Chúng ta sẽ chia nhỏ yêu cầu thành nhiều nhiệm vụ nhỏ bên trong:

    - Nhiệm vụ 1 - Nhận diện vị trí đặt lẵng hoa
    - Nhiệm vụ 2 - Gắp và di chuyển đến đền thờ Bác Giáp
    - Nhiệm vụ 3 - Thả lẵng hoa và quay về đường line ban đầu

- **Nhiệm vụ 1 - Nhận diện vị trí đặt lẵng hoa**

    Ban đầu, chúng ta cho robot mở tay gắp (lập trình servo quay đến góc 0 độ) để chuẩn bị cho việc gắp lẵng hoa:

..  figure:: images/nhiem_vu_3.2.png
    :scale: 100%
    :align: center 
|

    Ghi chú: Dưới đây là góc đóng và mở của tay gắp:

..  figure:: images/dong_mo_tay_gap.png
    :scale: 100%
    :align: center 
|

Trước vị trí đặt lẵng hoa (vị trí đánh số 1 như hình dưới), trên sa bàn có 1 đường line ngang để báo hiệu:

..  figure:: images/nhiem_vu_3.3.png
    :scale: 100%
    :align: center 
|

Khi đến vị trí vạch đen ngang, 4 mắt hồng ngoại trên robot đều sẽ thấy vạch đen, đồng thời, cảm biến siêu âm sẽ nhận được tín hiệu có vật cản trước mặt ở khoảng cách gần hơn 3cm. Lúc này, ta cho robot dừng lại:

..  figure:: images/nhiem_vu_3.4.png
    :scale: 70%
    :align: center 
|

- **Nhiệm vụ 2 - Gắp và di chuyển đến đền thờ Bác Giáp**

    Sau khi dừng lại, ta cho robot kẹp tay gắp lại để gắp lẵng hoa và tiếp tục di chuyển theo đường line. Trước đền thờ Bác Giáp, trên sa bàn cũng có vạch đen ngang để báo hiệu. Lúc này, robot sẽ rẽ trái và tiến tới để đến được đền thờ Bác Giáp rồi dừng lại.

    Theo robot khi viết tài liệu, khi rẽ trái (tốc độ 20) trong 0.15 giây và tiến tới (tốc độ 25) trong 2 giây thì sẽ đến đúng vị trí đền thờ trên sa bàn. Bạn cần tinh chỉnh lại các thông số này sao cho phù hợp với robot của mình, để robot đến đúng vị trí đền thờ nhé!


..  figure:: images/nhiem_vu_3.5.png
    :scale: 70%
    :align: center 
|

- **Nhiệm vụ 3 - Thả lẵng hoa và quay về đường line ban đầu** 

    Chúng ta tiến hành mở tay gắp (quay servo đến góc 0 độ) để thả lẵng hoa, sau đó lùi lại và rẽ phải, tiếp tục đi theo đường line đen.

    Tương tự như nhiệm vụ trước, bạn cần chỉnh lại thông số tốc độ và thời gian lùi lại, rẽ phải để robot có thể quay về đúng vạch line đen nhé! Dưới đây là chương trình tham khảo:

..  figure:: images/nhiem_vu_3.6.png
    :scale: 100%
    :align: center 
|

3.3 **Tải chương trình mẫu**
---------------
--------

Bạn có thể tham khảo chương trình hoàn chỉnh cho 3 nhiệm vụ tại đây:

* :download:`Bài thi Khám phá động Phong Nha <https://app.ohstem.vn/#!/share/yolobit/2NJhOZldXxLfhgP7olRogGwv5HK>`