line_array.read(PORT)
==========

.. image:: images/line-array-1.png
    :scale: 100 %
    :align: center


Đọc trạng thái của cảm biến dò vạch.
Trong đó:

    - *PORT* : Có giá trị từ ``1 ~ 6`` tương ứng từ PORT 1 đến PORT 6 của xController.
    - Kết quả trả về ``TUPLE`` 4 giá trị tương ứng với trạng thái của 4 mắt S1 đến S4, ví dụ: ``(0, 1, 1, 0)`` với ``0`` là đọc được line trắng còn ``1`` là line đen.


Ví dụ
----------------------

Kiểm tra vạch đen bằng mắt S2, S3

.. image:: images/input-vd-3.png
    :scale: 100 %
    :align: center
