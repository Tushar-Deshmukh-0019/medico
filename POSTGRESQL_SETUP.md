# 🐘 PostgreSQL Setup Guide

Complete guide to set up and use PostgreSQL with the Medical Decision Support System.

---

## 📦 Installation

### Windows

**Option 1: Download Installer**
1. Go to: https://www.postgresql.org/download/windows/
2. Download PostgreSQL 15 or higher
3. Run installer
4. Choose password for `postgres` user (remember this!)
5. Port: 5432 (default)
6. Install

**Option 2: Using Chocolatey**
```bash
choco install postgresql
```

**Option 3: Using WSL (Windows Subsystem for Linux)**
```bash
sudo apt-get update
sudo apt-get install postgresql postgresql-contrib
sudo service postgresql start
```

### Linux (Ubuntu/Debian)

```bash
sudo apt-get update
sudo apt-get install postgresql postgresql-contrib

# Start PostgreSQL
sudo service postgresql start

# Or with systemd
sudo systemctl start postgresql
```

### macOS

```bash
# Using Homebrew
brew install postgresql

# Start service
brew services start postgresql

# Or manually
pg_ctl -D /usr/local/var/postgres start
```

---

## ✅ Verify Installation

### Test PostgreSQL Connection

**Windows Command Prompt:**
```bash
psql -U postgres

# Should prompt for password
# Enter the password you set during installation
# You should see: postgres=#
```

**Linux/Mac:**
```bash
sudo -u postgres psql

# You should see: postgres=#
```

### Exit psql
```
\q
```

---

## 🗄️ Create Database & User

### Method 1: Using psql CLI

**Windows:**
```bash
# Open Command Prompt
psql -U postgres

# Create database
CREATE DATABASE medical_cdss;

# Create user
CREATE USER cdss_user WITH PASSWORD '<choose-a-strong-password>';

# Grant privileges
ALTER ROLE cdss_user SET client_encoding TO 'utf8';
ALTER ROLE cdss_user SET default_transaction_isolation TO 'read committed';
ALTER ROLE cdss_user SET default_transaction_deferrable TO on;
ALTER ROLE cdss_user SET default_transaction_readonly TO off;
GRANT ALL PRIVILEGES ON DATABASE medical_cdss TO cdss_user;

# Exit
\q
```

**Linux/Mac:**
```bash
sudo -u postgres psql

# Same commands as above
```

### Method 2: Using pgAdmin GUI

1. Install pgAdmin: https://www.pgadmin.org/download/
2. Open pgAdmin
3. Right-click "Servers"
4. Create → Server
5. Connect to localhost
6. Create database and user via GUI

---

## 🔧 Configuration

### Set Environment Variable (Local Development)

**Windows Command Prompt:**
```bash
set DATABASE_URL=<your PostgreSQL connection string>
```

**Windows PowerShell:**
```powershell
$env:DATABASE_URL = "<your PostgreSQL connection string>"
```

**Linux/Mac:**
```bash
export DATABASE_URL="<your PostgreSQL connection string>"
```

### .env File (Better Practice)

Create file: `c:\medical_cdss\.env`
```
DATABASE_URL=<your PostgreSQL connection string>
FLASK_ENV=development
FLASK_DEBUG=True
SECRET_KEY=your-secret-key-here
```

**Note:** Don't commit .env to git (already in .gitignore)

---

## 🚀 Start Using PostgreSQL

### Step 1: Install Python Dependencies

```bash
cd c:\medical_cdss

# Make sure venv is activated
venv\Scripts\activate

# Install packages
pip install -r requirements.txt
```

**Key package for PostgreSQL:**
- `psycopg2-binary==2.9.9` ✓ (Already in requirements.txt)

### Step 2: Start PostgreSQL Service

**Windows:**
```bash
# PostgreSQL starts automatically on boot
# Or start service manually:
# Services (services.msc) → postgresql → Start
```

**Linux:**
```bash
sudo service postgresql start
# or
sudo systemctl start postgresql
```

**Mac:**
```bash
brew services start postgresql
# or
pg_ctl -D /usr/local/var/postgres start
```

### Step 3: Run Your App

```bash
# Set DATABASE_URL (see above)
set DATABASE_URL=postgresql://cdss_user:password@localhost:5432/medical_cdss

# Start Flask
python app.py

# Visit http://localhost:5000
```

### Step 4: Verify Database

**Check data is being saved:**

```bash
# In psql
psql -U cdss_user -d medical_cdss -h localhost

# View tables
\dt

# Check patients table
SELECT * FROM patients;

# Check assessments table
SELECT * FROM assessments;

# Exit
\q
```

---

## 📊 PostgreSQL Data Types

The system uses these PostgreSQL data types:

| Python | SQLAlchemy | PostgreSQL |
|--------|-----------|-----------|
| int | Integer | INTEGER |
| str | String | VARCHAR |
| float | Float | REAL |
| datetime | DateTime | TIMESTAMP |
| text | Text | TEXT |
| bool | Boolean | BOOLEAN |

---

## 🔍 Useful PostgreSQL Commands

### Connect to Database

```bash
# As postgres user
psql -U postgres

# As specific user
psql -U cdss_user -d medical_cdss

# With host and port
psql -h localhost -p 5432 -U cdss_user -d medical_cdss
```

### List Databases

```bash
\l
```

### List Tables

```bash
\dt
```

### Describe Table

```bash
\d patients
\d assessments
```

### View Data

```bash
SELECT * FROM patients;
SELECT * FROM assessments WHERE risk_category = 'high';
SELECT COUNT(*) FROM assessments;
```

### Exit psql

```bash
\q
```

---

## ☁️ Cloud PostgreSQL

### Heroku PostgreSQL

```bash
# Add PostgreSQL to Heroku
heroku addons:create heroku-postgresql:basic

# Get connection string
heroku config | grep DATABASE_URL

# It will automatically set DATABASE_URL
```

### AWS RDS PostgreSQL

```bash
# Create RDS instance via AWS Console:
# 1. Services → RDS
# 2. Create database
# 3. Engine: PostgreSQL
# 4. DB instance identifier: medical-cdss-db
# 5. Master username: cdss_user
# 6. Master password: YourSecurePassword
# 7. Copy Endpoint

# Set environment variable
set DATABASE_URL=postgresql://cdss_user:password@medical-cdss-db.xxxxx.us-east-1.rds.amazonaws.com:5432/medical_cdss
```

### Azure PostgreSQL

```bash
# Create via Azure CLI:
az postgres server create \
  --resource-group rg \
  --name medical-cdss-db \
  --admin-user cdss_user \
  --admin-password YourSecurePassword \
  --sku-name B_Gen5_1

# Get connection string
az postgres server show --resource-group rg --name medical-cdss-db

# Set DATABASE_URL
```

### Google Cloud SQL

```bash
# Create instance via Google Cloud Console:
# 1. SQL Admin
# 2. Create instance
# 3. PostgreSQL
# 4. Configure

# Use Cloud SQL Proxy or connection string
```

---

## 🆘 Troubleshooting

### "Connection refused"

**Problem:** Cannot connect to PostgreSQL
**Solutions:**
```bash
# 1. Check if PostgreSQL is running
# Windows: Services → postgresql (should be running)
# Linux: sudo systemctl status postgresql
# Mac: brew services list

# 2. Check connection string
echo %DATABASE_URL%

# 3. Verify credentials
psql -h localhost -U cdss_user -d medical_cdss
```

### "Password authentication failed"

**Problem:** Wrong password
**Solution:**
```bash
# Reset password
psql -U postgres

ALTER USER cdss_user WITH PASSWORD '<new-strong-password>';

\q

# Update DATABASE_URL with new password
```

### "Database does not exist"

**Problem:** medical_cdss database not created
**Solution:**
```bash
psql -U postgres

CREATE DATABASE medical_cdss;

\q
```

### "Role does not exist"

**Problem:** User cdss_user not created
**Solution:**
```bash
psql -U postgres

CREATE USER cdss_user WITH PASSWORD '<choose-a-strong-password>';

GRANT ALL PRIVILEGES ON DATABASE medical_cdss TO cdss_user;

\q
```

### App won't start with PostgreSQL

**Problem:** Database connection error
**Solutions:**
```bash
# 1. Check DATABASE_URL is set
echo %DATABASE_URL%

# 2. Verify PostgreSQL is running
# Services or terminal

# 3. Test connection
psql -h localhost -U cdss_user -d medical_cdss

# 4. Check Flask logs for detailed error
# Should show connection error
```

---

## 📝 Complete Setup Example

### Full Setup from Scratch

**1. Install PostgreSQL**
```bash
# Download from https://www.postgresql.org/download/windows/
# Run installer
# Remember password for postgres user
```

**2. Create Database**
```bash
psql -U postgres

CREATE DATABASE medical_cdss;
CREATE USER cdss_user WITH PASSWORD '<choose-a-strong-password>';
GRANT ALL PRIVILEGES ON DATABASE medical_cdss TO cdss_user;

\q
```

**3. Configure Environment**
```bash
cd c:\medical_cdss

# Create .env file
echo DATABASE_URL=<your PostgreSQL connection string> > .env
```

**4. Install Dependencies**
```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

**5. Run App**
```bash
python app.py
# Visit http://localhost:5000
```

**6. Verify Database**
```bash
psql -U cdss_user -d medical_cdss

SELECT * FROM patients;
SELECT * FROM assessments;

\q
```

---

## 🔐 Security Best Practices

### 1. Strong Passwords
```bash
# Don't use: password, 123456, postgres
# Use: Mix of uppercase, lowercase, numbers, special characters
# Example: use a unique strong password stored outside the repository

# Character requirements:
# - Minimum 12 characters
# - Mix of types
# - No common words
```

### 2. Limit Access

**PostgreSQL:**
```bash
# Don't expose to internet
# Use VPN or SSH tunnel if needed
# Restrict IP addresses in pg_hba.conf
```

**Cloud PostgreSQL:**
```bash
# Use security groups
# Allow only app server IP
# Disable public access
```

### 3. Regular Backups

**Local:**
```bash
# Backup database
pg_dump -U cdss_user medical_cdss > backup.sql

# Restore from backup
psql -U cdss_user medical_cdss < backup.sql
```

**Cloud:**
```bash
# Enable automated backups
# Heroku: Automatic daily
# AWS RDS: Configure backup window
# Azure: Configure retention
```

### 4. Connection Security

**Use SSL/TLS:**
```bash
# Production connection strings should use SSL
DATABASE_URL=postgresql://user:pass@host:5432/db?sslmode=require
```

---

## 📊 Performance Tips

### 1. Indexing

```bash
# Indexes are automatically created on:
# - Primary keys (patient.id, assessment.id)
# - Foreign keys (assessment.patient_id)
# - Unique columns (patient.email)

# Check indexes
\d patients
```

### 2. Connection Pooling

**Already configured in app:**
```python
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {
    'pool_size': 10,          # 10 connections
    'pool_recycle': 3600,     # Recycle after 1 hour
    'pool_pre_ping': True,    # Test connection before use
}
```

### 3. Query Optimization

```bash
# Analyze slow queries
EXPLAIN ANALYZE SELECT * FROM assessments WHERE risk_category = 'high';

# Add index if needed
CREATE INDEX idx_risk_category ON assessments(risk_category);
```

---

## 📚 Resources

### PostgreSQL Documentation
- https://www.postgresql.org/docs/
- https://www.postgresql.org/docs/current/sql-syntax.html

### Connection Strings
- https://www.postgresql.org/docs/current/libpq-connect.html

### Tools
- **pgAdmin:** https://www.pgadmin.org/
- **DBeaver:** https://dbeaver.io/
- **psql:** Built-in command line tool

### Cloud Platforms
- **Heroku PostgreSQL:** https://devcenter.heroku.com/articles/heroku-postgresql
- **AWS RDS:** https://docs.aws.amazon.com/rds/latest/UserGuide/CHAP_PostgreSQL.html
- **Azure PostgreSQL:** https://docs.microsoft.com/en-us/azure/postgresql/
- **Google Cloud SQL:** https://cloud.google.com/sql/docs/postgres

---

## ✅ PostgreSQL Setup Checklist

- [ ] PostgreSQL installed
- [ ] PostgreSQL running
- [ ] Database `medical_cdss` created
- [ ] User `cdss_user` created
- [ ] PASSWORD SET
- [ ] psycopg2-binary installed (`pip install psycopg2-binary`)
- [ ] DATABASE_URL set
- [ ] app.py runs without errors
- [ ] Can create assessments
- [ ] Data saves to PostgreSQL
- [ ] Can query data with psql

---

## 🎉 You're Ready!

Your system is now configured to use PostgreSQL!

**Next Steps:**
1. Follow COMPLETE_GUIDE.md for testing
2. Deploy to cloud when ready
3. PostgreSQL will work the same everywhere!

---

**PostgreSQL Setup Guide Version**: 1.0.0
**Status**: Ready for PostgreSQL ✅
**Compatibility**: Local + All Cloud Platforms
