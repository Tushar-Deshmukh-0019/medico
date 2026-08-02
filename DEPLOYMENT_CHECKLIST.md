# 📋 Render Deployment Checklist

**Objective**: Deploy Medical CDSS to Render in 15 minutes  
**Your app will be live at**: `https://medical-cdss.onrender.com`

---

## ✅ Pre-Deployment (Do Locally First)

- [ ] **Verify code compiles**
  ```bash
  python -m py_compile app.py
  python -m py_compile database/connection.py
  python -m py_compile config.py
  ```

- [ ] **Verify all imports work**
  ```bash
  python -c "from config import config; from database.connection import db; from fuzzy import FuzzyEngine; print('✓ All imports OK')"
  ```

- [ ] **Git - Push to GitHub**
  ```bash
  git add .
  git commit -m "Ready for Render deployment"
  git push origin main
  ```

---

## ✅ Render - Create Database (5 minutes)

- [ ] **Go to Render Dashboard**: https://render.com/dashboard

- [ ] **Create PostgreSQL Service**
  - [ ] Click "New" → "PostgreSQL"
  - [ ] Name: `medical-cdss-db`
  - [ ] Database: `medical_cdss`
  - [ ] User: `postgres`
  - [ ] Region: [Select closest to you]
  - [ ] PostgreSQL Version: 15 (or latest)
  - [ ] Plan: **Free tier**
  - [ ] Click "Create Database"

- [ ] **Wait for creation** (2-3 minutes)
  - [ ] Status changes to "Available"

- [ ] **Copy Internal Database URL**
  - [ ] Click on database service
  - [ ] Copy "Internal Database URL" (starts with `postgresql://`)
  - [ ] **Save this value** - you need it in next steps!

---

## ✅ Render - Create Web Service (5 minutes)

- [ ] **Go to Render Dashboard**: https://render.com/dashboard

- [ ] **Create Web Service**
  - [ ] Click "New" → "Web Service"
  - [ ] Click "Connect a repository"
  - [ ] Search for `medical_cdss`
  - [ ] Click "Connect"

- [ ] **Configure Web Service**
  - [ ] Name: `medical-cdss`
  - [ ] Environment: `Python 3`
  - [ ] Region: **Same as database** (important!)
  - [ ] Branch: `main`
  - [ ] Build Command: `pip install -r requirements.txt`
  - [ ] Start Command: `gunicorn -w 4 -b 0.0.0.0:$PORT "app:create_app('production')"`

- [ ] **Add Environment Variables** (MOST IMPORTANT!)
  - [ ] Click "Add Environment Variable"
  - [ ] **Add DATABASE_URL**
    - Key: `DATABASE_URL`
    - Value: [Paste from Step above - PostgreSQL Internal URL]
  - [ ] **Add FLASK_ENV**
    - Key: `FLASK_ENV`
    - Value: `production`
  - [ ] **Add FLASK_DEBUG**
    - Key: `FLASK_DEBUG`
    - Value: `False`
  - [ ] **Add SECRET_KEY**
    - Key: `SECRET_KEY`
    - Value: Generate random string (see below)

- [ ] **Generate SECRET_KEY** (copy one):
  ```bash
  python -c "import os; print(os.urandom(16).hex())"
  ```
  Or use: `a3f7e2d9c5b1f4a6` (example - generate your own!)

- [ ] **Select Plan**
  - [ ] Free tier (Recommended)
  - Or Pro if you prefer

- [ ] **Click "Create Web Service"**

---

## ✅ Render - Verify Deployment (5 minutes)

- [ ] **Wait for deployment** (~5-10 minutes)
  - [ ] Watch logs in "Deploy" tab
  - [ ] Look for: "Service deployed successfully"
  - [ ] Status changes to "Live"

- [ ] **Expected log messages** (should see these):
  ```
  ✓ Building image
  ✓ Built successfully
  ✓ Pushing image
  ✓ Listening at: http://0.0.0.0:8080
  ✓ Database initialized successfully
  ✓ Render deployment detected
  ```

- [ ] **Test your app** (once deployment completes)
  - [ ] Go to: `https://medical-cdss.onrender.com`
  - [ ] Should see home page
  - [ ] Try filling an assessment form
  - [ ] Submit and verify result appears

- [ ] **Test health endpoint**
  - [ ] Visit: `https://medical-cdss.onrender.com/api/health`
  - [ ] Should return JSON with status

- [ ] **Test system info endpoint**
  - [ ] Visit: `https://medical-cdss.onrender.com/api/system-info`
  - [ ] Should return fuzzy engine details

---

## 🔧 If Something Goes Wrong

### Error: "DATABASE_URL not set"

**Action**:
1. Go to Web Service Settings (click service name)
2. Click "Settings" tab
3. Scroll to "Environment" section
4. Check DATABASE_URL is there
5. Value should start with `postgresql://`
6. If missing: Click "Add" and add it
7. Click "Save"
8. Click "Redeploy" button
9. Wait 5 minutes

### Error: "Connection refused" to localhost

**Cause**: Using local connection string instead of Render's  
**Action**: Follow "DATABASE_URL not set" fix above

### App doesn't load / spinning wheel

**Action**:
1. Go to "Logs" tab
2. Scroll to bottom
3. Look for error messages
4. Common fixes:
   - Missing DATABASE_URL (see above)
   - Syntax error in code
   - Missing package in requirements.txt

### Deployment keeps failing

**Check Build Logs**:
1. Click "Logs" tab
2. Look for Python errors
3. Run locally: `python -m py_compile app.py`
4. Check requirements.txt: `pip install -r requirements.txt`

---

## ✅ Post-Deployment

- [ ] **Share your app**
  - [ ] URL: `https://medical-cdss.onrender.com`
  - [ ] Works on phones and browsers

- [ ] **Monitor in Render Dashboard**
  - [ ] CPU usage should be low when idle
  - [ ] Memory stable
  - [ ] Logs show normal operation

- [ ] **Update code in future**
  - [ ] Make changes locally
  - [ ] Test: `python app.py` → `http://localhost:5000`
  - [ ] Push: `git add . && git commit -m "..." && git push`
  - [ ] Render auto-deploys in 1-2 minutes

- [ ] **Upgrade if needed**
  - [ ] Free tier sleeps after 15 min inactivity
  - [ ] Pro plan keeps running ($7/month)
  - [ ] Easy upgrade anytime

---

## 📚 Quick Reference

| What | Where |
|------|-------|
| **Full Guide** | `RENDER_DEPLOYMENT_ACTIONS.md` |
| **API Docs** | `COMPLETE_GUIDE.md` → API section |
| **Troubleshooting** | `RENDER_DEPLOYMENT_GUIDE.md` |
| **Code Status** | `DEPLOYMENT_STATUS_READY.md` |

---

## ⏱️ Timeline

| Step | Time | Status |
|------|------|--------|
| 1. Push to GitHub | 1 min | ⏳ Do first |
| 2. Create Database | 5 min | ⏳ While DB creates... |
| 3. Create Web Service | 5 min | ✓ Do next |
| 4. Deploy | 5-10 min | ✓ Auto |
| 5. Verify | 2 min | ✓ Final check |
| **TOTAL** | **15-20 min** | **✓ Done!** |

---

## 🎯 Success Looks Like

✅ Render shows "Live" status  
✅ https://medical-cdss.onrender.com loads  
✅ Health check returns status  
✅ Assessment form works  
✅ Results display correctly  
✅ Data saved in database  

---

## 💡 Tips

- **Free tier is enough** to start - upgrade later if needed
- **Database stays** even if web service resets
- **Auto-deploy** on git push to main
- **Logs always available** in Render dashboard
- **Instant redeploy** if needed

---

**Need help?** Check the full guide: `RENDER_DEPLOYMENT_ACTIONS.md`

**Ready? Let's go! 🚀**
