Cảm biến dò vạch đen
=============================================


Chức năng chính và chức năng của cảm biến dò vạch đen.

line_array.read(PORT)
----------------------

.. image:: images/line-array-1.png
    :width: 320
    :align: center


Đọc trạng thái của cảm biến dò vạch.
Trong đó:

    - *PORT* : Có giá trị từ ``1 ~ 6`` tương ứng từ PORT 1 đến PORT 6 của xController.
    - Kết quả trả về ``TUPLE`` 4 giá trị tương ứng với trạng thái của 4 mắt S1 đến S4, ví dụ: ``(0, 1, 1, 0)`` với ``0`` là đọc được line trắng còn ``1`` là line đen.


line_array.read(PORT, TUPLE)
----------------------

.. image:: images/line-array-2.png
    :width: 320
    :align: center

Đọc trạng thái từng mắt đọc của cảm biến dò vạch.
Trong đó:
    
    - *PORT* : Có giá trị từ ``1 ~ 6``tương ứng từ PORT 1 đến PORT 6 của xController.
    - *TUPLE* : Có giá trị từ ``S1 ~ S4`` tương ứng với 4 mắt đọc của Module.

Ví dụ
----------------------
Test module bám line đen

.. image:: images/line-array-3.png
    :width: 320
    :align: center

Test trạng thái mắt đọc số 1

.. image:: images/line-array-4.png
    :width: 320
    :align: center