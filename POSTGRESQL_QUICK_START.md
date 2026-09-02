# 🐘 PostgreSQL Quick Start (5 Minutes)

Get PostgreSQL set up and running immediately.

---

## ⚡ 5-Minute Setup

### Step 1: Install PostgreSQL (2 min)

**Windows:**
- Download: https://www.postgresql.org/download/windows/
- Run installer
- Remember the password!
- Port: 5432

**Linux:**
```bash
sudo apt-get install postgresql postgresql-contrib
```

**Mac:**
```bash
brew install postgresql
```

### Step 2: Create Database (1 min)

```bash
psql -U postgres

CREATE DATABASE medical_cdss;
CREATE USER cdss_user WITH PASSWORD '<choose-a-strong-password>';
GRANT ALL PRIVILEGES ON DATABASE medical_cdss TO cdss_user;

\q
```

### Step 3: Set Environment Variable (30 seconds)

**Windows CMD:**
```bash
set DATABASE_URL=<your PostgreSQL connection string>
```

**Windows PowerShell:**
```powershell
$env:DATABASE_URL = "<your PostgreSQL connection string>"
```

### Step 4: Run App (1.5 min)

```bash
cd c:\medical_cdss
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

**Visit:** http://localhost:5000

---

## ✅ Verify It Works

```bash
# Create an assessment
# Go to: http://localhost:5000/assessment
# Fill form and submit

# Check database
psql -U cdss_user -d medical_cdss -h localhost

SELECT * FROM patients;
SELECT * FROM assessments;

\q
```

---

## 📝 Connection String Format

```
postgresql://username:password@host:port/database

Example:
postgresql://cdss_user:<your-password>@localhost:5432/medical_cdss
```

---

## 🔑 Default Values

```
Host: localhost
Port: 5432
Database: medical_cdss
Username: cdss_user
Password: <your-password>
```

---

## 🆘 Quick Troubleshooting

| Issue | Solution |
|-------|----------|
| Connection refused | Start PostgreSQL service |
| Password wrong | Reset: `ALTER USER cdss_user WITH PASSWORD 'new_pass';` |
| Database not found | Create: `CREATE DATABASE medical_cdss;` |
| User not found | Create: `CREATE USER cdss_user WITH PASSWORD 'pass';` |

---

## 🚀 You're Done!

PostgreSQL is now configured and running!

**The app will automatically:**
- Create tables
- Store assessments
- Manage patients
- All in PostgreSQL

---

**Next:** Follow COMPLETE_GUIDE.md for testing and deployment!
