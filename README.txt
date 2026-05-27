ĐỒ ÁN CUỐI KỲ
HỌC PHẦN: KHAI THÁC DỮ LIỆU VÀ ỨNG DỤNG

ĐỀ TÀI:
Ứng dụng khai phá dữ liệu trong dự đoán bệnh nhân bỏ hẹn khám bệnh
và tình trạng học tập của sinh viên

THÀNH VIÊN THỰC HIỆN:
1. Nguyễn Dương Bảo Trân – MSSV: 3123410386
2. Giang Hào Tường – MSSV: 3123410421

1. CẤU TRÚC THƯ MỤC
/
|-- DataMining_Report.docx
|-- README.txt
|-- dataset1/
|   |-- KaggleV2-May-2016.csv
|   |-- medical_appointment_noshow_analysis.ipynb
|   |-- medical_model_comparison_results.csv
|
|-- dataset2/
    |-- data.csv
    |-- student_dropout_academic_success.ipynb
    |-- student_model_comparison_results.csv

2. MÔ TẢ CÁC TẬP TIN

2.1. DataMining_Report.docx
- Báo cáo chính của đồ án.
- Nội dung trình bày quy trình khai phá dữ liệu, phân tích hai bộ dữ liệu,
  kết quả mô hình phân loại, luật kết hợp, các insight và kết luận.

2.2. README.txt
- Tập tin mô tả cấu trúc folder và chức năng của các tập tin trong đồ án.

2.3. Folder dataset1

- KaggleV2-May-2016.csv
  Dữ liệu gốc của bộ Medical Appointment No Shows, được sử dụng để phân tích
  và dự đoán hành vi bệnh nhân không đến khám đúng lịch hẹn.

  Nguồn dữ liệu:
  https://www.kaggle.com/datasets/joniarroba/noshowappointments

- medical_appointment_noshow_analysis.ipynb
  Notebook xử lý Dataset 1, bao gồm:
  + đọc và kiểm tra dữ liệu;
  + tiền xử lý và xây dựng đặc trưng;
  + phân tích dữ liệu khám phá;
  + xây dựng và đánh giá mô hình phân loại;
  + khai phá luật kết hợp liên quan đến hành vi no-show.

- medical_model_comparison_results.csv
  Tập tin lưu kết quả so sánh các mô hình phân loại trên Dataset 1.

2.4. Folder dataset2

- data.csv
  Dữ liệu gốc của bộ Predict Students’ Dropout and Academic Success,
  được sử dụng để phân tích và dự đoán tình trạng học tập của sinh viên.

  Nguồn dữ liệu:
  https://archive.ics.uci.edu/dataset/697/predict+students+dropout+and+academic+success

- student_dropout_academic_success.ipynb
  Notebook xử lý Dataset 2, bao gồm:
  + đọc và kiểm tra dữ liệu;
  + tiền xử lý và xây dựng đặc trưng;
  + phân tích dữ liệu khám phá;
  + xây dựng và đánh giá mô hình phân loại đa lớp;
  + khai phá luật kết hợp cho nhóm Dropout và Graduate.

- student_model_comparison_results.csv
  Tập tin lưu kết quả so sánh các mô hình phân loại trên Dataset 2.

3. GHI CHÚ
- Các file dữ liệu CSV được đặt cùng folder với notebook tương ứng.
- Đồ án được thực hiện phục vụ mục đích học tập trong học phần Khai thác dữ liệu và ứng dụng.
- Hai bộ dữ liệu được sử dụng đều là dữ liệu công khai từ Kaggle và UCI Machine Learning Repository.