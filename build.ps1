# Script build automatic for Store EF in VS Code

$projectDir = "$PSScriptRoot\Store EF"
$packagesDir = "$PSScriptRoot\packages"
$binDir = "$projectDir\bin"
$roslynDir = "$binDir\roslyn"
$cscPath = "$packagesDir\Microsoft.CodeDom.Providers.DotNetCompilerPlatform.4.1.0\tools\Roslyn-4.1.0\csc.exe"

# Clean old bin dlls to ensure no reference assemblies are present
if (Test-Path $binDir) {
    Get-ChildItem -Path $binDir -Filter *.dll | Remove-Item -Force -ErrorAction SilentlyContinue
}
New-Item -ItemType Directory -Force -Path $binDir | Out-Null
New-Item -ItemType Directory -Force -Path $roslynDir | Out-Null

if (Test-Path "$packagesDir\Microsoft.CodeDom.Providers.DotNetCompilerPlatform.4.1.0\tools\Roslyn-4.1.0") {
    Copy-Item -Path "$packagesDir\Microsoft.CodeDom.Providers.DotNetCompilerPlatform.4.1.0\tools\Roslyn-4.1.0\*" -Destination $roslynDir -Recurse -Force
}

# Copy exact referenced DLLs from HintPaths in Store EF.csproj
[xml]$csproj = Get-Content "$projectDir\Store EF.csproj"
$hintPaths = $csproj.Project.ItemGroup.Reference.HintPath | Where-Object { $_ }
foreach ($hint in $hintPaths) {
    $fullHint = [System.IO.Path]::GetFullPath((Join-Path $projectDir $hint))
    if (Test-Path $fullHint) {
        Copy-Item -Path $fullHint -Destination $binDir -Force
    }
}

$csFiles = Get-ChildItem -Path $projectDir -Filter *.cs -Recurse | Select-Object -ExpandProperty FullName
$binDlls = Get-ChildItem -Path $binDir -Filter *.dll | Select-Object -ExpandProperty FullName

$frameworkAssemblies = @(
    "System.dll",
    "System.Core.dll",
    "System.Data.dll",
    "System.Data.DataSetExtensions.dll",
    "System.Drawing.dll",
    "System.EnterpriseServices.dll",
    "System.Net.Http.dll",
    "System.Runtime.Serialization.dll",
    "System.Security.dll",
    "System.Transactions.dll",
    "System.Web.dll",
    "System.Web.ApplicationServices.dll",
    "System.Web.DynamicData.dll",
    "System.Web.Entity.dll",
    "System.Web.Extensions.dll",
    "System.Web.Services.dll",
    "System.Xml.dll",
    "System.Xml.Linq.dll",
    "System.ComponentModel.DataAnnotations.dll",
    "netstandard.dll",
    "System.Runtime.dll"
)

# Extract EDMX schemas for Entity Framework metadata resources
$edmxPath = "$projectDir\Models\StoreDb.edmx"
$csdlPath = "$binDir\StoreDb.csdl"
$ssdlPath = "$binDir\StoreDb.ssdl"
$mslPath = "$binDir\StoreDb.msl"

if (Test-Path $edmxPath) {
    [xml]$edmx = Get-Content $edmxPath
    [System.IO.File]::WriteAllText($csdlPath, $edmx.Edmx.Runtime.ConceptualModels.Schema.OuterXml, [System.Text.Encoding]::UTF8)
    [System.IO.File]::WriteAllText($ssdlPath, $edmx.Edmx.Runtime.StorageModels.Schema.OuterXml, [System.Text.Encoding]::UTF8)
    [System.IO.File]::WriteAllText($mslPath, $edmx.Edmx.Runtime.Mappings.Mapping.OuterXml, [System.Text.Encoding]::UTF8)
}

$rspFile = "$binDir\build.rsp"
$rspLines = [System.Collections.Generic.List[string]]::new()
$rspLines.Add("/target:library")
$outputDll = "$binDir\Store EF.dll"
$rspLines.Add("/out:`"$outputDll`"")
$rspLines.Add("/langversion:latest")
$rspLines.Add("/debug:full")
$rspLines.Add("/utf8output")

if (Test-Path $csdlPath) {
    $rspLines.Add("/resource:`"$csdlPath`",Models.StoreDb.csdl")
    $rspLines.Add("/resource:`"$ssdlPath`",Models.StoreDb.ssdl")
    $rspLines.Add("/resource:`"$mslPath`",Models.StoreDb.msl")
    $rspLines.Add("/resource:`"$csdlPath`",Store_EF.Models.StoreDb.csdl")
    $rspLines.Add("/resource:`"$ssdlPath`",Store_EF.Models.StoreDb.ssdl")
    $rspLines.Add("/resource:`"$mslPath`",Store_EF.Models.StoreDb.msl")
}

foreach ($asm in $frameworkAssemblies) {
    $rspLines.Add("/r:`"$asm`"")
}
foreach ($dll in $binDlls) {
    if ($dll -ne $outputDll) {
        $rspLines.Add("/r:`"$dll`"")
    }
}
foreach ($cs in $csFiles) {
    $rspLines.Add("`"$cs`"")
}

[System.IO.File]::WriteAllLines($rspFile, $rspLines, [System.Text.Encoding]::UTF8)

Write-Host "Building Store EF using Roslyn Compiler..." -ForegroundColor Cyan
& $cscPath "@$rspFile"

if (Test-Path $outputDll) {
    Write-Host "BUILD SUCCESS! Store EF.dll created." -ForegroundColor Green
} else {
    Write-Host "BUILD FAILED!" -ForegroundColor Red
}

