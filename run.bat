@echo off
chcp 65001 > nul
echo ==============================================
echo   KHỞI ĐỘNG DỰ ÁN ECOMMERCE COMPUTER
echo ==============================================

echo [1/3] Đang khởi động SQL LocalDB...
sqllocaldb start MSSQLLocalDB > nul 2>&1

echo [2/3] Kiểm tra và build dự án...
powershell -ExecutionPolicy Bypass -File "%~dp0build.ps1"

if not exist "%~dp0Store EF\bin\Store EF.dll" (
    echo [LOI] Build that bai! Vui long kiem tra log o tren.
    pause
    exit /b 1
)

echo [3/3] Đang mở máy chủ IIS Express tại http://localhost:5000 ...
start http://localhost:5000
"C:\Program Files\IIS Express\iisexpress.exe" /path:"%~dp0Store EF" /port:5000
