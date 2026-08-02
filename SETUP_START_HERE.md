# 🚀 START HERE - Quick Setup Guide

Complete PostgreSQL setup and run the Medical CDSS app in **5-10 minutes**.

---

## ⚡ The Fastest Way (Windows Users)

### Step 1: Install PostgreSQL (2 minutes)

**Download and Install:**
1. Go to: https://www.postgresql.org/download/windows/
2. Download the installer for Windows
3. Run the installer
4. **Important:** Remember the superuser password!
5. Use default settings (Port: 5432)
6. Finish installation

**Verify Installation:**
- Open Command Prompt
- Type: `psql --version`
- Should see: `psql (PostgreSQL) 15.x` or similar

If you get "not recognized", add PostgreSQL to PATH:
- Copy: `C:\Program Files\PostgreSQL\15\bin`
- Add to Windows PATH (Google: "add to PATH windows" if unsure)
- Restart Command Prompt

---

### Step 2: Run Automated Setup (3 minutes)

**One-Click Setup (Recommended):**

1. Navigate to project folder:
   ```cmd
   cd c:\medical_cdss
   ```

2. Run the setup script:
   ```cmd
   setup_postgres.bat
   ```

3. Follow the prompts:
   - Enter PostgreSQL superuser password
   - Wait for setup to complete
   - Say "Y" to run the app

**That's it!** The app will start at http://localhost:5000

---

## 📋 Manual Setup (If Automated Fails)

### Step 1: Create Database

Open Command Prompt:

```cmd
psql -U postgres -h localhost
```

When prompted for password, enter your PostgreSQL superuser password.

Then copy-paste these commands:

```sql
CREATE DATABASE medical_cdss;
CREATE USER cdss_user WITH PASSWORD 'Password123!';
GRANT ALL PRIVILEGES ON DATABASE medical_cdss TO cdss_user;
GRANT ALL PRIVILEGES ON SCHEMA public TO cdss_user;
ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT ALL PRIVILEGES ON TABLES TO cdss_user;
ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT ALL PRIVILEGES ON SEQUENCES TO cdss_user;
\q
```

### Step 2: Set Environment Variable

**Command Prompt:**
```cmd
setx DATABASE_URL "postgresql://postgres:admin123@localhost:5432/medical_cdss"
```

**PowerShell:**
```powershell
[Environment]::SetEnvironmentVariable("DATABASE_URL", "postgresql://postgres:admin123@localhost:5432/medical_cdss", "User")
```

⚠️ **Restart Command Prompt after setting**

### Step 3: Run the App

```cmd
cd c:\medical_cdss
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

---

## ✅ Verify Everything Works

### Test 1: Open the App
- Browser: **http://localhost:5000**
- Should see: Home page with Medical CDSS logo

### Test 2: Create an Assessment
1. Go to: http://localhost:5000/assessment
2. Fill form:
   - Name: Test Patient
   - Age: 45
   - Blood Sugar: 150
   - BMI: 28
   - Blood Pressure: 130
3. Click "Assess Risk"
4. See risk score and recommendations

### Test 3: Check Database
```cmd
psql -U cdss_user -d medical_cdss -h localhost
```

Run:
```sql
SELECT * FROM patients;
SELECT * FROM assessments;
\q
```

### Test 4: API Health Check
- Browser: **http://localhost:5000/api/health**
- Should see JSON response with "healthy" status

---

## 🎯 Quick Reference

| What | Where |
|------|-------|
| Full Windows Setup Guide | `POSTGRES_WINDOWS_SETUP.md` |
| Complete Project Guide | `COMPLETE_GUIDE.md` |
| Usage Examples | `USAGE_EXAMPLES.md` |
| Database Configuration | `POSTGRESQL_CONFIG.md` |
| Heroku Deployment | `HEROKU_QUICK_DEPLOY.md` |
| AWS Deployment | `AWS_DEPLOYMENT.md` |

---

## 📝 Connection Details (Remember These)

```
Host:       localhost
Port:       5432
Database:   medical_cdss
Username:   cdss_user
Password:   Password123!
```

**Connection String:**
```
postgresql://cdss_user:Password123!@localhost:5432/medical_cdss
```

---

## 🆘 Troubleshooting

### ❌ "psql: command not found"
→ Add PostgreSQL bin to PATH or use full path:
```cmd
"C:\Program Files\PostgreSQL\15\bin\psql" -U postgres
```

### ❌ "FATAL: password authentication failed"
→ Wrong superuser password. Try the one you set during PostgreSQL install.

### ❌ "could not connect to server"
→ PostgreSQL service not running. Start it:
   - Windows Services → postgresql-x64-15 → Right-click Start

### ❌ "database does not exist"
→ Run Step 1 of manual setup to create the database

### ❌ Flask app won't start
→ Check if port 5000 is free, or set: `python app.py --port 5001`

---

## 🚀 Next Steps

1. ✅ PostgreSQL set up
2. ✅ Database created
3. ✅ App running at http://localhost:5000
4. 📖 Read `COMPLETE_GUIDE.md` for full documentation
5. 🌐 Deploy to cloud using `HEROKU_QUICK_DEPLOY.md` or `AWS_DEPLOYMENT.md`

---

## 💡 Pro Tips

- **Save credentials somewhere safe** - you'll need them for deployment
- **Run app from virtual environment** - `venv\Scripts\activate.bat`
- **Check logs** - Flask output in console shows what's happening
- **Use pgAdmin** - GUI tool for PostgreSQL management
- **Backup database** - Regular backups for production use

---

## ✨ You're Ready!

Your Medical CDSS system is now:
- ✅ Fuzzy logic engine ready
- ✅ PostgreSQL database configured
- ✅ Web interface running
- ✅ REST API functional
- ✅ Ready for production deployment

**Start exploring:** http://localhost:5000

---

**Need help?** Read the full guides in the root directory or check the troubleshooting sections.

Questions about deployment? See:
- `HEROKU_QUICK_DEPLOY.md` - 5-minute Heroku deployment
- `AWS_DEPLOYMENT.md` - AWS production setup
- `COMPLETE_GUIDE.md` - All deployment options
