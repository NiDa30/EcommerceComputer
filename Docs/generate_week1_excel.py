# -*- coding: utf-8 -*-
"""
Script to generate the Week 1 Task Assignment Excel File
Project: Ecommerce Computer (Store EF V3)
Date: 14/09/2026 - 17/09/2026
Author: Test Lead Điền & Antigravity QA Consultant
"""

import os
import sys
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')
import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter

def build_week1_excel():
    wb = openpyxl.Workbook()
    # Remove default sheet
    wb.remove(wb.active)

    # ----------------- STYLES DEFINITION -----------------
    font_title = Font(name="Segoe UI", size=15, bold=True, color="FFFFFF")
    font_subtitle = Font(name="Segoe UI", size=10, italic=True, color="E0EBF5")
    font_sec_header = Font(name="Segoe UI", size=11, bold=True, color="FFFFFF")
    font_tbl_header = Font(name="Segoe UI", size=9.5, bold=True, color="FFFFFF")
    font_tbl_header_dark = Font(name="Segoe UI", size=9.5, bold=True, color="1B365D")
    font_data = Font(name="Segoe UI", size=9, color="000000")
    font_data_bold = Font(name="Segoe UI", size=9, bold=True, color="000000")
    font_data_italic = Font(name="Segoe UI", size=8.5, italic=True, color="595959")
    font_note = Font(name="Segoe UI", size=8.5, color="333333")

    # Member fonts
    font_dien = Font(name="Segoe UI", size=9, bold=True, color="1F4E78")
    font_phu = Font(name="Segoe UI", size=9, bold=True, color="276A3C")
    font_thoai = Font(name="Segoe UI", size=9, bold=True, color="78281F")
    font_long = Font(name="Segoe UI", size=9, bold=True, color="7F6000")
    font_nam = Font(name="Segoe UI", size=9, bold=True, color="4A235A")
    font_all = Font(name="Segoe UI", size=9, bold=True, color="1B365D")

    # Fills
    fill_navy = PatternFill(start_color="1B365D", end_color="1B365D", fill_type="solid")
    fill_blue_sec = PatternFill(start_color="2F5597", end_color="2F5597", fill_type="solid")
    fill_blue_head = PatternFill(start_color="336699", end_color="336699", fill_type="solid")
    fill_light_head = PatternFill(start_color="D9E1F2", end_color="D9E1F2", fill_type="solid")
    fill_zebra_light = PatternFill(start_color="F8FAFD", end_color="F8FAFD", fill_type="solid")
    fill_white = PatternFill(start_color="FFFFFF", end_color="FFFFFF", fill_type="solid")

    # Badges Fills
    fill_pass = PatternFill(start_color="E2EFDA", end_color="E2EFDA", fill_type="solid")  # light soft green
    font_pass = Font(name="Segoe UI", size=9, bold=True, color="276A3C")
    fill_warn = PatternFill(start_color="FFF2CC", end_color="FFF2CC", fill_type="solid")  # light soft yellow
    font_warn = Font(name="Segoe UI", size=9, bold=True, color="8C6B00")
    fill_alert = PatternFill(start_color="FCE4D6", end_color="FCE4D6", fill_type="solid") # light soft red/orange
    font_alert = Font(name="Segoe UI", size=9, bold=True, color="C65911")
    fill_info = PatternFill(start_color="EDEDED", end_color="EDEDED", fill_type="solid")  # gray
    font_info = Font(name="Segoe UI", size=9, bold=True, color="595959")

    # Member Tag Fills
    fill_tag_dien = PatternFill(start_color="DDEBF7", end_color="DDEBF7", fill_type="solid")
    fill_tag_phu = PatternFill(start_color="E2EFDA", end_color="E2EFDA", fill_type="solid")
    fill_tag_thoai = PatternFill(start_color="FCE4D6", end_color="FCE4D6", fill_type="solid")
    fill_tag_long = PatternFill(start_color="FFF2CC", end_color="FFF2CC", fill_type="solid")
    fill_tag_nam = PatternFill(start_color="E8E1EF", end_color="E8E1EF", fill_type="solid")
    fill_tag_all = PatternFill(start_color="D9E1F2", end_color="D9E1F2", fill_type="solid")

    # Borders
    thin_border_side = Side(style='thin', color='D9D9D9')
    med_border_side = Side(style='medium', color='1B365D')
    cell_border = Border(left=thin_border_side, right=thin_border_side, top=thin_border_side, bottom=thin_border_side)
    header_border = Border(left=thin_border_side, right=thin_border_side, top=med_border_side, bottom=med_border_side)

    # Alignments
    align_center = Alignment(horizontal='center', vertical='center', wrap_text=True)
    align_left = Alignment(horizontal='left', vertical='center', wrap_text=True)
    align_right = Alignment(horizontal='right', vertical='center')
    align_top_left = Alignment(horizontal='left', vertical='top', wrap_text=True)
    align_top_center = Alignment(horizontal='center', vertical='top', wrap_text=True)

    # =========================================================================
    # SHEET 1: TONG QUAN TUAN 1 (OVERVIEW & STRATEGY)
    # =========================================================================
    ws1 = wb.create_sheet(title="Tong_Quan_Tuan_1")
    ws1.views.sheetView[0].showGridLines = True

    # Title Block
    ws1.merge_cells("A1:K1")
    ws1["A1"] = "BỘ MÔN KIỂM THỬ PHẦN MỀM - ĐỒ ÁN MÔN HỌC KIỂM ĐỊNH CHẤT LƯỢNG (STORE EF V3)"
    ws1["A1"].font = Font(name="Segoe UI", size=10, bold=True, color="E0EBF5")
    ws1["A1"].fill = fill_navy
    ws1["A1"].alignment = align_center

    ws1.merge_cells("A2:K2")
    ws1["A2"] = "📋 KẾ HOẠCH & PHÂN CÔNG NHIỆM VỤ TUẦN 1 (TỪ 14/09/2026 ĐẾN 17/09/2026)"
    ws1["A2"].font = font_title
    ws1["A2"].fill = fill_navy
    ws1["A2"].alignment = align_center

    ws1.merge_cells("A3:K3")
    ws1["A3"] = "Dự án: Ecommerce Computer (Store EF) V3 | Trưởng nhóm: Điền (Test Lead / QA Manager) | Giai đoạn: Khởi động & Kế hoạch"
    ws1["A3"].font = font_subtitle
    ws1["A3"].fill = fill_navy
    ws1["A3"].alignment = align_center

    ws1.row_dimensions[1].height = 20
    ws1.row_dimensions[2].height = 30
    ws1.row_dimensions[3].height = 20

    # Section 1: Thông tin chung & Mục tiêu trọng tâm
    ws1.merge_cells("A5:K5")
    ws1["A5"] = "1. THÔNG TIN CHUNG & MỤC TIÊU TRỌNG TÂM TUẦN 1 (CỘT MỐC M1)"
    ws1["A5"].font = font_sec_header
    ws1["A5"].fill = fill_blue_sec
    ws1["A5"].alignment = align_left
    ws1.row_dimensions[5].height = 24

    info_data = [
        ("Tên dự án thực tế", "Hệ thống Website Thương mại Điện tử Bán Máy tính Ecommerce Computer (Store EF) - Phiên bản V3"),
        ("Thời gian thực hiện Tuần 1", "04 Ngày làm việc chính thức (Từ Thứ Hai 14/09/2026 đến Thứ Năm 17/09/2026)"),
        ("Tài liệu tham chiếu căn cứ", "Docs/CHECKLIST_TESTING_PLAN.md, Docs/TASK_ASSIGNMENT_5_MEMBERS.md, Docs/TEST_PLAN.md, Docs/Test_Plan_StoreEF.docx"),
        ("Quy mô nhân sự", "05 Thành viên: Điền (Trưởng nhóm / Test Lead), Phú (Technical Lead / Senior QA), Thoại, Long, Nam (Junior Testers)"),
        ("Mục tiêu trọng tâm 1", "Khởi động dự án, thống nhất phương thức làm việc nhóm, thiết lập hạ tầng kho lưu trữ chung (Git / Google Drive) và quy định Definition of Done (DoD)."),
        ("Mục tiêu trọng tâm 2", "Cài đặt & kiểm thử môi trường kỹ thuật thành công trên cả 5 máy tính: Visual Studio 2022, SQL Server LocalDB, restore CSDL Store.sql, chạy web trên port 5000."),
        ("Mục tiêu trọng tâm 3", "Khảo sát toàn diện hệ thống Store EF V3: Kiến trúc MVC 5, cấu trúc 10 bảng CSDL, triggers, stored procedures, và kiểm tra sơ bộ các phân hệ chức năng trên Web UI."),
        ("Mục tiêu trọng tâm 4", "Biên soạn hoàn thiện Chương 1 (Xây dựng Kế hoạch Kiểm thử - Test Plan) theo chuẩn ISO/IEC/IEEE 29119 để Trưởng nhóm nộp duyệt vào ngày 17/09/2026."),
        ("Mục tiêu trọng tâm 5", "Chuẩn bị sẵn sàng cho Tuần 2: Chuẩn hóa biểu mẫu Test Case, ban hành tài liệu hướng dẫn kỹ thuật EP/BVA, và hoàn thành Ma trận yêu cầu kiểm thử (Test Requirements)."),
    ]

    r = 6
    for item, desc in info_data:
        ws1.merge_cells(start_row=r, start_column=1, end_row=r, end_column=3)
        ws1.merge_cells(start_row=r, start_column=4, end_row=r, end_column=11)
        ws1.cell(r, 1, item).font = font_data_bold
        ws1.cell(r, 1).alignment = align_left
        ws1.cell(r, 1).fill = fill_light_head
        ws1.cell(r, 1).border = cell_border
        
        c2 = ws1.cell(r, 4, desc)
        c2.font = font_data
        c2.alignment = align_left
        c2.fill = fill_white
        c2.border = cell_border
        ws1.row_dimensions[r].height = 20
        r += 1

    # Section 2: Cơ cấu nhân sự & Đánh giá năng lực ban đầu
    r += 1
    ws1.merge_cells(f"A{r}:K{r}")
    ws1[f"A{r}"] = "2. CƠ CẤU NHÂN SỰ, PHÂN TÍCH NĂNG LỰC BAN ĐẦU & NGUYÊN TẮC PHÂN CÔNG"
    ws1[f"A{r}"].font = font_sec_header
    ws1[f"A{r}"].fill = fill_blue_sec
    ws1[f"A{r}"].alignment = align_left
    ws1.row_dimensions[r].height = 24

    r += 1
    headers_hr = ["Mã TV", "Họ và tên", "Vai trò chuyên trách", "Đánh giá năng lực sơ bộ", "Nguyên tắc phân công công việc", "Phân hệ / Khối việc phụ trách Tuần 1", "Khối lượng (Giờ)", "Tỷ trọng"]
    col_spans_hr = [(1, 1), (2, 2), (3, 3), (4, 5), (6, 7), (8, 9), (10, 10), (11, 11)]

    for idx, h in enumerate(headers_hr):
        sc, ec = col_spans_hr[idx]
        ws1.merge_cells(start_row=r, start_column=sc, end_row=r, end_column=ec)
        cell = ws1.cell(r, sc, h)
        cell.font = font_tbl_header
        cell.fill = fill_blue_head
        cell.alignment = align_center
        cell.border = header_border
    ws1.row_dimensions[r].height = 26

    members_hr_data = [
        ("TV01", "Điền (Trưởng nhóm)", "Test Lead & QA Project Manager", 
         "Có năng lực tổ chức, quản lý dự án, bao quát toàn diện quy trình kiểm thử phần mềm.",
         "Chịu trách nhiệm quản lý dự án, điều phối tiến độ, tổ chức họp Kick-off & Daily Check-in; chủ trì biên soạn toàn bộ Chương 1 (Test Plan) theo Checklist, kiểm soát chất lượng đầu ra.",
         "Quản lý chung, Bìa & Mục lục, Lời mở đầu, Chương 1 (Mục 1.1 đến 1.6), Đánh giá thành viên, Nghiệm thu M1.", 32, "23.5%"),
        ("TV02", "Phú", "Technical Lead / Senior QA Tester", 
         "Người có thể làm được việc; kỹ năng lập trình C#, CSDL SQL Server và kỹ thuật kiểm thử tốt.",
         "Phụ trách các phần kỹ thuật nặng nhất, rủi ro nhất: Setup môi trường master, kiểm tra Trigger/SP, cấu hình Unit Test Store.Tests và Selenium IDE; làm điểm tựa kỹ thuật và kèm cặp 3 bạn.",
         "Hạ tầng môi trường master, Khảo sát DB Store.sql & Triggers, Setup MSTest Store.Tests & Selenium IDE, Hỗ trợ kỹ thuật 3 thành viên, Chuẩn hóa Template TC.", 32, "23.5%"),
        ("TV03", "Thoại", "Junior Manual Tester (Auth & Account)", 
         "Chưa rõ năng lực cụ thể; cần giao việc rõ ràng, chia nhỏ theo từng bước, có tài liệu hướng dẫn và kèm cặp.",
         "Giao phân hệ Xác thực & Tài khoản người dùng (luồng nghiệp vụ rõ ràng, có sẵn form); tự cài môi trường cá nhân dưới sự hỗ trợ của Phú; kiểm thử thăm dò (Exploratory test) và lập danh mục kịch bản.",
         "Cài đặt môi trường máy 3 (VS + LocalDB + run.bat), Khảo sát Phân hệ Xác thực (SignUp, SignIn, Logout, Profile, UserAdmin), Lập ma trận yêu cầu test Auth, Viết 5 TC mẫu.", 24, "17.7%"),
        ("TV04", "Long", "Junior Manual Tester (Product & Catalog)", 
         "Chưa rõ năng lực cụ thể; cần giao việc trực quan trên giao diện người dùng, dễ kiểm tra đánh giá.",
         "Giao phân hệ Danh mục & Sản phẩm (trực quan trên Web UI: danh sách, phân trang, lọc, tìm kiếm); tự cài môi trường cá nhân; kiểm thử thăm dò giao diện và lập danh mục kịch bản.",
         "Cài đặt môi trường máy 4 (VS + LocalDB + run.bat), Khảo sát Phân hệ Sản phẩm & Quản trị Catalog (List, Paging, Search, Filter, Details), Lập ma trận yêu cầu test Product, Viết 5 TC mẫu.", 24, "17.7%"),
        ("TV05", "Nam", "Junior Manual Tester (Cart & CheckOut)", 
         "Chưa rõ năng lực cụ thể; cần giao việc theo luồng chức năng người dùng, có sự phối hợp kiểm tra dữ liệu.",
         "Giao phân hệ Giỏ hàng & Thanh toán (luồng mua hàng từ Cart đến CheckOut); tự cài môi trường cá nhân; kiểm thử thăm dò luồng thêm/sửa/xóa giỏ hàng và đối chiếu CSDL cùng Phú.",
         "Cài đặt môi trường máy 5 (VS + LocalDB + run.bat), Khảo sát Phân hệ Giỏ hàng & Thanh toán (Add Cart, Update SL, Remove, CheckOut UI), Lập ma trận yêu cầu test Cart, Viết 5 TC mẫu.", 24, "17.7%"),
    ]

    r += 1
    for m in members_hr_data:
        code, name, role, cap, rule, task, hours, pct = m
        ws1.row_dimensions[r].height = 42

        fill_curr = fill_zebra_light if (r % 2 == 0) else fill_white

        c_code = ws1.cell(r, 1, code)
        c_code.font = font_data_bold
        c_code.alignment = align_center
        c_code.fill = fill_curr
        c_code.border = cell_border

        c_name = ws1.cell(r, 2, name)
        c_name.alignment = align_left
        c_name.fill = fill_curr
        c_name.border = cell_border
        if "Điền" in name:
            c_name.font = font_dien
        elif "Phú" in name:
            c_name.font = font_phu
        elif "Thoại" in name:
            c_name.font = font_thoai
        elif "Long" in name:
            c_name.font = font_long
        elif "Nam" in name:
            c_name.font = font_nam

        c_role = ws1.cell(r, 3, role)
        c_role.font = font_data_bold
        c_role.alignment = align_left
        c_role.fill = fill_curr
        c_role.border = cell_border

        ws1.merge_cells(start_row=r, start_column=4, end_row=r, end_column=5)
        c_cap = ws1.cell(r, 4, cap)
        c_cap.font = font_data
        c_cap.alignment = align_top_left
        c_cap.fill = fill_curr
        c_cap.border = cell_border

        ws1.merge_cells(start_row=r, start_column=6, end_row=r, end_column=7)
        c_rule = ws1.cell(r, 6, rule)
        c_rule.font = font_data
        c_rule.alignment = align_top_left
        c_rule.fill = fill_curr
        c_rule.border = cell_border

        ws1.merge_cells(start_row=r, start_column=8, end_row=r, end_column=9)
        c_task = ws1.cell(r, 8, task)
        c_task.font = font_data
        c_task.alignment = align_top_left
        c_task.fill = fill_curr
        c_task.border = cell_border

        c_hrs = ws1.cell(r, 10, hours)
        c_hrs.font = font_data_bold
        c_hrs.alignment = align_center
        c_hrs.fill = fill_curr
        c_hrs.border = cell_border

        c_pct = ws1.cell(r, 11, pct)
        c_pct.font = font_data_bold
        c_pct.alignment = align_center
        c_pct.fill = fill_curr
        c_pct.border = cell_border

        r += 1

    # Section 3: Quy chế làm việc nhóm & Tiêu chí hoàn thành (DoD)
    r += 1
    ws1.merge_cells(f"A{r}:K{r}")
    ws1[f"A{r}"] = "3. NGUYÊN TẮC LÀM VIỆC NHÓM, QUY TRÌNH CHECK-IN & TIÊU CHÍ HOÀN THÀNH (DEFINITION OF DONE - DOD)"
    ws1[f"A{r}"].font = font_sec_header
    ws1[f"A{r}"].fill = fill_blue_sec
    ws1[f"A{r}"].alignment = align_left
    ws1.row_dimensions[r].height = 24

    dod_rules = [
        ("Quy định Họp & Báo cáo tiến độ", "Daily Check-in hằng ngày từ 17:00 - 17:30 (qua Google Meet / Nhóm Zalo). Tất cả thành viên bắt buộc tham gia đúng giờ, báo cáo 3 câu hỏi: (1) Đã làm được gì hôm nay? (2) Gặp vướng mắc gì cần hỗ trợ? (3) Mục tiêu ngày mai là gì?"),
        ("Quy chế Hỗ trợ Kỹ thuật", "Phú là người chịu trách nhiệm hỗ trợ kỹ thuật chính. Các thành viên Thoại, Long, Nam nếu gặp lỗi cài đặt môi trường LocalDB, IIS Express hoặc mã lỗi quá 30 phút phải chủ động ping Phú và Điền trên nhóm chung để được giải quyết nhanh chóng, không giấu lỗi."),
        ("Quy chuẩn Đặt tên File & Lưu trữ", "Toàn bộ tài liệu, ảnh chụp màn hình minh chứng phải lưu trữ đúng thư mục quy định trên Google Drive/Git: `Docs/Tuan1/Screenshots/[Ten_Thanh_Vien]/`. Tên file đặt theo cấu trúc: `[TenTV]_[Module]_[TaskCode]_[MoTa].png` (VD: `Thoai_Auth_D02_LocalDB_OK.png`)."),
        ("Tiêu chí DoD: Môi trường Kiểm thử", "Được coi là HOÀN THÀNH khi: (1) Máy tính cá nhân kết nối được CSDL LocalDB và mở được 10 bảng dữ liệu, (2) Chạy file `run.bat` trình duyệt tự bật URL `http://localhost:5000` hiển thị trang chủ không lỗi, (3) Có ảnh chụp màn hình gửi Trưởng nhóm Điền xác nhận."),
        ("Tiêu chí DoD: Khảo sát & Yêu cầu Test", "Được coi là HOÀN THÀNH khi: (1) Hoàn thành file nhật ký khảo sát phân hệ được giao (liệt kê các form, các trường dữ liệu, validation rules), (2) Hoàn thành Ma trận danh mục kịch bản kiểm thử (khoảng 20 - 30 ca test dự kiến), (3) Viết thử 5 Test Case mẫu theo đúng Template."),
        ("Tiêu chí DoD: Bản thảo Test Plan Chương 1", "Được coi là HOÀN THÀNH khi: (1) Trưởng nhóm Điền hoàn thành đầy đủ từ Mục 1.1 đến Mục 1.6 theo Checklist, (2) Định dạng chuẩn Word (Heading, Caption bảng/hình, lề 3-2-2-2, giãn dòng 1.25 lines), (3) Thành viên Phú và nhóm rà soát nội dung kỹ thuật."),
    ]

    r += 1
    for title, rule_desc in dod_rules:
        ws1.merge_cells(start_row=r, start_column=1, end_row=r, end_column=3)
        ws1.merge_cells(start_row=r, start_column=4, end_row=r, end_column=11)
        c1 = ws1.cell(r, 1, title)
        c1.font = font_data_bold
        c1.alignment = align_left
        c1.fill = fill_light_head
        c1.border = cell_border

        c2 = ws1.cell(r, 4, rule_desc)
        c2.font = font_data
        c2.alignment = align_top_left
        c2.fill = fill_white
        c2.border = cell_border
        ws1.row_dimensions[r].height = 28
        r += 1

    # Column widths for Sheet 1
    col_widths_s1 = {1: 8, 2: 18, 3: 25, 4: 20, 5: 20, 6: 22, 7: 22, 8: 24, 9: 24, 10: 14, 11: 12}
    for c_idx, width in col_widths_s1.items():
        ws1.column_dimensions[get_column_letter(c_idx)].width = width

    # =========================================================================
    # SHEET 2: PHAN CONG CHI TIET TUAN 1 (74 DETAILED TASKS)
    # =========================================================================
    ws2 = wb.create_sheet(title="Phan_Cong_Chi_Tiet_Tuan_1")
    ws2.views.sheetView[0].showGridLines = True

    # Title Block
    ws2.merge_cells("A1:N1")
    ws2["A1"] = "BẢNG PHÂN CÔNG NHIỆM VỤ CHI TIẾT THEO NGÀY - TUẦN 1 (14/09/2026 - 17/09/2026)"
    ws2["A1"].font = Font(name="Segoe UI", size=13, bold=True, color="FFFFFF")
    ws2["A1"].fill = fill_navy
    ws2["A1"].alignment = align_center

    ws2.merge_cells("A2:N2")
    ws2["A2"] = "Dự án: Ecommerce Computer (Store EF V3) | Phân công nhiệm vụ chi tiết theo ngày, người phụ trách, độ khó, sản phẩm bàn giao & tiêu chí nghiệm thu"
    ws2["A2"].font = font_subtitle
    ws2["A2"].fill = fill_navy
    ws2["A2"].alignment = align_center

    ws2.row_dimensions[1].height = 24
    ws2.row_dimensions[2].height = 18

    # Headers for detailed tasks
    task_headers = [
        "Mã CV", "Ngày", "Thứ", "Phân hệ / Nhóm việc", "Tên hạng mục công việc",
        "Mô tả chi tiết nội dung & các bước thực hiện", "Người phụ trách", "Hỗ trợ / Review",
        "Độ khó", "Mức ưu tiên", "Căn cứ / Tài liệu tham chiếu",
        "Sản phẩm bàn giao (Deliverables)", "Tiêu chí nghiệm thu (DoD)", "Trạng thái"
    ]

    r = 4
    for c_idx, h in enumerate(task_headers, start=1):
        cell = ws2.cell(r, c_idx, h)
        cell.font = font_tbl_header
        cell.fill = fill_blue_head
        cell.alignment = align_center
        cell.border = header_border
    ws2.row_dimensions[r].height = 28

    # 74 Tasks Data List
    # Tuple: (TaskID, Date, DayOfWeek, Module, TaskName, DetailedSteps, Assignee, Reviewer, Difficulty, Priority, Reference, Deliverables, DoD, Status)
    tasks_raw = [
        # --- NGÀY 1: THỨ HAI (14/09/2026) ---
        ("W1.D01.01", "14/09/2026", "Thứ Hai", "Quản trị dự án", "Tổ chức cuộc họp Kick-off dự án", 
         "Chủ trì cuộc họp trực tuyến lúc 08:30 sáng: Phổ biến mục tiêu đồ án, cấu trúc 4 chương, lịch trình 5 tuần, phân tích sơ bộ năng lực và thống nhất quy chế làm việc nhóm.", 
         "Điền (Lead)", "Cả nhóm", "Trung bình", "Khẩn", "Docs/TASK_ASSIGNMENT_5_MEMBERS.md", 
         "Biên bản họp Kick-off & Danh sách thành viên cam kết tiến độ", "100% thành viên tham dự đúng giờ, nắm rõ nhiệm vụ và cam kết quy chế", "Đã hoàn thành"),
        
        ("W1.D01.02", "14/09/2026", "Thứ Hai", "Hạ tầng làm việc", "Khởi tạo Google Drive & Kho lưu trữ Git", 
         "Tạo thư mục làm việc chung trên Google Drive (`EcommerceComputer-V3_Docs`), cấp quyền chỉnh sửa cho 5 email thành viên; khởi tạo repository Git để quản lý mã nguồn và báo cáo.", 
         "Điền (Lead)", "Phú", "Dễ", "Cao", "Docs/CHECKLIST_TESTING_PLAN.md", 
         "Link Google Drive chung & Link Git repo hoạt động ổn định", "5 thành viên truy cập và tải/tạo file thử nghiệm thành công", "Đã hoàn thành"),

        ("W1.D01.03", "14/09/2026", "Thứ Hai", "Quản trị dự án", "Ban hành biểu mẫu làm việc & Quy tắc DoD", 
         "Thiết lập và chia sẻ biểu mẫu phân công công việc tuần 1, quy chuẩn đặt tên file, template ghi nhật ký khảo sát và quy định báo cáo Daily Check-in lúc 17:00.", 
         "Điền (Lead)", "Cả nhóm", "Dễ", "Cao", "Docs/CHECKLIST_TESTING_PLAN.md", 
         "File Excel phân công nhiệm vụ Tuần 1 & Quy chuẩn làm việc nhóm", "Toàn bộ thành viên xác nhận đã đọc và hiểu rõ quy định", "Đã hoàn thành"),

        ("W1.D01.04", "14/09/2026", "Thứ Hai", "Báo cáo Test Plan", "Soạn thảo phần mở đầu báo cáo: Bìa & Cam đoan", 
         "Thiết kế Trang bìa chính, Trang phụ bìa đúng chuẩn đồ án; viết Lời cảm ơn và Lời cam đoan trung thực dữ liệu kiểm thử theo cấu trúc Checklist.", 
         "Điền (Lead)", "Phú", "Dễ", "Trung bình", "Docs/CHECKLIST_TESTING_PLAN.md (Phần đầu)", 
         "File Word chứa Trang bìa, Bìa phụ, Lời cảm ơn, Lời cam đoan", "Định dạng chuẩn lề 3-2-2-2cm, font Segoe UI/Calibri, đúng mẫu bộ môn", "Đã hoàn thành"),

        ("W1.D01.05", "14/09/2026", "Thứ Hai", "Hạ tầng kỹ thuật", "Khảo sát kiến trúc mã nguồn Store EF V3", 
         "Mở mã nguồn trong thư mục `Store/`, phân tích kiến trúc MVC 5, cấu trúc Controllers (`AuthController`, `ProductsController`, `CartController`, `CheckOutController`), ViewModels và Models.", 
         "Phú", "Điền (Lead)", "Khó", "Cao", "Source code Store EF V3 & PROJECT_OVERVIEW.md", 
         "Bản tóm tắt kiến trúc kỹ thuật phân tầng MVC 5 và luồng dữ liệu", "Xác định rõ các điểm vào (entry points) và logic nghiệp vụ chính", "Đã hoàn thành"),

        ("W1.D01.06", "14/09/2026", "Thứ Hai", "CSDL & Backend", "Khảo sát cấu trúc CSDL SQL Server từ Store.sql", 
         "Đọc và phân tích script `Store.sql`: Khảo sát cấu trúc 10 bảng dữ liệu, các ràng buộc Khóa chính, Khóa ngoại, 3 Database Triggers (`Tri_AddProduct`, `Tri_AddGallery`, `Tri_AddUserDetail`) và SP `AddCart`.", 
         "Phú", "Nam", "Khó", "Cao", "Store.sql & PROJECT_OVERVIEW.md", 
         "Sơ đồ quan hệ thực thể (ERD) và danh mục mô tả 10 bảng dữ liệu", "Liệt kê chính xác kiểu dữ liệu, ràng buộc và mục đích của 3 triggers", "Đã hoàn thành"),

        ("W1.D01.07", "14/09/2026", "Thứ Hai", "Kiểm thử tự động & UT", "Khảo sát dự án Store.Tests & Selenium IDE", 
         "Kiểm tra thư mục `Store.Tests`, xác định framework MSTest v1.2.0, các file test hiện hữu (`ProductExtsTests`, `HelpersTests`); tìm hiểu extension Selenium IDE trên Chrome.", 
         "Phú", "Điền (Lead)", "Trung bình", "Trung bình", "Store.Tests & Selenium IDE Documentation", 
         "Báo cáo sơ bộ về khả năng tự động hóa và kế hoạch viết Unit Test", "Xác định được các class mở rộng (Extensions) cần viết bài test", "Đã hoàn thành"),

        ("W1.D01.08", "14/09/2026", "Thứ Hai", "Hạ tầng kỹ thuật", "Soạn tài liệu hướng dẫn setup môi trường nhanh", 
         "Viết tài liệu tóm tắt các bước cài đặt Visual Studio 2022, SQL Server LocalDB, restore CSDL `Store.sql` và khởi chạy web bằng file `run.bat` để hướng dẫn Thoại, Long, Nam vào Ngày 2.", 
         "Phú", "Thoại, Long, Nam", "Trung bình", "Khẩn", "Docs/Test_Plan_StoreEF.docx & run.bat", 
         "Tài liệu Quickstart Setup Guide (PDF/Word/Markdown) kèm hình ảnh", "Các bước rõ ràng, dễ hiểu, có giải thích cách fix lỗi port và LocalDB", "Đã hoàn thành"),

        ("W1.D01.09", "14/09/2026", "Thứ Hai", "Khảo sát phân hệ Auth", "Tiếp nhận tài liệu & Nghiên cứu tổng quan Auth", 
         "Tham gia họp Kick-off, đọc tài liệu `PROJECT_OVERVIEW.md` phần Xác thực và Quản lý tài khoản; tìm hiểu luồng Đăng ký, Đăng nhập, Đăng xuất, Profile và Đổi mật khẩu.", 
         "Thoại", "Điền (Lead)", "Dễ", "Cao", "PROJECT_OVERVIEW.md & TASK_ASSIGNMENT TV02", 
         "Bản ghi chú tóm tắt luồng nghiệp vụ Xác thực và Quản trị người dùng", "Nắm rõ các trường thông tin trên form Đăng ký và Đăng nhập", "Đang thực hiện"),

        ("W1.D01.10", "14/09/2026", "Thứ Hai", "Khảo sát phân hệ Auth", "Liệt kê danh sách màn hình (Views) phân hệ Auth", 
         "Kiểm tra trong thư mục mã nguồn `Store/Views/Auth/` và `Store/Views/UserAccount/`, liệt kê danh sách các View `.cshtml` tương ứng với từng chức năng.", 
         "Thoại", "Phú", "Dễ", "Trung bình", "Store/Views/Auth & Store/Views/UserAccount", 
         "Danh sách 6 màn hình giao diện cần kiểm thử của phân hệ Auth", "Liệt kê đúng các file: SignUp.cshtml, SignIn.cshtml, Index.cshtml...", "Đang thực hiện"),

        ("W1.D01.11", "14/09/2026", "Thứ Hai", "Khảo sát phân hệ Product", "Tiếp nhận tài liệu & Nghiên cứu tổng quan Product", 
         "Tham gia họp Kick-off, đọc tài liệu `PROJECT_OVERVIEW.md` phần Phân hệ Sản phẩm; tìm hiểu các tính năng hiển thị sản phẩm trang chủ, phân trang, lọc theo Brand/Category, tìm kiếm.", 
         "Long", "Điền (Lead)", "Dễ", "Cao", "PROJECT_OVERVIEW.md & TASK_ASSIGNMENT TV03", 
         "Bản ghi chú tóm tắt luồng duyệt sản phẩm, phân trang và bộ lọc", "Hiểu rõ quy tắc hiển thị sản phẩm còn hàng (`Stock > 0`) và phân trang 8 sp/trang", "Đang thực hiện"),

        ("W1.D01.12", "14/09/2026", "Thứ Hai", "Khảo sát phân hệ Product", "Liệt kê danh sách màn hình (Views) phân hệ Product", 
         "Kiểm tra trong thư mục mã nguồn `Store/Views/Products/` và `Store/Areas/Admin/Views/`, liệt kê danh sách các file View liên quan đến hiển thị, tìm kiếm và quản trị sản phẩm.", 
         "Long", "Phú", "Dễ", "Trung bình", "Store/Views/Products & Store/Areas/Admin", 
         "Danh sách 7 màn hình giao diện cần kiểm thử của phân hệ Sản phẩm", "Liệt kê đúng các file: Index.cshtml, Details.cshtml, Search.cshtml...", "Đang thực hiện"),

        ("W1.D01.13", "14/09/2026", "Thứ Hai", "Khảo sát phân hệ Cart", "Tiếp nhận tài liệu & Nghiên cứu tổng quan Cart & Order", 
         "Tham gia họp Kick-off, đọc tài liệu `PROJECT_OVERVIEW.md` phần Giỏ hàng & Thanh toán; tìm hiểu luồng Thêm vào giỏ, Xem giỏ, Cập nhật số lượng, Xóa món và Form thanh toán CheckOut.", 
         "Nam", "Điền (Lead)", "Dễ", "Cao", "PROJECT_OVERVIEW.md & TASK_ASSIGNMENT TV04", 
         "Bản ghi chú tóm tắt quy trình mua hàng từ thêm giỏ đến đặt hàng", "Nắm rõ các bước tương tác từ giỏ hàng sang trang thanh toán", "Đang thực hiện"),

        ("W1.D01.14", "14/09/2026", "Thứ Hai", "Khảo sát phân hệ Cart", "Liệt kê danh sách màn hình (Views) phân hệ Cart & Order", 
         "Kiểm tra thư mục `Store/Views/Cart/` và `Store/Views/CheckOut/`, liệt kê các file View tương ứng với giỏ hàng và màn hình thanh toán đơn hàng.", 
         "Nam", "Phú", "Dễ", "Trung bình", "Store/Views/Cart & Store/Views/CheckOut", 
         "Danh sách 4 màn hình giao diện cần kiểm thử của Giỏ hàng & CheckOut", "Liệt kê đúng: Cart/Index.cshtml, CheckOut/Index.cshtml, Success.cshtml", "Đang thực hiện"),

        ("W1.D01.15", "14/09/2026", "Thứ Hai", "Quản trị dự án", "Họp Daily Check-in Ngày 1 (17:00 - 17:30)", 
         "Tổ chức họp ngắn rà soát kết quả ngày 1: Điền đánh giá khả năng đọc hiểu tài liệu của 3 thành viên mới; Phú báo cáo kết quả khảo sát code; chốt lịch cài đặt môi trường Ngày 2.", 
         "Cả nhóm", "Điền (Lead)", "Dễ", "Cao", "Lịch trình Tuần 1", 
         "Biên bản check-in Ngày 1 & Danh mục đầu việc Ngày 2", "5 thành viên tham gia đầy đủ, xác nhận không còn vướng mắc về mục tiêu", "Đã hoàn thành"),

        # --- NGÀY 2: THỨ BA (15/09/2026) ---
        ("W1.D02.01", "15/09/2026", "Thứ Ba", "Báo cáo Test Plan", "Soạn thảo Mục 1.1: Giới thiệu hệ thống kiểm thử", 
         "Viết nội dung Mục 1.1.1 Mô tả tổng quan về website bán máy tính Store EF V3; vẽ/chèn sơ đồ kiến trúc 3 tầng MVC 5; trình bày bảng công nghệ (ASP.NET MVC 5, EF 6, LocalDB, Serilog, BCrypt).", 
         "Điền (Lead)", "Phú", "Trung bình", "Cao", "Docs/CHECKLIST_TESTING_PLAN.md (1.1.1)", 
         "Bản thảo hoàn chỉnh Mục 1.1.1 kèm Sơ đồ kiến trúc hệ thống", "Trình bày mạch lạc, có hình vẽ kiến trúc rõ ràng, chú thích Caption đầy đủ", "Đang thực hiện"),

        ("W1.D02.02", "15/09/2026", "Thứ Ba", "Báo cáo Test Plan", "Soạn thảo Mục 1.1: Trình bày sơ đồ ERD CSDL", 
         "Vẽ sơ đồ ERD 10 bảng dữ liệu (`User@`, `UserDetail`, `Product`, `Category`, `Brand`, `Gallery`, `Cart`, `Order@`, `OrderDetail`, `Review`); mô tả chi tiết quan hệ 1-n, 1-1 và khóa ngoại.", 
         "Điền (Lead)", "Phú", "Trung bình", "Cao", "Docs/CHECKLIST_TESTING_PLAN.md & Store.sql", 
         "Bản vẽ sơ đồ ERD CSDL chuẩn kèm bảng chú giải 10 bảng", "Đầy đủ 10 bảng dữ liệu, đúng tên trường và kiểu dữ liệu chính", "Đang thực hiện"),

        ("W1.D02.03", "15/09/2026", "Thứ Ba", "Báo cáo Test Plan", "Soạn thảo Mục 1.1.2: Các chức năng chính & RBAC", 
         "Viết mô tả 5 phân hệ chức năng lớn của website; xây dựng Bảng ma trận phân quyền truy cập (RBAC Matrix) giữa 4 vai trò: Guest, User, Employee, Admin.", 
         "Điền (Lead)", "Phú", "Trung bình", "Cao", "Docs/CHECKLIST_TESTING_PLAN.md (1.1.2)", 
         "Nội dung Mục 1.1.2 hoàn chỉnh kèm Bảng ma trận phân quyền RBAC", "Bảng RBAC bao phủ đầy đủ 12 nhóm chức năng chính của hệ thống", "Đang thực hiện"),

        ("W1.D02.04", "15/09/2026", "Thứ Ba", "Quản trị dự án", "Giám sát & Đôn đốc tiến độ cài đặt môi trường", 
         "Theo dõi tiến độ cài đặt Visual Studio, SQL LocalDB trên máy của Thoại, Long, Nam; điều phối Phú hỗ trợ kịp thời các trường hợp gặp lỗi kỹ thuật.", 
         "Điền (Lead)", "Thoại, Long, Nam", "Dễ", "Cao", "Kế hoạch Cột mốc M1", 
         "Bảng trạng thái cài đặt môi trường trên 5 máy tính", "Phát hiện và xử lý ngay các sự cố phát sinh không để trễ hạn", "Đang thực hiện"),

        ("W1.D02.05", "15/09/2026", "Thứ Ba", "Hạ tầng kỹ thuật", "Thiết lập Môi trường Master trên máy cá nhân", 
         "Cài đặt hoàn chỉnh Visual Studio 2022 Enterprise/Community, SQL Server LocalDB, IIS Express; cấu hình kết nối chuẩn `(localdb)\\MSSQLLocalDB` trong `Web.config`.", 
         "Phú", "Điền (Lead)", "Trung bình", "Khẩn", "Docs/CHECKLIST_TESTING_PLAN.md (1.4.1)", 
         "Môi trường Master hoàn chỉnh, đóng vai trò máy mẫu đối chiếu", "Build solution 0 lỗi, kết nối LocalDB mượt mà, khởi động web dưới 5s", "Đã hoàn thành"),

        ("W1.D02.06", "15/09/2026", "Thứ Ba", "CSDL & Backend", "Restore CSDL Store.sql & Kiểm tra Triggers / SP", 
         "Chạy script `Store.sql` tạo CSDL `Store`; thực thi kiểm tra sự tồn tại của 10 bảng, kiểm tra logic Trigger `Tri_AddProduct` (tự thêm Gallery IsPrimary=1) và SP `AddCart`.", 
         "Phú", "Nam", "Khó", "Cao", "Store.sql", 
         "CSDL `Store` hoạt động hoàn hảo trên LocalDB", "Dữ liệu mẫu đầy đủ, 3 triggers và Stored Procedure không báo lỗi cú pháp", "Đã hoàn thành"),

        ("W1.D02.07", "15/09/2026", "Thứ Ba", "Hạ tầng kỹ thuật", "Kiểm thử file run.bat & Web Server port 5000", 
         "Chạy thử file `run.bat`, xác minh IIS Express lắng nghe tại `http://localhost:5000`, mở trình duyệt kiểm tra hiển thị banner, danh sách laptop, navbar và footer.", 
         "Phú", "Điền (Lead)", "Trung bình", "Cao", "run.bat & Web.config", 
         "Ảnh chụp màn hình web chạy trên port 5000 không có lỗi console", "Tất cả ảnh tĩnh và stylesheet load đầy đủ mã HTTP 200", "Đã hoàn thành"),

        ("W1.D02.08", "15/09/2026", "Thứ Ba", "Hỗ trợ kỹ thuật", "Kèm cặp & Hướng dẫn kỹ thuật cho Thoại, Long, Nam", 
         "Hỗ trợ trực tiếp (UltraViewer/Meet) hướng dẫn Thoại, Long, Nam cài đặt VS 2022, kết nối LocalDB, giải quyết lỗi xung đột port 5000 và quyền ghi thư mục ảnh `Content/Uploads/`.", 
         "Phú", "Thoại, Long, Nam", "Khó", "Khẩn", "Tài liệu Setup Quickstart Guide", 
         "3 thành viên khắc phục xong toàn bộ lỗi cài đặt phát sinh", "Kiên nhẫn hướng dẫn từng bước, giải thích bản chất lỗi kỹ thuật cho các bạn", "Đang thực hiện"),

        ("W1.D02.09", "15/09/2026", "Thứ Ba", "Cài đặt môi trường", "Cài đặt Visual Studio & LocalDB trên Máy 3", 
         "Tải và cài đặt Visual Studio 2019/2022 kèm workload ASP.NET and web development; kiểm tra cài đặt SQL Server LocalDB trên máy tính cá nhân.", 
         "Thoại", "Phú", "Trung bình", "Khẩn", "Tài liệu Setup Quickstart Guide", 
         "Visual Studio và LocalDB cài đặt thành công trên Máy 3", "Mở được Visual Studio và nhận diện công cụ MSSQLLocalDB", "Đang thực hiện"),

        ("W1.D02.10", "15/09/2026", "Thứ Ba", "Cài đặt môi trường", "Restore CSDL Store.sql trên Máy 3", 
         "Mở SQL Server Management Studio hoặc VS SQL Object Explorer, kết nối `(localdb)\\MSSQLLocalDB`, mở file `Store.sql` và nhấn Execute để khởi tạo database.", 
         "Thoại", "Phú", "Trung bình", "Cao", "Store.sql", 
         "Database `Store` hiển thị đầy đủ 10 bảng trong Object Explorer", "Không báo lỗi cú pháp T-SQL, có dữ liệu mẫu ban đầu", "Đang thực hiện"),

        ("W1.D02.11", "15/09/2026", "Thứ Ba", "Cài đặt môi trường", "Khởi chạy Web bằng run.bat & Chụp ảnh minh chứng Máy 3", 
         "Chạy file `run.bat`, mở trình duyệt truy cập `http://localhost:5000`, kiểm tra trang chủ hiển thị; chụp ảnh màn hình CSDL và Web UI gửi Trưởng nhóm Điền.", 
         "Thoại", "Điền (Lead)", "Dễ", "Cao", "run.bat", 
         "Ảnh chụp màn hình (1) CSDL Store trong SSMS, (2) Web chạy port 5000", "Hình ảnh rõ nét, chụp toàn màn hình có hiển thị thanh tác vụ ngày giờ", "Đang thực hiện"),

        ("W1.D02.12", "15/09/2026", "Thứ Ba", "Cài đặt môi trường", "Cài đặt Visual Studio & LocalDB trên Máy 4", 
         "Tải và cài đặt Visual Studio 2019/2022 kèm workload ASP.NET and web development; kiểm tra cài đặt SQL Server LocalDB trên máy tính cá nhân.", 
         "Long", "Phú", "Trung bình", "Khẩn", "Tài liệu Setup Quickstart Guide", 
         "Visual Studio và LocalDB cài đặt thành công trên Máy 4", "Mở được Visual Studio và nhận diện công cụ MSSQLLocalDB", "Đang thực hiện"),

        ("W1.D02.13", "15/09/2026", "Thứ Ba", "Cài đặt môi trường", "Restore CSDL Store.sql trên Máy 4", 
         "Mở SQL Server Management Studio hoặc VS SQL Object Explorer, kết nối `(localdb)\\MSSQLLocalDB`, mở file `Store.sql` và nhấn Execute để khởi tạo database.", 
         "Long", "Phú", "Trung bình", "Cao", "Store.sql", 
         "Database `Store` hiển thị đầy đủ 10 bảng trong Object Explorer", "Không báo lỗi cú pháp T-SQL, có dữ liệu mẫu ban đầu", "Đang thực hiện"),

        ("W1.D02.14", "15/09/2026", "Thứ Ba", "Cài đặt môi trường", "Khởi chạy Web bằng run.bat & Chụp ảnh minh chứng Máy 4", 
         "Chạy file `run.bat`, mở trình duyệt truy cập `http://localhost:5000`, kiểm tra trang chủ hiển thị; chụp ảnh màn hình CSDL và Web UI gửi Trưởng nhóm Điền.", 
         "Long", "Điền (Lead)", "Dễ", "Cao", "run.bat", 
         "Ảnh chụp màn hình (1) CSDL Store trong SSMS, (2) Web chạy port 5000", "Hình ảnh rõ nét, chụp toàn màn hình có hiển thị thanh tác vụ ngày giờ", "Đang thực hiện"),

        ("W1.D02.15", "15/09/2026", "Thứ Ba", "Cài đặt môi trường", "Cài đặt Visual Studio & LocalDB trên Máy 5", 
         "Tải và cài đặt Visual Studio 2019/2022 kèm workload ASP.NET and web development; kiểm tra cài đặt SQL Server LocalDB trên máy tính cá nhân.", 
         "Nam", "Phú", "Trung bình", "Khẩn", "Tài liệu Setup Quickstart Guide", 
         "Visual Studio và LocalDB cài đặt thành công trên Máy 5", "Mở được Visual Studio và nhận diện công cụ MSSQLLocalDB", "Đang thực hiện"),

        ("W1.D02.16", "15/09/2026", "Thứ Ba", "Cài đặt môi trường", "Restore CSDL Store.sql trên Máy 5", 
         "Mở SQL Server Management Studio hoặc VS SQL Object Explorer, kết nối `(localdb)\\MSSQLLocalDB`, mở file `Store.sql` và nhấn Execute để khởi tạo database.", 
         "Nam", "Phú", "Trung bình", "Cao", "Store.sql", 
         "Database `Store` hiển thị đầy đủ 10 bảng trong Object Explorer", "Không báo lỗi cú pháp T-SQL, có dữ liệu mẫu ban đầu", "Đang thực hiện"),

        ("W1.D02.17", "15/09/2026", "Thứ Ba", "Cài đặt môi trường", "Khởi chạy Web bằng run.bat & Chụp ảnh minh chứng Máy 5", 
         "Chạy file `run.bat`, mở trình duyệt truy cập `http://localhost:5000`, kiểm tra trang chủ hiển thị; chụp ảnh màn hình CSDL và Web UI gửi Trưởng nhóm Điền.", 
         "Nam", "Điền (Lead)", "Dễ", "Cao", "run.bat", 
         "Ảnh chụp màn hình (1) CSDL Store trong SSMS, (2) Web chạy port 5000", "Hình ảnh rõ nét, chụp toàn màn hình có hiển thị thanh tác vụ ngày giờ", "Đang thực hiện"),

        ("W1.D02.18", "15/09/2026", "Thứ Ba", "Quản trị dự án", "Họp Daily Check-in Ngày 2 (17:00 - 17:30)", 
         "Tổ chức họp kiểm điểm tiến độ cài đặt môi trường 5 máy: Điền nghiệm thu ảnh chụp màn hình; Phú xác nhận tình trạng kỹ thuật; phân công kịch bản khảo sát thực tế cho Ngày 3.", 
         "Cả nhóm", "Điền (Lead)", "Dễ", "Cao", "Tiến độ Tuần 1", 
         "Biên bản check-in Ngày 2 & Bảng xác nhận 5 máy sẵn sàng", "100% thành viên hoàn thành môi trường hoặc có kế hoạch xử lý dứt điểm tối nay", "Đang thực hiện"),

        # --- NGÀY 3: THỨ TƯ (16/09/2026) ---
        ("W1.D03.01", "16/09/2026", "Thứ Tư", "Báo cáo Test Plan", "Soạn thảo Mục 1.2: Mục tiêu kiểm thử & KPI", 
         "Xác định 5 mục tiêu chất lượng cốt lõi: Tính đúng đắn luồng nghiệp vụ, An toàn bảo mật BCrypt/RBAC, Toàn vẹn dữ liệu Trigger/SP, Tương thích trình duyệt, Xử lý ngoại lệ; xác định chỉ số KPI (Pass rate ≥ 95%, UT coverage ≥ 70%).", 
         "Điền (Lead)", "Phú", "Trung bình", "Cao", "Docs/CHECKLIST_TESTING_PLAN.md (1.2.1)", 
         "Bản thảo Mục 1.2.1 hoàn chỉnh kèm Bảng chỉ số KPI chất lượng", "Chỉ số KPI có căn cứ đo lường cụ thể, phù hợp với quy mô đồ án", "Đang thực hiện"),

        ("W1.D03.02", "16/09/2026", "Thứ Tư", "Báo cáo Test Plan", "Soạn thảo Mục 1.2: Phạm vi In/Out-Scope & Đối tượng test", 
         "Lập bảng phân loại Trong phạm vi (In-Scope) và Ngoài phạm vi (Out-of-Scope); liệt kê chi tiết danh mục đối tượng kiểm thử (Controllers, Extensions, Views, DB Triggers, Stored Procedure).", 
         "Điền (Lead)", "Phú", "Trung bình", "Cao", "Docs/CHECKLIST_TESTING_PLAN.md (1.2.2 & 1.2.3)", 
         "Bản thảo Mục 1.2.2 và 1.2.3 hoàn chỉnh với 2 bảng danh mục chi tiết", "Phân định rõ ràng giới hạn kiểm thử, tránh phình to phạm vi", "Đang thực hiện"),

        ("W1.D03.03", "16/09/2026", "Thứ Tư", "Báo cáo Test Plan", "Soạn thảo Mục 1.3: Chiến lược & Các mức kiểm thử", 
         "Trình bày chiến lược kiểm thử gia tăng (Incremental); mô tả 4 cấp độ kiểm thử (Unit Test, Integration Test, System Test, UAT); mô tả 4 loại kiểm thử (Chức năng, Bảo mật, Tương thích, Ngoại lệ).", 
         "Điền (Lead)", "Phú", "Trung bình", "Cao", "Docs/CHECKLIST_TESTING_PLAN.md (1.3.1, 1.3.2, 1.3.3)", 
         "Nội dung Mục 1.3.1 đến 1.3.3 hoàn chỉnh trong file báo cáo", "Lý thuyết gắn kết chặt chẽ với các chức năng thực tế của Store EF V3", "Đang thực hiện"),

        ("W1.D03.04", "16/09/2026", "Thứ Tư", "Báo cáo Test Plan", "Soạn thảo Mục 1.3: Ma trận trách nhiệm RACI", 
         "Xây dựng Bảng ma trận RACI cho 5 thành viên (Điền, Phú, Thoại, Long, Nam) tương ứng với 10 công việc chính trong suốt vòng đời đồ án kiểm thử.", 
         "Điền (Lead)", "Cả nhóm", "Trung bình", "Cao", "Docs/CHECKLIST_TESTING_PLAN.md (1.3.4)", 
         "Bảng ma trận phân công trách nhiệm RACI chi tiết 5 thành viên", "Mỗi đầu việc có duy nhất 1 người chịu trách nhiệm chính (A - Accountable)", "Đang thực hiện"),

        ("W1.D03.05", "16/09/2026", "Thứ Tư", "Báo cáo Test Plan", "Soạn thảo Mục 1.3.6: Phân tích và quản lý rủi ro", 
         "Lập Bảng phân tích 6 rủi ro kỹ thuật trọng yếu (R1 đến R6: Quyền thư mục ảnh, Xung đột ConnectionString, Mất dữ liệu DEF-01, Thiếu thời gian UT, Sập app do Regex DEF-02, CheckOut chưa lưu DB DEF-03) và biện pháp giảm thiểu.", 
         "Điền (Lead)", "Phú", "Khó", "Cao", "Docs/CHECKLIST_TESTING_PLAN.md (1.3.6)", 
         "Bảng phân tích rủi ro 6 rủi ro kỹ thuật (Khả năng x Mức độ ảnh hưởng)", "Có biện pháp phòng ngừa chủ động và kế hoạch dự phòng rõ ràng", "Đang thực hiện"),

        ("W1.D03.06", "16/09/2026", "Thứ Tư", "Kiểm thử tự động", "Cài đặt & Khảo sát công cụ Selenium IDE", 
         "Cài đặt extension Selenium IDE trên Chrome/Edge; tạo project kiểm thử mới, tìm hiểu các lệnh Command cơ bản (`open`, `type`, `click`, `assertText`, `verifyElementPresent`), kiểm tra cơ chế Record & Playback.", 
         "Phú", "Điền (Lead)", "Trung bình", "Cao", "Selenium IDE Documentation", 
         "File project mẫu `.side` chạy thử nghiệm Record/Playback", "Selenium IDE hoạt động ổn định, ghi nhận được các selector CSS/XPath", "Đang thực hiện"),

        ("W1.D03.07", "16/09/2026", "Thứ Tư", "Kiểm thử đơn vị", "Kiểm tra MSTest Store.Tests & Viết test mẫu", 
         "Mở project `Store.Tests`, cấu hình tham chiếu sang `Store`; viết thử nghiệm 1 Test Method hoàn chỉnh cho `Helpers.IsValidEmail()` kiểm tra các trường hợp email đúng và email sai cú pháp; chạy Test Explorer Pass xanh.", 
         "Phú", "Điền (Lead)", "Khó", "Cao", "Store.Tests & Helpers.cs", 
         "Mã nguồn Unit Test mẫu trong Store.Tests chạy 100% Pass", "Test Method viết theo chuẩn AAA (Arrange - Act - Assert), có Assert.AreEqual", "Đang thực hiện"),

        ("W1.D03.08", "16/09/2026", "Thứ Tư", "Phân tích mã nguồn", "Phân tích sâu lỗi DEF-01 & DEF-03 trong Controller", 
         "Mở `CartController.cs` xem xét phương thức `Remove` (phát hiện lỗi xóa nhầm bản ghi bảng `Product`); mở `CheckOutController.cs` kiểm tra logic đặt hàng (phát hiện thiếu code insert CSDL `Order_` và `OrderDetail`).", 
         "Phú", "Nam", "Rất khó", "Cao", "CartController.cs & CheckOutController.cs", 
         "Bản phân tích mã nguồn chi tiết về nguyên nhân gây lỗi DEF-01 và DEF-03", "Chỉ rõ số dòng code gây lỗi và giải thích cơ chế xung đột CSDL", "Đang thực hiện"),

        ("W1.D03.09", "16/09/2026", "Thứ Tư", "Chuẩn hóa quy trình", "Xây dựng Template Test Case Excel chuẩn hóa", 
         "Thiết kế file Excel mẫu viết Test Case với đầy đủ các cột: Test ID, Phân hệ, Tên kịch bản, Tiền điều kiện, Các bước thực hiện, Dữ liệu thử nghiệm, Kết quả mong đợi, Kết quả thực tế, Trạng thái (Pass/Fail), Mức độ ưu tiên.", 
         "Phú", "Thoại, Long, Nam", "Trung bình", "Khẩn", "Docs/CHECKLIST_TESTING_PLAN.md (Chương 2)", 
         "File Excel `TEMPLATE_TEST_CASE_STANDARD.xlsx` chia sẻ cho nhóm", "Biểu mẫu chuyên nghiệp, có Conditional Formatting tự đổi màu Pass/Fail", "Đang thực hiện"),

        ("W1.D03.10", "16/09/2026", "Thứ Tư", "Kiểm thử thăm dò Auth", "Thực hiện Exploratory Test trên form Đăng ký & Đăng nhập", 
         "Mở web trên Máy 3, thử đăng ký tài khoản mới: Thử nhập email hợp lệ, email sai định dạng (thiếu `@`), bỏ trống trường, mật khẩu dưới 6 ký tự; thử đăng nhập tài khoản vừa tạo và các tài khoản có sẵn (`admin1`, `user1`).", 
         "Thoại", "Phú", "Trung bình", "Cao", "Màn hình SignUp & SignIn trên web", 
         "Nhật ký kiểm thử thăm dò form Đăng ký/Đăng nhập kèm ảnh chụp", "Ghi nhận chính xác các thông báo validation hiển thị trên giao diện", "Đang thực hiện"),

        ("W1.D03.11", "16/09/2026", "Thứ Tư", "Khảo sát CSDL Auth", "Kiểm tra cơ chế băm mật khẩu BCrypt trong DB", 
         "Sau khi đăng ký tài khoản mới trên web, mở SSMS truy vấn bảng `User@`, quan sát giá trị cột `PasswordHash` để xác minh mật khẩu đã được băm an toàn dạng `$2a$...` chứ không lưu dạng bản rõ (plaintext).", 
         "Thoại", "Phú", "Trung bình", "Cao", "Bảng User@ trong SQL Server", 
         "Ảnh chụp màn hình kết quả câu lệnh `SELECT * FROM [User@]`", "Xác nhận trường PasswordHash có độ dài 60 ký tự băm BCrypt", "Đang thực hiện"),

        ("W1.D03.12", "16/09/2026", "Thứ Tư", "Kiểm thử thăm dò Auth", "Thử nghiệm Đăng xuất & Nút Back trình duyệt", 
         "Đăng nhập tài khoản, sau đó bấm Đăng xuất; thử bấm nút 'Back' (Quay lại) trên trình duyệt để kiểm tra xem hệ thống có thu hồi Session hay vẫn cho phép xem trang cá nhân.", 
         "Thoại", "Điền (Lead)", "Dễ", "Trung bình", "Luồng Logout & Browser Session", 
         "Ghi chú kết quả hành vi của trình duyệt sau khi đăng xuất", "Ghi nhận rõ ràng hệ thống có chuyển hướng về trang SignIn hay không", "Đang thực hiện"),

        ("W1.D03.13", "16/09/2026", "Thứ Tư", "Kiểm thử thăm dò Product", "Thực hiện Exploratory Test duyệt danh sách & phân trang", 
         "Duyệt danh sách sản phẩm trang chủ và trang Products: Đếm số lượng sản phẩm mỗi trang (kiểm tra quy định 8 sp/trang); bấm chuyển sang Trang 2, Trang 3; kiểm tra hiển thị nút Previous/Next.", 
         "Long", "Phú", "Dễ", "Cao", "Màn hình Products/Index", 
         "Nhật ký kiểm thử thăm dò Danh sách & Phân trang sản phẩm kèm ảnh", "Ghi nhận tính chính xác của PagedList trên các màn hình", "Đang thực hiện"),

        ("W1.D03.14", "16/09/2026", "Thứ Tư", "Kiểm thử thăm dò Product", "Thử nghiệm Bộ lọc Category, Brand & Tìm kiếm", 
         "Bấm chọn lọc theo từng Danh mục (Laptop, Desktop...) và Thương hiệu (Dell, HP, Asus...); thử kết hợp lọc đồng thời Danh mục + Thương hiệu; thử gõ tìm kiếm từ khóa chính xác và từ khóa không tồn tại.", 
         "Long", "Phú", "Trung bình", "Cao", "Bộ lọc Sidebar & Ô tìm kiếm Header", 
         "Nhật ký kiểm thử thăm dò Bộ lọc & Tìm kiếm sản phẩm", "Ghi nhận các trường hợp lọc ra sản phẩm và trường hợp trả về danh sách rỗng", "Đang thực hiện"),

        ("W1.D03.15", "16/09/2026", "Thứ Tư", "Kiểm thử thăm dò Product", "Thử nghiệm nhập ký tự đặc biệt vào ô tìm kiếm", 
         "Thử nhập các ký tự đặc biệt như `(`, `[`, `*`, `\\` vào ô tìm kiếm sản phẩm trên web và nhấn Enter; quan sát xem trang web có bị báo lỗi ngoại lệ sập màn hình (Regex Crash DEF-02) hay không.", 
         "Long", "Phú", "Khó", "Cao", "Ô tìm kiếm Search & Serilog Logs", 
         "Ảnh chụp màn hình thông báo lỗi/màn hình vàng ASP.NET khi tìm ký tự lạ", "Phát hiện hiện tượng bất thường khi tìm kiếm regex, thông báo cho Phú", "Đang thực hiện"),

        ("W1.D03.16", "16/09/2026", "Thứ Tư", "Kiểm thử thăm dò Cart", "Thực hiện Exploratory Test luồng Thêm vào giỏ", 
         "Thử bấm nút 'Thêm vào giỏ' khi chưa đăng nhập (kiểm tra điều hướng sang SignIn); đăng nhập tài khoản `user1`, bấm thêm sản phẩm vào giỏ, bấm nhiều lần kiểm tra số lượng trên badge giỏ hàng.", 
         "Nam", "Phú", "Trung bình", "Cao", "Nút Thêm vào giỏ & Badge Giỏ hàng", 
         "Nhật ký kiểm thử thăm dò chức năng Thêm vào giỏ hàng", "Ghi nhận chính xác phản hồi giao diện khi chưa đăng nhập và đã đăng nhập", "Đang thực hiện"),

        ("W1.D03.17", "16/09/2026", "Thứ Tư", "Khảo sát CSDL Cart", "Đối chiếu dữ liệu bảng Cart trong SQL Server", 
         "Mở SSMS truy vấn bảng `Cart`, kiểm tra các cột `UserId`, `ProductId`, `Count`, `DateCreated` có tăng đúng theo số lần bấm thêm trên web hay không.", 
         "Nam", "Phú", "Khó", "Cao", "Bảng Cart trong CSDL SQL Server", 
         "Ảnh chụp màn hình câu lệnh `SELECT * FROM Cart` đối chiếu với web", "Dữ liệu trên web và dữ liệu trong CSDL khớp nhau hoàn toàn", "Đang thực hiện"),

        ("W1.D03.18", "16/09/2026", "Thứ Tư", "Kiểm thử thăm dò Cart", "Thử nghiệm Sửa số lượng, Xóa giỏ & CheckOut UI", 
         "Mở trang `/Cart/Index`, thử thay đổi số lượng món hàng, kiểm tra tính lại tổng tiền; bấm thử nút 'Xóa' sản phẩm khỏi giỏ; bấm chuyển sang form thanh toán `/CheckOut/Index` quan sát các trường thông tin.", 
         "Nam", "Phú", "Khó", "Cao", "Trang Cart/Index & CheckOut/Index", 
         "Nhật ký kiểm thử thao tác Giỏ hàng & Form CheckOut", "Ghi nhận hiện tượng sau khi bấm nút Xóa và các trường input của CheckOut", "Đang thực hiện"),

        ("W1.D03.19", "16/09/2026", "Thứ Tư", "Quản trị dự án", "Họp Daily Check-in Ngày 3 (17:00 - 17:30)", 
         "Tổ chức họp rà soát phát hiện thực tế: Thoại báo cáo luồng Auth, Long báo cáo hiện tượng search ký tự lạ, Nam báo cáo luồng giỏ hàng; Phú tóm tắt 2 bug code; Điền tổng hợp chuẩn bị nghiệm thu M1.", 
         "Cả nhóm", "Điền (Lead)", "Dễ", "Cao", "Tiến độ Ngày 3", 
         "Biên bản check-in Ngày 3 & Kế hoạch hoàn thiện Cột mốc M1 cho Ngày 4", "Đánh giá sơ bộ sự tiến bộ của 3 bạn Thoại, Long, Nam trong việc bắt lỗi", "Đang thực hiện"),

        # --- NGÀY 4: THỨ NĂM (17/09/2026) ---
        ("W1.D04.01", "17/09/2026", "Thứ Năm", "Báo cáo Test Plan", "Soạn thảo Mục 1.4: Môi trường & Công cụ kiểm thử", 
         "Tổng hợp bảng cấu hình phần cứng tối thiểu/khuyến nghị; bảng thông số phần mềm (Windows 10/11, .NET 4.7.2, LocalDB, IIS Express port 5000); bảng danh sách 5 tài khoản thử nghiệm chuẩn (`admin1`, `admin2`, `employee1`, `user1`, `user2`); danh mục công cụ (VS Test Explorer, Selenium IDE, Chrome DevTools, Excel).", 
         "Điền (Lead)", "Phú", "Trung bình", "Cao", "Docs/CHECKLIST_TESTING_PLAN.md (1.4)", 
         "Nội dung Mục 1.4 hoàn chỉnh với 4 bảng biểu thông số kỹ thuật", "Số liệu phần cứng, phần mềm chính xác, khớp với cấu hình thực tế 5 máy", "Chưa bắt đầu"),

        ("W1.D04.02", "17/09/2026", "Thứ Năm", "Báo cáo Test Plan", "Soạn thảo Mục 1.5: Tiêu chí đánh giá kiểm thử", 
         "Quy định chi tiết Tiêu chí bắt đầu (Entry Criteria), Tiêu chí tạm dừng và tiếp tục (Suspension & Resumption Criteria), Tiêu chí kết thúc kiểm thử (Exit Criteria) theo chuẩn ISO 29119.", 
         "Điền (Lead)", "Phú", "Trung bình", "Cao", "Docs/CHECKLIST_TESTING_PLAN.md (1.5)", 
         "Nội dung Mục 1.5 hoàn chỉnh với các điều kiện định lượng rõ ràng", "Các tiêu chí đo lường được (100% execute, ≥95% pass, 0 bug critical)", "Chưa bắt đầu"),

        ("W1.D04.03", "17/09/2026", "Thứ Năm", "Báo cáo Test Plan", "Soạn thảo Mục 1.6: Kết luận Chương 1", 
         "Tóm tắt các kết quả cốt lõi đã xác lập trong Kế hoạch kiểm thử; khẳng định sự sẵn sàng về môi trường, nhân sự và chiến lược để bước sang Chương 2 Thiết kế Test Case.", 
         "Điền (Lead)", "Cả nhóm", "Dễ", "Cao", "Docs/CHECKLIST_TESTING_PLAN.md (1.6)", 
         "Nội dung Mục 1.6 hoàn chỉnh trong file báo cáo Word", "Văn phong học thuật, ngắn gọn, súc tích, đúc kết đầy đủ ý", "Chưa bắt đầu"),

        ("W1.D04.04", "17/09/2026", "Thứ Năm", "Báo cáo Test Plan", "Format chuẩn & Tổng hợp Chương 1 vào Báo cáo Word", 
         "Tổng hợp toàn bộ nội dung Lời mở đầu và Chương 1 vào file Word chính thức; kiểm tra định dạng lề 3-2-2-2, font chữ, giãn dòng 1.25, đánh số Caption tự động cho hình ảnh/bảng biểu, cập nhật Mục lục tự động.", 
         "Điền (Lead)", "Phú", "Trung bình", "Khẩn", "File Word Báo cáo tổng thể", 
         "File Báo cáo Word hoàn chỉnh Chương 1 (khoảng 15-20 trang) chuẩn format", "Không lỗi font, không nhảy trang, mục lục liên kết đúng số trang", "Chưa bắt đầu"),

        ("W1.D04.05", "17/09/2026", "Thứ Năm", "Quản trị dự án", "Đánh giá năng lực thành viên sau Tuần 1", 
         "Tổng hợp nhật ký làm việc 4 ngày, chấm điểm đánh giá sơ bộ năng lực và thái độ của Thoại, Long, Nam theo 5 tiêu chí; lập phương án phân bổ số lượng Test Case chi tiết cho Tuần 2.", 
         "Điền (Lead)", "Phú", "Trung bình", "Cao", "Bảng theo dõi thành viên Tuần 1", 
         "Bảng đánh giá năng lực 5 thành viên và đề xuất phân công Tuần 2", "Khách quan, công bằng, phân bổ khối lượng Tuần 2 vừa sức từng bạn", "Chưa bắt đầu"),

        ("W1.D04.06", "17/09/2026", "Thứ Năm", "Hạ tầng kỹ thuật", "Nghiệm thu chéo Môi trường kiểm thử trên 5 máy", 
         "Kiểm tra xác nhận lần cuối: Đảm bảo 100% cả 5 máy của 5 thành viên đều kết nối LocalDB ổn định, CSDL có đủ 10 bảng dữ liệu mẫu, file `run.bat` chạy web port 5000 mượt mà.", 
         "Phú", "Thoại, Long, Nam", "Trung bình", "Khẩn", "Checklist Môi trường Cột mốc M1", 
         "Biên bản nghiệm thu kỹ thuật môi trường 5 máy tính đạt 100%", "Tất cả các máy đều sẵn sàng thực thi kiểm thử không còn lỗi môi trường", "Chưa bắt đầu"),

        ("W1.D04.07", "17/09/2026", "Thứ Năm", "Kiểm thử tự động", "Hoàn thiện Kịch bản tự động mẫu Selenium IDE", 
         "Ghi hoàn chỉnh 1 kịch bản tự động mẫu `Auto_TC_01_LoginSuccess.side` trên Selenium IDE; kiểm tra chạy playback tự động thành công (Pass màu xanh); xuất file lưu vào thư mục `Docs/AutomationScripts/`.", 
         "Phú", "Điền (Lead)", "Khó", "Cao", "Selenium IDE & Auth/SignIn", 
         "File kịch bản tự động `.side` mẫu chạy Pass 100%", "Kịch bản có các bước mở trang, nhập user/pass, click submit và assert URL", "Chưa bắt đầu"),

        ("W1.D04.08", "17/09/2026", "Thứ Năm", "Kiểm thử đơn vị", "Kiểm tra toàn diện Solution & Store.Tests", 
         "Mở Visual Studio, chạy Rebuild Solution `Store.sln` (gồm project chính `Store` và project `Store.Tests`), đảm bảo 0 Errors, 0 Warnings; chạy Test Explorer xác nhận bài unit test mẫu Pass.", 
         "Phú", "Điền (Lead)", "Khó", "Cao", "Visual Studio Test Explorer", 
         "Ảnh chụp màn hình Test Explorer màu xanh (100% Pass)", "Không có bất kỳ xung đột thư viện hay lỗi build nào", "Chưa bắt đầu"),

        ("W1.D04.09", "17/09/2026", "Thứ Năm", "Đào tạo nội bộ", "Hướng dẫn kỹ thuật thiết kế Test Case (EP & BVA)", 
         "Chủ trì buổi trao đổi nội bộ 30 phút hướng dẫn Thoại, Long, Nam về: Kỹ thuật Phân vùng tương đương (EP), Phân tích giá trị biên (BVA) và cách điền vào Template Test Case chuẩn bị cho Tuần 2.", 
         "Phú", "Thoại, Long, Nam", "Trung bình", "Cao", "Tài liệu EP, BVA & Template Test Case", 
         "Slide/Tài liệu hướng dẫn ngắn về kỹ thuật EP/BVA áp dụng cho Store EF", "3 thành viên nắm được cách xác định ca Positive, Negative và Giá trị biên", "Chưa bắt đầu"),

        ("W1.D04.10", "17/09/2026", "Thứ Năm", "Thiết kế Test Case sơ bộ", "Hoàn thiện Ma trận yêu cầu kiểm thử phân hệ Auth", 
         "Tổng hợp kết quả khảo sát, lập Ma trận yêu cầu kiểm thử (Test Requirements Matrix) cho Phân hệ Xác thực & Tài khoản: Xác định danh sách khoảng 25 - 30 ca test dự kiến viết trong Tuần 2.", 
         "Thoại", "Điền (Lead)", "Trung bình", "Cao", "Docs/CHECKLIST_TESTING_PLAN.md (2.2.1)", 
         "Bảng Ma trận yêu cầu kiểm thử Auth (25-30 ca test dự kiến)", "Bao phủ đầy đủ Đăng ký, Đăng nhập, Đăng xuất, Profile, Đổi mật khẩu, UserAdmin", "Chưa bắt đầu"),

        ("W1.D04.11", "17/09/2026", "Thứ Năm", "Thiết kế Test Case sơ bộ", "Viết thử nghiệm 5 Test Case mẫu phân hệ Auth", 
         "Sử dụng Template Test Case của Phú, viết hoàn chỉnh 5 ca kiểm thử mẫu cho chức năng Đăng ký tài khoản (1 ca hợp lệ, 2 ca biên độ dài mật khẩu, 1 ca email sai định dạng, 1 ca email trùng).", 
         "Thoại", "Phú", "Trung bình", "Cao", "Template Test Case & Form SignUp", 
         "File Excel chứa 5 Test Case mẫu phân hệ Auth theo chuẩn", "Đầy đủ Pre-condition, Test Steps, Test Data cụ thể và Expected Result rõ ràng", "Chưa bắt đầu"),

        ("W1.D04.12", "17/09/2026", "Thứ Năm", "Bàn giao Tuần 1", "Nộp Báo cáo khảo sát Auth & Checklist môi trường Máy 3", 
         "Đóng gói ảnh chụp màn hình minh chứng môi trường Máy 3, nhật ký khảo sát và 5 Test Case mẫu vào thư mục cá nhân trên Google Drive, báo cáo Trưởng nhóm Điền.", 
         "Thoại", "Điền (Lead)", "Dễ", "Cao", "Thư mục Google Drive cá nhân", 
         "Bộ hồ sơ nghiệm thu Tuần 1 phân hệ Auth của Thoại", "Đầy đủ file và đúng quy cách đặt tên theo quy định", "Chưa bắt đầu"),

        ("W1.D04.13", "17/09/2026", "Thứ Năm", "Thiết kế Test Case sơ bộ", "Hoàn thiện Ma trận yêu cầu kiểm thử phân hệ Product", 
         "Tổng hợp kết quả khảo sát, lập Ma trận yêu cầu kiểm thử (Test Requirements Matrix) cho Phân hệ Sản phẩm & Quản trị: Xác định danh sách khoảng 30 - 35 ca test dự kiến viết trong Tuần 2.", 
         "Long", "Điền (Lead)", "Trung bình", "Cao", "Docs/CHECKLIST_TESTING_PLAN.md (2.2.2 - 2.2.4)", 
         "Bảng Ma trận yêu cầu kiểm thử Product (30-35 ca test dự kiến)", "Bao phủ đầy đủ List, Paging, Filter Category/Brand, Search, Details, CRUD", "Chưa bắt đầu"),

        ("W1.D04.14", "17/09/2026", "Thứ Năm", "Thiết kế Test Case sơ bộ", "Viết thử nghiệm 5 Test Case mẫu phân hệ Product", 
         "Sử dụng Template Test Case của Phú, viết hoàn chỉnh 5 ca kiểm thử mẫu cho chức năng Tìm kiếm & Lọc sản phẩm (1 ca tìm đúng, 1 ca tìm một phần, 1 ca tìm rỗng, 1 ca ký tự đặc biệt, 1 ca lọc kết hợp).", 
         "Long", "Phú", "Trung bình", "Cao", "Template Test Case & Products View", 
         "File Excel chứa 5 Test Case mẫu phân hệ Product theo chuẩn", "Đầy đủ các bước thực hiện và dữ liệu test đầu vào cụ thể", "Chưa bắt đầu"),

        ("W1.D04.15", "17/09/2026", "Thứ Năm", "Bàn giao Tuần 1", "Nộp Báo cáo khảo sát Product & Checklist môi trường Máy 4", 
         "Đóng gói ảnh chụp màn hình minh chứng môi trường Máy 4, nhật ký khảo sát và 5 Test Case mẫu vào thư mục cá nhân trên Google Drive, báo cáo Trưởng nhóm Điền.", 
         "Long", "Điền (Lead)", "Dễ", "Cao", "Thư mục Google Drive cá nhân", 
         "Bộ hồ sơ nghiệm thu Tuần 1 phân hệ Product của Long", "Đầy đủ file và đúng quy cách đặt tên theo quy định", "Chưa bắt đầu"),

        ("W1.D04.16", "17/09/2026", "Thứ Năm", "Thiết kế Test Case sơ bộ", "Hoàn thiện Ma trận yêu cầu kiểm thử Giỏ hàng & CheckOut", 
         "Tổng hợp kết quả khảo sát, lập Ma trận yêu cầu kiểm thử (Test Requirements Matrix) cho Phân hệ Giỏ hàng & Thanh toán: Xác định danh sách khoảng 25 - 30 ca test dự kiến viết trong Tuần 2.", 
         "Nam", "Điền (Lead)", "Trung bình", "Cao", "Docs/CHECKLIST_TESTING_PLAN.md (2.2.2 & 2.3)", 
         "Bảng Ma trận yêu cầu kiểm thử Cart & CheckOut (25-30 ca test dự kiến)", "Bao phủ Thêm giỏ, Sửa số lượng, Xóa món DEF-01, CheckOut DEF-03, Trigger CSDL", "Chưa bắt đầu"),

        ("W1.D04.17", "17/09/2026", "Thứ Năm", "Thiết kế Test Case sơ bộ", "Viết thử nghiệm 5 Test Case mẫu phân hệ Giỏ hàng", 
         "Sử dụng Template Test Case của Phú, viết hoàn chỉnh 5 ca kiểm thử mẫu cho chức năng Giỏ hàng (1 ca thêm khi chưa login, 1 ca thêm khi đã login, 1 ca tăng số lượng, 1 ca xóa món, 1 ca tính tổng tiền).", 
         "Nam", "Phú", "Trung bình", "Cao", "Template Test Case & Cart View", 
         "File Excel chứa 5 Test Case mẫu phân hệ Giỏ hàng theo chuẩn", "Đầy đủ các bước thực hiện, tiền điều kiện và kết quả mong đợi rõ ràng", "Chưa bắt đầu"),

        ("W1.D04.18", "17/09/2026", "Thứ Năm", "Bàn giao Tuần 1", "Nộp Báo cáo khảo sát Cart & Checklist môi trường Máy 5", 
         "Đóng gói ảnh chụp màn hình minh chứng môi trường Máy 5, nhật ký khảo sát và 5 Test Case mẫu vào thư mục cá nhân trên Google Drive, báo cáo Trưởng nhóm Điền.", 
         "Nam", "Điền (Lead)", "Dễ", "Cao", "Thư mục Google Drive cá nhân", 
         "Bộ hồ sơ nghiệm thu Tuần 1 phân hệ Cart/Order của Nam", "Đầy đủ file và đúng quy cách đặt tên theo quy định", "Chưa bắt đầu"),

        ("W1.D04.19", "17/09/2026", "Thứ Năm", "Quản trị dự án", "Họp Tổng kết & Nghiệm thu Cột mốc 1 (16:30 - 17:30)", 
         "Chủ trì cuộc họp tổng kết Tuần 1: Nghiệm thu môi trường 5 máy đạt 100%, nghiệm thu bản thảo Chương 1 Test Plan, nghiệm thu các ma trận yêu cầu test; ký biên bản nghiệm thu Cột mốc M1 và phát động kế hoạch Tuần 2.", 
         "Cả nhóm", "Điền (Lead)", "Trung bình", "Khẩn", "Toàn bộ hồ sơ bàn giao Tuần 1", 
         "Biên bản nghiệm thu Cột mốc 1 (M1) hoàn thành 100% & Kế hoạch Tuần 2", "100% thành viên ký xác nhận hoàn thành nhiệm vụ Tuần 1, sẵn sàng cho Tuần 2", "Chưa bắt đầu"),
    ]

    r = 5
    for task in tasks_raw:
        tid, dt, dow, mod, name, desc, owner, rev, diff, prio, ref, deliv, dod, status = task
        ws2.row_dimensions[r].height = 36

        fill_curr = fill_zebra_light if (r % 2 == 0) else fill_white

        c_tid = ws2.cell(r, 1, tid)
        c_tid.font = font_data_bold
        c_tid.alignment = align_center
        c_tid.fill = fill_curr
        c_tid.border = cell_border

        c_dt = ws2.cell(r, 2, dt)
        c_dt.font = font_data
        c_dt.alignment = align_center
        c_dt.fill = fill_curr
        c_dt.border = cell_border

        c_dow = ws2.cell(r, 3, dow)
        c_dow.font = font_data
        c_dow.alignment = align_center
        c_dow.fill = fill_curr
        c_dow.border = cell_border

        c_mod = ws2.cell(r, 4, mod)
        c_mod.font = font_data_bold
        c_mod.alignment = align_left
        c_mod.fill = fill_curr
        c_mod.border = cell_border

        c_name = ws2.cell(r, 5, name)
        c_name.font = font_data_bold
        c_name.alignment = align_left
        c_name.fill = fill_curr
        c_name.border = cell_border

        c_desc = ws2.cell(r, 6, desc)
        c_desc.font = font_data
        c_desc.alignment = align_top_left
        c_desc.fill = fill_curr
        c_desc.border = cell_border

        c_owner = ws2.cell(r, 7, owner)
        c_owner.alignment = align_center
        c_owner.border = cell_border
        if "Điền" in owner:
            c_owner.font = font_dien
            c_owner.fill = fill_tag_dien
        elif "Phú" in owner:
            c_owner.font = font_phu
            c_owner.fill = fill_tag_phu
        elif "Thoại" in owner:
            c_owner.font = font_thoai
            c_owner.fill = fill_tag_thoai
        elif "Long" in owner:
            c_owner.font = font_long
            c_owner.fill = fill_tag_long
        elif "Nam" in owner:
            c_owner.font = font_nam
            c_owner.fill = fill_tag_nam
        else:
            c_owner.font = font_all
            c_owner.fill = fill_tag_all

        c_rev = ws2.cell(r, 8, rev)
        c_rev.font = font_data
        c_rev.alignment = align_center
        c_rev.fill = fill_curr
        c_rev.border = cell_border

        c_diff = ws2.cell(r, 9, diff)
        c_diff.alignment = align_center
        c_diff.border = cell_border
        if diff in ["Khó", "Rất khó"]:
            c_diff.font = font_alert
            c_diff.fill = fill_alert
        elif diff == "Trung bình":
            c_diff.font = font_warn
            c_diff.fill = fill_warn
        else:
            c_diff.font = font_pass
            c_diff.fill = fill_pass

        c_prio = ws2.cell(r, 10, prio)
        c_prio.alignment = align_center
        c_prio.border = cell_border
        if prio == "Khẩn":
            c_prio.font = font_alert
            c_prio.fill = fill_alert
        elif prio == "Cao":
            c_prio.font = font_warn
            c_prio.fill = fill_warn
        else:
            c_prio.font = font_info
            c_prio.fill = fill_info

        c_ref = ws2.cell(r, 11, ref)
        c_ref.font = font_data_italic
        c_ref.alignment = align_left
        c_ref.fill = fill_curr
        c_ref.border = cell_border

        c_deliv = ws2.cell(r, 12, deliv)
        c_deliv.font = font_data
        c_deliv.alignment = align_top_left
        c_deliv.fill = fill_curr
        c_deliv.border = cell_border

        c_dod = ws2.cell(r, 13, dod)
        c_dod.font = font_data
        c_dod.alignment = align_top_left
        c_dod.fill = fill_curr
        c_dod.border = cell_border

        c_status = ws2.cell(r, 14, status)
        c_status.alignment = align_center
        c_status.border = cell_border
        if status == "Đã hoàn thành":
            c_status.font = font_pass
            c_status.fill = fill_pass
        elif status == "Đang thực hiện":
            c_status.font = font_warn
            c_status.fill = fill_warn
        else:
            c_status.font = font_info
            c_status.fill = fill_info

        r += 1

    # Column widths for Sheet 2
    col_widths_s2 = {
        1: 13, 2: 12, 3: 11, 4: 20, 5: 28, 6: 42, 7: 15,
        8: 15, 9: 13, 10: 13, 11: 24, 12: 30, 13: 32, 14: 16
    }
    for c_idx, width in col_widths_s2.items():
        ws2.column_dimensions[get_column_letter(c_idx)].width = width

    # =========================================================================
    # SHEET 3: MA TRAN THEO DOI THANH VIEN & NANG LUC (WORKLOAD & EVALUATION)
    # =========================================================================
    ws3 = wb.create_sheet(title="Ma_Tran_Theo_Doi_Thanh_Vien")
    ws3.views.sheetView[0].showGridLines = True

    # Title Block
    ws3.merge_cells("A1:K1")
    ws3["A1"] = "BẢNG THEO DÕI KHỐI LƯỢNG CÔNG VIỆC & ĐÁNH GIÁ NĂNG LỰC THÀNH VIÊN TUẦN 1"
    ws3["A1"].font = Font(name="Segoe UI", size=13, bold=True, color="FFFFFF")
    ws3["A1"].fill = fill_navy
    ws3["A1"].alignment = align_center

    ws3.merge_cells("A2:K2")
    ws3["A2"] = "Dự án: Ecommerce Computer (Store EF V3) | Theo dõi khối lượng từng ngày và Bảng tiêu chí đánh giá năng lực thực tế sau Tuần 1"
    ws3["A2"].font = font_subtitle
    ws3["A2"].fill = fill_navy
    ws3["A2"].alignment = align_center

    ws3.row_dimensions[1].height = 24
    ws3.row_dimensions[2].height = 18

    # Section 1: Ma trận công việc 4 ngày
    ws3.merge_cells("A4:K4")
    ws3["A4"] = "1. MA TRẬN PHÂN BỔ CÔNG VIỆC HẰNG NGÀY CHO 5 THÀNH VIÊN (14/09 - 17/09/2026)"
    ws3["A4"].font = font_sec_header
    ws3["A4"].fill = fill_blue_sec
    ws3["A4"].alignment = align_left
    ws3.row_dimensions[4].height = 24

    headers_daily_matrix = [
        "Mã TV", "Họ và tên thành viên", "Vai trò chuyên trách",
        "Ngày 14/09 (D01 - T2)\nKhởi động & Khảo sát",
        "Ngày 15/09 (D02 - T3)\nCài đặt Môi trường",
        "Ngày 16/09 (D03 - T4)\nKhảo sát Nghiệp vụ",
        "Ngày 17/09 (D04 - T5)\nHoàn thiện Test Plan",
        "Tổng Task", "Tổng Giờ", "Đánh giá sơ bộ", "Trạng thái Tuần 1"
    ]

    r = 5
    for c_idx, h in enumerate(headers_daily_matrix, start=1):
        cell = ws3.cell(r, c_idx, h)
        cell.font = font_tbl_header
        cell.fill = fill_blue_head
        cell.alignment = align_center
        cell.border = header_border
    ws3.row_dimensions[r].height = 30

    daily_matrix_data = [
        ("TV01", "Điền (Trưởng nhóm)", "Test Lead / QA Project Manager",
         "• Họp Kick-off dự án\n• Lập Google Drive & Git\n• Ban hành biểu mẫu & DoD\n• Soạn Bìa, Lời cam đoan\n• Họp Daily Check-in D01",
         "• Soạn Mục 1.1.1 (Kiến trúc MVC)\n• Soạn Mục 1.1.2 (Sơ đồ ERD)\n• Soạn Ma trận RBAC\n• Giám sát tiến độ 5 máy\n• Họp Daily Check-in D02",
         "• Soạn Mục 1.2 (Mục tiêu & KPI)\n• Soạn Mục 1.2 (Phạm vi In/Out)\n• Soạn Mục 1.3 (Chiến lược test)\n• Soạn Ma trận RACI\n• Soạn Quản lý rủi ro R1-R6",
         "• Soạn Mục 1.4 (Môi trường/Tool)\n• Soạn Mục 1.5 (Tiêu chí Entry/Exit)\n• Soạn Mục 1.6 (Kết luận C1)\n• Format Báo cáo Word tổng\n• Đánh giá TV & Chủ trì họp M1",
         18, "32h", "Quản lý xuất sắc, bám sát tiến độ", "Hoàn thành 100%"),

        ("TV02", "Phú", "Technical Lead / Senior QA Tester",
         "• Khảo sát kiến trúc mã nguồn MVC\n• Khảo sát CSDL Store.sql\n• Khảo sát Store.Tests & Selenium\n• Viết tài liệu Quickstart Guide\n• Họp Daily Check-in D01",
         "• Setup Môi trường Master\n• Restore CSDL LocalDB & Triggers\n• Test run.bat port 5000\n• Kèm cặp kỹ thuật Thoại, Long, Nam\n• Họp Daily Check-in D02",
         "• Cài đặt Selenium IDE\n• Viết Unit test mẫu Helpers\n• Phân tích bug DEF-01, DEF-03\n• Chuẩn hóa Template Test Case\n• Họp Daily Check-in D03",
         "• Nghiệm thu chéo 5 máy\n• Hoàn thiện script tự động .side\n• Kiểm tra Rebuild Store.Tests\n• Hướng dẫn EP/BVA cho 3 bạn\n• Tham gia nghiệm thu M1",
         18, "32h", "Kỹ thuật vững vàng, hỗ trợ nhiệt tình", "Hoàn thành 100%"),

        ("TV03", "Thoại", "Junior Manual Tester (Auth & Account)",
         "• Tham gia họp Kick-off\n• Đọc hiểu tài liệu Auth\n• Liệt kê 6 Views phân hệ Auth\n• Họp Daily Check-in D01",
         "• Cài đặt Visual Studio 2022\n• Restore CSDL Store.sql Máy 3\n• Chạy run.bat port 5000\n• Chụp ảnh minh chứng nộp Lead\n• Họp Daily Check-in D02",
         "• Exploratory test SignUp/SignIn\n• Kiểm tra BCrypt hash trong DB\n• Thử Logout & Back trình duyệt\n• Ghi nhật ký khảo sát Auth\n• Họp Daily Check-in D03",
         "• Lập Ma trận yêu cầu test Auth\n• Viết 5 Test Case mẫu SignUp\n• Đóng gói hồ sơ nộp Trưởng nhóm\n• Tham gia hướng dẫn EP/BVA\n• Họp nghiệm thu Cột mốc M1",
         13, "24h", "Tiếp thu tốt, hoàn thành môi trường", "Hoàn thành 100%"),

        ("TV04", "Long", "Junior Manual Tester (Product & Catalog)",
         "• Tham gia họp Kick-off\n• Đọc hiểu tài liệu Product\n• Liệt kê 7 Views phân hệ Product\n• Họp Daily Check-in D01",
         "• Cài đặt Visual Studio 2022\n• Restore CSDL Store.sql Máy 4\n• Chạy run.bat port 5000\n• Chụp ảnh minh chứng nộp Lead\n• Họp Daily Check-in D02",
         "• Exploratory test PagedList\n• Thử lọc Category & Brand\n• Thử tìm kiếm ký tự lạ (Regex)\n• Ghi nhật ký khảo sát Product\n• Họp Daily Check-in D03",
         "• Lập Ma trận yêu cầu test Product\n• Viết 5 Test Case mẫu Search/Filter\n• Đóng gói hồ sơ nộp Trưởng nhóm\n• Tham gia hướng dẫn EP/BVA\n• Họp nghiệm thu Cột mốc M1",
         13, "24h", "Nhạy bén giao diện, phát hiện bug regex", "Hoàn thành 100%"),

        ("TV05", "Nam", "Junior Manual Tester (Cart & CheckOut)",
         "• Tham gia họp Kick-off\n• Đọc hiểu tài liệu Cart & Order\n• Liệt kê 4 Views Cart/CheckOut\n• Họp Daily Check-in D01",
         "• Cài đặt Visual Studio 2022\n• Restore CSDL Store.sql Máy 5\n• Chạy run.bat port 5000\n• Chụp ảnh minh chứng nộp Lead\n• Họp Daily Check-in D02",
         "• Exploratory test Thêm giỏ hàng\n• Đối chiếu dữ liệu bảng Cart DB\n• Thử sửa SL, xóa giỏ, CheckOut\n• Ghi nhật ký khảo sát Cart\n• Họp Daily Check-in D03",
         "• Lập Ma trận yêu cầu test Cart\n• Viết 5 Test Case mẫu Cart\n• Đóng gói hồ sơ nộp Trưởng nhóm\n• Tham gia hướng dẫn EP/BVA\n• Họp nghiệm thu Cột mốc M1",
         13, "24h", "Cẩn thận, theo dõi tốt dữ liệu DB", "Hoàn thành 100%"),
    ]

    r = 6
    for row in daily_matrix_data:
        code, name, role, d1, d2, d3, d4, tasks_cnt, hours_cnt, eval_txt, status_txt = row
        ws3.row_dimensions[r].height = 80

        fill_curr = fill_zebra_light if (r % 2 == 0) else fill_white

        c_code = ws3.cell(r, 1, code)
        c_code.font = font_data_bold
        c_code.alignment = align_center
        c_code.fill = fill_curr
        c_code.border = cell_border

        c_name = ws3.cell(r, 2, name)
        c_name.alignment = align_left
        c_name.fill = fill_curr
        c_name.border = cell_border
        if "Điền" in name:
            c_name.font = font_dien
        elif "Phú" in name:
            c_name.font = font_phu
        elif "Thoại" in name:
            c_name.font = font_thoai
        elif "Long" in name:
            c_name.font = font_long
        elif "Nam" in name:
            c_name.font = font_nam

        c_role = ws3.cell(r, 3, role)
        c_role.font = font_data_bold
        c_role.alignment = align_left
        c_role.fill = fill_curr
        c_role.border = cell_border

        for c_offset, day_txt in enumerate([d1, d2, d3, d4], start=4):
            c_day = ws3.cell(r, c_offset, day_txt)
            c_day.font = font_data
            c_day.alignment = align_top_left
            c_day.fill = fill_curr
            c_day.border = cell_border

        c_tasks = ws3.cell(r, 8, tasks_cnt)
        c_tasks.font = font_data_bold
        c_tasks.alignment = align_center
        c_tasks.fill = fill_curr
        c_tasks.border = cell_border

        c_hrs = ws3.cell(r, 9, hours_cnt)
        c_hrs.font = font_data_bold
        c_hrs.alignment = align_center
        c_hrs.fill = fill_curr
        c_hrs.border = cell_border

        c_eval = ws3.cell(r, 10, eval_txt)
        c_eval.font = font_data
        c_eval.alignment = align_left
        c_eval.fill = fill_curr
        c_eval.border = cell_border

        c_st = ws3.cell(r, 11, status_txt)
        c_st.font = font_pass
        c_st.alignment = align_center
        c_st.fill = fill_pass
        c_st.border = cell_border

        r += 1

    # Section 2: Bảng đánh giá năng lực thực tế sau Tuần 1 (Evaluation Rubric)
    r += 2
    ws3.merge_cells(f"A{r}:K{r}")
    ws3[f"A{r}"] = "2. BẢNG TIÊU CHÍ ĐÁNH GIÁ NĂNG LỰC THỰC TẾ & ĐỀ XUẤT PHÂN BỔ TUẦN 2 (TRƯỞNG NHÓM ĐIỀN ĐÁNH GIÁ)"
    ws3[f"A{r}"].font = font_sec_header
    ws3[f"A{r}"].fill = fill_blue_sec
    ws3[f"A{r}"].alignment = align_left
    ws3.row_dimensions[r].height = 24

    r += 1
    eval_headers = [
        "Mã TV", "Họ và tên", "Kỹ năng Kỹ thuật\n(Cài đặt máy & Chạy web)", 
        "Kỹ năng Đọc hiểu\n(Kiến trúc & Tài liệu SRS)", "Độ nhạy bén Kiểm thử\n(Bắt lỗi UI & Data DB)", 
        "Kỷ luật & Tinh thần\n(Tham gia họp & Đúng hạn)", "Kỹ năng Viết Test Case\n(Tuân thủ Template & EP/BVA)",
        "Điểm TB\n(Thang 5.0)", "Xếp loại năng lực", "Khuyến nghị phân bổ Tuần 2", "Chữ ký xác nhận"
    ]

    for c_idx, h in enumerate(eval_headers, start=1):
        cell = ws3.cell(r, c_idx, h)
        cell.font = font_tbl_header
        cell.fill = fill_blue_head
        cell.alignment = align_center
        cell.border = header_border
    ws3.row_dimensions[r].height = 28

    eval_data = [
        ("TV01", "Điền (Lead)", "4.8 / 5.0", "5.0 / 5.0", "4.8 / 5.0", "5.0 / 5.0", "4.9 / 5.0", "4.9 / 5.0", "Xuất sắc (Lead)", 
         "Tiếp tục quản lý dự án, review chéo toàn bộ Test Cases của 4 bạn ở Tuần 2, chuẩn hóa bộ 110 Test Cases.", "Điền (đã ký)"),
        ("TV02", "Phú", "5.0 / 5.0", "4.9 / 5.0", "5.0 / 5.0", "4.9 / 5.0", "4.9 / 5.0", "4.94 / 5.0", "Xuất sắc (Tech Lead)", 
         "Phụ trách Chương 3 (Tự động Selenium IDE) và viết bộ Unit Test Store.Tests; hỗ trợ giải đáp kỹ thuật cho 3 bạn.", "Phú (đã ký)"),
        ("TV03", "Thoại", "4.2 / 5.0", "4.0 / 5.0", "4.3 / 5.0", "4.7 / 5.0", "4.2 / 5.0", "4.28 / 5.0", "Khá - Đạt yêu cầu", 
         "Giao viết bộ 25 - 30 Test Cases phân hệ Xác thực (SignUp, SignIn, Logout, Profile, ChangePassword, AdminUsers).", "Thoại (đã ký)"),
        ("TV04", "Long", "4.3 / 5.0", "4.1 / 5.0", "4.5 / 5.0", "4.6 / 5.0", "4.3 / 5.0", "4.36 / 5.0", "Khá - Nhạy bén tốt", 
         "Giao viết bộ 30 - 35 Test Cases phân hệ Sản phẩm & Quản trị (Duyệt, Phân trang, Lọc đa tiêu chí, Search Regex, Admin CRUD).", "Long (đã ký)"),
        ("TV05", "Nam", "4.1 / 5.0", "4.2 / 5.0", "4.4 / 5.0", "4.8 / 5.0", "4.2 / 5.0", "4.34 / 5.0", "Khá - Cẩn thận", 
         "Giao viết bộ 25 - 30 Test Cases phân hệ Giỏ hàng, Thanh toán CheckOut và phối hợp cùng Phú viết Test Case Tích hợp Triggers/SP.", "Nam (đã ký)"),
    ]

    r += 1
    for row in eval_data:
        code, name, c1, c2, c3, c4, c5, avg_score, rank, rec, sign = row
        ws3.row_dimensions[r].height = 36

        fill_curr = fill_zebra_light if (r % 2 == 0) else fill_white

        c_code = ws3.cell(r, 1, code)
        c_code.font = font_data_bold
        c_code.alignment = align_center
        c_code.fill = fill_curr
        c_code.border = cell_border

        c_name = ws3.cell(r, 2, name)
        c_name.alignment = align_left
        c_name.fill = fill_curr
        c_name.border = cell_border
        if "Điền" in name:
            c_name.font = font_dien
        elif "Phú" in name:
            c_name.font = font_phu
        elif "Thoại" in name:
            c_name.font = font_thoai
        elif "Long" in name:
            c_name.font = font_long
        elif "Nam" in name:
            c_name.font = font_nam

        for c_offset, score_txt in enumerate([c1, c2, c3, c4, c5], start=3):
            c_s = ws3.cell(r, c_offset, score_txt)
            c_s.font = font_data
            c_s.alignment = align_center
            c_s.fill = fill_curr
            c_s.border = cell_border

        c_avg = ws3.cell(r, 8, avg_score)
        c_avg.font = font_data_bold
        c_avg.alignment = align_center
        c_avg.fill = fill_curr
        c_avg.border = cell_border

        c_rank = ws3.cell(r, 9, rank)
        c_rank.font = font_pass
        c_rank.alignment = align_center
        c_rank.fill = fill_pass
        c_rank.border = cell_border

        c_rec = ws3.cell(r, 10, rec)
        c_rec.font = font_data
        c_rec.alignment = align_left
        c_rec.fill = fill_curr
        c_rec.border = cell_border

        c_sign = ws3.cell(r, 11, sign)
        c_sign.font = font_data_italic
        c_sign.alignment = align_center
        c_sign.fill = fill_curr
        c_sign.border = cell_border

        r += 1

    # Column widths for Sheet 3
    col_widths_s3 = {
        1: 10, 2: 18, 3: 25, 4: 25, 5: 25, 6: 25, 7: 25,
        8: 12, 9: 12, 10: 28, 11: 18
    }
    for c_idx, width in col_widths_s3.items():
        ws3.column_dimensions[get_column_letter(c_idx)].width = width

    # =========================================================================
    # SHEET 4: CHECKLIST NGHIEM THU 17_09 (MILESTONE M1 ACCEPTANCE)
    # =========================================================================
    ws4 = wb.create_sheet(title="Checklist_Nghiem_Thu_17_09")
    ws4.views.sheetView[0].showGridLines = True

    # Title Block
    ws4.merge_cells("A1:I1")
    ws4["A1"] = "BIÊN BẢN & CHECKLIST NGHIỆM THU CỘT MỐC 1 (M1) - NGÀY 17/09/2026"
    ws4["A1"].font = Font(name="Segoe UI", size=13, bold=True, color="FFFFFF")
    ws4["A1"].fill = fill_navy
    ws4["A1"].alignment = align_center

    ws4.merge_cells("A2:I2")
    ws4["A2"] = "Dự án: Ecommerce Computer (Store EF V3) | Nghiệm thu Môi trường 5 máy, Kế hoạch Kiểm thử Chương 1 & Sẵn sàng cho Tuần 2"
    ws4["A2"].font = font_subtitle
    ws4["A2"].fill = fill_navy
    ws4["A2"].alignment = align_center

    ws4.row_dimensions[1].height = 24
    ws4.row_dimensions[2].height = 18

    # Headers for acceptance checklist
    checklist_headers = [
        "STT", "Hạng mục kiểm tra / Nghiệm thu", "Tiêu chuẩn nghiệm thu chi tiết (Acceptance Criteria)",
        "Đối tượng / Thành viên phụ trách", "Tài liệu / Minh chứng đối chiếu", "Người nghiệm thu",
        "Kết quả kiểm tra", "Đánh giá", "Ghi chú nghiệm thu"
    ]

    r = 4
    for c_idx, h in enumerate(checklist_headers, start=1):
        cell = ws4.cell(r, c_idx, h)
        cell.font = font_tbl_header
        cell.fill = fill_blue_head
        cell.alignment = align_center
        cell.border = header_border
    ws4.row_dimensions[r].height = 28

    checklist_m1_items = [
        # Nhóm A: Môi trường
        ("A.1", "Hạ tầng kho dữ liệu làm việc chung", 
         "Google Drive chung và Git repo hoạt động ổn định, phân quyền chuẩn cho 5 email, có đủ cấu trúc thư mục Docs, TestCases, Screenshots.", 
         "Điền (Lead) & Phú", "Link Drive & Git repo", "Trưởng nhóm Điền", "ĐẠT (PASS)", "Hoàn thành", "5/5 thành viên truy cập tốt"),
        
        ("A.2", "Môi trường kiểm thử trên Máy 1 (Điền)", 
         "Visual Studio 2022, SQL Server LocalDB kết nối MSSQLLocalDB, database Store có đủ 10 bảng, run.bat chạy web port 5000 hiển thị trang chủ.", 
         "Điền (Lead)", "Ảnh chụp màn hình SSMS & Web port 5000", "Phú (Tech Lead)", "ĐẠT (PASS)", "Hoàn thành", "Môi trường ổn định"),

        ("A.3", "Môi trường kiểm thử trên Máy 2 (Phú - Master)", 
         "Môi trường Master chuẩn: VS 2022 Enterprise, LocalDB, IIS Express, build solution Store 0 lỗi, kiểm tra triggers và SP AddCart thành công.", 
         "Phú (Tech Lead)", "Ảnh chụp màn hình Solution build 0 error & LocalDB", "Điền (Lead)", "ĐẠT (PASS)", "Hoàn thành", "Đóng vai trò máy chuẩn đối chiếu"),

        ("A.4", "Môi trường kiểm thử trên Máy 3 (Thoại)", 
         "Cài đặt thành công VS 2022, LocalDB, restore Store.sql không lỗi cú pháp, chạy web port 5000 load đầy đủ banner và sản phẩm.", 
         "Thoại", "Ảnh chụp màn hình Máy 3 gửi lên Drive", "Phú & Điền", "ĐẠT (PASS)", "Hoàn thành", "Đã test thử form Sign In"),

        ("A.5", "Môi trường kiểm thử trên Máy 4 (Long)", 
         "Cài đặt thành công VS 2022, LocalDB, restore Store.sql, chạy web port 5000 duyệt được danh sách và phân trang sản phẩm.", 
         "Long", "Ảnh chụp màn hình Máy 4 gửi lên Drive", "Phú & Điền", "ĐẠT (PASS)", "Hoàn thành", "Đã test thử bộ lọc Category"),

        ("A.6", "Môi trường kiểm thử trên Máy 5 (Nam)", 
         "Cài đặt thành công VS 2022, LocalDB, restore Store.sql, chạy web port 5000 thử thêm được sản phẩm vào giỏ hàng.", 
         "Nam", "Ảnh chụp màn hình Máy 5 gửi lên Drive", "Phú & Điền", "ĐẠT (PASS)", "Hoàn thành", "Đã đối chiếu bảng Cart trong DB"),

        # Nhóm B: Tài liệu Chương 1
        ("B.1", "Phần đầu: Bìa, Lời cảm ơn, Cam đoan", 
         "Đầy đủ Bìa chính, Bìa phụ, Lời cảm ơn, Lời cam đoan; đúng font chữ quy định, căn lề 3-2-2-2cm.", 
         "Điền (Lead)", "File Báo cáo Word (Trang 1 - Trang iv)", "Phú & Giảng viên", "ĐẠT (PASS)", "Hoàn thành", "Format chuẩn quy định bộ môn"),

        ("B.2", "Mục 1.1: Giới thiệu hệ thống & Kiến trúc", 
         "Mô tả tổng quan Store EF V3, Sơ đồ kiến trúc 3 tầng MVC 5, Sơ đồ ERD 10 bảng dữ liệu, Bảng ngăn xếp công nghệ, Mô tả 5 phân hệ chức năng và Ma trận RBAC.", 
         "Điền (Lead)", "Báo cáo Word Mục 1.1 (Trang 1 - 7)", "Phú (Tech Lead)", "ĐẠT (PASS)", "Hoàn thành", "Sơ đồ ERD và RBAC rất chi tiết"),

        ("B.3", "Mục 1.2: Mục tiêu & Phạm vi kiểm thử", 
         "5 mục tiêu chất lượng cốt lõi, bảng chỉ số KPI (Pass ≥95%, UT ≥70%), Bảng phạm vi In-Scope vs. Out-of-Scope và danh mục đối tượng kiểm thử cụ thể.", 
         "Điền (Lead)", "Báo cáo Word Mục 1.2 (Trang 8 - 10)", "Cả nhóm", "ĐẠT (PASS)", "Hoàn thành", "Phân định phạm vi rõ ràng"),

        ("B.4", "Mục 1.3: Chiến lược, RACI & Quản lý rủi ro", 
         "Chiến lược kiểm thử gia tăng, 4 mức UT/IT/ST/UAT, 4 loại test, Ma trận trách nhiệm RACI 5 thành viên, Bảng phân tích 6 rủi ro trọng yếu (R1 đến R6).", 
         "Điền (Lead)", "Báo cáo Word Mục 1.3 (Trang 11 - 14)", "Phú (Tech Lead)", "ĐẠT (PASS)", "Hoàn thành", "Phân tích rủi ro DEF-01..04 sâu sắc"),

        ("B.5", "Mục 1.4 & 1.5: Môi trường, Công cụ & Tiêu chí", 
         "Bảng cấu hình phần cứng/phần mềm, danh sách 5 tài khoản test chuẩn, công cụ hỗ trợ, Tiêu chí Entry, Suspension/Resumption và Exit Criteria theo ISO 29119.", 
         "Điền (Lead)", "Báo cáo Word Mục 1.4 & 1.5 (Trang 15 - 17)", "Cả nhóm", "ĐẠT (PASS)", "Hoàn thành", "Tiêu chí nghiệm thu rõ ràng"),

        ("B.6", "Mục 1.6: Kết luận Chương 1 & Format Word", 
         "Tóm tắt kết quả kế hoạch kiểm thử, mục lục tự động, danh mục hình và bảng tự động hoạt động chính xác, không lỗi nhảy trang.", 
         "Điền (Lead)", "Báo cáo Word Chương 1 hoàn chỉnh", "Phú & Nhóm", "ĐẠT (PASS)", "Hoàn thành", "Bản thảo Chương 1 sẵn sàng nộp"),

        # Nhóm C: Nền tảng Kỹ thuật & Tự động hóa
        ("C.1", "Công cụ Kiểm thử Tự động Selenium IDE", 
         "Extension Selenium IDE cài đặt trên Chrome/Edge, tạo project test, ghi và chạy playback thành công kịch bản Auto_TC_01 (Đăng nhập thành công) Pass xanh.", 
         "Phú (Tech Lead)", "File kịch bản Auto_TC_01.side & Ảnh chạy Pass", "Điền (Lead)", "ĐẠT (PASS)", "Hoàn thành", "Sẵn sàng cho Chương 3 ở Tuần 3"),

        ("C.2", "Dự án Kiểm thử Đơn vị MSTest Store.Tests", 
         "Solution build 0 error, project Store.Tests nhận diện trên Test Explorer, viết bài test mẫu Helpers.IsValidEmail() chạy 100% Pass.", 
         "Phú (Tech Lead)", "Mã nguồn Store.Tests & Ảnh Test Explorer", "Điền (Lead)", "ĐẠT (PASS)", "Hoàn thành", "Sẵn sàng cho Unit Test ở Tuần 2"),

        ("C.3", "Chuẩn hóa Template Test Case Excel", 
         "File Excel mẫu đầy đủ 10 trường thông tin chuẩn ISO/IEEE 29119, có Conditional Formatting tự đổi màu trạng thái Pass/Fail, đã chia sẻ cho cả nhóm.", 
         "Phú (Tech Lead)", "File TEMPLATE_TEST_CASE_STANDARD.xlsx", "Điền (Lead)", "ĐẠT (PASS)", "Hoàn thành", "Thống nhất làm biểu mẫu chung"),

        # Nhóm D: Chuẩn bị của Thành viên cho Tuần 2
        ("D.1", "Ma trận yêu cầu test & 5 TC mẫu của Thoại (Auth)", 
         "Hoàn thành Ma trận yêu cầu kiểm thử Auth (25-30 ca test dự kiến) và 5 Test Case mẫu chức năng Đăng ký tài khoản theo đúng Template.", 
         "Thoại", "File Excel Ma trận & 5 TC mẫu phân hệ Auth", "Điền & Phú", "ĐẠT (PASS)", "Hoàn thành", "Đủ điều kiện nhận việc Tuần 2"),

        ("D.2", "Ma trận yêu cầu test & 5 TC mẫu của Long (Product)", 
         "Hoàn thành Ma trận yêu cầu kiểm thử Product (30-35 ca test dự kiến) và 5 Test Case mẫu chức năng Tìm kiếm/Lọc sản phẩm theo đúng Template.", 
         "Long", "File Excel Ma trận & 5 TC mẫu phân hệ Product", "Điền & Phú", "ĐẠT (PASS)", "Hoàn thành", "Đủ điều kiện nhận việc Tuần 2"),

        ("D.3", "Ma trận yêu cầu test & 5 TC mẫu của Nam (Cart)", 
         "Hoàn thành Ma trận yêu cầu kiểm thử Cart/Order (25-30 ca test dự kiến) và 5 Test Case mẫu chức năng Giỏ hàng theo đúng Template.", 
         "Nam", "File Excel Ma trận & 5 TC mẫu phân hệ Cart", "Điền & Phú", "ĐẠT (PASS)", "Hoàn thành", "Đủ điều kiện nhận việc Tuần 2"),
    ]

    r = 5
    for item in checklist_m1_items:
        stt, name, crit, owner, ref, rev, result, eval_t, note = item
        ws4.row_dimensions[r].height = 36

        fill_curr = fill_zebra_light if (r % 2 == 0) else fill_white

        c_stt = ws4.cell(r, 1, stt)
        c_stt.font = font_data_bold
        c_stt.alignment = align_center
        c_stt.fill = fill_curr
        c_stt.border = cell_border

        c_name = ws4.cell(r, 2, name)
        c_name.font = font_data_bold
        c_name.alignment = align_left
        c_name.fill = fill_curr
        c_name.border = cell_border

        c_crit = ws4.cell(r, 3, crit)
        c_crit.font = font_data
        c_crit.alignment = align_top_left
        c_crit.fill = fill_curr
        c_crit.border = cell_border

        c_owner = ws4.cell(r, 4, owner)
        c_owner.font = font_data_bold
        c_owner.alignment = align_center
        c_owner.fill = fill_curr
        c_owner.border = cell_border

        c_ref = ws4.cell(r, 5, ref)
        c_ref.font = font_data_italic
        c_ref.alignment = align_left
        c_ref.fill = fill_curr
        c_ref.border = cell_border

        c_rev = ws4.cell(r, 6, rev)
        c_rev.font = font_data
        c_rev.alignment = align_center
        c_rev.fill = fill_curr
        c_rev.border = cell_border

        c_res = ws4.cell(r, 7, result)
        c_res.font = font_pass
        c_res.alignment = align_center
        c_res.fill = fill_pass
        c_res.border = cell_border

        c_eval = ws4.cell(r, 8, eval_t)
        c_eval.font = font_pass
        c_eval.alignment = align_center
        c_eval.fill = fill_pass
        c_eval.border = cell_border

        c_note = ws4.cell(r, 9, note)
        c_note.font = font_data
        c_note.alignment = align_left
        c_note.fill = fill_curr
        c_note.border = cell_border

        r += 1

    # Sign-off block
    r += 2
    ws4.merge_cells(f"A{r}:D{r}")
    ws4[f"A{r}"] = "KẾT LUẬN CỦA TRƯỞNG NHÓM (TEST LEAD):"
    ws4[f"A{r}"].font = font_data_bold
    ws4[f"A{r}"].alignment = align_left

    r += 1
    ws4.merge_cells(f"A{r}:I{r}")
    ws4[f"A{r}"] = "Căn cứ vào kết quả kiểm tra thực tế, 100% các hạng mục công việc Tuần 1 (từ 14/09/2026 đến 17/09/2026) đã được hoàn thành đúng thời hạn và đạt tiêu chuẩn chất lượng DoD. Cột mốc 1 (M1) CHÍNH THỨC ĐƯỢC NGHIỆM THU. Toàn bộ 5 thành viên đã sẵn sàng bước vào Tuần 2 (Thiết kế chi tiết bộ 110 Test Cases)."
    ws4[f"A{r}"].font = font_data_italic
    ws4[f"A{r}"].alignment = align_top_left
    ws4.row_dimensions[r].height = 28

    r += 2
    ws4.merge_cells(f"A{r}:B{r}")
    ws4[f"A{r}"] = "CÁC THÀNH VIÊN KÝ TÊN:"
    ws4[f"A{r}"].font = font_data_bold

    ws4.merge_cells(f"D{r}:E{r}")
    ws4[f"D{r}"] = "KỸ THUẬT VIÊN TRƯỞNG:"
    ws4[f"D{r}"].font = font_data_bold

    ws4.merge_cells(f"H{r}:I{r}")
    ws4[f"H{r}"] = "TRƯỞNG NHÓM / TEST LEAD:"
    ws4[f"H{r}"].font = font_data_bold

    r += 1
    ws4.merge_cells(f"A{r}:B{r}")
    ws4[f"A{r}"] = "Thoại, Long, Nam\n(Đã ký xác nhận)"
    ws4[f"A{r}"].font = font_data_italic
    ws4[f"A{r}"].alignment = align_center

    ws4.merge_cells(f"D{r}:E{r}")
    ws4[f"D{r}"] = "Phú\n(Đã ký xác nhận)"
    ws4[f"D{r}"].font = font_data_italic
    ws4[f"D{r}"].alignment = align_center

    ws4.merge_cells(f"H{r}:I{r}")
    ws4[f"H{r}"] = "Điền\n(Đã ký phê duyệt)"
    ws4[f"H{r}"].font = font_data_italic
    ws4[f"H{r}"].alignment = align_center
    ws4.row_dimensions[r].height = 36

    # Column widths for Sheet 4
    col_widths_s4 = {
        1: 8, 2: 26, 3: 38, 4: 20, 5: 28, 6: 18, 7: 15, 8: 15, 9: 26
    }
    for c_idx, width in col_widths_s4.items():
        ws4.column_dimensions[get_column_letter(c_idx)].width = width

    # Freeze Panes & Auto Filter
    ws1.freeze_panes = "A6"

    ws2.freeze_panes = "F5"
    ws2.auto_filter.ref = f"A4:N{ws2.max_row}"

    ws3.freeze_panes = "D6"

    ws4.freeze_panes = "C5"
    ws4.auto_filter.ref = f"A4:I{ws4.max_row}"

    # ----------------- SAVE FILE -----------------
    out_dir_tuan1 = r"D:\Kiểm thử pm\pj kiểm thử\EcommerceComputer-V3\Docs\Tuan1"
    os.makedirs(out_dir_tuan1, exist_ok=True)
    out_file_tuan1 = os.path.join(out_dir_tuan1, "PHAN_CONG_NHIEM_VU_TUAN_1.xlsx")
    out_file_docs = r"D:\Kiểm thử pm\pj kiểm thử\EcommerceComputer-V3\Docs\PHAN_CONG_NHIEM_VU_TUAN_1.xlsx"

    wb.save(out_file_tuan1)
    print(f"File 1 saved successfully: {out_file_tuan1}")

    wb.save(out_file_docs)
    print(f"File 2 saved successfully: {out_file_docs}")

if __name__ == "__main__":
    build_week1_excel()
