# 🐘 PostgreSQL Setup - Required Before Running App

Your app is configured to use PostgreSQL, but the database doesn't exist yet. Follow these steps:

---

## 🔧 Create PostgreSQL Database

### Step 1: Open PostgreSQL Command Line

```cmd
psql -U postgres -h localhost
```

When prompted, enter your PostgreSQL superuser password.

### Step 2: Create the Database

Copy and paste this command in psql:

```sql
CREATE DATABASE medical_cdss;
```

### Step 3: Verify Creation

```sql
\l
```

You should see `medical_cdss` in the list.

### Step 4: Exit

```sql
\q
```

---

## ✅ Your Configuration

**Your actual credentials are already set:**

```
Host:       localhost
Port:       5432
Database:   medical_cdss
Username:   postgres
Password:   <your-password>
```

**Connection String:**
```
postgresql://postgres:<your-password>@localhost:5432/medical_cdss
```

This is set in:
- `database/connection.py` (default)
- `.env` file
- All setup scripts

---

## 🚀 Run the App

Once you've created the database, run:

```cmd
cd c:\medical_cdss
python app.py
```

Flask will automatically:
1. Connect to PostgreSQL
2. Create all tables
3. Start the web server

Then visit: **http://localhost:5000**

---

## 📝 Quick Command Summary

```cmd
# 1. Create database
psql -U postgres -h localhost
CREATE DATABASE medical_cdss;
\q

# 2. Run app
cd c:\medical_cdss
python app.py

# 3. Access
http://localhost:5000
```

---

## ✨ That's All!

Your database is ready, and the app is configured to use it!
