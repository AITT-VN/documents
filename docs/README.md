HƯỚNG DẪN SỬ DỤNG READTHEDOCS
=========================
HƯỚNG DẪN CÀI ĐẶT LẦN ĐẦU

Bước 1: Cài đặt môi trường python.

Bước 2: Cài đặt Sphinx: pip install sphinx

Bước 3: Tạo đường dẫn đễn tập tin docs:

cd /path/to/project

mkdir docs

Nếu đã có sẵn thư mục docs thì vào bỏ qua bước này.

Bước 4: Chạy lệnh sphinx-quickstart tại đây:

cd docs

sphinx-quickstart

Phần bắt đầu nhanh này sẽ hướng dẫn bạn cách tạo cấu hình cơ bản; trong hầu hết các trường hợp, bạn chỉ có thể chấp nhận các giá trị mặc định. Khi hoàn tất, bạn sẽ có index.rst, conf.py và một số tệp khác. Chúng ta sẽ làm việc với các file này.

Bây giờ, hãy chỉnh sửa index.rst của bạn và thêm một số thông tin về dự án của bạn. Bao gồm nhiều chi tiết tùy thích
Tham khảo cú pháp reStructuredText: https://www.writethedocs.org/guide/writing/beginners-guide-to-docs/#id1 hoặc https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html.

Bước 5: Render file html: make html

----------------------------------
HƯỚNG DẪN THAY ĐỔI THEME READTHEDOCS

Nếu bạn đang thực hiện các thay đổi đối với tài liệu, bạn có thể muốn xây dựng
tài liệu cục bộ để bạn có thể xem trước các thay đổi của mình.

Bước 1: Trỏ CMD vào trong thư mục docs như trên

Bước 2: Tải sphinx_rtd_theme: pip install sphinx_rtd_theme

Bước 3: Vào file /source/conf.py

Vô hiệu hóa dòng này (Đây là theme mặc định của readthedocs): html_theme = 'alabaster'

Thêm dòng này: html_theme = 'sphinx_rtd_theme' 

Bước 3: Render file html: make html

----------------------------------
HƯỚNG DẪN CẬP NHẬT HTML READTHEDOCS SAU KHI THAY ĐỔI NỘI DUNG CÁC FILE RST:

Yêu cầu: Kiểm tra xem đã cài đặt sphinx chưa, nếu chưa thì chạy lệnh cài đặt pip install sphinx

Bước 1: Trỏ CMD vào trong thư mục docs như trên

Bước 2: Render file html: make html