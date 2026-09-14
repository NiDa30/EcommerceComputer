# 📄 KẾ HOẠCH KIỂM THỬ PHẦN MỀM (TEST PLAN)
## DỰ ÁN: ECOMMERCE COMPUTER (STORE EF) - PHIÊN BẢN V3

---

| **Thông Tin Dự Án** | **Nội Dung Chi Tiết** |
| :--- | :--- |
| **Tên dự án:** | Ecommerce Computer (Store EF) |
| **Phiên bản phần mềm:** | V3 (Release 3.0) |
| **Mã tài liệu:** | `TP-STOREEF-V3` |
| **Phiên bản tài liệu:** | 1.0 |
| **Ngày lập kế hoạch:** | 11/09/2026 |
| **Người lập:** | QA / Software Testing Team |
| **Người phê duyệt:** | Test Manager / Project Lead |
| **Môi trường ứng dụng:** | ASP.NET MVC 5 (.NET Framework 4.7.2), Entity Framework 6, SQL Server LocalDB |

---

## MỤC LỤC

1. [Giới thiệu chung (Introduction)](#1-giới-thiệu-chung-introduction)
   - 1.1. Mục đích tài liệu
   - 1.2. Tổng quan dự án
   - 1.3. Tài liệu tham khảo & Thuật ngữ viết tắt
2. [Mục tiêu Kiểm thử (Test Objectives)](#2-mục-tiêu-kiểm-thử-test-objectives)
   - 2.1. Mục tiêu chất lượng hệ thống
   - 2.2. Chỉ số KPI & Đo lường kiểm thử
3. [Phạm vi Kiểm thử (Test Scope)](#3-phạm-vi-kiểm-thử-test-scope)
   - 3.1. Hạng mục trong phạm vi (In-Scope)
   - 3.2. Hạng mục ngoài phạm vi (Out-of-Scope)
   - 3.3. Ma trận tính năng & Mức độ ưu tiên kiểm thử
4. [Chiến lược & Phương pháp Kiểm thử (Test Strategy)](#4-chiến-lược--phương-pháp-kiểm-thử-test-strategy)
   - 4.1. Cấp độ kiểm thử (Testing Levels)
   - 4.2. Các loại hình kiểm thử áp dụng (Testing Types)
   - 4.3. Kỹ thuật thiết kế kịch bản kiểm thử (Test Design Techniques)
   - 4.4. Kiểm thử các khuyết tật & Lỗ hổng đã nhận diện (Known Defect Analysis)
5. [Môi trường Kiểm thử (Test Environment)](#5-môi-trường-kiểm-thử-test-environment)
   - 5.1. Cấu hình phần cứng & Phần mềm
   - 5.2. Cấu hình Cơ sở dữ liệu & Ứng dụng
   - 5.3. Công cụ kiểm thử & Quản lý lỗi
   - 5.4. Dữ liệu kiểm thử & Tài khoản kiểm thử chuẩn
6. [Nguồn lực, Phân công & Vai trò (Resources & Roles)](#6-nguồn-lực-phân-công--vai-trò-resources--roles)
   - 6.1. Đội ngũ nhân sự dự kiến
   - 6.2. Ma trận trách nhiệm (RACI Matrix)
7. [Lịch trình & Các cột mốc (Schedule & Milestones)](#7-lịch-trình--các-cột-mốc-schedule--milestones)
   - 7.1. Lịch trình 4 tuần chi tiết
   - 7.2. Kế hoạch kiểm thử hồi quy (Regression Testing)
8. [Tiêu chí Chấp nhận (Acceptance Criteria)](#8-tiêu-chí-chấp-nhận-acceptance-criteria)
   - 8.1. Tiêu chí bắt đầu (Entry Criteria)
   - 8.2. Tiêu chí tạm dừng & Tiếp tục (Suspension & Resumption Criteria)
   - 8.3. Tiêu chí kết thúc kiểm thử (Exit Criteria)
9. [Quy trình Quản lý Lỗi & Sản phẩm bàn giao (Defects & Deliverables)](#9-quy-trình-quản-lý-lỗi--sản-phẩm-bàn-giao-defects--deliverables)
   - 9.1. Quy trình xử lý lỗi (Defect Life Cycle)
   - 9.2. Phân loại mức độ nghiêm trọng & Mức độ ưu tiên
   - 9.3. Danh mục sản phẩm bàn giao (Test Deliverables)
10. [Rủi ro & Kế hoạch Dự phòng (Risks & Mitigation Plan)](#10-rủi-ro--kế-hoạch-dự-phòng-risks--mitigation-plan)
11. [Phụ lục: Ma trận Kịch bản Kiểm thử Mẫu (Sample Test Cases)](#phụ-lục-ma-trận-kịch-bản-kiểm-thử-mẫu-sample-test-cases-outline)

---

## 1. Giới thiệu chung (Introduction)

### 1.1. Mục đích tài liệu
Tài liệu **Kế hoạch Kiểm thử (Test Plan)** này được lập nhằm xác định rõ ràng phạm vi, mục tiêu, chiến lược, nguồn lực, lịch trình và tiêu chí đánh giá cho toàn bộ hoạt động kiểm thử của dự án **Ecommerce Computer (Store EF) V3**. Tài liệu đóng vai trò làm chuẩn mực và căn cứ thực hiện cho đội ngũ QA/QC, Test Engineers và các bên liên quan (Developers, Project Manager) nhằm:
* Kiểm soát và nâng cao chất lượng phần mềm xuyên suốt chu trình phát triển.
* Phát hiện và xử lý sớm các khiếm khuyết phần mềm (Defects), hạn chế tối đa rủi ro phát sinh trong quá trình vận hành.
* Đảm bảo hệ thống đáp ứng đầy đủ các yêu cầu chức năng, phi chức năng, độ bảo mật và tính khả dụng trước khi bàn giao.

### 1.2. Tổng quan dự án
* **Tên ứng dụng:** Ecommerce Computer (Store EF).
* **Phiên bản phát hành:** V3 (Release 3.0).
* **Mô tả hệ thống:** Website thương mại điện tử chuyên kinh doanh các dòng sản phẩm máy tính xách tay (laptop), máy tính để bàn (desktop), màn hình vi tính, linh kiện và phụ kiện công nghệ từ các thương hiệu nổi tiếng thế giới (Dell, HP, Asus, Lenovo, Acer,...).
* **Kiến trúc & Ngăn xếp công nghệ:**
  - **Nền tảng & Khung ứng dụng:** C# / .NET Framework 4.7.2 / ASP.NET MVC 5 (v5.3.0).
  - **ORM & Truy cập dữ liệu:** Entity Framework 6 (v6.4.4) tiếp cận theo mô hình Database-First (`StoreDb.edmx`).
  - **Cơ sở dữ liệu:** Microsoft SQL Server (LocalDB `MSSQLLocalDB`, tên CSDL: `Store`).
  - **Bảo mật & Mã hóa:** `BCrypt.Net-Next` (v4.0.3) băm muối mật khẩu.
  - **Ghi nhật ký (Logging):** `Serilog` & `Serilog.Sinks.File` tự động lưu vết ngoại lệ vào file theo ngày `Logs/dd-MM-yyyy.txt`.
  - **Giao diện & Client-side:** Razor Views (.cshtml), Bootstrap 5.3.3, jQuery 3.7.1, jQuery Validation 1.21.0, PagedList.
  - **Máy chủ Web phát triển:** IIS Express chạy tại cổng mạng `http://localhost:5000`.
* **Đối tượng người dùng:**
  - **Khách (Guest):** Người dùng vãng lai chưa đăng nhập.
  - **Khách hàng (User):** Người dùng đã đăng ký tài khoản và đăng nhập.
  - **Nhân viên (Employee):** Quản lý kho hàng, sản phẩm, danh mục.
  - **Quản trị viên (Admin):** Toàn quyền quản trị hệ thống, quản lý tài khoản người dùng và phân quyền.

### 1.3. Tài liệu tham khảo & Thuật ngữ viết tắt
#### A. Tài liệu tham khảo:
1. `PROJECT_OVERVIEW.md` - Tài liệu kiến trúc và đặc tả chi tiết dự án Store EF V3 (`Docs/PROJECT_OVERVIEW.md`).
2. Script CSDL `Store.sql` (Cấu trúc bảng, Trigger, Stored Procedure, Dữ liệu khởi tạo).
3. Tiêu chuẩn quốc tế về tài liệu kiểm thử phần mềm ISO/IEC/IEEE 29119.

#### B. Bảng thuật ngữ viết tắt:
* **SRS:** Software Requirements Specification (Đặc tả yêu cầu phần mềm).
* **RBAC:** Role-Based Access Control (Kiểm soát truy cập dựa trên vai trò).
* **UT / FT / ST / UAT:** Unit Testing / Functional Testing / System Testing / User Acceptance Testing.
* **BVA:** Boundary Value Analysis (Phân tích giá trị biên).
* **EP:** Equivalence Partitioning (Phân vùng tương đương).
* **SUT:** System Under Test (Hệ thống đối tượng kiểm thử).

---

## 2. Mục tiêu Kiểm thử (Test Objectives)

### 2.1. Mục tiêu chất lượng hệ thống
1. **Xác thực toàn diện các luồng nghiệp vụ cốt lõi:**
   - Xác minh các quy trình: Đăng ký, Đăng nhập, Tìm kiếm, Lọc sản phẩm, Thêm vào giỏ hàng, Cập nhật giỏ, Đặt hàng (CheckOut) và Quản lý hồ sơ cá nhân.
2. **Đảm bảo tính an toàn & Bảo mật thông tin (Security & RBAC):**
   - Đảm bảo 100% mật khẩu được băm an toàn qua BCrypt trước khi ghi xuống CSDL; không lưu mật khẩu thô dưới bất kỳ hình thức nào.
   - Xác minh phân quyền truy cập chặt chẽ (RBAC) giữa 4 vai trò: Guest, User, Employee, Admin; ngăn chặn tuyệt đối việc người dùng thường truy cập URL quản trị bằng cách gõ trực tiếp link.
   - Kiểm tra khả năng chống tấn công SQL Injection và Regex Injection trên ô tìm kiếm sản phẩm.
3. **Đảm bảo tính hợp lệ & Toàn vẹn dữ liệu (Data Integrity):**
   - Xác minh cơ chế kiểm tra dữ liệu đầu vào (Form Validation) ở cả 2 phía: Client-side (jQuery Validation) và Server-side (Model Validation, Helper functions).
   - Kiểm tra sự hoạt động chính xác của các Database Triggers (`Tri_AddProduct`, `Tri_AddGallery`, `Tri_AddUserDetail`) và Stored Procedure `AddCart`.
4. **Đánh giá tính tương thích và trải nghiệm người dùng (UI/UX & Compatibility):**
   - Đảm bảo bố cục hiển thị Responsive mượt mà trên Desktop, Tablet và Mobile.
   - Đảm bảo tương thích trên 3 trình duyệt phổ biến: Google Chrome, Microsoft Edge, Mozilla Firefox.

### 2.2. Chỉ số KPI & Đo lường kiểm thử
* **Tỷ lệ bao phủ kiểm thử đơn vị (Unit Test Coverage):** Đạt tối thiểu **≥ 70%** cho các lớp nghiệp vụ lõi (`ProductExts`, `CartExts`, `ProductsExts`, `Helpers`).
* **Tỷ lệ thực thi kịch bản (Execution Rate):** Đạt **100%** kịch bản kiểm thử đã được phê duyệt.
* **Tỷ lệ đạt chuẩn (Pass Rate):** Đạt tối thiểu **≥ 95%** trên tổng số Test Cases thực thi.
* **Tồn đọng lỗi (Defect Leakage):** **0 lỗi mức Critical (Nghiêm trọng)** và **0 lỗi mức High (Mức cao)** còn tồn đọng trước khi ký biên bản bàn giao.

---

## 3. Phạm vi Kiểm thử (Test Scope)

### 3.1. Hạng mục trong phạm vi (In-Scope)

| STT | Phân hệ (Module) | Chi tiết các chức năng kiểm thử |
| :---: | :--- | :--- |
| **1** | **Xác thực & Ủy quyền (Auth)** | - Đăng ký tài khoản mới (`/Auth/SignUp`), kiểm tra định dạng email bằng `Helpers.IsValidEmail`, kiểm tra mật khẩu tối thiểu 6 ký tự.<br>- Đăng nhập (`/Auth/SignIn`), đối chiếu tài khoản, xác thực mật khẩu BCrypt, thiết lập Session (`UserId`, `Email`, `RoleName`).<br>- Đăng xuất (`/Auth/Logout`), xóa sạch Session (`Session.Clear()`). |
| **2** | **Danh mục & Sản phẩm (Products)** | - Trang chủ hiển thị danh sách sản phẩm còn hàng (`Stock > 0`), sản phẩm giảm giá/nổi bật.<br>- Tìm kiếm sản phẩm theo tiêu đề (Search Action) với từ khóa chuẩn và từ khóa chứa ký tự đặc biệt.<br>- Lọc đồng thời theo Danh mục (Category) và Thương hiệu (Brand).<br>- Phân trang PagedList (mặc định 8 sản phẩm/trang).<br>- Xem trang chi tiết sản phẩm: thông số kỹ thuật, hình ảnh chính, ảnh phụ gallery, tính toán giá khuyến mãi (`PromoPrice`) và phần trăm giảm giá. |
| **3** | **Giỏ hàng & Thanh toán (Cart & CheckOut)** | - Thêm sản phẩm vào giỏ hàng (yêu cầu đăng nhập, gọi SP `AddCart`, tăng số lượng nếu đã tồn tại).<br>- Xem giỏ hàng, tính tổng tiền tạm tính (`FormattedPrice`).<br>- Cập nhật số lượng sản phẩm trong giỏ.<br>- Xóa sản phẩm khỏi giỏ hàng (kiểm tra đặc biệt lỗi DEF-01).<br>- Điều hướng trang CheckOut, nhập thông tin nhận hàng và xác nhận đặt hàng. |
| **4** | **Hồ sơ & Tài khoản (UserAccount)** | - Xem và cập nhật thông tin cá nhân: Họ tên, Giới tính, Ngày sinh, Số điện thoại, Địa chỉ.<br>- Đổi mật khẩu: Xác thực mật khẩu cũ (BCrypt), xác nhận mật khẩu mới trùng khớp và đạt độ dài quy định. |
| **5** | **Quản trị hệ thống (Admin & Employee)** | - Quản lý sản phẩm: Thêm mới sản phẩm kèm ảnh chính và ảnh phụ, kiểm tra tính hợp lệ của file ảnh qua `Helpers.IsValidImage`, lưu file GUID vào `Public/Imgs/Products/`.<br>- Sửa thông tin sản phẩm, cập nhật hình ảnh.<br>- Xóa sản phẩm khỏi hệ thống.<br>- Quản lý thương hiệu (`BrandsController`) & danh mục (`CategoriesController`).<br>- Quản trị người dùng (Admin Only): Xem danh sách phân trang, thêm tài khoản quản trị/nhân viên, đổi vai trò, xóa người dùng. |
| **6** | **Kiểm thử đơn vị (Unit Testing)** | - Dự án `Store.Tests` sử dụng MSTest kiểm tra các phương thức mở rộng (`ProductExts`, `ProductsExts`, `CartExts`) và các tiện ích trong `Helpers.cs`. |
| **7** | **Xử lý ngoại lệ & Ghi log (Logging)** | - Xác nhận các ngoại lệ hệ thống được bắt trong khối `try-catch` và ghi log chi tiết vào file `Store EF/Logs/dd-MM-yyyy.txt` thông qua Serilog. |

### 3.2. Hạng mục ngoài phạm vi (Out-of-Scope)
* Tích hợp cổng thanh toán trực tuyến thực tế (VNPay, Momo, PayPal, ZaloPay - chỉ kiểm thử form nhập liệu CheckOut).
* Kiểm thử tải và kiểm thử hiệu năng ở quy mô lớn (Stress Testing, Load Testing > 10.000 concurrent users).
* Ứng dụng di động bản địa (Native Mobile App iOS / Android - chỉ kiểm thử Web Responsive trên thiết bị di động).
* Kiểm thử thâm nhập an ninh mạng chuyên sâu cấp hạ tầng máy chủ (Network Infrastructure Penetration Testing).

### 3.3. Ma trận tính năng & Mức độ ưu tiên kiểm thử (Feature Priority Matrix)

| STT | Phân hệ | Tên tính năng | Mức độ ưu tiên | Kỹ thuật kiểm thử áp dụng |
| :---: | :--- | :--- | :---: | :--- |
| **1** | Auth | Đăng ký tài khoản (Sign Up) | **Cao (High)** | FT, EP, BVA, Validation |
| **2** | Auth | Đăng nhập hệ thống (Sign In) | **Khẩn cấp (Critical)** | FT, Security (BCrypt), Session Test |
| **3** | Auth | Đăng xuất & Hủy phiên (Logout) | **Trung bình (Medium)** | FT, Session Management |
| **4** | Products | Danh sách sản phẩm & Phân trang | **Cao (High)** | FT, UI/UX, BVA (MaxPage) |
| **5** | Products | Tìm kiếm sản phẩm (Search) | **Cao (High)** | FT, Robustness (Regex Injection) |
| **6** | Products | Lọc theo Brand & Category | **Cao (High)** | FT, Decision Table Testing |
| **7** | Products | Xem chi tiết sản phẩm | **Trung bình (Medium)** | FT, Business Logic Verification |
| **8** | Cart | Thêm sản phẩm vào giỏ hàng | **Khẩn cấp (Critical)** | FT, Integration (SP AddCart) |
| **9** | Cart | Cập nhật số lượng & Xóa giỏ | **Khẩn cấp (Critical)** | FT, Defect Verification (DEF-01) |
| **10** | CheckOut | Nhập thông tin & Đặt hàng | **Cao (High)** | FT, Form Validation, Defect (DEF-03) |
| **11** | User | Cập nhật hồ sơ cá nhân | **Trung bình (Medium)** | FT, Database Verification |
| **12** | User | Đổi mật khẩu tài khoản | **Cao (High)** | FT, Security, BCrypt Verify |
| **13** | Admin/Emp | Thêm/Sửa/Xóa Sản phẩm & Upload ảnh | **Cao (High)** | FT, File Upload Security, Trigger Check |
| **14** | Admin | Quản lý người dùng & Phân quyền | **Khẩn cấp (Critical)** | FT, Security (RBAC Matrix) |

---

## 4. Chiến lược & Phương pháp Kiểm thử (Test Strategy)

Chiến lược kiểm thử áp dụng mô hình **Kiểm thử gia tăng (Incremental Testing)** kết hợp kiểm thử từ dưới lên (Bottom-up Unit Testing) và kiểm thử chức năng tổng thể từ đầu cuối đến đầu cuối (End-to-End Functional Testing).

### 4.1. Cấp độ kiểm thử (Testing Levels)
1. **Kiểm thử đơn vị (Unit Testing - UT):**
   - Được xây dựng trên framework **MSTest** (Visual Studio Test Explorer) tại dự án `Store.Tests`.
   - Tập trung vào các thuật toán tính toán giá, chiết khấu, phân trang và hàm kiểm tra hợp lệ:
     * `ProductExts.IsValid(Product p)`: Kiểm tra độ dài tiêu đề (`Title.Length >= 3`), giá trị tồn kho (`Stock >= 0`), giá tiền (`Price >= 1000`).
     * `ProductExts.FormattedPrice(Product p, int quantity)`: Kiểm tra định dạng tiền tệ Việt Nam (`100.000 ₫`), trường hợp có/không có giá khuyến mãi (`PromoPrice`), trường hợp `quantity` đặc biệt (1, 0, số âm, số lớn).
     * `ProductExts.DiscountPercentage(Product p)`: Kiểm tra công thức phần trăm giảm giá khi `PromoPrice < Price`, khi `PromoPrice == null`, khi `PromoPrice >= Price`.
     * `ProductsExts.MaxPage(int totalCount, int pageSize)`: Kiểm tra số trang khi tổng sản phẩm bằng 0, chia hết, chia có dư, kích thước trang âm hoặc bằng 0.
     * `Helpers.IsValidEmail(string email)`: Kiểm tra chuỗi email hợp lệ, email thiếu ký tự `@`, thiếu domain, chứa khoảng trắng.
     * `Helpers.IsValidImage(HttpPostedFileBase file)`: Kiểm tra định dạng ảnh hợp lệ (PNG, JPEG), phát hiện file giả mạo đuôi ảnh (file .exe/.txt đổi đuôi thành .jpg).
2. **Kiểm thử tích hợp (Integration Testing - IT):**
   - Kiểm tra sự tương tác giữa Controller với `StoreEntities` DbContext (Entity Framework).
   - Kiểm tra các ràng buộc toàn vẹn và Trigger trong CSDL:
     * Trigger `Tri_AddProduct`: Tự động tạo bản ghi `Gallery` với `IsPrimary = 1` khi tạo sản phẩm mới.
     * Trigger `Tri_AddGallery`: Rollback giao dịch nếu gán nhiều hơn một hình ảnh chính cho cùng một sản phẩm.
     * Trigger `Tri_AddUserDetail`: Tự động tạo thông tin `UserDetail` với tên mặc định từ email khi người dùng mới đăng ký.
     * Stored Procedure `AddCart`: Thêm mới khi chưa có và tăng số lượng khi đã tồn tại.
3. **Kiểm thử hệ thống & Chức năng (System & Functional Testing - FT):**
   - Kiểm thử thủ công theo quy trình nghiệp vụ trên giao diện web thực tế (Black-box Testing).
4. **Kiểm thử chấp nhận (User Acceptance Testing - UAT):**
   - Đánh giá khả năng đáp ứng theo kịch bản trải nghiệm người dùng thực tế từ lúc tìm kiếm đến lúc đặt hàng.

### 4.2. Các loại hình kiểm thử áp dụng (Testing Types)
* **Kiểm thử chức năng (Functional Testing):** Kiểm tra tính đúng đắn của từng nút bấm, form nhập liệu, đường dẫn liên kết và dữ liệu hiển thị.
* **Kiểm thử bảo mật (Security Testing):**
  - **Kiểm tra phân quyền (RBAC Testing):** Người dùng có vai trò `User` hoặc `Guest` gõ trực tiếp URL quản trị (`/Products/ProductManagement`, `/UserAccount/ManageUsers`) phải bị hệ thống chặn truy cập.
  - **Mã hóa mật khẩu:** Kiểm tra trực tiếp bảng `User@` trong CSDL để đảm bảo mật khẩu được băm an toàn qua thuật toán BCrypt.
  - **Session Management:** Kiểm tra việc xóa sạch phiên làm việc khi người dùng nhấn Đăng xuất (`Session.Clear()`), ngăn chặn quay lại trang cũ qua nút Back trình duyệt.
  - **SQL Injection & XSS:** Thử nghiệm đưa các đoạn mã độc hại vào ô tìm kiếm sản phẩm và các trường form thông tin.
* **Kiểm thử tương thích (Compatibility Testing):**
  - Trình duyệt: Google Chrome, Microsoft Edge, Mozilla Firefox.
  - Thiết bị: Kiểm tra hiển thị Responsive trên Desktop (1920x1080), Tablet (768x1024) và Mobile (375x667, 360x800).
* **Kiểm thử xử lý ngoại lệ (Exception Handling & Robustness Testing):**
  - Kiểm tra các tình huống nhập dữ liệu sai hoặc lỗi phát sinh: Hệ thống không được hiển thị "Màn hình vàng chết chóc" (Yellow Screen of Death) của ASP.NET làm lộ mã nguồn.
  - Kiểm tra xem Serilog có ghi nhận đầy đủ stack trace vào thư mục `Store EF/Logs/` hay không.

### 4.3. Kỹ thuật thiết kế kịch bản kiểm thử (Test Design Techniques)
* **Phân vùng tương đương (Equivalence Partitioning):** Áp dụng cho các trường Email, Mật khẩu, Số điện thoại, Giá sản phẩm, Số lượng tồn kho.
* **Phân tích giá trị biên (Boundary Value Analysis):** Áp dụng cho độ dài mật khẩu (biên 6 ký tự: 5, 6, 7), độ dài tên sản phẩm (biên 3 ký tự: 2, 3, 4), số lượng giỏ hàng, số trang hiển thị.
* **Bảng quyết định (Decision Table):** Áp dụng cho Ma trận phân quyền (Role vs. URL Action) và bộ lọc sản phẩm kết hợp nhiều điều kiện (Danh mục x Thương hiệu).
* **Kiểm thử chuyển trạng thái (State Transition Testing):** Áp dụng cho quy trình vòng đời giỏ hàng và đơn hàng.

### 4.4. Kiểm thử các khuyết tật & Lỗ hổng đã nhận diện (Known Defect Analysis)
Dựa trên phân tích mã nguồn trong tài liệu tổng quan dự án, đội ngũ kiểm thử đã thiết lập các kịch bản kiểm thử chuyên biệt để xác nhận và lập báo cáo lỗi (Defect Report) cho các vấn đề sau:

| Mã Bug | Vị trí phát hiện | Mô tả lỗi thực tế (Actual Bug) | Hành vi kỳ vọng (Expected) | Mức độ nghiêm trọng |
| :---: | :--- | :--- | :--- | :---: |
| **DEF-01** | `CartController.cs` (Dòng 76) | Khi gọi Action `Remove` với `confirm = true`, mã nguồn đang thực thi lệnh `store.Products.Remove(p)` dẫn tới **xóa vĩnh viễn sản phẩm khỏi bảng Product trong CSDL** thay vì xóa giỏ hàng! | Hệ thống chỉ được xóa bản ghi của người dùng trong bảng `Cart`, sản phẩm gốc trong bảng `Product` phải giữ nguyên. | **Critical (Khẩn cấp)** |
| **DEF-02** | `ProductsController.cs` (`Search` Action) | Sử dụng `Regex.IsMatch(c.Title.ToLower(), $"({product})")` mà không xử lý Escape ký tự. Khi người dùng tìm kiếm chứa các ký tự đặc biệt như `(`, `[`, `*`, `\`, hệ thống sẽ ném ngoại lệ chưa được xử lý và làm sập trang. | Hệ thống phải xử lý an toàn chuỗi tìm kiếm hoặc dùng `Contains()` / `Regex.Escape()`, không gây crash ứng dụng. | **High (Cao)** |
| **DEF-03** | `CheckOutController.cs` (`CheckOut` Action) | Action CheckOut mới chỉ trả về View giao diện, chưa cài đặt mã xử lý lưu dữ liệu đơn hàng vào bảng `Order@` và `OrderDetail`. | Sau khi bấm Đặt hàng, dữ liệu đơn hàng phải được lưu vào CSDL và xóa sạch giỏ hàng tương ứng. | **High (Cao)** |
| **DEF-04** | `ProductsController.cs`, `UserAccountController.cs` | Các Action quản trị chưa có thuộc tính lọc phân quyền kiểm tra Role trong Session, dẫn tới nguy cơ người dùng vai trò `User` có thể truy cập nếu biết URL. | Áp dụng Authorization Filter chặt chẽ, chỉ cho phép vai trò tương ứng theo đúng Ma trận phân quyền. | **High (Cao)** |

---

## 5. Môi trường Kiểm thử (Test Environment)

### 5.1. Cấu hình phần cứng & Phần mềm
* **Phần cứng kiểm thử:**
  - Vi xử lý: Tối thiểu Intel Core i3 / AMD Ryzen 3 (Khuyến nghị Core i5 trở lên).
  - Bộ nhớ RAM: Tối thiểu 8 GB RAM (Khuyến nghị 16 GB).
  - Ổ cứng: Tối thiểu 20 GB dung lượng trống chuẩn SSD.
* **Phần mềm máy chủ & Môi trường thực thi:**
  - Hệ điều hành: Windows 10 / Windows 11 (64-bit).
  - Nền tảng thực thi: Microsoft .NET Framework 4.7.2.
  - Máy chủ web: IIS Express (chạy trên cổng `http://localhost:5000`).
  - Hệ quản trị CSDL: Microsoft SQL Server LocalDB (`MSSQLLocalDB`, Tên DB: `Store`).
  - Trình biên dịch: Roslyn C# Compiler (csc.exe v4.1.0).

### 5.2. Cấu hình Cơ sở dữ liệu & Ứng dụng
1. **Khởi động dịch vụ SQL LocalDB:**
   ```cmd
   sqllocaldb start MSSQLLocalDB
   ```
2. **Nạp CSDL và dữ liệu mẫu:**
   Sử dụng tiện ích `sqlcmd` thực thi file script chuẩn:
   ```cmd
   sqlcmd -S "(localdb)\MSSQLLocalDB" -i "Store.sql"
   ```
3. **Cấu hình kết nối trong `Store EF/Web.config`:**
   ```xml
   <connectionStrings>
     <add name="StoreEntities" 
          connectionString="metadata=res://*/Models.StoreDb.csdl|res://*/Models.StoreDb.ssdl|res://*/Models.StoreDb.msl;provider=System.Data.SqlClient;provider connection string=&quot;data source=(localdb)\MSSQLLocalDB;Initial Catalog=Store;Integrated Security=True;MultipleActiveResultSets=True;App=EntityFramework&quot;" 
          providerName="System.Data.EntityClient" />
   </connectionStrings>
   ```
4. **Khởi chạy ứng dụng:**
   - Chạy nhanh bằng cách nhấp đúp file `run.bat` tại thư mục gốc. Script sẽ tự động bật LocalDB, gọi `build.ps1` biên dịch mã nguồn và khởi chạy IIS Express tại `http://localhost:5000`.

### 5.3. Công cụ kiểm thử & Quản lý lỗi
* **Kiểm thử đơn vị:** Visual Studio Test Explorer, MSTest Framework.
* **Kiểm thử thủ công & API:** Google Chrome DevTools, Postman.
* **Kiểm thử tương thích:** Microsoft Edge, Mozilla Firefox, Chrome Responsive Mode.
* **Quản lý Test Cases & Lỗi:** Microsoft Excel, Jira, GitHub Issues hoặc Trello.
* **Theo dõi nhật ký hệ thống:** Notepad++, đọc file log hàng ngày tại `Store EF/Logs/dd-MM-yyyy.txt`.

### 5.4. Dữ liệu kiểm thử & Tài khoản kiểm thử chuẩn
Hệ thống sử dụng các tài khoản thử nghiệm được nạp sẵn từ script `Store.sql` (Mật khẩu mặc định chung: `123456`):

| STT | Địa chỉ Email | Mật khẩu mặc định | Vai trò (Role) | Mục đích kiểm thử |
| :---: | :--- | :---: | :---: | :--- |
| **1** | `admin1@example.com` | `123456` | **Admin** | Kiểm thử quyền quản trị cao nhất, quản lý người dùng, phân quyền |
| **2** | `admin2@example.com` | `123456` | **Admin** | Kiểm thử quản trị viên thứ hai (kiểm tra phân trang, bảo vệ tài khoản admin) |
| **3** | `employee1@example.com` | `123456` | **Employee** | Kiểm thử quyền nhân viên (thêm/sửa sản phẩm, upload ảnh, thêm danh mục) |
| **4** | `user1@example.com` | `123456` | **User** | Kiểm thử luồng khách hàng mua sắm, giỏ hàng, cập nhật thông tin cá nhân |
| **5** | `user2@example.com` | `123456` | **User** | Kiểm thử dữ liệu độc lập giữa các tài khoản người dùng khác nhau |

---

## 6. Nguồn lực, Phân công & Vai trò (Resources & Roles)

### 6.1. Đội ngũ nhân sự dự kiến
* **01 Test Manager / QA Lead:** Lập kế hoạch kiểm thử, phân công công việc, rà soát Test Cases, điều phối cuộc họp Bug Triage và phê duyệt báo cáo nghiệm thu.
* **02 Manual Test Engineers:** Phân tích tài liệu yêu cầu, thiết kế bộ Test Cases chi tiết, chuẩn bị dữ liệu test, thực thi kiểm thử chức năng, giao diện, tương thích, bảo mật và ghi nhận lỗi.
* **01 Unit Test / Automation Engineer:** Xây dựng và thực thi các bài kiểm thử đơn vị trên MSTest (`Store.Tests`), đo lường độ bao phủ mã nguồn (Code Coverage).
* **01 Developer Support:** Phối hợp thiết lập môi trường, giải thích kiến trúc mã nguồn và tiến hành sửa lỗi khi nhận defect report.

### 6.2. Ma trận trách nhiệm (RACI Matrix)

| Hoạt động kiểm thử | Test Manager | Manual Tester | Unit Test Engineer | Developer |
| :--- | :---: | :---: | :---: | :---: |
| Xây dựng & Cập nhật Test Plan | **A / R** | C | C | I |
| Thiết kế Test Cases (Chức năng, Bảo mật, UI) | A | **R** | C | I |
| Xây dựng kịch bản Unit Test (MSTest) | A | I | **R** | C |
| Thiết lập môi trường kiểm thử & Seed DB | C | R | R | **A** |
| Thực thi kiểm thử chức năng & Giao diện | A | **R** | I | I |
| Thực thi Unit Test & Đo Code Coverage | A | I | **R** | C |
| Báo cáo khiếm khuyết (Defect Logging) | A | **R** | **R** | I |
| Sửa lỗi phần mềm (Bug Fixing) | I | I | I | **A / R** |
| Kiểm thử lại (Retest) & Kiểm thử hồi quy | A | **R** | R | I |
| Tổng kết & Phê duyệt Test Summary Report | **A / R** | C | C | I |

*(Ghi chú: A = Accountable, R = Responsible, C = Consulted, I = Informed)*

---

## 7. Lịch trình & Các cột mốc (Schedule & Milestones)

Chu kỳ kiểm thử được lập kế hoạch thực hiện trong **4 tuần** (20 ngày làm việc):

| Cột mốc | Giai đoạn | Hoạt động chính | Sản phẩm đầu ra (Deliverable) | Thời gian |
| :--- | :---: | :--- | :--- | :---: |
| **M1: Khởi động** | Tuần 1 | - Họp kick-off, phân tích yêu cầu từ `PROJECT_OVERVIEW.md`.<br>- Thiết lập môi trường kiểm thử: LocalDB, Visual Studio, IIS Express.<br>- Hoàn thiện và phê duyệt Test Plan. | - Tài liệu Kế hoạch Kiểm thử (`TEST_PLAN.md` / `.docx`).<br>- Môi trường kiểm thử sẵn sàng hoạt động. | Tuần 1 (Ngày 1-5) |
| **M2: Thiết kế** | Tuần 2 | - Thiết kế chi tiết bộ Test Cases cho các phân hệ: Auth, Products, Cart, CheckOut, UserAccount, Admin.<br>- Thiết kế kịch bản Unit Test (MSTest) cho `ProductExts`, `CartExts`, `Helpers`.<br>- Chuẩn bị dữ liệu kiểm thử (Test Data). | - Tài liệu Đặc tả Kịch bản Kiểm thử (Test Cases Specification).<br>- Bộ mã nguồn Unit Test trong dự án `Store.Tests`. | Tuần 2 (Ngày 6-10) |
| **M3: Thực thi** | Tuần 3 | - Thực thi toàn bộ Test Cases chức năng trên Web UI (Test Cycle 1).<br>- Chạy Unit Test suite, đo lường Code Coverage.<br>- Kiểm thử xác nhận các lỗi đã nhận diện (DEF-01, DEF-02, DEF-03, DEF-04).<br>- Ghi nhận defect vào hệ thống theo dõi lỗi.<br>- Họp Bug Triage hàng ngày với Dev để thống nhất tiến độ fix bug. | - Danh sách lỗi phát hiện (Defect Log).<br>- Báo cáo tiến độ thực thi kiểm thử hàng ngày. | Tuần 3 (Ngày 11-15) |
| **M4: Đánh giá** | Tuần 4 | - Kiểm thử lại (Retest) các defect đã được Developer sửa.<br>- Chạy kiểm thử hồi quy (Regression Testing) toàn bộ luồng nghiệp vụ cốt lõi.<br>- Kiểm thử tương thích đa trình duyệt lần cuối.<br>- Lập Báo cáo Tổng kết Kiểm thử (Test Summary Report) và bàn giao. | - Báo cáo Tổng kết Kiểm thử (Test Summary Report).<br>- Biên bản nghiệm thu chất lượng phần mềm. | Tuần 4 (Ngày 16-20) |

### Kế hoạch Kiểm thử Hồi quy (Regression Testing Plan)
* **Thời điểm:** Tuần 4, ngay sau khi Developer bàn giao bản build khắc phục các defect.
* **Phạm vi hồi quy:**
  1. Tự động chạy lại 100% các bài Unit Test trong `Store.Tests`.
  2. Thực thi lại toàn bộ kịch bản Happy Path: Đăng ký -> Đăng nhập -> Chọn sản phẩm -> Giỏ hàng -> Đổi mật khẩu.
  3. Kiểm tra chuyên sâu vùng mã nguồn vừa sửa đổi (đặc biệt là Action `CartController.Remove` và Action `ProductsController.Search`).

---

## 8. Tiêu chí Chấp nhận (Acceptance Criteria)

### 8.1. Tiêu chí bắt đầu (Entry Criteria)
* Kế hoạch Kiểm thử (Test Plan) đã được Test Manager phê duyệt.
* Mã nguồn dự án được build thành công không lỗi (0 Build Errors) bằng `build.ps1` hoặc Visual Studio.
* Cơ sở dữ liệu `Store` đã được khởi tạo thành công trên LocalDB thông qua script `Store.sql`.
* Ứng dụng web chạy ổn định trên IIS Express tại cổng `http://localhost:5000`.
* Đội ngũ kiểm thử đã được phân quyền và sẵn sàng thực thi nhiệm vụ.

### 8.2. Tiêu chí tạm dừng & Tiếp tục (Suspension & Resumption Criteria)
* **Tiêu chí tạm dừng (Suspension Criteria):**
  - Xuất hiện lỗi nghiêm trọng (Blocker) ở luồng cốt lõi khiến ứng dụng sập ngay từ trang chủ hoặc trang đăng nhập.
  - Cơ sở dữ liệu hoặc kết nối Entity Framework bị hỏng trên diện rộng không thể đọc/ghi dữ liệu.
  - Tỷ lệ lỗi chặn kiểm thử vượt quá 30% số lượng test cases dự kiến thực hiện trong ngày.
* **Tiêu chí tiếp tục (Resumption Criteria):**
  - Developer đã khắc phục triệt để lỗi Blocker và bàn giao bản build mới ổn định.
  - Cơ sở dữ liệu được khôi phục trạng thái chuẩn bằng script `Store.sql`.

### 8.3. Tiêu chí kết thúc kiểm thử (Exit Criteria)
* **100%** Test Cases được phê duyệt đã được thực thi đầy đủ.
* Tỷ lệ Test Case thành công (Pass Rate) đạt tối thiểu **≥ 95%**.
* **0 (không)** lỗi mức Critical (Nghiêm trọng) hoặc High (Cao) còn tồn đọng.
* Lỗi mức Medium (Trung bình) không quá 3 lỗi và đã có kế hoạch xử lý ở phiên bản bảo trì.
* Tỷ lệ bao phủ kiểm thử đơn vị (Unit Test Coverage) đạt tối thiểu **≥ 70%** cho các lớp nghiệp vụ lõi.
* Báo cáo tổng kết kiểm thử (Test Summary Report) đã được Test Manager rà soát và phê duyệt chính thức.

---

## 9. Quy trình Quản lý Lỗi & Sản phẩm bàn giao (Defects & Deliverables)

### 9.1. Quy trình xử lý lỗi (Defect Life Cycle)
Vòng đời của một lỗi phát hiện trong quá trình kiểm thử tuân theo các trạng thái chuẩn:
1. **New (Mới):** Tester phát hiện lỗi, ghi nhận vào hệ thống kèm các bước tái hiện và bằng chứng.
2. **Assigned (Phân công):** QA Lead xem xét tính hợp lệ và phân công cho Developer chịu trách nhiệm module đó.
3. **Open (Đang mở):** Developer xác nhận lỗi và bắt đầu tiến hành phân tích nguyên nhân.
4. **Fixed (Đã sửa):** Developer hoàn thành việc sửa mã nguồn và bàn giao bản build mới cho QA.
5. **Retesting (Đang test lại):** Tester thực thi lại kịch bản kiểm thử trên bản build đã sửa lỗi.
6. **Verified / Closed (Đã xác minh / Đóng):** Tester xác nhận lỗi đã được khắc phục hoàn toàn và đóng defect.
7. **Reopened (Mở lại):** Nếu lỗi vẫn còn tái diễn sau khi test lại, tester chuyển trạng thái sang Reopened kèm phản hồi chi tiết.

### 9.2. Phân loại mức độ nghiêm trọng & Mức độ ưu tiên
* **Mức độ nghiêm trọng (Severity):**
  - **S1 - Critical (Khẩn cấp):** Ứng dụng bị sập, mất mát dữ liệu, vi phạm bảo mật nghiêm trọng (ví dụ: `DEF-01` xóa nhầm sản phẩm khỏi CSDL).
  - **S2 - High (Cao):** Tính năng nghiệp vụ chính bị lỗi, không có phương án thay thế (ví dụ: Tìm kiếm ký tự đặc biệt gây crash, tính sai tiền).
  - **S3 - Medium (Trung bình):** Tính năng phụ hoạt động sai lệch, nhưng người dùng vẫn có thể hoàn tất công việc bằng cách khác.
  - **S4 - Low (Thấp):** Lỗi giao diện, sai chính tả, lệch khoảng cách bố cục UI.
* **Mức độ ưu tiên (Priority):**
  - **P1 - High:** Yêu cầu Developer sửa ngay lập tức trong vòng 24 giờ.
  - **P2 - Medium:** Sửa trong bản build tiếp theo trong tuần.
  - **P3 - Low:** Sửa khi có thời gian hoặc chuyển sang chu kỳ nâng cấp kế tiếp.

### 9.3. Danh mục sản phẩm bàn giao (Test Deliverables)
1. **Tài liệu Kế hoạch Kiểm thử (Test Plan):** Bản kế hoạch toàn diện (File `TEST_PLAN.md` và `Test_Plan_StoreEF.docx`).
2. **Bộ Đặc tả Kịch bản Kiểm thử (Test Cases Specification):** Danh sách toàn bộ các Test Cases chi tiết (ID, Tiêu đề, Dữ liệu đầu vào, Các bước thực hiện, Kết quả mong đợi, Trạng thái Pass/Fail).
3. **Mã nguồn Unit Test (Unit Test Code):** Dự án `Store.Tests` trên nền tảng MSTest.
4. **Báo cáo Lỗi (Defect Report / Bug Log):** Danh mục toàn bộ lỗi phát hiện, mức độ nghiêm trọng, trạng thái xử lý và ảnh chụp bằng chứng.
5. **Báo cáo Tổng kết Kiểm thử (Test Summary Report):** Báo cáo đánh giá tổng thể chất lượng phần mềm, thống kê kết quả thực thi và khuyến nghị phát hành.

---

## 10. Rủi ro & Kế hoạch Dự phòng (Risks & Mitigation Plan)

| STT | Rủi ro nhận diện (Risk) | Khả năng | Tác động | Kế hoạch dự phòng & Giảm thiểu (Mitigation) |
| :---: | :--- | :---: | :---: | :--- |
| **R1** | **Lỗi phân quyền thư mục tải ảnh:** Ứng dụng không ghi được ảnh do thư mục `Store EF/Public/Imgs/Products/` bị khóa quyền ghi. | Trung bình | **Cao** | Kiểm tra và cấp quyền ghi đầy đủ (Full Write Permissions) cho nhóm `IIS_IUSRS` / `Users` trên thư mục ngay từ giai đoạn M1. |
| **R2** | **Xung đột chuỗi kết nối CSDL (Connection String):** Khác biệt tên instance SQL Server giữa các máy dev/test. | Cao | **Trung bình** | Chuẩn hóa quy trình sử dụng script `run.bat` tự động kết nối `(localdb)\MSSQLLocalDB` mặc định; hướng dẫn cấu hình `Web.config` chi tiết trong tài liệu. |
| **R3** | **Dữ liệu mẫu bị phá hủy do lỗi DEF-01:** Thao tác test xóa giỏ hàng vô tình xóa mất sản phẩm trong bảng `Product`. | Cao | **Cao** | Luôn chuẩn bị sẵn lệnh chạy tự động script `Store.sql` để nhanh chóng khôi phục CSDL về trạng thái sạch chỉ trong vài giây. |
| **R4** | **Thiếu thời gian hoàn thiện Unit Test cho Controller:** Khó khăn khi giả lập `HttpContext`, `Session` và `DbContext`. | Cao | **Trung bình** | Tập trung nguồn lực Unit Test vào các hàm nghiệp vụ độc lập (`ProductExts`, `CartExts`, `Helpers`), Controller chỉ kiểm thử các kịch bản cơ bản (Happy Path). |
| **R5** | **Sập ứng dụng khi tìm kiếm ký tự đặc biệt (DEF-02):** Tester nhập ký tự regex làm dừng chu trình kiểm thử module tìm kiếm. | Trung bình | **Trung bình** | Ghi nhận bug mức High, ghi nhận vết lỗi trong `Logs/dd-MM-yyyy.txt`, tạm thời kiểm thử tính năng lọc theo danh mục/thương hiệu trong khi chờ Dev fix. |
| **R6** | **Tính năng CheckOut chưa lưu dữ liệu vào CSDL (DEF-03):** Không thể kiểm tra luồng hoàn tất đơn hàng và trừ tồn kho. | Chắc chắn (100%) | **Trung bình** | Kiểm thử form CheckOut ở mức độ client-side validation và UI response, ghi nhận bug để Dev bổ sung nghiệp vụ lưu `Order@` và `OrderDetail`. |

---

## PHỤ LỤC: MA TRẬN KỊCH BẢN KIỂM THỬ MẪU (SAMPLE TEST CASES OUTLINE)

| Mã Test Case | Phân hệ | Tên kịch bản | Dữ liệu đầu vào | Kết quả mong đợi |
| :--- | :--- | :--- | :--- | :--- |
| `TC_AUTH_01` | Auth | Đăng ký thành công với dữ liệu hợp lệ | Email: `newuser@store.test`<br>Mật khẩu: `Abc@123456` | Đăng ký thành công, tự động tạo `UserDetail` với tên `newuser`, mật khẩu được băm BCrypt trong CSDL. |
| `TC_AUTH_02` | Auth | Đăng ký thất bại do email đã tồn tại | Email: `user1@example.com` (đã có) | Hiển thị thông báo lỗi "Email đã được sử dụng", không cho phép đăng ký. |
| `TC_AUTH_03` | Auth | Đăng ký thất bại do mật khẩu < 6 ký tự | Mật khẩu: `12345` | Hiển thị thông báo lỗi validation mật khẩu phải có ít nhất 6 ký tự. |
| `TC_AUTH_04` | Auth | Đăng nhập thành công | `user1@example.com` / `123456` | Đăng nhập thành công, lưu Session, hiển thị tên người dùng trên thanh Header. |
| `TC_AUTH_05` | Auth | Đăng xuất người dùng | Nhấp vào nút "Đăng xuất" | Xóa toàn bộ Session, điều hướng về trang `/Auth/SignIn`, không thể nhấn Back để quay lại. |
| `TC_PROD_01` | Products | Tìm kiếm sản phẩm theo tên thông thường | Từ khóa: `Dell` | Hiển thị danh sách các sản phẩm chứa chữ "Dell", phân trang tối đa 8 sản phẩm/trang. |
| `TC_PROD_02` | Products | Kiểm thử tính bền vững ô tìm kiếm (Regex Test) | Từ khóa: `(`, `[`, `*`, `\` | Hệ thống không bị crash hoặc ném lỗi server 500, hiển thị thông báo "Không tìm thấy sản phẩm". |
| `TC_CART_01` | Cart | Thêm sản phẩm khi chưa đăng nhập | Bấm "Thêm vào giỏ" khi là Guest | Chuyển hướng người dùng về trang Đăng nhập (`/Auth/SignIn`). |
| `TC_CART_02` | Cart | Thêm sản phẩm nhiều lần | Bấm thêm sản phẩm A 2 lần | Số lượng sản phẩm A trong giỏ hàng tăng lên thành 2, cập nhật số lượng icon giỏ hàng trên Header. |
| `TC_CART_03` | Cart | Xóa sản phẩm khỏi giỏ hàng (Kiểm tra DEF-01) | Bấm Xóa sản phẩm A khỏi giỏ | Bản ghi trong giỏ hàng bị xóa; kiểm tra trong CSDL sản phẩm A vẫn tồn tại bình thường trong bảng `Product`. |
| `TC_SECU_01` | Security | Người dùng User truy cập URL Quản trị Admin | Gõ URL: `/UserAccount/ManageUsers` | Hệ thống từ chối truy cập, chuyển hướng về trang thông báo lỗi hoặc trang chủ. |
| `TC_UNIT_01` | Unit Test | Kiểm tra hàm `ProductExts.FormattedPrice` | Giá gốc: 10.000.000, Promo: 8.000.000, Qty: 2 | Trả về chuỗi định dạng tiền tệ đúng: `16.000.000 ₫`. |
| `TC_UNIT_02` | Unit Test | Kiểm tra hàm `Helpers.IsValidEmail` | Input: `test@@domain..com` | Trả về `false`. |

---

> **Tài liệu Kế hoạch Kiểm thử được lưu trữ tại:** `Docs/TEST_PLAN.md`  
> **Tài liệu tham chiếu:** `Docs/PROJECT_OVERVIEW.md`  
> **Bản quyền thuộc về:** Đội ngũ Đảm bảo Chất lượng Phần mềm (QA/QC Team) - Ecommerce Computer V3.
