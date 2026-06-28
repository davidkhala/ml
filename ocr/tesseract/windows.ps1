function Set-Path
{
    (Invoke-WebRequest -Uri https://raw.githubusercontent.com/davidkhala/windows-utils/refs/heads/master/powershell/path.ps1 -UseBasicParsing).Content | Invoke-Expression
    Add-Path "C:\Program Files\Tesseract-OCR\"
    Add-Path "C:\Program Files\Tesseract-OCR\" User
    tesseract --version
}