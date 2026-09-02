# 🐘 PostgreSQL Configuration for Medical CDSS

Complete configuration guide for PostgreSQL support in your application.

---

## ✅ What's Been Updated

### requirements.txt
- ✅ Added: `psycopg2-binary==2.9.9` (PostgreSQL adapter)
- ✅ Removed: `PyMySQL==1.1.0` (MySQL adapter)

### database/connection.py
- ✅ Updated to support PostgreSQL URLs
- ✅ Auto-converts Heroku postgres:// to postgresql://
- ✅ Includes connection pooling configuration
- ✅ Handles PostgreSQL-specific options

### Configuration
- ✅ Automatically detects DATABASE_URL environment variable
- ✅ Falls back to local PostgreSQL if not set
- ✅ Supports all cloud platforms

---

## 🚀 LOCAL SETUP

### Installation

**Windows (Easiest):**
1. Download PostgreSQL: https://www.postgresql.org/download/windows/
2. Run installer
3. Remember postgres password
4. Complete

**Linux (Ubuntu/Debian):**
```bash
sudo apt-get update
sudo apt-get install postgresql postgresql-contrib
sudo service postgresql start
```

**macOS (Homebrew):**
```bash
brew install postgresql
brew services start postgresql
```

### Create Database

**Option A: Command Line**
```bash
# Connect as admin
psql -U postgres

# Create database
CREATE DATABASE medical_cdss;

# Create user
CREATE USER cdss_user WITH PASSWORD '<choose-a-strong-password>';

# Grant permissions
GRANT ALL PRIVILEGES ON DATABASE medical_cdss TO cdss_user;

# Exit
\q
```

**Option B: pgAdmin GUI**
1. Install pgAdmin (https://www.pgadmin.org/)
2. Right-click Servers → Create → Server
3. Create database and user via interface

### Environment Setup

**Create .env file:**
```bash
# Windows
echo DATABASE_URL=<your PostgreSQL connection string> > .env
```

**Or manually create file:** `c:\medical_cdss\.env`
```
DATABASE_URL=<your PostgreSQL connection string>
FLASK_ENV=development
FLASK_DEBUG=True
```

### Start Application

```bash
# Activate virtual environment
venv\Scripts\activate

# Install dependencies (with PostgreSQL support)
pip install -r requirements.txt

# Run application
python app.py

# Visit http://localhost:5000
```

---

## ☁️ CLOUD DEPLOYMENT

### Heroku + PostgreSQL

**1. Create Heroku App**
```bash
heroku create your-app-name
```

**2. Add PostgreSQL**
```bash
heroku addons:create heroku-postgresql:basic
```

**3. DATABASE_URL Auto Set**
```bash
# Heroku automatically sets DATABASE_URL
# No configuration needed!
```

**4. Deploy**
```bash
git push heroku main
```

**5. Verify**
```bash
heroku config | grep DATABASE_URL
heroku logs --tail
```

### AWS + RDS PostgreSQL

**1. Create RDS Instance**
```bash
aws rds create-db-instance \
  --db-instance-identifier medical-cdss-db \
  --db-instance-class db.t3.micro \
  --engine postgres \
  --allocated-storage 20 \
  --master-username cdss_user \
  --master-user-password '<set-in-secret-manager>'
```

**2. Get Connection Endpoint**
```bash
aws rds describe-db-instances \
  --db-instance-identifier medical-cdss-db \
  --query 'DBInstances[0].Endpoint'
```

**3. Set Environment Variable**
```bash
eb setenv DATABASE_URL='<your managed PostgreSQL connection string>'
eb deploy
```

### Azure + PostgreSQL

**1. Create PostgreSQL Server**
```bash
az postgres server create \
  --resource-group my-rg \
  --name medical-cdss-db \
  --location eastus \
  --admin-user cdss_user \
  --admin-password '<set-in-secret-manager>' \
  --sku-name B_Gen5_1
```

**2. Create Database**
```bash
az postgres db create \
  --resource-group my-rg \
  --server-name medical-cdss-db \
  --name medical_cdss
```

**3. Set Connection String**
```bash
# Get FQDN
az postgres server show \
  --resource-group my-rg \
  --name medical-cdss-db

# Set DATABASE_URL in App Settings
az webapp config appsettings set \
  --resource-group my-rg \
  --name your-app \
  --settings DATABASE_URL='<your managed PostgreSQL connection string>'
```

### Google Cloud + Cloud SQL

**1. Create PostgreSQL Instance**
```bash
gcloud sql instances create medical-cdss-db \
  --database-version POSTGRES_14 \
  --tier db-f1-micro \
  --region us-central1
```

**2. Create Database**
```bash
gcloud sql databases create medical_cdss \
  --instance=medical-cdss-db
```

**3. Create User**
```bash
gcloud sql users create cdss_user \
  --instance=medical-cdss-db \
  --password='<set-in-secret-manager>'
```

**4. Set CONNECTION_NAME**
```bash
# Use Cloud SQL Proxy or
# Set DATABASE_URL in Cloud Run environment
```

---

## 🔧 Configuration Details

### Connection String Components

```
postgresql://[user]:[password]@[host]:[port]/[database]

Example:
postgresql://cdss_user:MyPass123@localhost:5432/medical_cdss

Cloud Examples:
# Heroku (auto-set)
postgresql://xxx:yyy@ec2-xxx.compute-1.amazonaws.com:5432/zzz

# AWS RDS
postgresql://cdss_user:MyPass@medical-cdss-db.xxxxx.us-east-1.rds.amazonaws.com:5432/medical_cdss

# Azure
postgresql://cdss_user:MyPass@medical-cdss-db.postgres.database.azure.com:5432/medical_cdss

# GCP Cloud SQL
postgresql://cdss_user:MyPass@/medical_cdss?unix_socket_dir=/cloudsql/project:region:instance
```

### Connection Pool Settings

**Already configured in app:**
```python
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {
    'pool_size': 10,              # Max 10 connections
    'pool_recycle': 3600,         # Recycle after 1 hour
    'pool_pre_ping': True,        # Test before using
}
```

**Adjust for your needs:**
```python
# For high traffic
'pool_size': 20,
'max_overflow': 40,

# For low traffic
'pool_size': 5,
'max_overflow': 10,
```

---

## 🗄️ Database Schema

The system automatically creates these PostgreSQL tables:

**patients**
```sql
CREATE TABLE patients (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE,
    phone VARCHAR(20),
    date_of_birth DATE,
    gender VARCHAR(10),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

**assessments**
```sql
CREATE TABLE assessments (
    id SERIAL PRIMARY KEY,
    patient_id INTEGER NOT NULL REFERENCES patients(id),
    blood_sugar REAL NOT NULL,
    bmi REAL NOT NULL,
    age INTEGER NOT NULL,
    blood_pressure REAL NOT NULL,
    risk_score REAL NOT NULL,
    risk_category VARCHAR(20) NOT NULL,
    blood_sugar_status VARCHAR(50),
    bmi_category VARCHAR(50),
    bp_category VARCHAR(50),
    clinical_notes TEXT,
    recommendations TEXT,
    assessment_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

---

## 📊 Useful PostgreSQL Queries

### View All Patients
```bash
psql -U cdss_user -d medical_cdss

SELECT id, name, email, created_at FROM patients;
```

### View Assessments
```bash
SELECT * FROM assessments ORDER BY assessment_date DESC;
```

### Count Assessments by Risk
```bash
SELECT 
    risk_category,
    COUNT(*) as count,
    ROUND(AVG(risk_score), 2) as avg_risk
FROM assessments
GROUP BY risk_category;
```

### Get Patient History
```bash
SELECT a.*, p.name FROM assessments a
JOIN patients p ON a.patient_id = p.id
WHERE p.id = 1
ORDER BY a.assessment_date DESC;
```

### Recent Assessments
```bash
SELECT a.id, p.name, a.risk_score, a.risk_category, a.assessment_date
FROM assessments a
JOIN patients p ON a.patient_id = p.id
ORDER BY a.assessment_date DESC
LIMIT 10;
```

---

## 🔒 Security Best Practices

### Local Development
- Use a unique strong password managed outside the repository
- Don't use 'password' or '123456'
- Store in .env (not in code)

### Production
- Use very strong passwords (20+ chars)
- Enable SSL/TLS for connections
- Restrict IP access to PostgreSQL
- Regular backups enabled
- Connection encryption enabled

### Connection String with SSL
```
postgresql://user:pass@host:5432/db?sslmode=require
```

---

## 🚨 Troubleshooting

### Cannot Connect to PostgreSQL
```bash
# 1. Check if running
# Windows: Services → postgresql (should be running)
# Linux: sudo systemctl status postgresql

# 2. Test connection
psql -h localhost -U cdss_user -d medical_cdss

# 3. Check DATABASE_URL
echo %DATABASE_URL%

# 4. Verify credentials
# Username: cdss_user
# Password: set through the deployment secret manager
# Database: medical_cdss
# Host: localhost
# Port: 5432
```

### Password Authentication Failed
```bash
# Reset password
psql -U postgres

ALTER USER cdss_user WITH PASSWORD '<new-strong-password>';

\q

# Update DATABASE_URL
```

### Database Does Not Exist
```bash
psql -U postgres

CREATE DATABASE medical_cdss;

\q
```

### Tables Not Created
```bash
# Flask should create on first run
python app.py

# Check tables exist
psql -U cdss_user -d medical_cdss

\dt
```

---

## ✅ Verification Checklist

- [ ] PostgreSQL installed
- [ ] PostgreSQL running (verify with `psql -U postgres`)
- [ ] Database `medical_cdss` created
- [ ] User `cdss_user` created with password
- [ ] `psycopg2-binary` in requirements.txt
- [ ] DATABASE_URL set (check with `echo %DATABASE_URL%`)
- [ ] `.env` file created (with DATABASE_URL)
- [ ] App starts without database errors
- [ ] Can create assessments (data saves to PostgreSQL)
- [ ] Can query data in psql

---

## 📚 Resources

### PostgreSQL Documentation
- https://www.postgresql.org/docs/current/

### psycopg2 (Python PostgreSQL Adapter)
- https://www.psycopg.org/

### Cloud Platform PostgreSQL
- **Heroku:** https://devcenter.heroku.com/articles/heroku-postgresql
- **AWS RDS:** https://aws.amazon.com/rds/postgresql/
- **Azure:** https://azure.microsoft.com/en-us/services/postgresql/
- **Google Cloud:** https://cloud.google.com/sql/docs/postgres

### Tools
- **pgAdmin:** https://www.pgadmin.org/ (GUI tool)
- **DBeaver:** https://dbeaver.io/ (Universal tool)

---

## 🎉 PostgreSQL is Configured!

Your system is now using PostgreSQL!

**Compatibility:**
- ✅ Local development
- ✅ Heroku
- ✅ AWS RDS
- ✅ Azure Database
- ✅ Google Cloud SQL
- ✅ Any PostgreSQL server

**Next Steps:**
1. Set up local PostgreSQL (follow above)
2. Run `python app.py`
3. Create assessments
4. Deploy to cloud when ready

---

**PostgreSQL Configuration Version**: 1.0.0
**Status**: Ready to Use ✅
**Tested Platforms**: Local, Heroku, AWS, Azure, GCP
