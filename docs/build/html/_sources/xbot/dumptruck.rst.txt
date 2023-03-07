**Bộ Dump Truck**
=================

1. Giới thiệu 
----------
-----------

Dump Truck là bộ phụ kiện được dùng để gắn lên xBot để vui chơi hoặc thi đấu trong các cuộc thi về Robotics. Sản phẩm được làm từ chất liệu an toàn, độ bền cao, phù hợp cho bé vui chơi tại nhà hoặc để ứng dụng vào giảng dạy bộ môn Robot cho học sinh.

.. raw:: html

 <iframe width="560" height="315" src="https://www.youtube.com/embed/DREgkUCVX-c" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
| 

2. Link sản phẩm 
-------
------------

..  image:: images/gio.png
    :alt: some image
    :target: https://ohstem.vn/product/dump-truck/
    :class: with-shadow
    :scale: 100%
    :align: center
|

3. Hướng dẫn lắp ráp
-------------------
-------------------

.. image:: images/dump_1.png
    :width: 900px
    :align: center
|   
.. image:: images/dump_2.png
    :width: 900px
    :align: center
|   

.. image:: images/dump_3.png
    :width: 900px
    :align: center
|   
.. image:: images/dump_4.png
    :width: 900px
    :align: center
|   
.. image:: images/dump_5.png
    :width: 900px
    :align: center
|   
.. image:: images/dump_6.png
    :width: 900px
    :align: center
|   
.. image:: images/dump_7.png
    :width: 900px
    :align: center
|   
.. image:: images/dump_8.png
    :width: 900px
    :align: center
|   
.. image:: images/dump_9.png
    :width: 900px
    :align: center
|   
.. image:: images/dump_10.png
    :width: 900px
    :align: center
|   
.. image:: images/dump_11.png
    :width: 900px
    :align: center
|   
.. image:: images/dump_12.png
    :width: 900px
    :align: center
|   
.. image:: images/dump_13.png
    :width: 900px
    :align: center
|   
.. image:: images/dump_14.png
    :width: 900px
    :align: center
|   
.. image:: images/dump_15.png
    :width: 900px
    :align: center
|   

**Ở bước này, chúng ta sẽ phải canh góc của servo để lập trình nâng hạ thùng xe cho xBot. Có 8 cổng servo từ S1 đến S8, chúng ta có thể dùng tùy ý. Ở đây ta sẽ dùng cổng S1 để điều khiển nâng hạ. Bạn sẽ phải lập trình cho servo quay về vị trí 0 độ với lệnh:**

.. image:: images/dump_15.png
    :scale: 100%
    :align: center
|  

Sau khi chỉnh góc ở vị trí hạ xong, chúng ta sẽ ráp tiếp tục.

.. image:: images/dump_16.png
    :width: 900px
    :align: center
|   
.. image:: images/dump_17.png
    :width: 900px
    :align: center
|   
.. image:: images/dump_18.png
    :width: 900px
    :align: center
|   
.. image:: images/dump_19.png
    :width: 900px
    :align: center
|   
.. image:: images/dump_20.png
    :width: 900px
    :align: center
|   


4. Hướng dẫn lập trình
-------------------
-------------------

Chúng ta đã thiết lập góc hạ xuống ở 0 độ, OhStem gợi ý các bạn góc nâng ở 110 độ ( có thể tùy chỉnh thay đổi theo ý muốn). 

Bạn có thể lập trình cho xBot nâng lên 2 giây sau đó hạ xuống 2 giây lặp lại bằng lệnh : 

.. image:: images/dump_22.png
    :scale: 100%
    :align: center
|  

Hoặc bạn cũng có thể lập trình cho robot nâng hạ chậm hơn bằng lệnh:

.. image:: images/dump_23.png
    :scale: 100%
    :align: center
|