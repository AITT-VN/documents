2. Nhiệm vụ 1 - Khám phá động Phong Nha
=========

2.1 Khu vực thi đấu & Yêu cầu 
------------
---------

Robot cần phải lần lượt sáng đèn LED với 3 màu theo thứ tự: Đỏ, vàng, xanh dương tương ứng với 3 khoảng trống trên đường line: 

..  figure:: images/nhiem_vu_1.png
    :scale: 100%
    :align: center 

    Nhiệm vụ 1

**Số điểm gợi ý:** Khi bật đúng màu đèn LED tại 1 vị trí khoảng trống, đội thi sẽ được 10 điểm (bật đúng 3 màu tại 3 vị trí sẽ được 30 điểm).


2.2 Hướng dẫn viết chương trình
-------
----------

Để lập trình cho robot Rover thi đấu, bạn cần tải thư viện **Robot Rover** và thư viện **Robocon**.

..  figure:: images/thu_vien.png
    :scale: 100%
    :align: center 

    Xem hướng dẫn tải thư viện `tại đây <https://docs.ohstem.vn/en/latest/module/cai-dat-thu-vien.html>`_.

Vì trên sa bàn này có nhiều nhiệm vụ khác nhau, nên chúng ta sẽ sử dụng đến khái niệm hàm. Mỗi hàm sẽ giải quyết 1 nhiệm vụ, để chương trình chính được đơn giản và tránh sai sót khi viết chương trình.

Trong nhiệm vụ đầu tiên này, chúng ta sẽ tạo 1 hàm và đặt tên là bài thi 1, đồng thời gọi tên nó trong chương trình chính.

..  figure:: images/ham_nhiem_vu_1.png
    :scale: 70%
    :align: center 
|

Chương trình giải quyết nhiệm vụ 1 sẽ nằm trong khối lệnh **hàm bài thi 1** này.

Để giải quyết nhiệm vụ 1, chúng ta sẽ chia nhỏ yêu cầu thành nhiều nhiệm vụ nhỏ hơn:

    - Nhiệm vụ 1-  Bật đèn đỏ ở nét đứt đầu tiên
    - Nhiệm vụ 2 - Bật đèn vàng ở nét đứt tiếp theo 
    - Nhiệm vụ 3 - Bật đèn xanh dương cuối cùng 

- **Nhiệm vụ 1 - Bật đèn đỏ ở nét đứt đầu tiên:**

    Robot đi theo đường line đen, đến khi hết vạch đen (4 mắt đều đọc được nền trắng) thì robot bật đèn LED màu đỏ. Sau đó, robot tiến tới 1 chút để đi qua khoảng trống này.

..  figure:: images/nhiem_vu_1.1.png
    :scale: 70%
    :align: center 
|

- **Nhiệm vụ 2 - Bật đèn vàng ở nét đứt tiếp theo**

    Tương tự như trên, khi robot khi đi hết vạch đen thì bật đèn LED màu vàng, sau đó tiến tới 1 chút.

..  figure:: images/nhiem_vu_1.2.png
    :scale: 70%
    :align: center 
|

- **Nhiệm vụ 3 - Bật đèn xanh dương cuối cùng** 

    Lập trình tương tự như trên, nhưng sau khi đi qua khoảng trống thì ta cho robot tiếp tục đi theo vạch đen để tiếp tục các thử thách tiếp theo. Chương trình hoàn chỉnh sẽ như sau:

..  figure:: images/nhiem_vu_1.3.png
    :scale: 80%
    :align: center 
|

2.3 **Tải chương trình mẫu**
---------------
--------

Bạn có thể tải chương trình mẫu tại đây:

* :download:`Nhiệm vụ 1 <https://app.ohstem.vn/#!/share/yolobit/2NLvGgb8rm1JDbtNwhnXPtFcDUP>`
