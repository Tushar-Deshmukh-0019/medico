# 🐘 PostgreSQL Setup for Windows - Medical CDSS

Complete step-by-step guide to set up PostgreSQL on Windows for the Medical Decision Support System.

---

## 📋 Table of Contents

1. [Install PostgreSQL](#install-postgresql)
2. [Create Database and User](#create-database-and-user)
3. [Configure Connection](#configure-connection)
4. [Run the Application](#run-the-application)
5. [Verify Setup](#verify-setup)
6. [Troubleshooting](#troubleshooting)

---

## 🔧 Install PostgreSQL

### Step 1: Download PostgreSQL

1. Go to: **https://www.postgresql.org/download/windows/**
2. Click "Download the installer"
3. Choose the latest version (14, 15, or 16)

### Step 2: Run the Installer

1. Run the downloaded `.exe` file
2. **Important settings:**
   - **Installation directory:** `C:\Program Files\PostgreSQL\15` (or your version)
   - **Port:** `5432` (default is fine)
   - **Superuser password:** Write this down! Example: `postgres123`
   - **Service name:** `postgresql-x64-15` (or similar)

### Step 3: Complete Installation

- Check "Launch Stack Builder at Exit?" → **Uncheck** (we don't need extra components)
- Finish installation

### Step 4: Verify Installation

Open Command Prompt and run:

```cmd
psql --version
```

**Expected output:** `psql (PostgreSQL) 15.x` or similar

If you get "psql is not recognized", add PostgreSQL to your PATH:

**Option A: Use Full Path**
```cmd
"C:\Program Files\PostgreSQL\15\bin\psql" --version
```

**Option B: Add to Windows PATH**
1. Right-click Computer → Properties
2. Advanced System Settings
3. Environment Variables
4. Add `C:\Program Files\PostgreSQL\15\bin` to PATH
5. Restart Command Prompt

---

## 🗄️ Create Database and User

### Step 1: Connect to PostgreSQL

Open Command Prompt and run:

```cmd
psql -U postgres -h localhost
```

**If prompted for password:** Enter the superuser password you set during installation

### Step 2: Create Medical CDSS Database

Copy-paste these commands into the psql prompt:

```sql
-- Create the database
CREATE DATABASE medical_cdss;

-- Create a dedicated user
CREATE USER cdss_user WITH PASSWORD 'Password123!';

-- Grant all privileges to the user
GRANT ALL PRIVILEGES ON DATABASE medical_cdss TO cdss_user;

-- Grant schema privileges
GRANT ALL PRIVILEGES ON SCHEMA public TO cdss_user;

-- Grant table privileges (for future tables)
ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT ALL PRIVILEGES ON TABLES TO cdss_user;
ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT ALL PRIVILEGES ON SEQUENCES TO cdss_user;

-- Exit psql
\q
```

### Step 3: Verify Creation

```cmd
psql -U postgres -d medical_cdss -h localhost
```

When prompted for password, enter: `admin123`

If successful, you'll see:
```
medical_cdss=>
```

Exit with:
```
\q
```

---

## 🔌 Configure Connection

### Option 1: Using Environment Variable (Recommended)

**Windows Command Prompt:**
```cmd
setx DATABASE_URL "postgresql://postgres:admin123@localhost:5432/medical_cdss"
```

**Windows PowerShell:**
```powershell
[Environment]::SetEnvironmentVariable("DATABASE_URL", "postgresql://postgres:admin123@localhost:5432/medical_cdss", "User")
```

⚠️ **After setting, restart Command Prompt or PowerShell**

### Option 2: Using .env File (Alternative)

Create file: `c:\medical_cdss\.env`

```
DATABASE_URL=postgresql://postgres:admin123@localhost:5432/medical_cdss
FLASK_ENV=development
```

### Option 3: Modify connection.py (For Testing Only)

Edit `c:\medical_cdss\database\connection.py` and change line 27:

```python
database_url = 'postgresql://postgres:admin123@localhost:5432/medical_cdss'
```

---

## 🚀 Run the Application

### Step 1: Open Command Prompt

Navigate to project directory:
```cmd
cd c:\medical_cdss
```

### Step 2: Activate Virtual Environment (if exists)

```cmd
venv\Scripts\activate
```

Or create a new one:
```cmd
python -m venv venv
venv\Scripts\activate
```

### Step 3: Install Dependencies

```cmd
pip install -r requirements.txt
```

### Step 4: Start the Application

```cmd
python app.py
```

**Expected output:**
```
 * Running on http://127.0.0.1:5000
 * Press CTRL+C to quit
```

### Step 5: Access the Application

Open your browser and go to: **http://localhost:5000**

---

## ✅ Verify Setup

### Test 1: Database Connection

The Flask app will automatically:
1. Connect to PostgreSQL
2. Create tables (`patients` and `assessments`)
3. Show "✓ Database initialized successfully" in console

### Test 2: Create an Assessment

1. Go to: **http://localhost:5000/assessment**
2. Fill in the form:
   - Name: "Test Patient"
   - Age: 45
   - Blood Sugar: 150
   - BMI: 28
   - Blood Pressure: 130
3. Click "Assess Risk"
4. See the risk score and recommendations

### Test 3: Check Database

Open Command Prompt:

```cmd
psql -U cdss_user -d medical_cdss -h localhost
```

Run these queries:

```sql
-- See all patients
SELECT * FROM patients;

-- See all assessments
SELECT * FROM assessments;

-- Count assessments
SELECT COUNT(*) FROM assessments;

-- Exit
\q
```

### Test 4: API Health Check

Open browser and visit: **http://localhost:5000/api/health**

Expected response:
```json
{
  "status": "success",
  "data": {
    "status": "healthy",
    "fuzzy_engine": "ready",
    "database": "connected"
  }
}
```

---

## 🆘 Troubleshooting

### Problem: "psql: command not found" or "is not recognized"

**Solution:** PostgreSQL bin directory not in PATH

1. Find your PostgreSQL installation: `C:\Program Files\PostgreSQL\15\bin\`
2. Use full path:
   ```cmd
   "C:\Program Files\PostgreSQL\15\bin\psql" -U postgres
   ```
3. Or add to PATH (see [Step 4 of Install PostgreSQL](#step-4-verify-installation))

---

### Problem: "FATAL: password authentication failed for user 'postgres'"

**Solution:** Wrong password

1. Reset the password:
   ```cmd
   "C:\Program Files\PostgreSQL\15\bin\psql" -U postgres -h localhost
   ```
2. If you forgot the password, reinstall PostgreSQL and choose a new one

---

### Problem: "could not connect to server: No such file or directory"

**Solution:** PostgreSQL service not running

1. Open Services (services.msc):
   - Right-click Start → Run → type `services.msc`
2. Find `postgresql-x64-15` (or your version)
3. Right-click → Start
4. Try connecting again

Or check if running:
```cmd
tasklist | findstr postgres
```

---

### Problem: "database 'medical_cdss' does not exist"

**Solution:** Database wasn't created

1. Connect as superuser:
   ```cmd
   psql -U postgres -h localhost
   ```
2. Run:
   ```sql
   CREATE DATABASE medical_cdss;
   ```

---

### Problem: "permission denied for schema public"

**Solution:** User doesn't have privileges

1. Connect as superuser:
   ```cmd
   psql -U postgres -h localhost -d medical_cdss
   ```
2. Run:
   ```sql
   GRANT ALL PRIVILEGES ON SCHEMA public TO cdss_user;
   GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO cdss_user;
   ```

---

### Problem: Flask app says "cannot connect to PostgreSQL"

**Solution:** Check connection string

1. Verify environment variable is set:
   ```cmd
   echo %DATABASE_URL%
   ```
2. If not set, restart Command Prompt after setting it
3. Check connection string format:
   ```
   postgresql://username:password@host:port/database
   ```
4. Verify values:
   - Host: `localhost` (not 127.0.0.1)
   - Port: `5432` (default PostgreSQL port)
   - Database: `medical_cdss` (name you created)
   - Username: `cdss_user` (user you created)
   - Password: `Password123!` (password you set)

---

### Problem: Port 5432 already in use

**Solution:** Another service using the port

1. Find what's using port 5432:
   ```cmd
   netstat -ano | findstr :5432
   ```
2. Either:
   - Stop PostgreSQL and reconfigure to different port during reinstall
   - Or kill the process: `taskkill /PID <PID> /F`

---

## 📝 Connection String Reference

### Format:
```
postgresql://username:password@host:port/database
```

### Examples:

**Local development (with password):**
```
postgresql://cdss_user:Password123!@localhost:5432/medical_cdss
```

**Local development (no password):**
```
postgresql://cdss_user@localhost:5432/medical_cdss
```

**With special characters in password (URL encode):**
```
postgresql://cdss_user:Pass%40word123@localhost:5432/medical_cdss
```
(@ becomes %40, # becomes %23, etc.)

---

## 🎯 Quick Reference

| Item | Value |
|------|-------|
| Host | localhost |
| Port | 5432 |
| Database | medical_cdss |
| Username | postgres |
| Password | admin123 |
| Connection String | `postgresql://postgres:admin123@localhost:5432/medical_cdss` |

---

## ✨ You're All Set!

Once setup is complete:

1. **PostgreSQL running** with `medical_cdss` database
2. **Application running** at http://localhost:5000
3. **Assessments stored** in PostgreSQL database
4. **Ready for deployment** to cloud (Heroku, AWS, etc.)

---

## 📚 Next Steps

1. Read: `COMPLETE_GUIDE.md` - Full guide including deployment
2. Read: `USAGE_EXAMPLES.md` - How to use the system
3. Read: `POSTGRESQL_CONFIG.md` - Advanced PostgreSQL configuration
4. Deploy: See `HEROKU_QUICK_DEPLOY.md` or `AWS_DEPLOYMENT.md`

---

## 🔗 Useful Links

- PostgreSQL Official: https://www.postgresql.org/
- PostgreSQL Windows Download: https://www.postgresql.org/download/windows/
- PostgreSQL Documentation: https://www.postgresql.org/docs/
- psycopg2 (Python adapter): https://www.psycopg.org/

---

**Questions?** Check the troubleshooting section or read POSTGRESQL_CONFIG.md for advanced setup!
