2. 4. Robot di chuyển bị lệch, không quay được góc chính xác
==================
Khi nạp chương trình , robot di chuyển tự động bị lệch nhiều, bạn hãy tham khảo cách sau đây để khắc phục.


Nguyên nhân:
    - Do thiết lập tạo động cơ robot chưa khai báo cảm biến góc và di chuyển dùng cảm biến góc.
    - Đặt ORC Hub bị xiên, xéo làm cảm biến tính toán giá trị chưa đúng.

..  figure:: images/orc05.jpg
    :scale: 100%
    :align: center 

Cách xử lý:
    - Bổ sung 2 khối lệnh này vào phía dưới câu lệnh tạo robot.
    - Lắp ORC Hub ngay ngắn lại trên robot.

    
