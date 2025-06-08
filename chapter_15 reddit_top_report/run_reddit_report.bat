@echo off
REM ──────────────────────────────────────────────────────────────────────────
REM Activate virtual environment (Windows PowerShell syntax)
REM NOTE: If using cmd.exe, adjust to call `venv\Scripts\activate.bat`
call venv\Scripts\Activate.bat

REM Run the pipeline
python scraper.py
python generate_report.py
python send_email.py

REM Deactivate venv (optional)
deactivate
