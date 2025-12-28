@echo off
REM Content Generator Web App Startup Script
REM Windows Batch File

echo.
echo ================================================================================
echo  🎨 Content Generator Web App - ACE Framework
echo ================================================================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python from https://www.python.org
    pause
    exit /b 1
)

REM Check if virtual environment exists
if not exist ".venv\" (
    echo 📦 Creating virtual environment...
    python -m venv .venv
)

REM Activate virtual environment
echo ✅ Activating virtual environment...
call .venv\Scripts\activate.bat

REM Check if Flask is installed
pip show flask >nul 2>&1
if %errorlevel% neq 0 (
    echo 📥 Installing dependencies...
    pip install flask flask-cors ace-framework
)

REM Check for API key
if "%GROQ_API_KEY%"=="" (
    echo.
    echo ⚠️  WARNING: GROQ_API_KEY environment variable not set!
    echo.
    echo Set it before running:
    echo   $env:GROQ_API_KEY = "your-api-key-here"
    echo.
    set /p api_key="Enter your Groq API key (or press Enter to skip): "
    if not "!api_key!"=="" (
        set GROQ_API_KEY=!api_key!
    )
)

echo.
echo ================================================================================
echo  🚀 Starting Content Generator Web App
echo ================================================================================
echo.
echo 🌐 Open your browser and go to: http://localhost:5000
echo.
echo Press Ctrl+C to stop the server
echo.
echo ================================================================================
echo.

REM Run the Flask app
python app.py

pause
