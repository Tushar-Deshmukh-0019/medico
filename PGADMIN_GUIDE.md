# 🐘 pgAdmin Guide - View Tables and Attributes Locally

Complete guide to view your Medical CDSS database tables and attributes using pgAdmin.

---

## 📥 Step 1: Download and Install pgAdmin

### Option A: Standalone Installation (Recommended)

1. Go to: **https://www.pgadmin.org/download/pgadmin-4-windows/**
2. Download the Windows installer
3. Run the installer and follow prompts:
   - Install location: Default is fine
   - Create shortcut: Yes
   - Launch after install: Yes
4. Set a master password (remember it!)
5. pgAdmin opens in your browser automatically

### Option B: Already Have PostgreSQL?

pgAdmin might already be installed with PostgreSQL:
- Windows Start Menu → Search "pgAdmin"
- Or go to: `C:\Program Files\PostgreSQL\15\bin\pgAdmin4.exe`

### Verify Installation

After installation, pgAdmin opens at:
- **URL:** http://localhost:5050
- **Master Password:** The one you set during install

---

## 🔌 Step 2: Connect to Your PostgreSQL Database

### Method 1: Quick Connection (Automatic)

1. **Open pgAdmin** (already open in browser, or visit http://localhost:5050)
2. **Left sidebar** → Click "Servers"
3. **Right-click "Servers"** → Select "Create" → "Server"
4. **General Tab:**
   - Name: `medical_cdss` (or any name)
5. **Connection Tab:**
   - **Hostname/address:** `localhost`
   - **Port:** `5432`
   - **Maintenance database:** `postgres`
   - **Username:** `postgres`
    - **Password:** your configured PostgreSQL password
   - **Check: Save password?** ✓ Yes
6. **Click "Save"**

### Method 2: Manual Connection

If connection doesn't work automatically:

1. **Click the + icon** next to "Servers" in left sidebar
2. **Fill in connection details:**
   ```
   Host:     localhost
   Port:     5432
   User:     postgres
    Password: your configured PostgreSQL password
   Database: medical_cdss
   ```
3. **Test Connection** button → Should say "connected"
4. **Save**

---

## 📊 Step 3: View Your Database and Tables

### Navigate to Database

1. **Left Sidebar:** Expand `Servers` → `localhost` (or your server name)
2. **Right-click on server** → Click "Refresh" (if needed)
3. **Expand** → `Databases`
4. **Find:** `medical_cdss` database
5. **Click on it** to select

### View All Tables

1. **Expand `medical_cdss`**
2. **Expand** → `Schemas`
3. **Expand** → `public`
4. **Expand** → `Tables`

You should see three tables:
- **patients**
- **assessments**
- **users**

---

## 📋 Step 4: View Table Structure and Attributes

### View Table Columns (Attributes)

For each table, you can view its structure:

1. **Click on a table** (e.g., `patients`)
2. **Right-click** → **Properties**
3. **Columns tab** shows all attributes:
   - Column name
   - Data type
   - Nullable (Yes/No)
   - Default value

### Example: patients Table

**Columns you should see:**
```
id              INTEGER (Primary Key, Auto-increment)
name            VARCHAR(120) (Not null)
age             INTEGER (Nullable)
email           VARCHAR(120) (Nullable)
phone           VARCHAR(20) (Nullable)
created_at      TIMESTAMP
updated_at      TIMESTAMP
```

### Example: assessments Table

**Columns you should see:**
```
id                  INTEGER (Primary Key, Auto-increment)
patient_id          INTEGER (Foreign Key → patients.id)
blood_sugar         FLOAT
bmi                 FLOAT
age                 INTEGER
blood_pressure      FLOAT
risk_score          FLOAT
risk_category       VARCHAR(50)
blood_sugar_status  VARCHAR(50)
bmi_category        VARCHAR(50)
bp_category         VARCHAR(50)
recommendations     TEXT
created_at          TIMESTAMP
updated_at          TIMESTAMP
```

### Example: users Table

**Columns you should see:**
```
id              INTEGER (Primary Key, Auto-increment)
username        VARCHAR(120) (Unique)
email           VARCHAR(120) (Unique)
password_hash   VARCHAR(255)
created_at      TIMESTAMP
updated_at      TIMESTAMP
```

---

## 🔍 Step 5: View Table Data

### View Data in a Table

1. **Right-click on a table** (e.g., `assessments`)
2. **Select** → **View/Edit Data** → **All Rows**
3. A new tab opens showing all data in that table

### Columns Visible:
- All attributes/columns
- All rows/records
- Sortable
- Filterable
- Editable

### Example Output

For `assessments` table, you'll see:
```
| id | patient_id | blood_sugar | bmi | age | risk_score | risk_category | created_at |
|----|------------|-------------|-----|-----|------------|---------------|-----------|
| 1  | 1          | 150         | 28  | 45  | 72.5       | High          | 2024-08-02|
| 2  | 2          | 95          | 23  | 30  | 18.3       | Low           | 2024-08-02|
```

---

## 🔗 Step 6: View Table Relationships

### See Foreign Keys

1. **Right-click on `assessments` table**
2. **Properties** → **Foreign Keys tab**
3. You should see:
   ```
   patient_id → references patients(id)
   ```

### View Related Data

1. **In Data view:** Click on `patient_id` value
2. **You can see:** Which patient this assessment belongs to

---

## 🎯 Step-by-Step Example: Check Your Data

### Complete Walkthrough

1. **Open pgAdmin**
   - Browser: http://localhost:5050

2. **Login if needed**
   - Master password you created

3. **Navigate to data**
   - Servers → localhost → Databases → medical_cdss → Schemas → public → Tables

4. **View patients table**
   - Right-click `patients` → Properties
   - See all columns (id, name, age, email, phone, created_at, updated_at)

5. **View patient data**
   - Right-click `patients` → View/Edit Data → All Rows
   - See all patient records

6. **View assessments table**
   - Right-click `assessments` → Properties
   - See all columns (blood_sugar, bmi, age, bp, risk_score, etc.)

7. **View assessment data**
   - Right-click `assessments` → View/Edit Data → All Rows
   - See all assessment results with risk scores

8. **Check relationships**
   - Click on a patient_id in assessments
   - See which patient it belongs to

Done! 🎉

---

## 📝 Quick Reference: Table Attributes

### patients Table (7 columns)
| Column | Type | Purpose |
|--------|------|---------|
| id | INTEGER (PK) | Patient ID |
| name | VARCHAR(120) | Patient name |
| age | INTEGER | Patient age |
| email | VARCHAR(120) | Contact email |
| phone | VARCHAR(20) | Contact phone |
| created_at | TIMESTAMP | Record created date |
| updated_at | TIMESTAMP | Last updated date |

### assessments Table (13 columns)
| Column | Type | Purpose |
|--------|------|---------|
| id | INTEGER (PK) | Assessment ID |
| patient_id | INTEGER (FK) | Reference to patient |
| blood_sugar | FLOAT | Blood sugar mg/dL |
| bmi | FLOAT | BMI kg/m² |
| age | INTEGER | Age in years |
| blood_pressure | FLOAT | BP mmHg |
| risk_score | FLOAT | Diabetes risk 0-100% |
| risk_category | VARCHAR(50) | Low/Medium/High |
| blood_sugar_status | VARCHAR(50) | Normal/High/etc |
| bmi_category | VARCHAR(50) | Normal/Obese/etc |
| bp_category | VARCHAR(50) | Normal/High/etc |
| recommendations | TEXT | Health recommendations |
| created_at | TIMESTAMP | Created date |

### users Table (5 columns)
| Column | Type | Purpose |
|--------|------|---------|
| id | INTEGER (PK) | User ID |
| username | VARCHAR(120) | Login username |
| email | VARCHAR(120) | User email |
| password_hash | VARCHAR(255) | Hashed password |
| created_at | TIMESTAMP | Account created date |

---

## 🛠️ Useful pgAdmin Features

### Run SQL Queries

1. **Top menu** → **Tools** → **Query Tool**
2. **Write SQL** in the editor:
   ```sql
   SELECT * FROM assessments;
   SELECT COUNT(*) FROM patients;
   SELECT AVG(risk_score) FROM assessments;
   ```
3. **Press:** F5 or click **Execute** button
4. **See results** below

### Export Data

1. **Right-click table** → **Backup**
2. **Or:** View/Edit Data → Export to CSV

### Create Database Backup

1. **Right-click on database** → **Backup**
2. **Choose format:** Custom (recommended)
3. **Save backup file**

### Restore from Backup

1. **Right-click database** → **Restore**
2. **Select your backup file**
3. **Click Restore**

---

## 🔍 Verify Your Connection Works

### Test Query

1. **Open pgAdmin**
2. **Top menu** → **Tools** → **Query Tool**
3. **Paste this query:**
   ```sql
   SELECT table_name 
   FROM information_schema.tables 
   WHERE table_schema = 'public';
   ```
4. **Click Execute (F5)**
5. **You should see:**
   ```
   assessments
   patients
   users
   ```

If you see these tables, everything is working! ✅

---

## 🔐 Login Credentials for pgAdmin

When pgAdmin opens:
- **Username:** (usually your email or admin)
- **Password:** The master password you set during installation

If you forgot the master password:
- Reinstall pgAdmin
- Or use command line: `pgadmin4 --admin-user admin@example.com`

---

## ❌ Troubleshooting

### Problem: Can't Connect to PostgreSQL

**Solution:**
1. Check if PostgreSQL is running
2. Windows Services → postgresql-x64-15 → Start
3. Verify the credentials configured for your environment
4. Try different hostname: localhost or 127.0.0.1

### Problem: Database Not Showing

**Solution:**
1. Create the database first:
   ```cmd
   psql -U postgres -h localhost
   CREATE DATABASE medical_cdss;
   \q
   ```
2. Refresh pgAdmin: F5
3. Right-click server → Refresh

### Problem: Can't See Tables

**Solution:**
1. Run your Flask app: `python app.py`
2. This creates tables automatically
3. Refresh pgAdmin
4. Expand Tables again

### Problem: Port Already in Use

**Solution:**
- pgAdmin default: 5050
- PostgreSQL default: 5432
- Check if services are running
- Use different port: Edit pgAdmin config

---

## 🌐 Useful pgAdmin URLs

- **Main Dashboard:** http://localhost:5050
- **Query Tool:** http://localhost:5050/?action=open&cmd=query
- **Object Properties:** Right-click → Properties
- **Data Viewer:** Right-click → View/Edit Data

---

## 📊 Monitor Database in Real-Time

### Activity Monitoring

1. **Right-click server** → **Dashboard**
2. **See:**
   - Connected clients
   - Active queries
   - Database size
   - Transaction info

### Query Performance

1. **Tools** → **Query Tool**
2. **Write query**
3. **Explain button** shows execution plan

---

## ✨ Tips and Tricks

### Keyboard Shortcuts in Query Tool
- **F5** - Execute query
- **Ctrl+A** - Select all
- **Ctrl+E** - Execute selected
- **Ctrl+S** - Save query

### Quick Navigation
- **Ctrl+Shift+O** - Object browser
- **F4** - Editor panel
- **F5** - Execute

### Auto-refresh Data
- Right-click table → Properties
- General tab → Check "Auto-refresh"
- Interval in seconds

---

## 🎓 Next Steps

Once you've verified your tables:

1. **Run the Flask app:**
   ```cmd
   cd c:\medical_cdss
   python app.py
   ```

2. **Create some assessments:**
   - Visit http://localhost:5000/assessment
   - Fill form and submit
   - Check database in pgAdmin

3. **Watch data populate:**
   - Refresh pgAdmin
   - See new rows in assessments and patients tables

4. **Run SQL queries:**
   - Check average risk scores
   - Find high-risk patients
   - View assessment history

---

## 📚 Additional Resources

- **pgAdmin Official:** https://www.pgadmin.org/
- **PostgreSQL Docs:** https://www.postgresql.org/docs/
- **SQL Tutorial:** https://www.w3schools.com/sql/

---

## ✅ Verification Checklist

After following this guide, you should have:

- [ ] pgAdmin installed and running
- [ ] Connected to PostgreSQL successfully
- [ ] Viewed `medical_cdss` database
- [ ] Seen 3 tables: patients, assessments, users
- [ ] Viewed table structure (columns/attributes)
- [ ] Viewed table data (rows)
- [ ] Understood relationships (patient_id → patients)
- [ ] Can run SQL queries
- [ ] Can export/backup data

All checked? You're ready to use pgAdmin! 🎉

---

**Happy database exploring! 🐘🗄️**
