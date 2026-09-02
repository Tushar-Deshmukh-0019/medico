@echo off
REM ===============================================
REM Medical CDSS PostgreSQL Setup for Windows
REM ===============================================
REM This batch script sets up PostgreSQL automatically

setlocal enabledelayedexpansion

echo.
echo ===============================================
echo Medical CDSS - PostgreSQL Windows Setup
echo ===============================================
echo.

REM Check if psql is available
where psql >nul 2>nul
if %errorlevel% neq 0 (
    echo.
    echo [ERROR] PostgreSQL is not installed or psql is not in PATH
    echo.
    echo Please install PostgreSQL from: https://www.postgresql.org/download/windows/
    echo.
    echo After installation, add PostgreSQL bin to your PATH:
    echo   - PostgreSQL bin path: C:\Program Files\PostgreSQL\15\bin
    echo.
    pause
    exit /b 1
)

echo [OK] PostgreSQL found!
psql --version
echo.

REM Set environment variable from the operator's existing configuration.
echo [STEP 1] Setting DATABASE_URL environment variable...
if "%DATABASE_URL%"=="" (
    echo [ERROR] Set DATABASE_URL before running this script.
    exit /b 1
)
setx DATABASE_URL "%DATABASE_URL%"
echo [OK] DATABASE_URL set!
echo.

REM Get PostgreSQL superuser password
echo [STEP 2] PostgreSQL Superuser Setup
echo.
echo Enter your PostgreSQL superuser password (default: postgres)
set /p PGPASSWORD="PostgreSQL Superuser Password: "
if "%PGPASSWORD%"=="" set PGPASSWORD=postgres
echo.

REM Create database and user
echo [STEP 3] Creating database and user...
echo Please confirm the PostgreSQL superuser password when prompted.
echo.

psql -U postgres -h localhost -f setup_database.sql
if %errorlevel% neq 0 (
    echo.
    echo [ERROR] Failed to create database. Possible reasons:
    echo   - PostgreSQL service is not running
    echo   - Wrong superuser password
    echo   - Database already exists
    echo.
    pause
    exit /b 1
)

echo [OK] Database created!
echo.

REM Test connection
echo [STEP 4] Testing database connection...
echo.

psql -U cdss_user -d medical_cdss -h localhost -c "SELECT version();" 2>nul
if %errorlevel% neq 0 (
    echo [ERROR] Cannot connect to database!
    echo.
    echo Troubleshooting:
    echo   1. Check if PostgreSQL service is running
    echo   2. Verify database was created successfully
    echo   3. Check username and password
    echo.
    pause
    exit /b 1
)

echo [OK] Connection successful!
echo.

REM Install Python dependencies
echo [STEP 5] Installing Python dependencies...
echo.

if not exist venv (
    python -m venv venv
)

call venv\Scripts\activate.bat

pip install -r requirements.txt --quiet
if %errorlevel% neq 0 (
    echo [ERROR] Failed to install dependencies
    pause
    exit /b 1
)

echo [OK] Dependencies installed!
echo.

REM Offer to run the app
echo ===============================================
echo [SUCCESS] Setup Complete!
echo ===============================================
echo.
echo Database Details:
echo   Database: medical_cdss
echo   Username: cdss_user
echo   Password: configured by the operator
echo   Host: localhost
echo   Port: 5432
echo.
echo Next step: Run the Flask application
echo.

set /p RUNAPP="Do you want to start the Flask app now? (Y/N): "
if /i "%RUNAPP%"=="Y" (
    echo.
    echo Starting Flask application...
    echo Visit: http://localhost:5000
    echo.
    echo Press Ctrl+C to stop the application
    echo.
    python app.py
) else (
    echo.
    echo To start the app later, run:
    echo   cd c:\medical_cdss
    echo   venv\Scripts\activate.bat
    echo   python app.py
    echo.
    echo Then visit: http://localhost:5000
    echo.
)

pause
