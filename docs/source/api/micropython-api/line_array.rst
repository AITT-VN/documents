:mod:`line_array` --- Line Array Module
=============================================

.. module:: line_array
    :synopsis: Line Array Module

Chức năng chính và chức năng của ``line_array``

Function
----------------------

.. function:: line_array.read(PORT)

    Đọc trạng thái của line finder array.
    Trong đó:

        - *PORT* : Có giá trị từ ``0 ~ 5`` tương ứng từ PORT 1 đến PORT 6 của xController.
        - Kết quả trả về ``TUPLE`` 4 giá trị tương ứng với trạng thái của 4 mắt S1 đến S4, ví dụ: ``(0, 1, 1, 0)`` với ``0`` là đọc được line trắng còn ``1`` là line đen.

.. function:: line_array.read(PORT, TUPLE)

    Đọc trạng thái từng mắt đọc của Module.
    Trong đó:
    
        - *PORT* : Có giá trị từ ``0 ~ 5``tương ứng từ PORT 1 đến PORT 6 của xController.
        - *TUPLE* : Có giá trị từ ``0 ~ 3`` tương ứng với 4 mắt đọc của Module.

Sample Code
----------------------
Test module bám line đen

.. code-block:: python

    while True:
        if line_array.read(0) == (0, 1, 1, 0):
            print(' Đang đi theo line')
        else:
            print('Đang đi lệch khỏi line')

Test trạng thái mắt đọc số 1

.. code-block:: python

    while True:
        print(line_array.read(0,0))
        time(1)