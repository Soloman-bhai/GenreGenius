@echo off
cd /d "%~dp0"
echo 🔁 Activating virtual environment...
call venv\Scripts\activate

echo 🚀 Starting Flask app...
cd server

REM Start Flask server in background
start cmd /k python app.py

REM Wait a few seconds to let Flask start
timeout /t 3 > nul

REM Open in default browser
start http://127.0.0.1:5000

pause
