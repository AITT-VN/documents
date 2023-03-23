3. Nhiệm vụ 3 - Robot tự né vật cản
============

3.1 Khu vực thi đấu & Yêu cầu
--------
-----------

Để thực hiện nhiệm vụ này, Robot sẽ xuất phát tại vị trí ô vuông màu đỏ số 3, và kết thúc nhiệm vụ tại vị trí ô vuông màu đỏ số 1.

Trên sa bàn sẽ đặt 1 vật cản tại vị trí được đánh dấu số 3 như hình dưới, robot cần đi theo vạch đen và khi gặp vật cản thì di chuyển vòng qua để né tránh, sau đó quay lại vạch đen và đi tiếp để đến đích (là ô màu đỏ số 1).

..  figure:: images/nhiem_vu_3.png
    :scale: 100%
    :align: center 

    Nhiệm vụ 3
|


3.2 Hướng dẫn viết chương trình
-----
-------

Chúng ta sẽ tạo thêm một hàm để robot đi vòng qua vật cản, sau đó quay trở lại đường line đen và tiếp tục di chuyển. 

Trong chương trình, robot sẽ liên tục đi theo đường line, cho đến khi phát hiện vật cản trên đường đi. Nếu khoảng cách đến vật cản bé hơn 8cm, robot sẽ dừng lại, sau đó đi vòng qua vật cản bằng cách rẽ phải, sau đó rẽ trái liên tục trở về đường line.

Theo như robot khi viết tài liệu hướng dẫn này, robot rẽ phải tốc độ 50 trong 0.15s, sau đó quay 2 động cơ trái phải như chương trình dưới thì robot sẽ quay lại đường line được. Bạn cần tinh chỉnh tốc độ này sao cho phù hợp với robot của bạn nhé!

..  figure:: images/vong_qua_vat_can.png
    :scale: 80%
    :align: center 
|

Sau khi viết xong hàm này, bạn hãy tiến hành gọi tên chúng trong chương trình chính nhé! 

3.3 **Tải chương trình mẫu**
---------------
--------

Bạn có thể tải chương trình hoàn chỉnh của 3 nhiệm vụ: 

* :download:`Bài thi sa bàn robot cơ bản <https://app.ohstem.vn/#!/share/yolobit/2NJ9Lff3p3Rud9a74iSXJFuAKdq>`