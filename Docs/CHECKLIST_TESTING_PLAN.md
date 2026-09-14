# 📋 BẢNG KIỂM TRA CÔNG VIỆC KIỂM THỬ (TESTING PLAN CHECKLIST)

## BÁO CÁO & ĐỒ ÁN MÔN HỌC: KIỂM THỬ PHẦN MỀM (SOFTWARE TESTING & QA)

> **Dự án thực hành:** Ecommerce Computer (Store EF) V3  
> **Cấu trúc chuẩn:** Theo đề cương đồ án tốt nghiệp / Báo cáo kiểm thử 4 chương  
> **Tài liệu tham chiếu:** `Docs/PROJECT_OVERVIEW.md` & `Docs/TEST_PLAN.md`  
> **Trạng thái tổng quan:** [ ] Đang thực hiện | Tiến độ: 0%

---

## 📌 HƯỚNG DẪN SỬ DỤNG CHECKLIST

- Bảng kiểm tra này liệt kê toàn bộ các công việc chi tiết cần thực hiện theo từng đề mục trong cấu trúc đồ án/báo cáo kiểm thử.
- Đánh dấu `[x]` vào các ô vuông khi hoàn thành từng đầu việc tương ứng.
- Tại mỗi mục đều có phần **Yêu cầu nội dung**, **Công việc cụ thể (Tasks)** và **Sản phẩm đầu ra (Deliverables / Bằng chứng)** cần đính kèm vào báo cáo Word.

---

## PHẦN ĐẦU TÀI LIỆU: BÌA & CÁC DANH MỤC

### [ ] Bìa báo cáo & Trang phụ bìa

- [ ] Thiết kế trang bìa chính đúng quy chuẩn (Tên trường, khoa, môn học, tên đề tài/đồ án, GVHD, SVTH, MSSV, Niên khóa).
- [ ] Thiết kế trang bìa phụ có đầy đủ chữ ký hoặc thông tin xác nhận.
- [ ] Kiểm tra định dạng lề: Trái 3.0cm, Phải 2.0cm, Trên 2.0cm, Dưới 2.0cm.

### [ ] Lời cảm ơn & Lời cam đoan

- [ ] Viết Lời cảm ơn gửi tới Giảng viên hướng dẫn và Bộ môn.
- [ ] Viết Lời cam đoan về tính trung thực của kết quả kiểm thử và số liệu trong đồ án.

### [ ] ii. Mục lục (Table of Contents)

- [ ] Tạo mục lục tự động trong Word (Heading 1, 2, 3, 4).
- [ ] Đánh số trang kiểu La Mã (`i`, `ii`, `iii`,...) cho phần mở đầu đến trước Lời mở đầu.
- [ ] Kiểm tra đồng bộ số trang sau khi hoàn thiện nội dung cuối cùng.

### [ ] v. Danh mục hình (List of Figures)

- [ ] Đánh chỉ số Caption tự động cho tất cả hình ảnh (`Hình 1.1`, `Hình 1.2`, `Hình 2.1`,...).
- [ ] Tạo bảng Danh mục hình tự động từ công cụ _Insert Table of Figures_.
- [ ] Đảm bảo mỗi hình chụp giao diện, biểu đồ kiến trúc, màn hình test đều có chú thích rõ ràng.

### [ ] vi. Danh mục bảng (List of Tables)

- [ ] Đánh chỉ số Caption tự động cho tất cả bảng biểu (`Bảng 1.1`, `Bảng 1.2`, `Bảng 2.1`,...).
- [ ] Tạo bảng Danh mục bảng tự động.
- [ ] Kiểm tra tiêu đề bảng đặt phía trên bảng, căn giữa hoặc lề trái nhất quán.

### [ ] vii. Danh mục chữ viết tắt (List of Abbreviations)

- [ ] Liệt kê và giải nghĩa các thuật ngữ viết tắt: SRS, SUT, RBAC, UT, FT, IT, ST, UAT, EP, BVA, KPI, DEF, GUI, DB, EF.

---

## LỜI MỞ ĐẦU (Trang 1)

- [ ] **Bối cảnh & Tính cấp thiết của đề tài:**
  - [ ] Nêu vai trò then chốt của hoạt động Đảm bảo Chất lượng (QA) và Kiểm thử Phần mềm (Testing) trong quy trình phát triển phần mềm hiện đại (SDLC).
  - [ ] Thực trạng rủi ro bảo mật, lỗi thất thoát doanh thu trong các hệ thống thương mại điện tử nếu không được kiểm thử bài bản.
- [ ] **Lý do lựa chọn hệ thống kiểm thử:**
  - [ ] Giới thiệu website bán hàng công nghệ Ecommerce Computer (Store EF) V3 xây dựng trên nền tảng ASP.NET MVC 5 và Entity Framework 6.
  - [ ] Nêu tính đa dạng của hệ thống: có nghiệp vụ mua bán, giỏ hàng, thanh toán, upload hình ảnh, phân quyền RBAC và các database triggers phức tạp.
- [ ] **Mục đích & Đóng góp của đề tài:**
  - [ ] Nắm vững và vận dụng toàn diện quy trình kiểm thử từ lập kế hoạch, thiết kế test case, kiểm thử tự động đến thực thi và báo cáo defect.
- [ ] **Bố cục của báo cáo:** Tóm tắt ngắn gọn nội dung của 4 chương trong báo cáo.

---

## CHƯƠNG 1. XÂY DỰNG KẾ HOẠCH KIỂM THỬ (Trang 2 - 16)

### 1.1. Giới thiệu hệ thống cần kiểm thử

#### 1.1.1. Mô tả hệ thống

- [ ] Viết mô tả tổng quan về website bán máy tính Ecommerce Computer (Store EF) V3.
- [ ] Vẽ hoặc chèn Sơ đồ kiến trúc hệ thống MVC 5 phân tầng (Presentation, Application, Data Access, Database) từ `PROJECT_OVERVIEW.md`.
- [ ] Trình bày ngăn xếp công nghệ: C# .NET Framework 4.7.2, ASP.NET MVC 5.3.0, EF 6.4.4, SQL Server LocalDB, BCrypt.Net-Next, Serilog, PagedList, Bootstrap 5.
- [ ] Trình bày sơ đồ quan hệ thực thể (ERD) với 10 bảng dữ liệu: `User@`, `UserDetail`, `Brand`, `Category`, `Product`, `Gallery`, `Cart`, `Order@`, `OrderDetail`, `Review`.

#### 1.1.2. Các chức năng chính của hệ thống

- [ ] Phân tích chi tiết chức năng phân hệ Xác thực (Đăng ký, Đăng nhập, Đăng xuất, mã hóa BCrypt).
- [ ] Phân tích chức năng phân hệ Sản phẩm (Hiển thị trang chủ, Danh mục, Thương hiệu, Tìm kiếm Regex, Chi tiết sản phẩm, Tính giá khuyến mãi/giảm giá).
- [ ] Phân tích chức năng phân hệ Giỏ hàng & CheckOut (Thêm/Sửa/Xóa giỏ, Gọi SP `AddCart`, Form đặt hàng).
- [ ] Phân tích chức năng phân hệ Quản lý tài khoản (Xem/Sửa hồ sơ cá nhân, Đổi mật khẩu).
- [ ] Phân tích chức năng phân hệ Quản trị (Admin / Employee: Quản lý sản phẩm kèm upload ảnh, quản lý danh mục/thương hiệu, quản lý người dùng & phân quyền).
- [ ] Lập bảng Ma trận phân quyền truy cập (RBAC Matrix) giữa 4 vai trò: Guest, User, Employee, Admin.

### 1.2. Mục tiêu và phạm vi kiểm thử

#### 1.2.1. Mục tiêu kiểm thử

- [ ] Xác định 5 mục tiêu chất lượng cốt lõi: Xác minh tính đúng đắn luồng nghiệp vụ, Đảm bảo an toàn bảo mật (BCrypt & RBAC), Đảm bảo toàn vẹn dữ liệu (Triggers & SP), Tương thích đa trình duyệt, Kiểm thử độ bền vững ngoại lệ.
- [ ] Xác định các chỉ số KPI: Tỷ lệ thực thi 100%, Tỷ lệ Pass ≥ 95%, Bao phủ Unit Test ≥ 70%, 0 lỗi Critical/High tồn đọng.

#### 1.2.2. Phạm vi kiểm thử

- [ ] Lập bảng danh mục **Trong phạm vi (In-Scope)**: Auth, Products, Cart, CheckOut, UserAccount, Admin Management, Unit Testing trong `Store.Tests`, Logging Serilog.
- [ ] Lập bảng danh mục **Ngoài phạm vi (Out-of-Scope)**: Cổng thanh toán trực tuyến thực tế bên ngoài (VNPAY/Momo), Kiểm thử tải quy mô lớn (>10.000 CCU), Native Mobile App, Tấn công thâm nhập mạng vật lý.

#### 1.2.3. Đối tượng kiểm thử

- [ ] Liệt kê chi tiết các đối tượng cụ thể:
  - [ ] Mã nguồn C# Controller (`AuthController.cs`, `ProductsController.cs`, `CartController.cs`, `CheckOutController.cs`, `UserAccountController.cs`).
  - [ ] Các phương thức mở rộng & nghiệp vụ (`ProductExts.cs`, `CartExts.cs`, `ProductsExts.cs`, `Helpers.cs`).
  - [ ] Giao diện Web (Razor Views `.cshtml`, Form HTML, jQuery Validation).
  - [ ] Tầng Cơ sở dữ liệu: Bảng dữ liệu, Ràng buộc Khóa chính/Khóa ngoại, Trigger `Tri_AddProduct`, `Tri_AddGallery`, `Tri_AddUserDetail`, Stored Procedure `AddCart`.

### 1.3. Kế hoạch kiểm thử

#### 1.3.1. Chiến lược kiểm thử

- [ ] Trình bày chiến lược Kiểm thử gia tăng (Incremental Testing).
- [ ] Mô tả sự kết hợp giữa Kiểm thử từ dưới lên (Bottom-up Unit Testing) và Kiểm thử hộp đen từ đầu cuối đến đầu cuối (End-to-End Functional Testing).

#### 1.3.2. Các mức kiểm thử áp dụng

- [ ] **Kiểm thử đơn vị (Unit Testing):** Trình bày mục tiêu, phạm vi và công cụ MSTest trên dự án `Store.Tests`.
- [ ] **Kiểm thử tích hợp (Integration Testing):** Kiểm tra tích hợp giữa Controller với DbContext, kiểm tra tương tác Database Triggers và Stored Procedure.
- [ ] **Kiểm thử hệ thống (System Testing):** Kiểm thử luồng chức năng người dùng trên toàn bộ website.
- [ ] **Kiểm thử chấp nhận (UAT):** Kiểm tra hành trình khách hàng mua máy tính hoàn chỉnh.

#### 1.3.3. Các loại kiểm thử áp dụng

- [ ] **Kiểm thử chức năng (Functional Testing):** Kiểm tra form nhập liệu, chuyển trang, tính toán đơn hàng.
- [ ] **Kiểm thử bảo mật (Security Testing):** Kiểm tra phân quyền URL, băm mật khẩu BCrypt, Session clear sau Logout, phòng chống SQL Injection và Regex Crash.
- [ ] **Kiểm thử tương thích (Compatibility Testing):** Kiểm tra trên Google Chrome, Microsoft Edge, Mozilla Firefox và hiển thị Responsive trên PC, Tablet, Smartphone.
- [ ] **Kiểm thử ngoại lệ & Bền vững (Robustness & Exception Testing):** Bẫy lỗi không làm lộ màn hình vàng ASP.NET, xác minh ghi file log Serilog.

#### 1.3.4. Phân công nhân sự

- [ ] Lập bảng cơ cấu vai trò dự án: Test Manager, Manual Tester, Unit Test Engineer, Developer Support.
- [ ] Lập bảng Ma trận trách nhiệm RACI cho 10 công việc chính trong dự án.

#### 1.3.5. Lịch trình thực hiện kiểm thử

- [ ] Vẽ Biểu đồ Gantt (Gantt Chart) tiến độ 4 tuần (20 ngày làm việc).
- [ ] Lập bảng chi tiết 4 cột mốc: M1 Khởi động -> M2 Thiết kế -> M3 Thực thi -> M4 Đánh giá & Bàn giao.
- [ ] Trình bày kế hoạch kiểm thử hồi quy (Regression Testing Plan) chi tiết cho tuần 4.

#### 1.3.6. Rủi ro và biện pháp xử lý

- [ ] Lập bảng phân tích 6 rủi ro trọng yếu (R1: Quyền thư mục ảnh, R2: Xung đột Connection String, R3: Mất dữ liệu do lỗi DEF-01, R4: Thiếu thời gian Unit Test Controller, R5: Sập ứng dụng do Regex Crash DEF-02, R6: CheckOut chưa lưu DB DEF-03).
- [ ] Đưa ra biện pháp giảm thiểu và phương án dự phòng chi tiết cho từng rủi ro.

### 1.4. Môi trường và công cụ kiểm thử

#### 1.4.1. Môi trường kiểm thử

- [ ] Bảng cấu hình phần cứng tối thiểu & khuyến nghị (CPU, RAM, SSD).
- [ ] Bảng thông số phần mềm: Windows 10/11 64-bit, .NET Framework 4.7.2, IIS Express (port 5000), LocalDB `MSSQLLocalDB`, Visual Studio 2019/2022.
- [ ] Hướng dẫn thiết lập CSDL qua script `Store.sql` và khởi chạy ứng dụng nhanh qua `run.bat`.
- [ ] Lập bảng danh sách 5 tài khoản thử nghiệm chuẩn (`admin1`, `admin2`, `employee1`, `user1`, `user2`).

#### 1.4.2. Công cụ hỗ trợ kiểm thử

- [ ] Visual Studio Test Explorer (MSTest v1.2.0).
- [ ] Google Chrome DevTools / Responsive Viewport Simulator.
- [ ] Postman (kiểm tra gửi request HTTP).
- [ ] Selenium IDE (ghi và chạy kịch bản kiểm thử tự động).
- [ ] Microsoft Excel / Jira / GitHub Issues (quản lý kịch bản và theo dõi defect).

### 1.5. Tiêu chí đánh giá kết quả kiểm thử

- [ ] Tiêu chí bắt đầu (Entry Criteria).
- [ ] Tiêu chí tạm dừng và tiếp tục kiểm thử (Suspension & Resumption Criteria).
- [ ] Tiêu chí kết thúc kiểm thử (Exit Criteria).

### 1.6. Kết luận chương 1

- [ ] Tóm tắt ngắn gọn các điểm cốt lõi đã xác lập trong Kế hoạch kiểm thử.

---

## CHƯƠNG 2. THIẾT KẾ TEST CASE, TEST DATA (Trang 17 - 100)

### 2.1. Phương pháp thiết kế Test Case

#### 2.1.1. Phân vùng tương đương (Equivalence Partitioning)

- [ ] Trình bày cơ sở lý thuyết kỹ thuật Phân vùng tương đương (Lớp hợp lệ / Không hợp lệ).
- [ ] Bảng minh họa phân vùng cho các trường dữ liệu dự án: Email, Độ dài mật khẩu (>= 6), Giá sản phẩm (>= 1000), Tồn kho (>= 0).

#### 2.1.2. Phân tích giá trị biên (Boundary Value Analysis)

- [ ] Trình bày lý thuyết BVA (Min-, Min, Min+, Nom, Max-, Max, Max+).
- [ ] Bảng xác định giá trị biên: Biên mật khẩu (5, 6, 7 ký tự), Biên tiêu đề sản phẩm (2, 3, 4 ký tự), Biên phân trang MaxPage (0, 1, chia hết, chia dư).

#### 2.1.3. Bảng quyết định (Decision Table)

- [ ] Trình bày lý thuyết Bảng quyết định.
- [ ] Xây dựng Bảng quyết định cho: Phân quyền truy cập chức năng theo vai trò (Guest / User / Employee / Admin) và Bộ lọc sản phẩm kết hợp Danh mục x Thương hiệu.

### 2.2. Thiết kế Test Case và Test Data kiểm thử chức năng

_(Mỗi Test Case cần có: Test Case ID, Phân hệ, Tên kịch bản, Tiền điều kiện, Các bước thực hiện, Dữ liệu đầu vào, Kết quả mong đợi, Mức độ ưu tiên)_

#### 2.2.1. Phân hệ Khách hàng và Tài khoản (Customer & Account)

- [ ] **Chức năng Đăng ký tài khoản (Sign Up):**
  - [ ] TC Đăng ký thành công với thông tin hợp lệ (Email mới, Mật khẩu >= 6 ký tự).
  - [ ] TC Đăng ký thất bại: Bỏ trống Email / Bỏ trống Mật khẩu.
  - [ ] TC Đăng ký thất bại: Email sai định dạng (thiếu `@`, thiếu domain, chứa ký tự lạ).
  - [ ] TC Đăng ký thất bại: Email đã tồn tại trong hệ thống.
  - [ ] TC Đăng ký thất bại: Mật khẩu dưới 6 ký tự (5 ký tự - kiểm thử giá trị biên).
  - [ ] TC Kiểm tra mật khẩu trong DB được mã hóa BCrypt sau khi đăng ký.
  - [ ] TC Kiểm tra tự động tạo bản ghi `UserDetail` qua Trigger `Tri_AddUserDetail`.
- [ ] **Chức năng Đăng nhập (Sign In):**
  - [ ] TC Đăng nhập thành công với tài khoản User hợp lệ.
  - [ ] TC Đăng nhập thành công với tài khoản Admin / Employee.
  - [ ] TC Đăng nhập thất bại: Sai mật khẩu (mật khẩu không khớp hash BCrypt).
  - [ ] TC Đăng nhập thất bại: Email không tồn tại trong CSDL.
  - [ ] TC Đăng nhập thất bại: Bỏ trống Email hoặc Mật khẩu.
  - [ ] TC Đăng nhập thành công kiểm tra lưu Session (`UserId`, `Email`, `RoleName`).
  - [ ] TC Thử nghiệm SQL Injection trên form Đăng nhập (`' OR '1'='1`).
- [ ] **Chức năng Đăng xuất (Logout):**
  - [ ] TC Đăng xuất thành công, xóa sạch Session, chuyển về màn hình đăng nhập.
  - [ ] TC Bấm nút Back trên trình duyệt sau khi đăng xuất (kiểm tra không giữ session).
- [ ] **Chức năng Hồ sơ cá nhân (Profile):**
  - [ ] TC Xem thông tin cá nhân đúng với dữ liệu trong `UserDetail`.
  - [ ] TC Cập nhật thành công: Họ tên, Giới tính, Ngày sinh, SĐT, Địa chỉ hợp lệ.
  - [ ] TC Cập nhật thất bại: SĐT chứa chữ cái hoặc không đúng định dạng.
- [ ] **Chức năng Đổi mật khẩu (Change Password):**
  - [ ] TC Đổi mật khẩu thành công khi nhập đúng mật khẩu hiện tại và mật khẩu mới khớp nhau.
  - [ ] TC Đổi mật khẩu thất bại: Sai mật khẩu hiện tại.
  - [ ] TC Đổi mật khẩu thất bại: Mật khẩu mới và Nhập lại mật khẩu không trùng khớp.
  - [ ] TC Đổi mật khẩu thất bại: Mật khẩu mới có độ dài < 6 ký tự.
- [ ] **Chức năng Quản lý người dùng (Dành riêng cho Admin):**
  - [ ] TC Admin xem danh sách toàn bộ người dùng kèm phân trang.
  - [ ] TC Admin thêm mới tài khoản và phân vai trò Admin / Employee / User.
  - [ ] TC Admin thay đổi quyền hạn của tài khoản.
  - [ ] TC Admin xóa tài khoản người dùng và kiểm tra xóa tầng `UserDetail` (Cascade).

#### 2.2.2. Phân hệ Sản phẩm, Giỏ hàng và Đơn hàng (Products, Cart & Orders)

- [ ] **Chức năng Duyệt danh sách & Phân trang:**
  - [ ] TC Hiển thị danh sách sản phẩm trang chủ còn tồn kho (`Stock > 0`).
  - [ ] TC Phân trang danh sách sản phẩm (đúng 8 sản phẩm mỗi trang).
  - [ ] TC Chuyển đổi giữa các trang (Trang 1, Trang 2, Trang cuối).
- [ ] **Chức năng Lọc sản phẩm (Filter):**
  - [ ] TC Lọc sản phẩm theo từng Danh mục (Laptop, Desktop, Tablet, Monitor, Accessory).
  - [ ] TC Lọc sản phẩm theo Thương hiệu (Dell, HP, Asus, Lenovo, Acer).
  - [ ] TC Lọc kết hợp đồng thời Danh mục và Thương hiệu.
  - [ ] TC Lọc theo điều kiện không có sản phẩm nào thỏa mãn (hiển thị thông báo rỗng).
- [ ] **Chức năng Tìm kiếm sản phẩm (Search):**
  - [ ] TC Tìm kiếm theo từ khóa chính xác (VD: "Dell XPS").
  - [ ] TC Tìm kiếm không phân biệt chữ hoa, chữ thường.
  - [ ] TC Tìm kiếm theo từ khóa một phần (VD: "Asus").
  - [ ] TC Tìm kiếm với từ khóa không tồn tại.
  - [ ] TC Tìm kiếm với ô nhập rỗng hoặc chỉ toàn khoảng trắng.
  - [ ] TC Kiểm thử tính bền vững ô tìm kiếm (Regex Crash DEF-02): Nhập ký tự `(`, `[`, `*`, `\`.
- [ ] **Chức năng Xem chi tiết sản phẩm:**
  - [ ] TC Hiển thị đầy đủ Tên, Giá gốc, Giá khuyến mãi, Tồn kho, Mô tả, Hãng, Danh mục.
  - [ ] TC Kiểm tra tính toán đúng tỷ lệ phần trăm giảm giá qua `ProductExts.DiscountPercentage`.
  - [ ] TC Kiểm tra định dạng tiền tệ Việt Nam đồng qua `ProductExts.FormattedPrice`.
  - [ ] TC Hiển thị ảnh đại diện chính và thư viện ảnh phụ (Galleries).
- [ ] **Chức năng Quản lý Giỏ hàng (Cart):**
  - [ ] TC Thêm sản phẩm vào giỏ khi chưa đăng nhập (Chuyển hướng về `/Auth/SignIn`).
  - [ ] TC Thêm sản phẩm vào giỏ khi đã đăng nhập (Thêm mới với số lượng 1 qua SP `AddCart`).
  - [ ] TC Thêm tiếp sản phẩm đã có trong giỏ (Số lượng tự động cộng dồn lên 1).
  - [ ] TC Xem giỏ hàng: Kiểm tra danh sách món hàng, đơn giá, số lượng, tổng tiền tạm tính.
  - [ ] TC Cập nhật số lượng sản phẩm trong giỏ hàng.
  - [ ] TC Xóa sản phẩm khỏi giỏ hàng (Kiểm tra đặc biệt lỗi DEF-01: Chỉ xóa dòng trong `Cart`, không xóa sản phẩm trong `Product`).
- [ ] **Chức năng Đặt hàng & Thanh toán (CheckOut):**
  - [ ] TC Điều hướng vào trang CheckOut từ Giỏ hàng.
  - [ ] TC Kiểm tra tính hợp lệ của Form đặt hàng (Họ tên, SĐT, Địa chỉ nhận hàng, Ghi chú).
  - [ ] TC Đặt hàng khi để trống trường bắt buộc (báo lỗi validation).
  - [ ] TC Xác nhận đặt hàng (Kiểm tra DEF-03: Kiểm tra hành vi lưu đơn hàng vào CSDL).
- [ ] **Chức năng Quản trị Sản phẩm (Admin & Employee):**
  - [ ] TC Thêm mới sản phẩm hợp lệ kèm tải file ảnh (.jpg, .png).
  - [ ] TC Thêm sản phẩm thất bại: Bỏ trống tiêu đề hoặc độ dài tiêu đề < 3 ký tự.
  - [ ] TC Thêm sản phẩm thất bại: Giá < 1000 hoặc Tồn kho < 0.
  - [ ] TC Thêm sản phẩm thất bại: Upload file không phải ảnh (.exe, .pdf) - kiểm tra `Helpers.IsValidImage`.
  - [ ] TC Chỉnh sửa thông tin sản phẩm và thay đổi ảnh đại diện.
  - [ ] TC Xóa sản phẩm khỏi hệ thống.

#### 2.2.3 & 2.2.4. Phân hệ Nghiệp vụ Mở rộng / Đánh giá & Khuyến mãi

_(Mục này tương ứng mục 2.2.3 và 2.2.4 trong đề cương gốc của trường, áp dụng cho các chức năng tương đương của dự án Ecommerce)_

- [ ] **Chức năng Đánh giá sản phẩm (Reviews & Ratings):**
  - [ ] TC Đánh giá sản phẩm với số sao từ 1 đến 5 và bình luận hợp lệ.
  - [ ] TC Người dùng chưa đăng nhập không được phép gửi đánh giá.
  - [ ] TC Đánh giá với bình luận rỗng hoặc đánh giá vượt ngoài khoảng 1-5 sao.
- [ ] **Chức năng Quản lý Thương hiệu & Danh mục (Brands & Categories - Admin/Employee):**
  - [ ] TC Thêm mới thương hiệu thành công.
  - [ ] TC Thêm mới thương hiệu thất bại do trùng tên (Unique Constraint).
  - [ ] TC Thêm mới danh mục sản phẩm thành công.
  - [ ] TC Thêm mới danh mục thất bại do trùng tên.

### 2.3. Thiết kế Test Case và Test Data kiểm thử tích hợp (Integration Testing)

- [ ] **Tích hợp Controller & Entity Framework DbContext:**
  - [ ] TC Kiểm tra Controller truy vấn đúng dữ liệu qua `StoreEntities`.
  - [ ] TC Kiểm tra xử lý ngắt kết nối CSDL và ghi log qua Serilog.
- [ ] **Tích hợp Database Triggers & Stored Procedures:**
  - [ ] TC Tích hợp Trigger `Tri_AddProduct`: Thêm sản phẩm mới -> Kiểm tra tự động phát sinh bản ghi `Gallery` với `IsPrimary = 1`.
  - [ ] TC Tích hợp Trigger `Tri_AddGallery`: Cố ý gán 2 hình ảnh `IsPrimary = 1` cho cùng 1 sản phẩm -> Kiểm tra giao dịch bị hủy (Rollback).
  - [ ] TC Tích hợp Trigger `Tri_AddUserDetail`: Đăng ký tài khoản mới -> Kiểm tra bảng `UserDetail` được chèn tự động với tên trích từ email.
  - [ ] TC Tích hợp Stored Procedure `AddCart`: Gọi thủ tục với `@userId` và `@productId` chưa có trong giỏ -> Tạo mới dòng số lượng 1; gọi lần 2 -> Tăng số lượng lên 2.
- [ ] **Tích hợp Kiểm soát truy cập (RBAC Integration):**
  - [ ] TC Tài khoản vai trò `User` gõ trực tiếp URL `/Products/ProductManagement` -> Bị từ chối truy cập.
  - [ ] TC Tài khoản vai trò `User` gõ trực tiếp URL `/UserAccount/ManageUsers` -> Bị từ chối truy cập.
  - [ ] TC Tài khoản vai trò `Employee` gõ trực tiếp URL `/UserAccount/ManageUsers` -> Bị từ chối truy cập.

### 2.4. Kết luận chương 2

- [ ] Bảng tổng hợp số lượng Test Cases đã thiết kế theo từng phân hệ.
- [ ] Nhận xét về độ bao phủ kịch bản kiểm thử chức năng và tích hợp.

---

## CHƯƠNG 3. KIỂM THỬ TỰ ĐỘNG WEBSITE (Trang 101 - 119)

### 3.1. Tổng quan về kiểm thử tự động

#### 3.1.1. Khái niệm kiểm thử tự động

- [ ] Trình bày định nghĩa kiểm thử tự động (Automation Testing).
- [ ] Phân biệt giữa Kiểm thử thủ công (Manual) và Kiểm thử tự động (Automation).

#### 3.1.2. Vai trò của kiểm thử tự động

- [ ] Tăng tốc độ thực thi các bài kiểm thử lặp đi lặp lại.
- [ ] Giảm thiểu sai sót do yếu tố con người trong kiểm thử hồi quy (Regression Testing).
- [ ] Nâng cao độ tin cậy và hỗ trợ tích hợp liên tục (CI/CD).

#### 3.1.3. Ưu điểm và hạn chế của kiểm thử tự động

- [ ] Lập bảng so sánh Ưu điểm (Nhanh, lặp lại chính xác, chạy 24/7) và Hạn chế (Chi phí xây dựng ban đầu cao, bảo trì kịch bản khi UI thay đổi).

### 3.2. Công cụ kiểm thử tự động Selenium IDE

#### 3.2.1. Giới thiệu Selenium IDE

- [ ] Giới thiệu lịch sử, kiến trúc extension trên trình duyệt Chrome/Edge/Firefox.
- [ ] Chụp ảnh màn hình giao diện cài đặt Selenium IDE extension trên trình duyệt.

#### 3.2.2. Các thành phần của Selenium IDE

- [ ] Giải thích các khái niệm: Command (Lệnh: `open`, `type`, `click`, `assertText`), Target (Bộ định vị: `id=...`, `name=...`, `xpath=...`, `css=...`), Value (Giá trị truyền vào).
- [ ] Giải thích khái niệm Test Suites, Test Cases, Assertions (Kiểm tra cứng) và Verifications (Kiểm tra mềm).
- [ ] Hướng dẫn cách Record (Ghi kịch bản) và Playback (Chạy lại kịch bản).

### 3.3. Tiêu chí lựa chọn Test Case để tự động hóa

- [ ] Xác định các tiêu chí tuyển chọn Test Case:
  - [ ] Các kịch bản thuộc luồng nghiệp vụ chính (Critical & Happy Path).
  - [ ] Các kịch bản chạy thường xuyên trong kiểm thử hồi quy.
  - [ ] Các kịch bản ít bị biến động giao diện.
  - [ ] Các form nhập liệu với nhiều bộ dữ liệu kiểm thử lặp lại.

### 3.4. Danh sách Test Case được tự động hóa

- [ ] **Kịch bản tự động 1 (Auto_TC_01): Đăng nhập thành công**
  - [ ] Ghi kịch bản Selenium IDE: Mở trang -> Click Đăng nhập -> Nhập email, pass -> Click Submit -> Assert hiển thị tên người dùng trên Header.
  - [ ] Chụp ảnh màn hình bảng lệnh trong Selenium IDE và log thực thi thành công.
- [ ] **Kịch bản tự động 2 (Auto_TC_02): Đăng nhập thất bại do sai mật khẩu**
  - [ ] Ghi kịch bản: Nhập tài khoản đúng, mật khẩu sai -> Assert hiển thị thông báo lỗi.
- [ ] **Kịch bản tự động 3 (Auto_TC_03): Đăng ký tài khoản mới**
  - [ ] Ghi kịch bản: Nhập thông tin đăng ký hợp lệ -> Assert chuyển hướng và thông báo thành công.
- [ ] **Kịch bản tự động 4 (Auto_TC_04): Tìm kiếm sản phẩm theo từ khóa**
  - [ ] Ghi kịch bản: Nhập từ khóa "Dell" vào ô tìm kiếm -> Nhấn Enter -> Assert danh sách kết quả chứa tiêu đề "Dell".
- [ ] **Kịch bản tự động 5 (Auto_TC_05): Thêm sản phẩm vào giỏ hàng**
  - [ ] Ghi kịch bản: Đăng nhập -> Chọn sản phẩm -> Click "Thêm vào giỏ" -> Điều hướng vào Giỏ hàng -> Assert sản phẩm hiển thị trong bảng giỏ hàng.
- [ ] Xuất file kịch bản tự động định dạng `.side` và lưu trữ trong thư mục mã nguồn/tài liệu.

### 3.5. Kết luận chương 3

- [ ] Tóm tắt kết quả xây dựng bộ kiểm thử tự động trên Selenium IDE.

---

## CHƯƠNG 4. THỰC THI KIỂM THỬ VÀ BÁO CÁO LỖI (Trang 120 - 239)

### 4.1. Thực thi kiểm thử chức năng (Functional Test Execution)

_(Mỗi mục cần có bảng kết quả: Test ID, Tên kịch bản, Kết quả mong đợi, Kết quả thực tế, Trạng thái Pass/Fail, Ảnh chụp minh chứng)_

#### 4.1.1. Kết quả kiểm thử nhóm chức năng Khách hàng và Tài khoản

- [ ] Chạy và ghi nhận kết quả các Test Case Đăng ký (`TC_AUTH_01` -> `TC_AUTH_03`,...).
- [ ] Chạy và ghi nhận kết quả các Test Case Đăng nhập (`TC_AUTH_04`,...).
- [ ] Chạy và ghi nhận kết quả các Test Case Đăng xuất (`TC_AUTH_05`).
- [ ] Chạy và ghi nhận kết quả các Test Case Hồ sơ cá nhân (Profile).
- [ ] Chạy và ghi nhận kết quả các Test Case Đổi mật khẩu.
- [ ] Chạy và ghi nhận kết quả các Test Case Quản lý người dùng của Admin.
- [ ] Chụp đầy đủ ảnh chụp màn hình minh chứng cho các trường hợp Pass và Fail.

#### 4.1.2. Kết quả kiểm thử nhóm chức năng Sản phẩm, Giỏ hàng và Đơn hàng

- [ ] Chạy và ghi nhận kết quả Danh sách & Phân trang sản phẩm.
- [ ] Chạy và ghi nhận kết quả Bộ lọc sản phẩm (Brand & Category).
- [ ] Chạy và ghi nhận kết quả Tìm kiếm sản phẩm (Ghi nhận lỗi Regex Crash DEF-02).
- [ ] Chạy và ghi nhận kết quả Trang chi tiết sản phẩm & Tính khuyến mãi.
- [ ] Chạy và ghi nhận kết quả Quản lý Giỏ hàng (Ghi nhận lỗi nghiêm trọng DEF-01 khi xóa giỏ).
- [ ] Chạy và ghi nhận kết quả Đặt hàng CheckOut (Ghi nhận thiếu logic lưu DB DEF-03).
- [ ] Chạy và ghi nhận kết quả Quản trị sản phẩm của Admin/Employee (Upload ảnh, CRUD).

#### 4.1.3 & 4.1.4. Kết quả kiểm thử nhóm Nghiệp vụ Mở rộng / Đánh giá & Quản trị

- [ ] Chạy và ghi nhận kết quả chức năng Đánh giá sản phẩm (Reviews).
- [ ] Chạy và ghi nhận kết quả chức năng Quản lý Thương hiệu & Danh mục.
- [ ] Chạy và ghi nhận kết quả phân quyền RBAC (Ghi nhận lỗ hổng URL DEF-04).

### 4.2. Thực thi kiểm thử tích hợp (Integration Test Execution)

- [ ] Chạy và ghi nhận kết quả kiểm tra Trigger `Tri_AddProduct` (Bản ghi Gallery tự sinh).
- [ ] Chạy và ghi nhận kết quả kiểm tra Trigger `Tri_AddGallery` (Rollback khi có 2 ảnh chính).
- [ ] Chạy và ghi nhận kết quả kiểm tra Trigger `Tri_AddUserDetail` (UserDetail tự sinh).
- [ ] Chạy và ghi nhận kết quả kiểm tra Stored Procedure `AddCart` (Thêm mới / Tăng số lượng).
- [ ] Chạy toàn bộ Unit Test suite trong `Store.Tests` trên Test Explorer và chụp ảnh màn hình kết quả Pass.

### 4.3. Thực thi kiểm thử tự động (Automation Test Execution)

- [ ] Chạy toàn bộ Test Suites trên Selenium IDE.
- [ ] Ghi nhận thời gian chạy của từng Test Case tự động.
- [ ] Lập bảng thống kê kết quả chạy tự động (Pass / Fail, thời gian thực thi).
- [ ] Chụp ảnh màn hình kết quả chạy màu xanh (Passed) trên giao diện Selenium IDE.

### 4.4. Tổng hợp kết quả kiểm thử

#### 4.4.1. Thống kê số lượng Test Case

- [ ] Lập bảng tổng kết số lượng Test Case theo từng phân hệ và từng loại kiểm thử (Manual, Unit Test, Automation).
- [ ] Vẽ Biểu đồ tròn (Pie Chart) phân bố Test Cases theo phân hệ.

#### 4.4.2. Tỷ lệ Pass/Fail

- [ ] Lập bảng thống kê chi tiết số lượng Pass, Fail, Blocked.
- [ ] Tính toán Tỷ lệ Đạt: `Pass Rate = (Passed / Total Executed) * 100%`.
- [ ] Đối chiếu với KPI đề ra ở Chương 1 (Pass Rate ≥ 95%).

#### 4.4.3. Đánh giá độ bao phủ kiểm thử

- [ ] Đánh giá độ bao phủ yêu cầu chức năng (Functional Coverage).
- [ ] Đánh giá độ bao phủ mã nguồn của Unit Test (Code Coverage ≥ 70%).

### 4.5. Báo cáo lỗi (Defect Report)

#### 4.5.1. Danh sách lỗi phát hiện được

- [ ] Lập Bảng Defect Log tổng hợp đầy đủ các cột: Defect ID, Tiêu đề lỗi, Phân hệ, Mức độ nghiêm trọng (Severity), Mức ưu tiên (Priority), Người phát hiện, Trạng thái (Open/Fixed/Closed).
- [ ] Viết mô tả chi tiết Bug Report cho 4 lỗi trọng yếu của dự án:
  - [ ] **DEF-01:** `CartController.Remove` xóa nhầm sản phẩm trong bảng `Product` khi người dùng xóa khỏi giỏ hàng.
  - [ ] **DEF-02:** `ProductsController.Search` bị sập (Crash) do ngoại lệ Regex Injection khi nhập `(`, `[`, `*`, `\`.
  - [ ] **DEF-03:** `CheckOutController.CheckOut` chưa có mã lưu dữ liệu đơn hàng vào bảng `Order@` và `OrderDetail`.
  - [ ] **DEF-04:** Lỗ hổng kiểm soát truy cập trực tiếp URL quản trị đối với tài khoản vai trò `User`.
- [ ] Đính kèm ảnh chụp màn hình lỗi và file log ngoại lệ trích xuất từ `Store EF/Logs/dd-MM-yyyy.txt`.

#### 4.5.2. Phân loại mức độ nghiêm trọng của lỗi

- [ ] Thống kê số lượng lỗi theo mức độ: Critical (S1), High (S2), Medium (S3), Low (S4).
- [ ] Vẽ Biểu đồ cột phân loại mức độ nghiêm trọng của các defect tìm thấy.

#### 4.5.3. Đề xuất hướng khắc phục

- [ ] Đề xuất phương án sửa mã nguồn cụ thể cho từng lỗi:
  - [ ] Sửa DEF-01: Thay đổi `store.Products.Remove(p)` thành `store.Carts.Remove(cartItem)`.
  - [ ] Sửa DEF-02: Dùng `Regex.Escape(product)` hoặc chuyển sang phương thức `c.Title.ToLower().Contains(product.ToLower())`.
  - [ ] Sửa DEF-03: Triển khai logic lưu `Order_` và duyệt `Cart` để tạo `OrderDetail`, trừ tồn kho `Stock` và xóa giỏ hàng.
  - [ ] Sửa DEF-04: Thêm Filter kiểm tra `Session["RoleName"] == "Admin"` hoặc `"Employee"` trước khi cho phép vào Action quản trị.

### 4.6. Kết luận chương 4

- [ ] Tóm tắt kết quả thực thi kiểm thử và tình trạng chất lượng thực tế của phần mềm.

---

## KẾT LUẬN (Trang 240)

- [ ] **Các kết quả chính đạt được của đề tài:**
  - [ ] Hoàn thành toàn diện quy trình kiểm thử phần mềm cho website Ecommerce Computer V3.
  - [ ] Xây dựng bộ tài liệu chuẩn: Test Plan, Test Cases Specification, Automation Scripts, Defect Report.
  - [ ] Phát hiện và phân tích chính xác các lỗi logic và bảo mật nghiêm trọng trong hệ thống.
- [ ] **Hạn chế của đề tài:**
  - [ ] Chưa thực hiện kiểm thử hiệu năng/chịu tải quy mô lớn bằng JMeter.
  - [ ] Mức độ bao phủ kiểm thử tự động mới dừng lại ở các luồng cơ bản trên Selenium IDE.
- [ ] **Hướng phát triển tiếp theo:**
  - [ ] Mở rộng kiểm thử tự động với framework Selenium WebDriver C# / Python tích hợp CI/CD.
  - [ ] Thực hiện kiểm thử an toàn thông tin chuyên sâu (Penetration Testing với OWASP ZAP).

---

## TÀI LIỆU THAM KHẢO (Trang 241)

- [ ] Trình bày danh mục tài liệu tham khảo theo đúng chuẩn quy định (IEEE hoặc APA):
  - [ ] Giáo trình Kiểm thử phần mềm của trường/bộ môn.
  - [ ] Tiêu chuẩn ISO/IEC/IEEE 29119 Software Testing.
  - [ ] Tài liệu Microsoft ASP.NET MVC 5 & Entity Framework 6 Documentation.
  - [ ] Tài liệu Selenium IDE Documentation (`selenium.dev`).
  - [ ] Tài liệu tổng quan dự án `PROJECT_OVERVIEW.md` của Store EF V3.

---

> **Tập tin được lưu tại:** `Docs/CHECKLIST_TESTING_PLAN.md`  
> **Dự án:** Ecommerce Computer (Store EF) V3  
> **Được chuẩn hóa cho:** Báo cáo, Đồ án môn học Kiểm thử Phần mềm & Đảm bảo Chất lượng.
