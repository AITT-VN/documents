# Build OhStem Education Wiki

Tài liệu dùng Sphinx, giao diện Read the Docs và MyST để đọc Markdown bên cạnh các trang reStructuredText.

```powershell
python -m pip install -r requirements.txt
python -m sphinx -b html source build/html
```

Mở `build/html/index.html` để xem bản HTML. Khi build trên Read the Docs, dùng cấu hình `.readthedocs.yaml` ở gốc repo.

Các trang Markdown và ảnh trong `source/wiki-assets` được chuyển từ
[OhStem Wiki Hub](https://github.com/AITT-VN/ohstem-wiki), commit
`f99b68ad4099a579ece64916351d097ceacff046`. Thứ tự bài trong từng mục
dựa trên `_meta.js` của wiki. Các nút hướng dẫn lắp ráp và video từ MDX
được chuyển thành liên kết để dùng trong bản HTML của Sphinx.
