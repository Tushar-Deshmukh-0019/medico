# 🚀 PythonAnywhere Deployment Guide - Medical CDSS

**Deploy your Medical CDSS to PythonAnywhere for FREE (forever!)** 

No credit card needed. Always free tier available.

---

## ✨ Why PythonAnywhere?

- ✅ **Always FREE** - No expiration
- ✅ **Python-optimized** - Built for Python apps
- ✅ **Easy setup** - 15 minutes
- ✅ **PostgreSQL support** - Full database
- ✅ **Web-based IDE** - Edit code online
- ✅ **No credit card** - Free plan is real
- ✅ **Beginner-friendly** - Great docs

---

## 💰 Pricing

| Plan | Price | Best For |
|------|-------|----------|
| Free | $0 | Prototyping, testing |
| Hacker | $5/mo | Small production |
| Hacker+ | $7/mo | More resources |

Free plan includes:
- 1 web app
- 100MB database
- 512MB RAM
- 512MB storage

---

## 📋 STEP-BY-STEP DEPLOYMENT

### Step 1: Create PythonAnywhere Account (2 minutes)

1. **Go to:** https://www.pythonanywhere.com
2. **Click** "Create a free account"
3. **Choose username** (will be in your URL)
4. **Enter email**
5. **Set password**
6. **Click** "Register"
7. **Verify email** (check inbox)
8. **Login**

Done! You're in. ✓

### Step 2: Upload Your Code (5 minutes)

**Option A: Using Web Files Interface (Easiest)**

1. **Go to "Files" tab**
2. **Create folder:** Click "New Folder"
   - Name: `medical_cdss`
3. **Click folder to open it**
4. **Upload files:**
   - Click "Upload a file"
   - Upload each folder:
     - app.py
     - config.py
     - requirements.txt
     - fuzzy/ (upload as folder)
     - database/ (upload as folder)
     - templates/ (upload as folder)
     - static/ (upload as folder)

**Option B: Using Git (Advanced)**

1. Go to Web/Bash console
2. Clone your GitHub repo:
   ```bash
   git clone https://github.com/yourusername/medical_cdss.git
   ```
3. All files downloaded

### Step 3: Create PostgreSQL Database (3 minutes)

1. **Go to "Databases" tab**
2. **Click** "Start a new database"
3. **Choose "PostgreSQL"**
4. **Set details:**
   - Database name: `medical_cdss_db`
   - Initial username: `postgres`
   - Password: Create a strong one (write it down!)
5. **Click** "Create database"
6. **Copy connection details:**
   ```
   Database: medical_cdss_db
   Username: postgres
   Password: [your password]
   Host: [your-pythonanywhere-username].postgres.pythonanywhere.com
   Port: 5432
   ```

### Step 4: Create Web App (3 minutes)

1. **Go to "Web" tab**
2. **Click** "Add a new web app"
3. **Select:**
   - Next (choose username - it's your domain)
   - Python 3.10
   - Flask
   - Next → Next
4. **Your web app is created!**
5. **You get URL:** `https://yourusername.pythonanywhere.com`

### Step 5: Configure WSGI File (2 minutes)

1. **Still in Web tab**
2. **Find "WSGI configuration file"**
3. **Click** the file path (looks like: `/var/www/yourusername_pythonanywhere_com_wsgi.py`)
4. **Replace content with:**

```python
# WSGI configuration file at /var/www/yourusername_pythonanywhere_com_wsgi.py
import sys
import os

# Add your project directory to sys.path
path = '/home/yourusername/medical_cdss'
if path not in sys.path:
    sys.path.append(path)

# Set environment variables
os.environ['DATABASE_URL'] = 'postgresql://postgres:yourpassword@yourusername.postgres.pythonanywhere.com:5432/medical_cdss_db'
os.environ['FLASK_ENV'] = 'production'

# Import Flask app
from app import app as application
```

**Replace:**
- `yourusername` with your PythonAnywhere username
- `yourpassword` with your database password
- Database connection string with your actual string

### Step 6: Install Requirements (2 minutes)

1. **Go to "Consoles" tab**
2. **Start "Bash console"**
3. **Run:**
   ```bash
   cd /home/yourusername/medical_cdss
   pip install -r requirements.txt
   ```
4. **Wait for installation** (1-2 minutes)
5. **Check for errors**

### Step 7: Reload Web App (1 minute)

1. **Go back to "Web" tab**
2. **Click** "Reload" button
3. **Wait 30 seconds**
4. **Your app is live!** 🎉

---

## ✅ Verify Deployment

### Check if it's working:

1. **Visit your URL:**
   ```
   https://yourusername.pythonanywhere.com
   ```
   You should see the Medical CDSS home page

2. **Test the form:**
   ```
   https://yourusername.pythonanywhere.com/assessment
   ```
   Submit an assessment

3. **Check API:**
   ```
   https://yourusername.pythonanywhere.com/api/health
   ```
   Should return JSON

4. **View in database:**
   - Go to "Databases" tab
   - Your data is stored!

---

## 🔄 Updating Your App

### To make changes:

1. **Edit files locally**
2. **Test on http://localhost:5000**
3. **Upload to PythonAnywhere:**
   - Files tab → upload new version
   - Or use Git to pull changes
4. **Reload web app:**
   - Web tab → "Reload" button
5. **Changes live immediately!**

---

## 🐘 Managing Your Database

### View Data in pgAdmin

1. **Connection settings:**
   ```
   Host: yourusername.postgres.pythonanywhere.com
   Port: 5432
   Database: medical_cdss_db
   User: postgres
   Password: your_password
   ```

2. **Connect in pgAdmin:**
   - New Server → Enter details
   - View your live data!

### Backup Your Database

In PythonAnywhere:
1. Go to "Databases" tab
2. Click database name
3. Download backup

---

## 📊 Monitor Performance

### View Error Logs

1. **Web tab**
2. **Scroll down to "Log files"**
3. **Click** to view:
   - Server error log
   - Access log
   - Browser error log

### Check CPU/Memory

1. **Web tab**
2. **See "Web app summary"**
3. Shows current resource usage

---

## 🆘 Common Issues & Solutions

### Issue: "ModuleNotFoundError: No module named 'flask'"

**Solution:**
1. Install requirements in Bash console:
   ```bash
   pip install -r requirements.txt
   ```
2. Reload web app

### Issue: "Database connection error"

**Solution:**
1. Check WSGI file has correct connection string
2. Verify password is correct
3. Verify database exists in Databases tab
4. Reload web app

### Issue: "Static files not loading"

**Solution:**
1. Make sure static/ folder is uploaded
2. In Web tab, add static file mapping:
   - URL: `/static/`
   - Directory: `/home/yourusername/medical_cdss/static`

### Issue: "502 Bad Gateway error"

**Solution:**
1. Check logs (Web tab → Log files)
2. Look for error messages
3. Usually configuration issue
4. Common: missing DATABASE_URL
5. Fix WSGI file, reload

---

## 📝 WSGI File Quick Reference

Your WSGI file needs:
```python
import sys
import os
sys.path.append('/home/yourusername/medical_cdss')
os.environ['DATABASE_URL'] = 'your_database_url'
from app import app as application
```

Key parts:
- `sys.path` - tells where your code is
- `os.environ` - sets environment variables
- `from app import app as application` - imports your Flask app

---

## 🔐 Security Checklist

- [ ] Database password is strong
- [ ] Never commit .env file
- [ ] Don't share your WSGI file
- [ ] Use DATABASE_URL environment variable
- [ ] Set FLASK_ENV=production

---

## 💡 Tips & Tricks

### Custom Domain
1. Go to "Account" → "Web address"
2. Buy custom domain or add existing
3. Configure DNS records
4. Your own domain!

### Email Notifications
1. Web tab → "Email when an error is logged"
2. Get alerts when app crashes
3. Fix problems faster

### Schedule Tasks
1. "Scheduled tasks" tab
2. Run maintenance tasks
3. Cleanup old data
4. Send reports

### Switch to Paid
1. When free plan gets tight
2. Upgrade to Hacker ($5/mo)
3. More CPU, RAM, storage
4. Can scale up anytime

---

## 🎓 Next Steps

1. ✅ Deployed on PythonAnywhere
2. 📊 Share your URL
3. 🗄️ Monitor database
4. 🔄 Update when needed
5. 💰 Upgrade if needed

---

## 📞 PythonAnywhere Support

- **Docs:** https://help.pythonanywhere.com/
- **Forum:** https://www.pythonanywhere.com/forums/
- **Email:** support@pythonanywhere.com

---

## ✨ You're Done!

Your Medical CDSS is live on PythonAnywhere!

**Your live URL:**
```
https://yourusername.pythonanywhere.com
```

**Forever free!** No credit card ever needed. No expiration date.

**Share it with anyone!** 🎉

---

## 📋 Quick Checklist

- [ ] Created PythonAnywhere account
- [ ] Uploaded all code files
- [ ] Created PostgreSQL database
- [ ] Configured WSGI file with DATABASE_URL
- [ ] Installed requirements (pip install -r requirements.txt)
- [ ] Reloaded web app
- [ ] Verified app is running
- [ ] Tested assessment form
- [ ] Shared URL

**All done? Your app is live and free!** ✅

