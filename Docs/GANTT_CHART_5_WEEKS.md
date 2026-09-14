# 📊 KẾ HOẠCH TIẾN ĐỘ & BIỂU ĐỒ GANTT THEO DÕI HẰNG NGÀY (5 TUẦN)
## DỰ ÁN: ECOMMERCE COMPUTER (STORE EF) - PHIÊN BẢN V3

> **Căn cứ kế hoạch:** Dựa trên cấu trúc đề cương tại Docs/CHECKLIST_TESTING_PLAN.md, tài liệu Docs/TEST_PLAN.md và phân công tại Docs/TASK_ASSIGNMENT_5_MEMBERS.md.  
> **Thời gian thực hiện:** **5 Tuần** (25 ngày làm việc chính thức, từ Thứ Hai 14/09/2026 đến Thứ Sáu 16/10/2026).  
> **Quy mô nhân sự:** 05 Thành viên chuyên trách (TV01 - Test Lead, TV02 - Manual Auth, TV03 - Manual Prod, TV04 - Integration/DB, TV05 - Automation/UT).  
> **File Excel theo dõi tương ứng:** Docs/GANTT_CHART_5_WEEKS_DAILY.xlsx.

---

## 📈 1. BIỂU ĐỒ GANTT TỔNG THỂ (MERMAID GANTT DIAGRAM)

`mermaid
gantt
    title BIỂU ĐỒ GANTT THEO DÕI HẰNG NGÀY CHO 5 TUẦN (25 NGÀY LÀM VIỆC)
    dateFormat  YYYY-MM-DD
    axisFormat  %d/%m
    excludes    weekends

    section Tuần 1: Khởi động & Test Plan
    Họp Kick-off & Lập Git/Drive (TV01, All)       :active, t1_1, 2026-09-14, 2d
    Khảo sát kiến trúc Store EF & DB (TV02, TV03)  :t1_2, 2026-09-14, 3d
    Cài đặt môi trường 5 máy & run.bat (TV03, TV04):t1_3, 2026-09-15, 3d
    Khảo sát DB Triggers & Store.Tests (TV04, TV05):t1_4, 2026-09-15, 3d
    Biên soạn Chương 1 & Test Plan (TV01)          :t1_5, 2026-09-15, 4d
    Nghiệm thu Cột mốc 1 - M1 (Cả nhóm)            :crit, m1, 2026-09-18, 1d

    section Tuần 2: Thiết kế Test Cases
    Soạn lý thuyết EP, BVA mục 2.1 (TV02)         :t2_1, 2026-09-21, 2d
    Thiết kế TC Auth & Account 2.2.1 (TV02)        :t2_2, 2026-09-21, 4d
    Thiết kế TC Product & Admin 2.2.2-4 (TV03)     :t2_3, 2026-09-21, 4d
    Thiết kế TC Giỏ hàng & CheckOut 2.2.2 (TV04)   :t2_4, 2026-09-21, 3d
    Thiết kế TC Tích hợp DB Triggers 2.3 (TV04)    :t2_5, 2026-09-23, 3d
    Thiết kế kịch bản Unit Test Store.Tests (TV05) :t2_6, 2026-09-21, 4d
    Review chéo & Nghiệm thu Cột mốc 2 - M2 (TV01) :crit, m2, 2026-09-24, 2d

    section Tuần 3: Tự động hóa & Cycle 1
    Biên soạn Chương 3 Selenium IDE (TV05)        :t3_1, 2026-09-28, 3d
    Ghi 5 script tự động .side (TV05)              :t3_2, 2026-09-29, 4d
    Thực thi test Web Đợt 1 Auth (TV02)            :t3_3, 2026-09-28, 4d
    Thực thi test Web Đợt 1 Product (TV03)         :t3_4, 2026-09-28, 4d
    Thực thi test Web Đợt 1 Cart & SQL (TV04)      :t3_5, 2026-09-28, 4d
    Theo dõi Pass/Fail & Nghiệm thu M3 (TV01, All) :crit, m3, 2026-10-01, 2d

    section Tuần 4: Tích hợp & Defect Reports
    Thực thi test Tích hợp Triggers & SP (TV04)    :t4_1, 2026-10-05, 3d
    Chạy Selenium IDE & MSTest Coverage (TV05)     :t4_2, 2026-10-05, 3d
    Test bảo mật & Báo cáo DEF-04 (TV02)           :t4_3, 2026-10-05, 3d
    Test Regex Crash & Báo cáo DEF-02 (TV03)       :t4_4, 2026-10-05, 3d
    Xác nhận & Báo cáo DEF-01, DEF-03 (TV04)       :t4_5, 2026-10-06, 3d
    Đề xuất giải pháp sửa code mục 4.5.3 (TV05)    :t4_6, 2026-10-07, 3d
    Họp Bug Triage & Nghiệm thu M4 (TV01, All)     :crit, m4, 2026-10-08, 2d

    section Tuần 5: Retest, Regression & Nộp bài
    Retest DEF-01 đến DEF-04 sau fix (TV02, TV03, TV04) :t5_1, 2026-10-12, 2d
    Regression Test tự động Selenium & MSTest (TV05)    :t5_2, 2026-10-12, 3d
    Kiểm thử hồi quy chéo Cross-testing (Cả nhóm)       :t5_3, 2026-10-13, 2d
    Tổng hợp kết quả 4.4, biểu đồ & KL C4 (TV01)        :t5_4, 2026-10-13, 3d
    Soạn Kết luận & Tài liệu tham khảo (TV01, TV02)     :t5_5, 2026-10-14, 2d
    Thiết kế Slide PPT thuyết trình (TV04, TV05)         :t5_6, 2026-10-14, 3d
    Format chuẩn file Word (.docx) & Đóng gói (TV01)    :t5_7, 2026-10-15, 2d
    Họp tổng kết, ký biên bản & Nộp bài (Cả nhóm)       :crit, m5, 2026-10-16, 1d
`

---

## 👥 2. MA TRẬN PHÂN CÔNG CÔNG VIỆC HẰNG NGÀY CHO 5 THÀNH VIÊN (25 NGÀY)

### 👤 Bảng phân vai chuyên trách:
* **TV01:** Test Lead / QA Project Manager
* **TV02:** Manual Tester 1 (Auth & Account Specialist)
* **TV03:** Manual Tester 2 (Product Catalog & Admin Specialist)
* **TV04:** Integration & Business Flow Tester (Cart, Order & DB)
* **TV05:** Automation & Unit Test Engineer

---

### 🗓️ CHI TIẾT CÔNG VIỆC TỪNG NGÀY CHO 5 THÀNH VIÊN:

#### 🔹 TUẦN 1: KHỞI ĐỘNG, KHẢO SÁT & LẬP KẾ HOẠCH (14/09 – 18/09/2026)

| Ngày | Thứ / Ngày | TV01 (Lead) | TV02 (Auth) | TV03 (Prod) | TV04 (Cart/DB) | TV05 (Auto/UT) |
| :---: | :---: | :--- | :--- | :--- | :--- | :--- |
| **D01** | T2 14/09 | Họp Kick-off, thống nhất phân công, lập Git/Drive | Phân tích kiến trúc MVC Store EF, đọc overview | Khảo sát cấu trúc bảng Product, Category, Brand | Phân tích CSDL SQL Server, bảng Cart & Order_ | Khảo sát công cụ Selenium IDE & MSTest |
| **D02** | T3 15/09 | Soạn Bìa, Mục lục, Lời mở đầu, Mục 1.1 | Cài VS 2022, LocalDB, restore DB Store.sql | Cài môi trường máy, test file run.bat port 5000 | Kiểm tra Trigger Tri_AddProduct, Tri_AddGallery | Cài extension Selenium IDE, tạo Store.Tests |
| **D03** | T4 16/09 | Soạn Mục 1.2 (Mục tiêu, Phạm vi) & 1.3 RACI | Test sơ bộ Đăng ký/nhập, cơ chế BCrypt hash | Kiểm tra UI Danh sách SP, phân trang, lọc sơ bộ | Kiểm tra thao tác Giỏ hàng, phát hiện bug xóa | Viết unit test mẫu Helpers.IsValidEmail() |
| **D04** | T5 17/09 | Soạn Mục 1.4 – 1.5 (Môi trường, Entry/Exit) | Lập danh mục yêu cầu test Auth & Profile | Lập danh mục yêu cầu test Product & Admin | Lập danh mục test Giỏ, CheckOut, Triggers/SP | Kiểm tra khả năng Record/Playback Selenium |
| **D05** | T6 18/09 | Hoàn thiện Test Plan, review Cột mốc 1 (M1) | Hoàn tất cài đặt môi trường, review Chương 1 | Hoàn tất cài đặt môi trường, review Chương 1 | Hoàn tất cài đặt môi trường, review Chương 1 | Hoàn tất cài đặt môi trường, review Chương 1 |

---

#### 🔹 TUẦN 2: THIẾT KẾ TEST CASES CHỨC NĂNG & TÍCH HỢP (21/09 – 25/09/2026)

| Ngày | Thứ / Ngày | TV01 (Lead) | TV02 (Auth) | TV03 (Prod) | TV04 (Cart/DB) | TV05 (Auto/UT) |
| :---: | :---: | :--- | :--- | :--- | :--- | :--- |
| **D06** | T2 21/09 | Xây dựng biểu mẫu chuẩn hóa Test Case | Soạn cơ sở lý thuyết EP, BVA (Mục 2.1) | Thiết kế TC Duyệt sản phẩm & Phân trang | Thiết kế TC Thêm vào giỏ (chưa/đã login) | Lập danh mục Test Case cho Unit Test |
| **D07** | T3 22/09 | Giám sát tiến độ viết TC, giải đáp nghiệp vụ | Thiết kế TC Đăng ký (Sign Up) & Đăng nhập | Thiết kế TC Bộ lọc đa tiêu chí (Filter) & Search | Thiết kế TC Xem giỏ, Sửa SL, Xóa món (DEF-01) | Viết mã Unit Test IsValidEmail, IsValidImage |
| **D08** | T4 23/09 | Bắt đầu peer review bộ TC của TV02 & TV03 | Thiết kế TC Đăng xuất, Profile & Đổi mật khẩu | Thiết kế TC Chi tiết sản phẩm & Admin CRUD | Thiết kế TC Thanh toán CheckOut lưu DB (DEF-03) | Viết mã Unit Test cho ProductExts lõi |
| **D09** | T5 24/09 | Review bộ TC của TV04 & kịch bản Unit Test | Thiết kế TC Phân quyền RBAC URL Admin User | Thiết kế TC Đánh giá (Reviews), Brand/Cat | Thiết kế TC Tích hợp: Triggers Tri_*, SP AddCart | Viết mã Unit Test MaxPage, build Solution OK |
| **D10** | T6 25/09 | Chuẩn hóa, đóng gói bộ Test Cases (M2) | Hoàn thiện bộ 25-35 TC Auth/Account | Hoàn thiện bộ 30-40 TC Product/Admin | Hoàn thiện bộ 25-35 TC Cart/CheckOut/DB | Hoàn thiện mã nguồn Unit Test Store.Tests |

---

#### 🔹 TUẦN 3: KIỂM THỬ TỰ ĐỘNG & THỰC THI CYCLE 1 (28/09 – 02/10/2026)

| Ngày | Thứ / Ngày | TV01 (Lead) | TV02 (Auth) | TV03 (Prod) | TV04 (Cart/DB) | TV05 (Auto/UT) |
| :---: | :---: | :--- | :--- | :--- | :--- | :--- |
| **D11** | T2 28/09 | Khởi tạo bảng Test Run theo dõi thực thi | Thực thi test Đăng ký tài khoản (Sign Up) | Thực thi test Duyệt sản phẩm, Phân trang | Thực thi test Thêm sản phẩm vào giỏ hàng | Soạn nội dung Mục 3.1 & 3.2 Chương 3 |
| **D12** | T3 29/09 | Giám sát tỷ lệ Pass/Fail ban đầu Cycle 1 | Thực thi test Đăng nhập, Đăng xuất, Session | Thực thi test Tìm kiếm sản phẩm thông thường | Thực thi test Sửa số lượng, ghi nhận DEF-01 | Soạn 3.3, ghi kịch bản Auto_TC_01 (Login OK) |
| **D13** | T4 30/09 | Rà soát các ca test thất bại (Fail test case) | Thực thi test Cập nhật Profile, Đổi mật khẩu | Thực thi test Xem chi tiết, Admin sửa SP | Thực thi test CheckOut đặt hàng, log DEF-03 | Ghi kịch bản Auto_TC_02 & Auto_TC_03 |
| **D14** | T5 01/10 | Chuẩn bị khung Chương 4 trong báo cáo | Thực thi test Quản trị người dùng Admin | Thực thi test Đánh giá, Quản lý Brand/Category | Thực thi test Trigger Tri_AddProduct, Gallery | Ghi Auto_TC_04 (Search) & 05 (Add Cart) .side |
| **D15** | T6 02/10 | Họp tổng kết Cycle 1, nghiệm thu M3 | Hoàn tất chụp ảnh minh chứng kiểm thử Auth | Hoàn tất chụp ảnh minh chứng kiểm thử Prod | Hoàn tất chụp ảnh minh chứng Web & SQL | Chạy thử nghiệm 5 kịch bản tự động .side |

---

#### 🔹 TUẦN 4: KIỂM THỬ TÍCH HỢP, DEFECT REPORTS & SỬA CODE (05/10 – 09/10/2026)

| Ngày | Thứ / Ngày | TV01 (Lead) | TV02 (Auth) | TV03 (Prod) | TV04 (Cart/DB) | TV05 (Auto/UT) |
| :---: | :---: | :--- | :--- | :--- | :--- | :--- |
| **D16** | T2 05/10 | Thiết lập mẫu Defect Report chuẩn Severity | Kiểm thử bảo mật URL Admin /Admin/Users | Kiểm thử Regex Crash: nhập (, [, *, \ ô tìm | Thực thi test Trigger Tri_AddUserDetail & SP | Chạy Selenium IDE đo thời gian, chạy MSTest |
| **D17** | T3 06/10 | Chủ trì họp Bug Triage phân loại lỗi S1->S4 | Lập Defect Report hoàn chỉnh cho DEF-04 | Trích log Serilog, lập Defect Report DEF-02 | Lập Defect Report hoàn chỉnh cho DEF-01 | Đo Code Coverage Visual Studio (đạt ≥ 70%) |
| **D18** | T4 07/10 | Soạn Mục 4.1 & 4.2 trong file báo cáo Word | Rà soát toàn bộ ảnh minh chứng Auth/Account | Rà soát ảnh minh chứng Prod, viết mục 2.4 | Lập Defect Report hoàn chỉnh cho DEF-03 | Nghiên cứu và viết giải pháp sửa DEF-01, 02 |
| **D19** | T5 08/10 | Thống kê tỷ lệ Pass/Fail, bảng defect 4.5.1 | Hỗ trợ TV05 kiểm tra logic giải pháp RBAC | Hỗ trợ TV05 giải pháp Regex.Escape() | Kiểm tra logic tạo đơn hàng Order_ cho DEF-03 | Viết hoàn chỉnh mã sửa lỗi DEF-03, 04 (4.5.3) |
| **D20** | T6 09/10 | Họp review nghiệm thu Cột mốc 4 (M4) | Rà soát lại hồ sơ lỗi phân hệ Auth | Rà soát lại hồ sơ lỗi phân hệ Product | Rà soát lại hồ sơ lỗi Giỏ hàng & CSDL | Hoàn thiện mục 4.5.3 Đề xuất sửa mã nguồn |

---

#### 🔹 TUẦN 5: RETEST, REGRESSION, HOÀN THIỆN BÁO CÁO & BÀN GIAO (12/10 – 16/10/2026)

| Ngày | Thứ / Ngày | TV01 (Lead) | TV02 (Auth) | TV03 (Prod) | TV04 (Cart/DB) | TV05 (Auto/UT) |
| :---: | :---: | :--- | :--- | :--- | :--- | :--- |
| **D21** | T2 12/10 | Lập kế hoạch Retest & Regression chi tiết | Retest DEF-04 sau khi áp dụng code fix RBAC | Retest DEF-02 sau khi fix Regex.Escape() | Retest DEF-01 (xóa giỏ) & DEF-03 (lưu đơn) | Chạy lại MSTest kiểm tra tính toàn vẹn code |
| **D22** | T3 13/10 | Soạn Mục 4.6 (Kết luận C4) & Phần KẾT LUẬN | Kiểm thử hồi quy chéo (Cross-test Cart/Prod) | Kiểm thử hồi quy chéo (Cross-test Auth/User) | Kiểm tra tính nhất quán CSDL sau hồi quy | Chạy Regression test 5 script Selenium IDE |
| **D23** | T4 14/10 | Vẽ biểu đồ tròn/cột phân bố Test Case & Lỗi | Đóng góp phần Đánh giá & Hướng phát triển | Rà soát Danh mục hình/bảng/từ viết tắt | Chuẩn bị nội dung Slide thuyết trình | Chuẩn hóa danh mục TÀI LIỆU THAM KHẢO |
| **D24** | T5 15/10 | Format toàn bộ file Word (lề, font, mục lục) | Đọc soát chính tả, đối chiếu số liệu báo cáo | Đọc soát chính tả, kiểm tra liên kết hình ảnh | Thiết kế hoàn thiện Slide PowerPoint (15-20s) | Đóng gói mã nguồn test, file script .side |
| **D25** | T6 16/10 | Họp tổng duyệt, nghiệm thu M5 & Nộp bài | Ký biên bản xác nhận đóng góp của nhóm | Ký biên bản xác nhận đóng góp của nhóm | Ký biên bản xác nhận đóng góp của nhóm | Ký biên bản xác nhận đóng góp của nhóm |

---

## 🎯 3. CÁC CỘT MỐC NGHIỆM THU TUẦN (WEEKLY MILESTONES M1 - M5)

| Cột mốc | Tuần | Thời gian | Trọng tâm kiểm thử & bàn giao | Tiêu chí nghiệm thu (Deliverables) | Tiến độ | Đánh giá |
| :---: | :---: | :---: | :--- | :--- | :---: | :---: |
| **M1** | **Tuần 1** | 14/09 – 18/09/2026 | Khởi động dự án, khảo sát yêu cầu, cài đặt môi trường 5 máy, hoàn thiện Test Plan | • Bản thảo Chương 1 hoàn chỉnh.<br>• 5 máy chạy thành công web Store EF port 5000.<br>• Biên bản phân công nhiệm vụ. | 100% | Hoàn thành |
| **M2** | **Tuần 2** | 21/09 – 25/09/2026 | Thiết kế chi tiết bộ Test Cases cho toàn bộ các phân hệ chức năng và tích hợp | • Bộ Test Cases Specification (100 - 120 TC).<br>• Dự án Unit Test Store.Tests build thành công.<br>• Bản thảo Chương 2 hoàn chỉnh. | 100% | Hoàn thành |
| **M3** | **Tuần 3** | 28/09 – 02/10/2026 | Thực thi Test Execution Cycle 1, xây dựng Chương 3 và 5 kịch bản tự động hóa | • Bản thảo Chương 3 hoàn chỉnh.<br>• 5 file kịch bản tự động Selenium IDE (.side).<br>• Bảng kết quả thực thi Đợt 1 kèm ảnh chụp. | 100% | Hoàn thành |
| **M4** | **Tuần 4** | 05/10 – 09/10/2026 | Kiểm thử tích hợp CSDL, lập Defect Reports cho 4 bug lớn và đề xuất sửa mã nguồn | • 4 Defect Reports (DEF-01 -> DEF-04).<br>• Ảnh chụp Code Coverage Visual Studio ≥ 70%.<br>• Mục 4.5.3 Đề xuất giải pháp sửa mã nguồn. | 100% | Hoàn thành |
| **M5** | **Tuần 5** | 12/10 – 16/10/2026 | Retest, chạy Regression Testing, format toàn bộ file báo cáo Word và nộp bài | • File Báo cáo Word (.docx) format chuẩn.<br>• Slide thuyết trình PowerPoint.<br>• Bộ hồ sơ đồ án đầy đủ (Word, Excel, Code). | 100% | Hoàn thành |

---

## 📁 4. TÀI LIỆU THAM CHIẾU LIÊN KẾT
* **File Excel tương tác (Gantt Chart hằng ngày 5 tuần):** Docs/GANTT_CHART_5_WEEKS_DAILY.xlsx
* **File Excel bảng theo dõi tuần:** Docs/BANG_THEO_DOI_TIEN_DO_NHOM.xlsx
* **Tài liệu phân chia nhiệm vụ 5 thành viên:** Docs/TASK_ASSIGNMENT_5_MEMBERS.md
* **Kế hoạch kiểm thử tổng thể:** Docs/TEST_PLAN.md
* **Đề cương kiểm tra báo cáo:** Docs/CHECKLIST_TESTING_PLAN.md
