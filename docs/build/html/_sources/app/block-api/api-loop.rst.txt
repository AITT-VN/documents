Các khối lệnh "Vòng lặp"
==========

time.sleep(s)
----------------------

Tạm dừng chương trình trong khoảng thời gian ``t`` (giây).

.. image:: images/loop-1.png
    :scale: 100 %
    :align: center

wait_for(lambda: )
----------------------

Dừng chương trình cho đến khi điều kiện bằng ``True``.

.. image:: images/loop-2.png
    :scale: 100 %
    :align: center

while False:
----------------------

Vòng lặp chính của chương trình. Các khối lệnh nằm trong vòng lặp lại mãi cho đến khi gặp khối lệnh ``Thoát``.

.. image:: images/loop-3.png
    :scale: 100 %
    :align: center

for count in range(x):
----------------------

Thực hiện các lệnh nằm bên trong một số lần ``x``.

.. image:: images/loop-4.png
    :scale: 100 %
    :align: center

while False: hoặc while not False:
----------------------

**trong:** Miễn là điều kiện còn đúng thì thực hiện các lệnh bên trong nó.

**cho đến:** Miễn là điều kiện còn sai thì thực hiện các lệnh bên trong nó. Khi điều kiện đúng thì ngưng lại.

.. image:: images/loop-5.png
    :scale: 100 %
    :align: center

for i in range(start, end):
----------------------

Cho biến ``i`` lấy giá trị từ số bắt đầu ``start`` đến số kết thúc ``end``, đếm theo khoảng thời gian (tính theo giây) đã chỉ định và thực hiện các khối lệnh được chỉ định.

.. image:: images/loop-6.png
    :scale: 100 %
    :align: center

for j in []:
----------------------

Trong một danh sách, lấy từng thành phần gán vào biến j, rồi thực hiện các lệnh bên trong nó.

.. image:: images/loop-7.png
    :scale: 100 %
    :align: center

break
----------------------

Thoát khỏi bất kì vòng lặp nào.

.. image:: images/loop-8.png
    :scale: 100 %
    :align: center


Các ví dụ
----------------------

**Ví dụ 1:** Sử dụng ""vòng lặp mãi""

.. image:: images/loop-9.png
    :scale: 100 %
    :align: center

**Ví dụ 2:** Sử dụng vòng lặp ""for""

.. image:: images/loop-10.png
    :scale: 100 %
    :align: center

**Ví dụ 3:** Sử dụng vòng lặp ""chờ cho đến khi""

.. image:: images/loop-11.png
    :scale: 100 %
    :align: center

**Ví dụ 4:** Sử dụng khối ""thoát"". Loa sẽ phát nốt nhạc 10 lần. Nếu bạn nhấn nút trên xController, loa sẽ dừng phát nhạc ngay lập tức.

.. image:: images/loop-12.png
    :scale: 100 %
    :align: center