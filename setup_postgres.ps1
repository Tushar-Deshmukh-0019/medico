# ===============================================
# Medical CDSS PostgreSQL Setup for Windows
# PowerShell Version
# ===============================================
# Run this script with: powershell -ExecutionPolicy Bypass -File setup_postgres.ps1

Write-Host "=======================================" -ForegroundColor Cyan
Write-Host "Medical CDSS - PostgreSQL Setup" -ForegroundColor Cyan
Write-Host "=======================================" -ForegroundColor Cyan
Write-Host ""

# Check if psql is available
$psql = Get-Command psql -ErrorAction SilentlyContinue

if (-not $psql) {
    Write-Host "[ERROR] PostgreSQL is not installed or not in PATH" -ForegroundColor Red
    Write-Host ""
    Write-Host "Please install PostgreSQL from:" -ForegroundColor Yellow
    Write-Host "  https://www.postgresql.org/download/windows/" -ForegroundColor Yellow
    Write-Host ""
    Write-Host "Then add to PATH:" -ForegroundColor Yellow
    Write-Host "  C:\Program Files\PostgreSQL\15\bin" -ForegroundColor Yellow
    Write-Host ""
    Read-Host "Press Enter to exit"
    exit 1
}

Write-Host "[OK] PostgreSQL found!" -ForegroundColor Green
psql --version
Write-Host ""

# Step 1: Set environment variable
Write-Host "[STEP 1] Setting DATABASE_URL environment variable..." -ForegroundColor Cyan
if ([string]::IsNullOrWhiteSpace($env:DATABASE_URL)) {
    Write-Host "[ERROR] Set DATABASE_URL before running this script." -ForegroundColor Red
    exit 1
}
$dbUrl = $env:DATABASE_URL
[Environment]::SetEnvironmentVariable("DATABASE_URL", $dbUrl, "User")
Write-Host "[OK] DATABASE_URL set!" -ForegroundColor Green
Write-Host ""

# Step 2: Get superuser password
Write-Host "[STEP 2] PostgreSQL Superuser Setup" -ForegroundColor Cyan
Write-Host ""
$pgPassword = Read-Host "Enter PostgreSQL superuser password (default: postgres)"
if ([string]::IsNullOrWhiteSpace($pgPassword)) {
    $pgPassword = "postgres"
}
Write-Host ""

# Step 3: Create database using SQL script
Write-Host "[STEP 3] Creating database and user..." -ForegroundColor Cyan
Write-Host "Please enter the superuser password when prompted." -ForegroundColor Yellow
Write-Host ""

$env:PGPASSWORD = $pgPassword
& psql -U postgres -h localhost -f setup_database.sql
$lastExitCode = $LASTEXITCODE
Remove-Item env:PGPASSWORD

if ($lastExitCode -ne 0) {
    Write-Host ""
    Write-Host "[ERROR] Failed to create database" -ForegroundColor Red
    Write-Host ""
    Write-Host "Possible reasons:" -ForegroundColor Yellow
    Write-Host "  - PostgreSQL service is not running" -ForegroundColor Yellow
    Write-Host "  - Wrong superuser password" -ForegroundColor Yellow
    Write-Host "  - Database already exists" -ForegroundColor Yellow
    Write-Host ""
    Read-Host "Press Enter to exit"
    exit 1
}

Write-Host "[OK] Database created!" -ForegroundColor Green
Write-Host ""

# Step 4: Test connection
Write-Host "[STEP 4] Testing database connection..." -ForegroundColor Cyan
Write-Host ""

$testOutput = & psql -U cdss_user -d medical_cdss -h localhost -c "SELECT version();" 2>&1
$testExitCode = $LASTEXITCODE
Remove-Item env:PGPASSWORD

if ($testExitCode -ne 0) {
    Write-Host "[ERROR] Cannot connect to database!" -ForegroundColor Red
    Write-Host ""
    Write-Host "Troubleshooting:" -ForegroundColor Yellow
    Write-Host "  1. Check if PostgreSQL service is running" -ForegroundColor Yellow
    Write-Host "  2. Verify database was created successfully" -ForegroundColor Yellow
    Write-Host "  3. Check username and password" -ForegroundColor Yellow
    Write-Host ""
    Read-Host "Press Enter to exit"
    exit 1
}

Write-Host "[OK] Connection successful!" -ForegroundColor Green
Write-Host $testOutput
Write-Host ""

# Step 5: Create virtual environment and install dependencies
Write-Host "[STEP 5] Setting up Python environment..." -ForegroundColor Cyan
Write-Host ""

if (-not (Test-Path "venv")) {
    Write-Host "Creating virtual environment..." -ForegroundColor Cyan
    python -m venv venv
}

Write-Host "Activating virtual environment..." -ForegroundColor Cyan
& ".\venv\Scripts\Activate.ps1"

Write-Host "Installing dependencies..." -ForegroundColor Cyan
pip install -r requirements.txt --quiet

if ($LASTEXITCODE -ne 0) {
    Write-Host "[ERROR] Failed to install dependencies" -ForegroundColor Red
    Read-Host "Press Enter to exit"
    exit 1
}

Write-Host "[OK] Dependencies installed!" -ForegroundColor Green
Write-Host ""

# Summary
Write-Host "=======================================" -ForegroundColor Green
Write-Host "[SUCCESS] Setup Complete!" -ForegroundColor Green
Write-Host "=======================================" -ForegroundColor Green
Write-Host ""

Write-Host "Database Details:" -ForegroundColor Cyan
Write-Host "  Database:  medical_cdss" -ForegroundColor White
Write-Host "  Username:  cdss_user" -ForegroundColor White
Write-Host "  Password:  configured by the operator" -ForegroundColor White
Write-Host "  Host:      localhost" -ForegroundColor White
Write-Host "  Port:      5432" -ForegroundColor White
Write-Host ""

Write-Host "Environment Variable:" -ForegroundColor Cyan
Write-Host "  DATABASE_URL=$dbUrl" -ForegroundColor White
Write-Host ""

Write-Host "Next step: Run the Flask application" -ForegroundColor Cyan
Write-Host ""

$runApp = Read-Host "Do you want to start the Flask app now? (Y/N)"

if ($runApp -eq "Y" -or $runApp -eq "y") {
    Write-Host ""
    Write-Host "Starting Flask application..." -ForegroundColor Cyan
    Write-Host "Visit: http://localhost:5000" -ForegroundColor Yellow
    Write-Host ""
    Write-Host "Press Ctrl+C to stop the application" -ForegroundColor Yellow
    Write-Host ""
    python app.py
} else {
    Write-Host ""
    Write-Host "To start the app later, run:" -ForegroundColor Cyan
    Write-Host "  cd c:\medical_cdss" -ForegroundColor White
    Write-Host "  .\venv\Scripts\Activate.ps1" -ForegroundColor White
    Write-Host "  python app.py" -ForegroundColor White
    Write-Host ""
    Write-Host "Then visit: http://localhost:5000" -ForegroundColor Yellow
    Write-Host ""
}

Read-Host "Press Enter to exit"
