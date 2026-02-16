@echo off
echo ========================================
echo GATE 2026-2027 Daily Planner
echo ========================================
echo.
echo Installing dependencies...
pip install -r requirements.txt
echo.
echo Starting Flask application...
echo.
echo Access the app at: http://localhost:5000
echo.
echo Login credentials:
echo   Sohel: sohel / sohel123
echo   Anju: anju / anju123
echo.
echo Press Ctrl+C to stop the server
echo ========================================
echo.
python app.py
