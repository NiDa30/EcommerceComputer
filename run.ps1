# Script chạy dự án EcommerceComputer-V3

Write-Host "==============================================" -ForegroundColor Cyan
Write-Host "   KHỞI ĐỘNG DỰ ÁN ECOMMERCE COMPUTER" -ForegroundColor Cyan
Write-Host "==============================================" -ForegroundColor Cyan

# 1. Khởi động SQL LocalDB
Write-Host "[1/3] Đang khởi động SQL LocalDB..." -ForegroundColor Yellow
sqllocaldb start MSSQLLocalDB | Out-Null

# 2. Biên dịch mã nguồn nếu cần
$dllPath = "$PSScriptRoot\Store EF\bin\Store EF.dll"
if (-not (Test-Path $dllPath)) {
    Write-Host "[2/3] Chưa thấy file dll, đang biên dịch dự án..." -ForegroundColor Yellow
    & "$PSScriptRoot\build.ps1"
} else {
    Write-Host "[2/3] Dự án đã được biên dịch sẵn sàng." -ForegroundColor Green
}

# 3. Chạy IIS Express
$projectPath = "$PSScriptRoot\Store EF"
$url = "http://localhost:5000"
Write-Host "[3/3] Đang khởi động IIS Express tại $url ..." -ForegroundColor Green

Start-Process $url
& "C:\Program Files\IIS Express\iisexpress.exe" /path:"$projectPath" /port:5000
