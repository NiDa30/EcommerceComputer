# 👥 BẢNG PHÂN CHIA NHIỆM VỤ ĐỒ ÁN KIỂM THỬ (NHÓM 5 THÀNH VIÊN)
## DỰ ÁN: ECOMMERCE COMPUTER (STORE EF) - PHIÊN BẢN V3
> **Căn cứ phân công:** Dựa trên cấu trúc đề cương báo cáo tại `Docs/CHECKLIST_TESTING_PLAN.md` và tài liệu `Docs/TEST_PLAN.md`.  
> **Mục tiêu:** Phân bổ cân đối khối lượng công việc, rõ ràng vai trò trách nhiệm, đảm bảo hoàn thành đúng hạn đồ án môn học Kiểm thử phần mềm.  
> **Ngày thiết lập:** 11/09/2026 | **Phiên bản:** 1.0  

---

## 📌 BẢNG TỔNG QUAN THÀNH VIÊN & VAI TRÒ CHÍNH

| STT | Mã vai trò | Họ và tên thành viên | Mã số sinh viên (MSSV) | Vai trò chuyên trách trong nhóm | Module / Nhiệm vụ phụ trách chính |
| :---: | :---: | :--- | :---: | :--- | :--- |
| **1** | **TV01** | **[Họ tên SV 1 - Trưởng nhóm]** | `[MSSV 01]` | **Test Lead / QA Project Manager** | Quản lý dự án, Lập Test Plan (Chương 1), Bìa & Mục lục, Tổng hợp kết quả (4.4, 4.6), Kết luận & Tài liệu tham khảo, Format tài liệu tổng. |
| **2** | **TV02** | **[Họ tên SV 2]** | `[MSSV 02]` | **Manual Tester 1 (Auth & Account Specialist)** | Phân hệ Xác thực (Đăng ký, Đăng nhập, Đăng xuất), Hồ sơ cá nhân (Profile), Đổi mật khẩu, Quản trị người dùng Admin, Kiểm thử bảo mật RBAC & Session. |
| **3** | **TV03** | **[Họ tên SV 3]** | `[MSSV 03]` | **Manual Tester 2 (Product Catalog & Admin Specialist)** | Phân hệ Sản phẩm (Danh sách, Phân trang, Lọc đa tiêu chí, Tìm kiếm Regex), Chi tiết sản phẩm, Quản trị sản phẩm (CRUD + Upload ảnh), Quản lý Brand & Category, Đánh giá (Reviews). |
| **4** | **TV04** | **[Họ tên SV 4]** | `[MSSV 04]` | **Integration & Business Flow Tester (Cart, Order & DB)** | Phân hệ Giỏ hàng (Cart) & Thanh toán (CheckOut), Toàn bộ Kiểm thử tích hợp (Triggers `Tri_AddProduct`, `Tri_AddGallery`, `Tri_AddUserDetail`, SP `AddCart`, DbContext), Phân tích bug DEF-01 & DEF-03. |
| **5** | **TV05** | **[Họ tên SV 5]** | `[MSSV 05]` | **Automation & Unit Test Engineer** | Toàn bộ Chương 3 (Kiểm thử tự động Selenium IDE, ghi 5 kịch bản .side), Kiểm thử đơn vị MSTest (`Store.Tests`), Đo Code Coverage, Đề xuất giải pháp sửa lỗi code (4.5.3). |

---

## 📊 MA TRẬN PHÂN BỔ KHỐI LƯỢNG THEO ĐỀ CƯƠNG BÁO CÁO (WBS)

* **P (Primary - Phụ trách chính):** Người trực tiếp thực hiện, viết nội dung báo cáo, thiết kế test case/script và chụp ảnh minh chứng.
* **S (Support / Review - Phối hợp & Rà soát):** Người hỗ trợ chạy test chéo, phản biện, kiểm tra lại lỗi hoặc review nội dung.

| Phần mục trong báo cáo | Tiêu đề nội dung | TV01 (Lead) | TV02 (Auth) | TV03 (Prod) | TV04 (Cart/DB) | TV05 (Auto/UT) |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: |
| **Bìa & Danh mục** | Bìa, Mục lục, Danh mục hình/bảng/từ viết tắt | **P** | S | S | S | S |
| **Lời mở đầu** | Bối cảnh, lý do chọn đề tài, bố cục báo cáo | **P** | S | - | - | - |
| **1.1** | Giới thiệu hệ thống, kiến trúc MVC, ERD, chức năng | **P** | S | S | S | - |
| **1.2** | Mục tiêu, phạm vi (In/Out-of-Scope), đối tượng test | **P** | S | - | - | S |
| **1.3** | Chiến lược kiểm thử, RACI, Gantt chart, phân tích rủi ro | **P** | - | - | S | S |
| **1.4 – 1.5** | Môi trường test, công cụ, tiêu chí Entry/Exit | **P** | S | S | S | S |
| **1.6** | Kết luận chương 1 | **P** | - | - | - | - |
| **2.1** | Cơ sở lý thuyết thiết kế test (EP, BVA, Decision Table) | S | **P** | S | - | - |
| **2.2.1** | Thiết kế Test Case: Khách hàng & Tài khoản | - | **P** | - | - | S |
| **2.2.2 (Sản phẩm)** | Thiết kế Test Case: Danh sách, Lọc, Tìm kiếm, Chi tiết, CRUD | - | - | **P** | - | - |
| **2.2.2 (Giỏ & Đơn)** | Thiết kế Test Case: Giỏ hàng & Thanh toán CheckOut | - | - | - | **P** | - |
| **2.2.3 & 2.2.4** | Thiết kế Test Case: Đánh giá (Reviews), Brand & Category | - | - | **P** | - | - |
| **2.3** | Thiết kế Test Case kiểm thử tích hợp (Triggers, SP, RBAC) | - | S | - | **P** | S |
| **2.4** | Kết luận chương 2 | S | - | **P** | - | - |
| **3.1 – 3.2** | Lý thuyết kiểm thử tự động & Giới thiệu Selenium IDE | - | - | - | - | **P** |
| **3.3 – 3.4** | Tiêu chí chọn TC & Danh sách 5 kịch bản tự động hóa | - | S (Review) | S (Review) | - | **P** |
| **3.5** | Kết luận chương 3 | - | - | - | - | **P** |
| **4.1.1** | Thực thi test chức năng: Khách hàng & Tài khoản | - | **P** | - | - | - |
| **4.1.2 (Sản phẩm)** | Thực thi test chức năng: Sản phẩm & Quản trị kho | - | - | **P** | - | - |
| **4.1.2 (Giỏ & Đơn)** | Thực thi test chức năng: Giỏ hàng & CheckOut | - | - | - | **P** | - |
| **4.1.3 & 4.1.4** | Thực thi test: Đánh giá, Thương hiệu, Danh mục | - | - | **P** | - | - |
| **4.2** | Thực thi kiểm thử tích hợp & Chạy MSTest Unit Test | - | - | - | **P** | **P** |
| **4.3** | Thực thi kiểm thử tự động Selenium IDE | - | - | - | - | **P** |
| **4.4** | Tổng hợp kết quả, thống kê Pass/Fail, độ bao phủ | **P** | S | S | S | S |
| **4.5** | Lập Defect Report, phân loại mức độ, đề xuất sửa lỗi | S | **P** (DEF-04) | **P** (DEF-02) | **P** (DEF-01,03) | **P** (Fix code) |
| **4.6** | Kết luận chương 4 | **P** | - | - | - | - |
| **KẾT LUẬN** | Đánh giá kết quả đạt được, hạn chế, hướng phát triển | **P** | S | S | S | S |
| **TÀI LIỆU THAM KHẢO** | Danh mục tài liệu tham khảo theo chuẩn trích dẫn | **P** | S | - | - | S |

---

## 📋 PHÂN CÔNG CÔNG VIỆC CHI TIẾT CHO TỪNG THÀNH VIÊN

### 👤 THÀNH VIÊN 1: TRƯỞNG NHÓM (TEST LEAD & QA PROJECT MANAGER)
> **Mục tiêu:** Điều phối tiến độ chung, đảm bảo tính nhất quán của báo cáo, chịu trách nhiệm Chương 1, tổng hợp Chương 4 và đóng gói tài liệu nộp.

* **Nhiệm vụ cụ thể:**
  1. **Khởi động dự án & Quản lý:**
     - Thiết lập kho lưu trữ (Git / Google Drive) chia sẻ tài liệu cho cả nhóm.
     - Lập lịch họp nhóm hàng tuần (Check-in tiến độ) và giải quyết các vướng mắc kỹ thuật.
     - Kiểm soát chất lượng (QA review) các bảng Test Case và Defect Report do các thành viên gửi lên.
  2. **Biên soạn Báo cáo (Word):**
     - Thiết kế Trang bìa, Bìa phụ, Lời cảm ơn, Lời cam đoan.
     - Viết **Lời mở đầu** (Tính cấp thiết, lý do chọn dự án Store EF V3, mục tiêu, bố cục).
     - Viết toàn bộ **Chương 1: XÂY DỰNG KẾ HOẠCH KIỂM THỬ** (Mục 1.1 đến 1.6).
     - Viết mục **4.4: Tổng hợp kết quả kiểm thử** (Vẽ biểu đồ phân bố Test Case, tính tỷ lệ Pass/Fail, đánh giá độ bao phủ).
     - Viết mục **4.6: Kết luận chương 4**.
     - Viết phần **KẾT LUẬN** (Kết quả đạt được, hạn chế, hướng phát triển) và **TÀI LIỆU THAM KHẢO**.
     - Tạo Mục lục tự động, Danh mục hình tự động, Danh mục bảng tự động.
  3. **Hỗ trợ thực thi:**
     - Tham gia kiểm thử chéo (Cross-testing) nghiệm thu cuối cùng ở Tuần 4.
* **Sản phẩm bàn giao (Deliverables):**
  - File tài liệu Word tổng thể được format chuẩn chỉn chu (lề, font chữ, mục lục, bảng biểu).
  - Bản Test Plan hoàn chỉnh đã được thống nhất giữa các thành viên.

---

### 👤 THÀNH VIÊN 2: MANUAL TESTER 1 (AUTH & ACCOUNT SPECIALIST)
> **Mục tiêu:** Chịu trách nhiệm toàn diện về chất lượng phân hệ Xác thực, Hồ sơ người dùng và Quản trị tài khoản Admin; kiểm soát an toàn bảo mật mật khẩu và phân quyền RBAC.

* **Nhiệm vụ cụ thể:**
  1. **Nghiên cứu & Thiết kế lý thuyết:**
     - Biên soạn mục **2.1: Phương pháp thiết kế Test Case** (Lý thuyết Phân vùng tương đương EP, Phân tích giá trị biên BVA, Bảng quyết định).
  2. **Thiết kế Test Case & Test Data (Mục 2.2.1):**
     - Viết bộ Test Cases cho chức năng **Đăng ký (Sign Up)**: Validate định dạng email, mật khẩu >= 6 ký tự, email trùng lặp, băm mật khẩu BCrypt trong DB, trigger tạo `UserDetail`.
     - Viết bộ Test Cases cho chức năng **Đăng nhập (Sign In)**: Đăng nhập thành công các quyền (User, Admin, Employee), sai mật khẩu, tài khoản không tồn tại, lưu Session, thử nghiệm SQL Injection.
     - Viết bộ Test Cases cho chức năng **Đăng xuất (Logout)**: Xóa Session, ngăn chặn bấm nút Back trình duyệt.
     - Viết bộ Test Cases cho chức năng **Hồ sơ cá nhân (Profile)**: Xem và cập nhật thông tin Họ tên, Giới tính, Ngày sinh, SĐT, Địa chỉ.
     - Viết bộ Test Cases cho chức năng **Đổi mật khẩu**: Kiểm tra mật khẩu cũ (BCrypt), xác nhận mật khẩu mới.
     - Viết bộ Test Cases cho chức năng **Quản trị người dùng (Admin User Management)**: Xem danh sách phân trang, thêm tài khoản quản trị/nhân viên, đổi vai trò, xóa tài khoản.
  3. **Thực thi kiểm thử & Báo cáo lỗi (Mục 4.1.1 & 4.5):**
     - Thực thi toàn bộ Test Cases đã thiết kế, ghi lại kết quả Actual Result, đánh giá Pass/Fail.
     - Chụp ảnh màn hình minh chứng cho tất cả các ca kiểm thử.
     - Phân tích và viết báo cáo lỗi chi tiết cho **DEF-04: Lỗ hổng kiểm soát truy cập trực tiếp URL quản trị đối với tài khoản vai trò User**.
* **Sản phẩm bàn giao (Deliverables):**
  - Bảng đặc tả Test Cases chi tiết phân hệ Auth & Account (khoảng 25 - 35 Test Cases).
  - Bảng kết quả thực thi kiểm thử kèm ảnh chụp màn hình minh chứng.
  - Bản mô tả lỗi Defect Report cho DEF-04.

---

### 👤 THÀNH VIÊN 3: MANUAL TESTER 2 (PRODUCT CATALOG & ADMIN SPECIALIST)
> **Mục tiêu:** Chịu trách nhiệm toàn diện về phân hệ Danh mục & Sản phẩm, từ góc nhìn người mua hàng (Duyệt, Tìm kiếm, Lọc) đến góc nhìn quản trị viên (Thêm, Sửa, Xóa, Upload ảnh sản phẩm).

* **Nhiệm vụ cụ thể:**
  1. **Thiết kế Test Case & Test Data (Mục 2.2.2 - Phần Sản phẩm & 2.2.3, 2.2.4):**
     - Viết bộ Test Cases cho chức năng **Duyệt danh sách & Phân trang**: Hiển thị sản phẩm còn tồn kho (`Stock > 0`), phân trang PagedList đúng 8 sp/trang, chuyển trang.
     - Viết bộ Test Cases cho chức năng **Bộ lọc sản phẩm (Filter)**: Lọc theo Category, lọc theo Brand, lọc kết hợp đồng thời Danh mục & Thương hiệu, trường hợp không có sản phẩm.
     - Viết bộ Test Cases cho chức năng **Tìm kiếm sản phẩm (Search)**: Tìm kiếm theo tên chính xác, một phần, không phân biệt hoa thường, từ khóa không tồn tại, ô tìm kiếm rỗng.
     - Viết bộ Test Cases kiểm thử tính bền vững ô tìm kiếm (Regex Crash): Nhập các ký tự đặc biệt `(`, `[`, `*`, `\`.
     - Viết bộ Test Cases cho chức năng **Xem chi tiết sản phẩm**: Hiển thị thông số, ảnh chính và ảnh phụ galleries, tính đúng tỷ lệ giảm giá và định dạng tiền tệ VNĐ (`vi-VN`).
     - Viết bộ Test Cases cho chức năng **Quản trị sản phẩm (Admin/Employee)**: Thêm mới sản phẩm kèm upload ảnh (kiểm tra `Helpers.IsValidImage`), sửa thông tin sản phẩm, xóa sản phẩm.
     - Viết bộ Test Cases cho chức năng **Đánh giá sản phẩm (Reviews)** và **Quản lý Thương hiệu / Danh mục**.
  2. **Thực thi kiểm thử & Báo cáo lỗi (Mục 4.1.2 - Phần Sản phẩm & 4.1.3, 4.1.4):**
     - Thực thi toàn bộ Test Cases trên giao diện website, ghi nhận Pass/Fail.
     - Chụp đầy đủ ảnh chụp màn hình minh chứng cho các trường hợp.
     - Phân tích và viết báo cáo lỗi chi tiết cho **DEF-02: Lỗi sập ứng dụng (Crash) do Regex Injection trong ProductsController.Search khi nhập ký tự đặc biệt**.
  3. **Biên soạn mục 2.4: Kết luận chương 2** (Tổng hợp số lượng Test Case đã thiết kế của cả nhóm).
* **Sản phẩm bàn giao (Deliverables):**
  - Bảng đặc tả Test Cases phân hệ Sản phẩm & Quản trị (khoảng 30 - 40 Test Cases).
  - Bảng kết quả thực thi kiểm thử kèm ảnh chụp màn hình minh chứng.
  - Bản mô tả lỗi Defect Report cho DEF-02 (kèm log file Serilog trích xuất ngoại lệ).

---

### 👤 THÀNH VIÊN 4: INTEGRATION & BUSINESS FLOW TESTER (CART, ORDER & DB)
> **Mục tiêu:** Chịu trách nhiệm kiểm thử luồng chuyển đổi kinh doanh quan trọng nhất (Giỏ hàng & CheckOut) và kiểm thử tầng tích hợp CSDL (Triggers, Stored Procedures, Entity Framework).

* **Nhiệm vụ cụ thể:**
  1. **Thiết kế Test Case & Test Data (Mục 2.2.2 - Phần Giỏ hàng & Đơn hàng, Mục 2.3):**
     - Viết bộ Test Cases cho chức năng **Giỏ hàng (Cart)**: Thêm vào giỏ khi chưa đăng nhập (điều hướng SignIn), thêm khi đã đăng nhập (gọi SP `AddCart`), thêm nhiều lần tăng số lượng, xem giỏ và tính tổng tiền, cập nhật số lượng món hàng.
     - Viết bộ Test Cases kiểm tra **Xóa sản phẩm khỏi giỏ hàng** (Kiểm tra đặc biệt lỗi DEF-01).
     - Viết bộ Test Cases cho chức năng **Thanh toán (CheckOut)**: Điều hướng từ giỏ hàng sang form CheckOut, validate các trường thông tin giao hàng bắt buộc, xác nhận đặt hàng.
     - Viết bộ Test Cases cho **Kiểm thử tích hợp (Integration Testing - Mục 2.3)**:
       * Tích hợp Trigger `Tri_AddProduct`: Tự động thêm bản ghi vào `Gallery` với `IsPrimary = 1`.
       * Tích hợp Trigger `Tri_AddGallery`: Rollback giao dịch nếu cố ý gán 2 ảnh chính cho 1 sản phẩm.
       * Tích hợp Trigger `Tri_AddUserDetail`: Tự động sinh bản ghi `UserDetail` khi đăng ký tài khoản.
       * Tích hợp Stored Procedure `AddCart`: Kiểm tra logic thêm mới / tăng số lượng.
       * Tích hợp Controller & Entity Framework `StoreEntities`.
  2. **Thực thi kiểm thử & Báo cáo lỗi (Mục 4.1.2 - Phần Giỏ hàng, Mục 4.2):**
     - Thực thi toàn bộ Test Cases chức năng Giỏ hàng, CheckOut và Kiểm thử tích hợp.
     - Chụp ảnh màn hình minh chứng các thao tác trên Web và câu lệnh truy vấn SQL Server kiểm tra dữ liệu bảng `Cart`, `Product`, `Order_`, `OrderDetail`.
     - Phân tích và viết báo cáo lỗi chi tiết cho:
       * **DEF-01: Lỗi nghiêm trọng trong `CartController.Remove` xóa nhầm sản phẩm trong bảng `Product`**.
       * **DEF-03: Chức năng `CheckOut` chưa có mã xử lý lưu dữ liệu đơn hàng vào CSDL**.
* **Sản phẩm bàn giao (Deliverables):**
  - Bảng đặc tả Test Cases Giỏ hàng, Đơn hàng & Kiểm thử tích hợp (khoảng 25 - 35 Test Cases).
  - Bảng kết quả thực thi kiểm thử kèm ảnh chụp màn hình giao diện web và dữ liệu SQL Server.
  - Bản mô tả lỗi Defect Report cho DEF-01 và DEF-03.

---

### 👤 THÀNH VIÊN 5: AUTOMATION & UNIT TEST ENGINEER
> **Mục tiêu:** Chịu trách nhiệm toàn bộ mảng Kiểm thử Tự động (Selenium IDE) của Chương 3 và mảng Kiểm thử Đơn vị (MSTest); hỗ trợ đề xuất phương án sửa lỗi mã nguồn ở Chương 4.

* **Nhiệm vụ cụ thể:**
  1. **Xây dựng nội dung Chương 3: KIỂM THỬ TỰ ĐỘNG WEBSITE:**
     - Viết mục **3.1: Tổng quan về kiểm thử tự động** (Khái niệm, vai trò, ưu nhược điểm).
     - Viết mục **3.2: Công cụ kiểm thử tự động Selenium IDE** (Kiến trúc extension, Command, Target, Value, Assertions vs. Verifications, Record & Playback).
     - Viết mục **3.3: Tiêu chí lựa chọn Test Case để tự động hóa** (Happy path, Regression test).
     - Xây dựng, ghi và hoàn thiện **5 Kịch bản kiểm thử tự động (Mục 3.4)** trên Selenium IDE:
       * `Auto_TC_01`: Đăng nhập thành công với tài khoản chuẩn.
       * `Auto_TC_02`: Đăng nhập thất bại do sai mật khẩu.
       * `Auto_TC_03`: Đăng ký tài khoản người dùng mới.
       * `Auto_TC_04`: Tìm kiếm sản phẩm theo từ khóa "Dell".
       * `Auto_TC_05`: Thêm sản phẩm vào giỏ hàng.
     - Xuất file kịch bản `.side` lưu vào thư mục dự án/tài liệu.
     - Viết mục **3.5: Kết luận chương 3**.
  2. **Thực thi kiểm thử tự động & Đơn vị (Mục 4.2 & 4.3):**
     - Chạy thực thi 5 kịch bản tự động trên Selenium IDE, ghi nhận thời gian chạy và chụp ảnh kết quả Pass màu xanh.
     - Viết và chạy các bài Unit Test trên MSTest trong dự án `Store.Tests` cho các lớp nghiệp vụ lõi: `ProductExts.IsValid()`, `ProductExts.FormattedPrice()`, `ProductExts.DiscountPercentage()`, `ProductsExts.MaxPage()`, `Helpers.IsValidEmail()`, `Helpers.IsValidImage()`.
     - Đo lường và chụp ảnh màn hình độ bao phủ mã nguồn (Code Coverage ≥ 70%) trên Visual Studio Test Explorer.
  3. **Đóng góp kỹ thuật cho Báo cáo lỗi (Mục 4.5.2 & 4.5.3):**
     - Phân loại mức độ nghiêm trọng của lỗi (Severity S1 -> S4).
     - **Viết đề xuất giải pháp kỹ thuật sửa mã nguồn cụ thể (Fix code)** cho cả 4 lỗi DEF-01, DEF-02, DEF-03, DEF-04.
* **Sản phẩm bàn giao (Deliverables):**
  - Nội dung hoàn chỉnh Chương 3 trong file Word báo cáo.
  - File kịch bản kiểm thử tự động Selenium IDE (`.side`).
  - Dự án mã nguồn Unit Test `Store.Tests` chạy thành công 100% Pass và ảnh chụp Code Coverage.
  - Mục giải pháp khắc phục lỗi code chi tiết ở mục 4.5.3.

---

## 📅 LỊCH TRÌNH PHỐI HỢP & CỘT MỐC BÀN GIAO (4 TUẦN)

```mermaid
gantt
    title LỊCH TRÌNH PHỐI HỢP NHÓM 5 THÀNH VIÊN (4 TUẦN)
    dateFormat  YYYY-MM-DD
    section Tuần 1: Khởi động
    TV01: Test Plan, Lời mở đầu, Chương 1           :active, t1_1, 2026-09-14, 5d
    TV02, TV03, TV04, TV05: Cài môi trường, chạy thử :t1_2, 2026-09-14, 5d
    section Tuần 2: Thiết kế
    TV02: Viết TC Auth & Account (Mục 2.2.1)        :t2_1, 2026-09-21, 5d
    TV03: Viết TC Product & Admin (Mục 2.2.2)       :t2_2, 2026-09-21, 5d
    TV04: Viết TC Giỏ hàng & Tích hợp (2.2.2, 2.3)   :t2_3, 2026-09-21, 5d
    TV05: Viết Chương 3 & Tạo script Selenium IDE   :t2_4, 2026-09-21, 5d
    TV01: Rà soát & Chuẩn hóa bảng Test Cases        :t2_5, 2026-09-23, 3d
    section Tuần 3: Thực thi
    TV02: Chạy test Auth, chụp ảnh, log DEF-04      :t3_1, 2026-09-28, 5d
    TV03: Chạy test Product, chụp ảnh, log DEF-02   :t3_2, 2026-09-28, 5d
    TV04: Chạy test Giỏ/Đơn/DB, log DEF-01, DEF-03  :t3_3, 2026-09-28, 5d
    TV05: Chạy test Auto, Unit Test, Code Coverage  :t3_4, 2026-09-28, 5d
    section Tuần 4: Tổng kết
    Cả nhóm: Retest lỗi, Họp Bug Review             :t4_1, 2026-10-05, 2d
    TV01, TV05: Tổng hợp số liệu, biểu đồ, sửa lỗi  :t4_2, 2026-10-07, 2d
    TV01: Format tài liệu, in ấn, nộp báo cáo       :t4_3, 2026-10-09, 1d
```

| Cột mốc | Thời gian | Nhiệm vụ chính của từng thành viên | Kết quả nghiệm thu cột mốc |
| :---: | :---: | :--- | :--- |
| **Cột mốc 1 (M1)** | **Tuần 1** | - **TV01:** Họp nhóm, thống nhất phân công, hoàn thiện Chương 1 và Kế hoạch kiểm thử.<br>- **TV02, TV03, TV04, TV05:** Cài đặt Visual Studio, SQL LocalDB, restore `Store.sql`, test thử file `run.bat` đảm bảo web chạy trên port 5000. | - Biên bản họp phân công nhiệm vụ.<br>- Môi trường kiểm thử trên 5 máy sẵn sàng.<br>- Bản thảo Chương 1 hoàn thành. |
| **Cột mốc 2 (M2)** | **Tuần 2** | - **TV02:** Hoàn thiện mục 2.1 và bộ Test Cases Auth/Account (2.2.1).<br>- **TV03:** Hoàn thiện bộ Test Cases Sản phẩm/Admin (2.2.2, 2.2.3, 2.2.4).<br>- **TV04:** Hoàn thiện bộ Test Cases Giỏ hàng/CheckOut và Tích hợp CSDL (2.2.2, 2.3).<br>- **TV05:** Hoàn thiện nội dung Chương 3 và xuất 5 kịch bản Selenium IDE `.side`.<br>- **TV01:** Review chéo toàn bộ Test Cases, đảm bảo đủ ID, Steps, Expected Result. | - Bộ Test Cases Specification hoàn chỉnh (khoảng 90 - 120 Test Cases).<br>- File kịch bản tự động `.side`.<br>- Bản thảo Chương 2 và Chương 3 hoàn thành. |
| **Cột mốc 3 (M3)** | **Tuần 3** | - **TV02, TV03, TV04:** Thực thi test trên Web, ghi nhận kết quả Pass/Fail, chụp ảnh bằng chứng từng ca kiểm thử.<br>- **TV05:** Chạy kịch bản tự động Selenium IDE, chạy MSTest và đo Code Coverage.<br>- **TV02, TV03, TV04:** Lập báo cáo lỗi cho 4 bug trọng yếu (DEF-01, DEF-02, DEF-03, DEF-04). | - Bảng kết quả thực thi kiểm thử có đầy đủ ảnh chụp minh chứng.<br>- Báo cáo lỗi chi tiết cho các defect.<br>- Bản thảo Chương 4 (mục 4.1, 4.2, 4.3, 4.5.1). |
| **Cột mốc 4 (M4)** | **Tuần 4** | - **Cả nhóm:** Kiểm thử lại (Retest) các ca lỗi, chạy kiểm thử hồi quy.<br>- **TV05:** Hoàn thiện đề xuất sửa code mục 4.5.3.<br>- **TV01:** Tổng hợp số liệu thống kê (4.4), vẽ biểu đồ, viết Kết luận & Tài liệu tham khảo.<br>- **TV01:** Rà soát chính tả, đánh số trang, cập nhật mục lục tự động, in ấn và nộp bài. | - File Báo cáo đồ án môn học Word (.docx) hoàn chỉnh 100%.<br>- Slide thuyết trình (PowerPoint).<br>- Thư mục nộp bài đầy đủ: Báo cáo, Test Cases Excel, File script `.side`, Code Unit Test. |

---

## 🎯 TIÊU CHUẨN HOÀN THÀNH CÔNG VIỆC (DEFINITION OF DONE - DOD)

Trước khi một thành viên được xác nhận là hoàn thành nhiệm vụ của mình, công việc phải thỏa mãn các tiêu chí sau:
1. **Đối với Test Case:**
   - Đầy đủ các trường thông tin: Mã Test Case chuẩn hóa, Tên ca kiểm thử, Tiền điều kiện, Các bước thực hiện chi tiết, Dữ liệu đầu vào cụ thể, Kết quả mong đợi rõ ràng.
   - Có kiểm thử cả trường hợp Hợp lệ (Positive) và Bất hợp lệ / Biên (Negative / Boundary).
2. **Đối với Kết quả Thực thi:**
   - Có trạng thái rõ ràng: `PASS` hoặc `FAIL`.
   - Bắt buộc có **ảnh chụp màn hình minh chứng** tương ứng với từng Test Case (kết quả hiển thị trên web, câu lệnh DB hoặc thông báo lỗi).
3. **Đối với Báo cáo Lỗi (Defect Report):**
   - Đầy đủ các bước tái hiện (Steps to Reproduce) để bất kỳ ai cũng có thể làm lại được.
   - Nêu rõ Kết quả thực tế (Actual Result) vs. Kết quả mong đợi (Expected Result).
   - Đính kèm ảnh chụp màn hình lỗi hoặc trích xuất log lỗi từ `Logs/dd-MM-yyyy.txt`.
4. **Đối với Soạn thảo Văn bản Báo cáo:**
   - Trình bày đúng font chữ quy định (Calibri hoặc Times New Roman), cỡ chữ 12-13pt, dãn dòng 1.2 - 1.3 lines.
   - Bảng biểu và hình ảnh đều có đánh số và chú thích (Caption) chuẩn.

---

## 📈 BẢNG THEO DÕI TIẾN ĐỘ THỰC HIỆN CỦA NHÓM (WEEKLY TRACKING SHEET)

| STT | Thành viên | Nhiệm vụ chính phụ trách | Tuần 1 | Tuần 2 | Tuần 3 | Tuần 4 | Đánh giá đóng góp | Chữ ký xác nhận |
| :---: | :---: | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **1** | **TV01** | Test Lead, Chương 1, Tổng hợp, Báo cáo tổng thể | [ ] 100% | [ ] 100% | [ ] 100% | [ ] 100% | Đạt yêu cầu | ____________ |
| **2** | **TV02** | Manual Tester 1 (Auth, Account, Profile, Admin User) | [ ] 100% | [ ] 100% | [ ] 100% | [ ] 100% | Đạt yêu cầu | ____________ |
| **3** | **TV03** | Manual Tester 2 (Products, Search, Filter, Admin Prod) | [ ] 100% | [ ] 100% | [ ] 100% | [ ] 100% | Đạt yêu cầu | ____________ |
| **4** | **TV04** | Integration & Cart/Order Tester (Giỏ hàng, DB, Triggers) | [ ] 100% | [ ] 100% | [ ] 100% | [ ] 100% | Đạt yêu cầu | ____________ |
| **5** | **TV05** | Automation & Unit Tester (Chương 3, Selenium IDE, MSTest) | [ ] 100% | [ ] 100% | [ ] 100% | [ ] 100% | Đạt yêu cầu | ____________ |

---

> **Tài liệu được lưu trữ tại:** `Docs/TASK_ASSIGNMENT_5_MEMBERS.md`  
> **Tham chiếu liên kết:** [`CHECKLIST_TESTING_PLAN.md`](file:///D:/Ki%E1%BB%83m%20th%E1%BB%AD%20pm/pj%20ki%E1%BB%83m%20th%E1%BB%AD/EcommerceComputer-V3/Docs/CHECKLIST_TESTING_PLAN.md) & [`TEST_PLAN.md`](file:///D:/Ki%E1%BB%83m%20th%E1%BB%AD%20pm/pj%20ki%E1%BB%83m%20th%E1%BB%AD/EcommerceComputer-V3/Docs/TEST_PLAN.md)  
> **Áp dụng cho:** Nhóm 5 sinh viên thực hiện đồ án môn học Kiểm thử phần mềm.
