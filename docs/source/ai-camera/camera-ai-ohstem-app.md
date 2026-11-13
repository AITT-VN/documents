# 2. Camera AI với OhStem App

## 1. Giới thiệu
Ngoài cách dùng **module Camera AI** (xem [mục 1. Camera AI](/ai-camera/camera-ai.md)), OhStem App còn có sẵn công cụ **Camera AI** chạy ngay trên trình duyệt. Công cụ này dùng **webcam của laptop/điện thoại** để nhận dạng thay cho module camera, nên bạn có thể thử nghiệm mô hình AI mà **chưa cần mua module**.

Cách huấn luyện và nạp mô hình AI **hoàn toàn giống** với module Camera AI, chỉ **khác ở cách mở giao diện**:

| | Module Camera AI | Camera AI trên OhStem App |
|---|---|---|
| Cách mở giao diện | Gõ **địa chỉ IP của camera** vào trình duyệt | Vào **app.ohstem.vn** → chọn thiết bị **Camera AI** |
| Nguồn hình ảnh | Camera OV2640 trên module | Webcam của laptop/điện thoại |
| Cấu hình wifi cho camera | Cần (mục 5.1 của trang Camera AI) | Không cần |
| Mua thêm phần cứng | Cần module Camera AI | Không cần |
| Gửi kết quả cho board | UART (dây Grove) hoặc server IoT | USB/Bluetooth (qua OhStem App) hoặc server IoT |
| Phù hợp với | Sản phẩm hoàn thiện, robot di chuyển | Học thử, demo trên lớp, kiểm tra mô hình trước khi lắp vào sản phẩm |

Giao diện 2 bên gần như giống nhau (cùng có phần **Mô hình AI** và **Cài đặt IoT**), nên khi đã làm quen một bên thì bạn dùng bên còn lại rất nhanh.

## 2. Thiết bị cần sử dụng

| Hình ảnh | Sản phẩm | Mua hàng |
|:--------:|:---------|:--------:|
| ![yolo uno](/wiki-assets/images/module/ai-camera/images/yolo_uno.png) | Mạch Yolo UNO | [Mua sản phẩm ](https://shop.ohstem.vn/san-pham/yolo-uno/) |

Ngoài ra bạn cần một **laptop hoặc điện thoại có webcam** để làm camera nhận dạng.

**Lưu ý:** Hướng dẫn bên dưới thực hiện với **Yolo UNO**, vì khối lệnh `khởi tạo Camera AI dùng OhStem App` nằm trong thư viện **Camera AI** của Yolo UNO. Với board khác, bạn cần kiểm tra thư viện của board đó có khối lệnh tương ứng hay không.

## 3. Mở giao diện Camera AI trên OhStem App
Đây chính là **điểm khác duy nhất** so với module Camera AI: thay vì gõ địa chỉ IP của camera, bạn mở giao diện từ OhStem App.

**Bước 1:** Truy cập [https://app.ohstem.vn/](https://app.ohstem.vn/), vào **Lập trình thiết bị** và chọn thiết bị **Camera AI**:
![chon thiet bi camera ai](/wiki-assets/images/module/ai-camera/images/app_chon_thietbi.png)


**Bước 2:** Giao diện được hiển thị như hình:
![giao dien camera ai](/wiki-assets/images/module/ai-camera/images/app_giaodien.png)


Các thông tin cần lưu ý (giống hệt trang địa chỉ IP của module camera):

- **Loại mô hình:** chọn **Hình ảnh**
- **Mô hình AI:** để trống nếu muốn dùng mô hình tự huấn luyện, hoặc chọn một mô hình có sẵn
- **Link mô hình:** đường liên kết mô hình bạn tự huấn luyện. Nếu chọn mô hình có sẵn thì hệ thống tự điền link
- **Độ chính xác:** từ 0 - 100, là mức độ chính xác mà bạn mong muốn cho kết quả nhận diện

## 4. Chọn hoặc huấn luyện mô hình AI
## **4.1 Dùng mô hình có sẵn**
Ở mục **Mô hình AI**, bạn có thể chọn ngay một trong các mô hình mẫu để thử nghiệm mà không cần huấn luyện: **Face or no face**, **Dog or not**, **Face mask or no mask**, **KDI AI Hackathon 2023**.

Với hướng dẫn này, chọn mô hình **Face mask or no mask** (có khẩu trang hoặc không khẩu trang):
![chon mo hinh](/wiki-assets/images/module/ai-camera/images/app_mohinh.png)


Sau khi chọn, ô **Link mô hình** sẽ được tự động điền.

## **4.2 Dùng mô hình tự huấn luyện**
Cách huấn luyện mô hình **giống hoàn toàn** với module Camera AI: dùng Google Teachable Machine để huấn luyện, xuất ra link mô hình rồi dán vào ô **Link mô hình**.

Xem hướng dẫn chi tiết ở **mục 5.2 Huấn luyện mô hình - Tạo link mô hình** của trang [1. Camera AI](/ai-camera/camera-ai.md).

**Lưu ý:** Đặt tên các lớp (class) bằng tiếng Anh không dấu, ví dụ `Masked`, `NoMask`, `Nobody`. Tên này sẽ được dùng lại trong khối lệnh **camera nhận dạng được là** ở mục 6.

## 5. Bật camera và nhận dạng
Chọn nút **Bật camera** để kiểm tra kết quả nhận diện. Trình duyệt sẽ xin quyền truy cập webcam, bạn chọn **Cho phép (Allow)**:
![bat camera](/wiki-assets/images/module/ai-camera/images/app_batcamera.png)


Bên trái là hình ảnh từ webcam, bên phải là **Kết quả nhận dạng AI** kèm độ tin cậy của từng lớp (ví dụ `NoMask` 100%, `Masked` 0%, `Nobody` 0%).

**Lưu ý:** Giữ tab này luôn mở và không ẩn đi trong lúc nhận dạng, vì việc xử lý mô hình AI diễn ra ngay trên trình duyệt.

## 6. Lập trình thiết bị đọc kết quả
## **6.1 Tải thư viện**
Vào mục **Mở rộng** của **Yolo UNO**, tải thư viện **Camera AI**:
![thu vien camera ai](/wiki-assets/images/module/ai-camera/images/camera_uno_thuvien.png)


Các khối lệnh của danh mục **AI CAMERA**:
![khoi lenh camera ai](/wiki-assets/images/module/ai-camera/images/camera_uno_khoilenh.png)


Với cách dùng OhStem App, bạn khởi tạo bằng khối `khởi tạo Camera AI dùng OhStem App` thay cho khối `khởi tạo Camera AI chân RX ... TX ...` (khối dùng cho module camera nối dây Grove).

## **6.2 Viết chương trình**
Thực hiện các thao tác sau để mở chương trình mẫu **Nhận diện hình ảnh bằng OhStem App**: chọn biểu tượng **Project mẫu**, vào nhóm **4. Dự án AI**:
![mo chuong trinh](/wiki-assets/images/module/ai-camera/images/app_mo_chuongtrinh.png)


Chương trình hiển thị như sau:
![chuong trinh](/wiki-assets/images/module/ai-camera/images/app_chuongtrinh.png)


## **6.3 Giải thích chương trình**
Khi Yolo UNO khởi động, **Camera AI trên OhStem App** sẽ được khởi tạo. Sau đó cứ mỗi 0.1 giây, chương trình **cập nhật nhận dạng** từ camera và xử lý:

- Nếu camera nhận dạng được `Masked` (có đeo khẩu trang) thì đổi đèn LED trên board thành **màu xanh**
- Nếu camera nhận dạng được `NoMask` (không đeo khẩu trang) thì đổi đèn LED thành **màu đỏ**
- Nếu camera nhận dạng được `Nobody` (không có người) thì **tắt đèn**

**Lưu ý:** Vì kết quả nhận dạng được gửi từ trình duyệt sang board qua OhStem App, bạn cần giữ thiết bị **đang kết nối với app** (USB hoặc Bluetooth) và giữ tab Camera AI luôn mở.

## 7. Nâng cao - Gửi kết quả lên server IoT
Nếu muốn gửi kết quả nhận dạng lên Internet (để thiết bị ở xa đọc được, hoặc để hiển thị trên bảng điều khiển), bạn khai báo thêm phần **Cài đặt IoT** ngay trong giao diện Camera AI:
![cai dat iot](/wiki-assets/images/module/ai-camera/images/app_caidat_iot.png)


- **Server:** chọn **OhStem**
- **Server URL:** hệ thống tự điền (`wss://mqtt.ohstem.vn:8084/mqtt`)
- **User:** username của bảng điều khiển IoT bạn đã tạo
- **Kênh dữ liệu:** kênh thông tin đã chọn (V1 … V20)
- **Tần suất gửi (giây):** khoảng thời gian giữa 2 lần gửi kết quả

Cách tạo bảng điều khiển IoT và viết chương trình cho thiết bị nhận dữ liệu từ bảng điều khiển được hướng dẫn ở **mục 7** của trang [1. Camera AI](/ai-camera/camera-ai.md).

Nếu chỉ cần thiết bị xử lý qua USB hoặc Bluetooth thì có thể bỏ qua phần Cài đặt IoT này.

## 8. Một số lưu ý khi sử dụng

| Tình huống | Cách xử lý |
|------------|------------|
| Không hiện hình webcam | Kiểm tra trình duyệt đã được **cho phép truy cập camera** chưa, và webcam không bị ứng dụng khác chiếm dụng |
| Kết quả nhận dạng không cập nhật | Không ẩn (minimize) hoặc đóng tab Camera AI trong lúc nhận dạng |
| Board không nhận được kết quả | Kiểm tra thiết bị còn **đang kết nối với OhStem App** qua USB/Bluetooth, và chương trình dùng đúng khối `khởi tạo Camera AI dùng OhStem App` |
| Nhận dạng sai nhiều | Thu thập thêm mẫu ảnh khi huấn luyện, huấn luyện lại mô hình, hoặc giảm giá trị **Độ chính xác** |
| Muốn dùng camera rời thay cho webcam | Chuyển sang dùng module Camera AI, xem trang [1. Camera AI](/ai-camera/camera-ai.md) |
