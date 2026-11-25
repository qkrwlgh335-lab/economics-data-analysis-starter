$ErrorActionPreference = "Stop"
Set-Location $PSScriptRoot
Write-Host "Checking Python 3.12 or 3.13"
if (-not (Get-Command py -ErrorAction SilentlyContinue)) { throw "Install Python from python.org first." }
if (-not (Test-Path ".venv\Scripts\python.exe")) {
    py -3.12 --version
    if ($LASTEXITCODE -eq 0) { py -3.12 -m venv .venv }
    else { py -3.13 -m venv .venv }
    if ($LASTEXITCODE -ne 0) { throw "Python 3.12/3.13 required." }
}
& .\.venv\Scripts\python.exe -m pip install -r requirements.txt
if ($LASTEXITCODE -ne 0) { throw "Package installation failed." }
& .\.venv\Scripts\python.exe examples/demo.py
if ($LASTEXITCODE -ne 0) { throw "Demo failed." }
& .\.venv\Scripts\python.exe -m unittest discover -s tests
if ($LASTEXITCODE -ne 0) { throw "Tests failed." }
