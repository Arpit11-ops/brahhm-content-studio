@echo off
REM Nightly catalog refresh for Brahhm brands.
REM Registered via: schtasks /Create /SC DAILY /ST 03:00 /TN "Brahhm Catalog Refresh" /TR "..."
REM Unregister:     schtasks /Delete /TN "Brahhm Catalog Refresh" /F

cd /d "%~dp0.."

REM Resolve a stable Python interpreter. Task Scheduler's env has a minimal PATH.
set "PYEXE="
if exist "C:\Users\arpit\AppData\Local\Microsoft\WindowsApps\py.exe" set "PYEXE=C:\Users\arpit\AppData\Local\Microsoft\WindowsApps\py.exe -3"
if not defined PYEXE if exist "C:\Users\arpit\AppData\Local\hermes\hermes-agent\venv\Scripts\python.exe" set "PYEXE=C:\Users\arpit\AppData\Local\hermes\hermes-agent\venv\Scripts\python.exe"
if not defined PYEXE (
    echo [%date% %time%] ERROR: no Python interpreter found >> research\catalogs\refresh.log
    exit /b 2
)

echo [%date% %time%] START (using %PYEXE%) >> research\catalogs\refresh.log
%PYEXE% scripts\refresh_catalogs.py >> research\catalogs\refresh.log 2>&1
set RC=%ERRORLEVEL%
echo [%date% %time%] END rc=%RC% >> research\catalogs\refresh.log
exit /b %RC%
