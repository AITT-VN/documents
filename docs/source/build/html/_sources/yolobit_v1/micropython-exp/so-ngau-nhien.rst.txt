Số ngẫu nhiên
=============================================

Trong nhiều chương trình, bạn sẽ cần tạo ra một số ngẫu nhiên không đoán trước được, giống như khi bạn thảy xúc xắc mà không biết trước nó sẽ hiện ra số nào. Điều này giúp cho các trò chơi trở nên hấp dẫn hơn.

.. image:: images/ls-7-1.png
    :width: 600
    :align: center

MicroPython đi kèm thư viện tên là random giúp bạn tạo ra được một số ngẫu nhiên trong một khoảng nào đó tùy ý muốn của bạn.

Chương trình dưới đây sẽ hiện ra một tên ngẫu nhiên mỗi lần chạy.

.. code-block:: python

  from yolobit import *

  import random

  names = [“Mary”, “Yolanda”, “Damien”, “Alia”, “Kushal”, “Mei Xiu”, “Zoltan” ]

  display.scroll(names[random.randint(0, 6)])

Chúng ta sử dụng hàm ``random.randint(start, end)`` để tạo ra 1 số ngẫu nhiên trong khoảng từ start đến end. Trong chương trình trên, chúng ta có 1 danh sách gồm 7 cái tên nên chúng ta tạo ra số ngẫu nhiên từ 0 đến 6 (tổng cộng là 7 số) và lấy một tên ra trong danh sách theo số này. Trong máy tính, thứ tự luôn bắt đầu từ 0 thay vì 1 nên chúng ta cũng tạo ra số từ 0 đến 6.

Để lấy ra một phần tử trong danh sách thì chúng ta dùng 2 dấu ngoặc vuông và truyền vào số thự tự của phần tử đó trong nhóm. Giả sử hàm ``random.randint(0, 6)`` ở trên trả ra kết quả là số 3 thì khi đó câu lệnh sẽ trợ thành:

.. code-block:: python

  display.scroll(names[3])

``names[3]`` sẽ trả ra phần tử có số thứ tự là 3 (đếm từ 0 nhé) trong danh sách, tức là cái tên ``Alia``. Khi đó câu lệnh sẽ trở thành:

.. code-block:: python

  display.scroll(“Alia”)

Và tên này sẽ được hiện ra trên màn hình Led. Thật là dễ phải không nào.