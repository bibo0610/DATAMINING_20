ĐỒ ÁN CUỐI KÌ KHAI THÁC DỮ LIỆU VÀ ỨNG DỤNG

Ứng dụng khai phá dữ liệu trong dự đoán bệnh nhân bỏ hẹn khám bệnh và tình trạng học tập của sinh viên

THÀNH VIÊN THỰC HIỆN:
1. Họ và tên: Nguyễn Dương Bảo Trân
   MSSV: 3123410386
2. Họ và tên: Giang Hào Tường
   MSSV: 3123410421

====================================================================
1. MÔ TẢ CHUNG
====================================================================

Đồ án thực hiện trên 2 bộ dữ liệu khác nhau, thuộc hai lĩnh vực là y tế và giáo dục.

- Dataset 1: Medical Appointment No Shows
  Bộ dữ liệu này được khai thác theo hai hướng:
  + phân loại để dự đoán bệnh nhân có bỏ hẹn khám bệnh hay không (No-show);
  + phân tích kết hợp để tìm các tổ hợp điều kiện thường xuất hiện cùng với hành vi no-show.

- Dataset 2: Predict Students’ Dropout and Academic Success
  Bộ dữ liệu này được khai thác theo hai hướng:
  + phân loại để dự đoán tình trạng học tập của sinh viên thuộc một trong ba nhóm Dropout, Enrolled hoặc Graduate;
  + phân tích kết hợp để tìm các tổ hợp đặc trưng thường xuất hiện cùng với nhóm Dropout hoặc Graduate.

Ngoài phần xây dựng mô hình học máy, đồ án còn tập trung vào hướng khai phá dữ liệu thông qua:
- tiền xử lý dữ liệu,
- phân tích thống kê mô tả,
- phân tích đơn biến và đa biến,
- phân tích theo nhóm,
- khai phá luật kết hợp,
- so sánh và đánh giá mô hình.

====================================================================
2. DANH SÁCH CÁC TẬP TIN TRONG FOLDER
====================================================================

2.1. FILE BÁO CÁO
- DM_Report.docx
  File báo cáo chính của đồ án, được trình bày theo mẫu báo cáo môn học.

2.2. FILE README
- README.txt
  File mô tả các tập tin có trong folder, nội dung chính của từng file.

2.3. DỮ LIỆU GỐC

- KaggleV2-May-2016.csv
  Bộ dữ liệu Medical Appointment No Shows, dùng cho bài toán dự đoán bệnh nhân bỏ hẹn khám bệnh.

  Nguồn dữ liệu:
  https://www.kaggle.com/datasets/joniarroba/noshowappointments

  Nội dung dữ liệu:
  Bộ dữ liệu gồm thông tin liên quan đến các cuộc hẹn khám bệnh như:
  + giới tính,
  + độ tuổi,
  + khu vực sinh sống,
  + học bổng,
  + bệnh nền,
  + ngày đặt lịch,
  + ngày khám,
  + tin nhắn nhắc lịch,
  + trạng thái bệnh nhân có đến khám hay không.

  Mục tiêu phân tích:
  - xác định các yếu tố ảnh hưởng đến hành vi no-show,
  - xây dựng mô hình dự đoán bệnh nhân có nguy cơ bỏ hẹn,
  - khai phá các mẫu hành vi liên quan đến no-show.

- data.csv
  Bộ dữ liệu Predict Students’ Dropout and Academic Success, dùng cho bài toán dự đoán tình trạng học tập của sinh viên.

  Nguồn dữ liệu:
  https://archive.ics.uci.edu/dataset/697/predict+students+dropout+and+academic+success

  Nội dung dữ liệu:
  Bộ dữ liệu gồm các thuộc tính liên quan đến:
  + thông tin nhân khẩu học,
  + hình thức tuyển sinh,
  + ngành học,
  + học phí,
  + học bổng,
  + tình trạng nợ học phí,
  + kết quả học tập học kỳ 1,
  + kết quả học tập học kỳ 2,
  + trạng thái học tập cuối cùng của sinh viên.

  Mục tiêu phân tích:
  - xác định các yếu tố ảnh hưởng đến tình trạng học tập,
  - dự đoán sinh viên thuộc nhóm Dropout, Enrolled hay Graduate,
  - khai phá các mẫu dữ liệu đặc trưng cho sinh viên có nguy cơ bỏ học hoặc có khả năng tốt nghiệp.

2.4. NOTEBOOK PHÂN TÍCH

- medical_appointment_noshow_analysis.ipynb: notebook phân tích cho Dataset 1.

  Nội dung chính của notebook:
  + đọc dữ liệu và kiểm tra thông tin tổng quan,
  + kiểm tra dữ liệu thiếu, dữ liệu trùng lặp,
  + tiền xử lý dữ liệu,
  + tạo các thuộc tính mới như waiting_days, age_group, waiting_group, chronic_count,
  + phân tích thống kê mô tả,
  + phân tích đơn biến và đa biến,
  + phân tích theo nhóm để tìm các mẫu dữ liệu nổi bật,
  + khai phá luật kết hợp để tìm các tổ hợp điều kiện liên quan đến no-show,
  + xây dựng và đánh giá các mô hình phân loại:
    * Logistic Regression
    * Decision Tree
    * Random Forest
  + so sánh mô hình và rút ra kết luận.

- student_dropout_academic_success.ipynb: notebook phân tích cho Dataset 2.

  Nội dung chính của notebook:
  + đọc dữ liệu và kiểm tra thông tin tổng quan,
  + kiểm tra chất lượng dữ liệu,
  + tiền xử lý dữ liệu,
  + chuẩn hóa tên cột,
  + rút trích các đặc trưng phục vụ khai phá dữ liệu như:
    * age_group
    * admission_grade_group
    * sem1_approved_group
    * sem2_approved_group
    * sem1_grade_group
    * sem2_grade_group
  + phân tích thống kê mô tả,
  + phân tích đơn biến và đa biến,
  + phân tích theo nhóm sinh viên,
  + khai phá luật kết hợp để tìm các mẫu liên quan đến Dropout và Graduate,
  + xây dựng và đánh giá các mô hình phân loại:
    * Logistic Regression
    * Decision Tree
    * Random Forest
  + so sánh mô hình và rút ra kết luận.

2.5. FILE KẾT QUẢ

- medical_model_comparison_results.csv
  File lưu bảng so sánh kết quả các mô hình của Dataset 1.
  Các chỉ số gồm:
  + Accuracy
  + Precision
  + Recall
  + F1-score
  + ROC-AUC

- student_model_comparison_results.csv
  File lưu bảng so sánh kết quả các mô hình của Dataset 2.
  Các chỉ số gồm:
  + Accuracy
  + Precision_macro
  + Recall_macro
  + F1_macro
  + F1_weighted
  + ROC_AUC_OVR_weighted

====================================================================
3. CẤU TRÚC THƯ MỤC
====================================================================

Cấu trúc các tập tin trong folder project như sau:

/
|-- DM_Report.docx
|-- README.txt
|-- dataset1
  |-- KaggleV2-May-2016.csv
  |-- medical_appointment_noshow_analysis.ipynb
  |-- medical_model_comparison_results.csv
|-- dataset2
  |-- data.csv
  |-- student_dropout_academic_success.ipynb
  |-- student_model_comparison_results.csv

====================================================================
4. CÔNG CỤ VÀ THƯ VIỆN SỬ DỤNG
====================================================================

Ngôn ngữ lập trình:
- Python 3.x

Môi trường chạy:
- Jupyter Notebook hoặc Visual Studio Code

Các thư viện Python sử dụng:
- pandas
- numpy
- matplotlib
- seaborn
- scikit-learn
- mlxtend

====================================================================
5. NỘI DUNG KHAI PHÁ DỮ LIỆU CHÍNH
====================================================================

5.1. Đối với Dataset 1
Các nội dung khai phá dữ liệu chính gồm:
- phân tích phân bố tuổi, giới tính, khu vực khám bệnh, thời gian chờ,
- phân tích tỷ lệ no-show theo nhóm tuổi và nhóm thời gian chờ,
- phân tích mối quan hệ giữa việc nhận SMS và hành vi no-show,
- phân tích theo khu vực khám bệnh,
- khai phá luật kết hợp để tìm các tổ hợp điều kiện liên quan đến no-show,
- huấn luyện và đánh giá các mô hình phân loại để dự đoán bệnh nhân bỏ hẹn.

5.2. Đối với Dataset 2
Các nội dung khai phá dữ liệu chính gồm:
- phân tích phân bố target (Dropout, Enrolled, Graduate),
- phân tích các biến học vụ và tài chính,
- phân tích theo nhóm điểm đầu vào, số môn đạt, điểm học kỳ,
- phân tích các yếu tố như học bổng, nợ học phí, học phí đúng hạn,
- khai phá luật kết hợp để tìm các mẫu liên quan đến Dropout và Graduate,
- huấn luyện và đánh giá các mô hình phân loại đa lớp.

====================================================================
6. KẾT QUẢ TỔNG QUAN
====================================================================

- Dataset 1:
  Mô hình tốt nhất hiện tại là Logistic Regression.
  Kết quả cho thấy bài toán dự đoán bệnh nhân no-show là khả thi, nhưng vẫn cần cải thiện thêm để nâng cao Precision.

- Dataset 2:
  Mô hình tốt nhất hiện tại là Random Forest.
  Kết quả cho thấy bài toán dự đoán tình trạng học tập của sinh viên là khá khả thi và có thể hỗ trợ nhà trường trong việc phát hiện sớm sinh viên có nguy cơ bỏ học.

====================================================================
7. GHI CHÚ
====================================================================

Project được thực hiện cho mục đích học tập trong môn Khai thác dữ liệu và ứng dụng.
Mọi bộ dữ liệu được sử dụng trong đồ án đều là dữ liệu công khai từ Kaggle và UCI.