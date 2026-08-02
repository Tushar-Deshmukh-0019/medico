# 🚀 Render.com Deployment Guide - Medical CDSS

**Deploy your Medical CDSS to Render.com in 10 minutes!**

Render is the easiest way to deploy Flask apps with PostgreSQL.

---

## ✨ Why Render?

- ✅ **Easiest setup** - 10 minutes
- ✅ **Free trial** - 15 days included
- ✅ **GitHub integration** - Auto-deploy
- ✅ **PostgreSQL included** - No extra setup
- ✅ **One-click deploy** - No command line
- ✅ **Production ready** - Not just for testing
- ✅ **Cheap** - $7/month hobby tier

---

## 💰 Pricing

| Plan | Price | Free Trial | Best For |
|------|-------|-----------|----------|
| Free | $0 | 15 days | Testing |
| Hobby | $7/mo | Included | Production |
| Standard | $25/mo | Included | High traffic |

---

## 📋 STEP-BY-STEP DEPLOYMENT

### Step 1: Create Render Account (2 minutes)

1. **Go to:** https://render.com
2. **Click** "Get Started"
3. **Sign up with:**
   - GitHub (recommended for auto-deploy)
   - Or email/password
4. **Verify email**
5. Done! ✓

### Step 2: Push Code to GitHub (5 minutes)

**Option A: If code is already on GitHub**
- Skip to Step 3

**Option B: Upload to GitHub**

1. Go to: https://github.com
2. Create new repository: `medical_cdss`
3. Upload all files from `c:\medical_cdss\`
4. Include:
   - app.py
   - requirements.txt
   - config.py
   - database/ folder
   - fuzzy/ folder
   - templates/ folder
   - static/ folder
   - .gitignore
   - Procfile (already in your project)
5. Commit and push

**Don't upload:**
- .env (keep it local)
- medical_cdss.db (local database)
- __pycache__ folders

### Step 3: Create Web Service on Render (3 minutes)

1. **Login to Render:** https://dashboard.render.com
2. **Click** "New +"
3. **Select** "Web Service"
4. **Connect GitHub:**
   - Click "Connect GitHub account"
   - Authorize Render
   - Select repository: `medical_cdss`
   - Click "Connect"

### Step 4: Configure Deployment (2 minutes)

In the service settings, fill in:

**Basic Settings:**
- **Name:** `medical-cdss` (lowercase, hyphens)
- **Environment:** `Python 3`
- **Region:** `Oregon` (or closest to you)
- **Branch:** `main`

**Build Settings:**
- **Build Command:**
  ```
  pip install -r requirements.txt
  ```

- **Start Command:**
  ```
  gunicorn app:app
  ```

### Step 5: Add Database (2 minutes)

1. **In Render Dashboard**
2. **Click** "New +"
3. **Select** "PostgreSQL"
4. **Fill in:**
   - **Name:** `medical-cdss-db`
   - **Database:** `medical_cdss`
   - **User:** `postgres`
   - **Password:** Generate (copy it!)
   - **Region:** Same as web service
5. **Click** "Create Database"
6. **Copy the connection string** (looks like):
   ```
   postgresql://user:password@hostname:port/database
   ```

### Step 6: Connect Database to Web Service (2 minutes)

1. **Go back to Web Service settings**
2. **Scroll to** "Environment"
3. **Click** "Add Environment Variable"
4. **Add variable:**
   - **Key:** `DATABASE_URL`
   - **Value:** Paste the PostgreSQL connection string from Step 5
5. **Add another variable:**
   - **Key:** `FLASK_ENV`
   - **Value:** `production`
6. **Click** "Save"

### Step 7: Deploy! (5-10 minutes)

1. **Click** "Deploy"
2. **Watch the deploy progress** (real-time logs)
3. **Wait for "Deploy successful"** message
4. **You'll get a URL** like:
   ```
   https://medical-cdss.onrender.com
   ```

**That's it! Your app is live!** 🎉

---

## ✅ Verify Deployment

### Check if it's working:

1. **Visit your URL:**
   ```
   https://medical-cdss.onrender.com
   ```
   You should see the Medical CDSS home page

2. **Test the assessment form:**
   ```
   https://medical-cdss.onrender.com/assessment
   ```
   Fill in data and submit

3. **Check API:**
   ```
   https://medical-cdss.onrender.com/api/health
   ```
   Should return JSON response

4. **View history:**
   ```
   https://medical-cdss.onrender.com/history
   ```
   Should show your assessments

---

## 🔄 Auto-Deploy from GitHub

Render automatically redeploys when you push to GitHub!

**Workflow:**
1. Make changes locally
2. Test on http://localhost:5000
3. Push to GitHub: `git push origin main`
4. Render automatically deploys
5. Your live app updates in 2-3 minutes

---

## 🐘 Managing Your Database

### View Database in pgAdmin

1. **Connection settings:**
   - Host: From Render PostgreSQL URL
   - Port: 5432
   - Database: medical_cdss
   - User: postgres
   - Password: Your generated password

2. **Connect in pgAdmin:**
   - New Server → Fill details → Save
   - View your live data!

### Backup Your Database

In Render dashboard:
1. Click your PostgreSQL instance
2. Go to "Backups" tab
3. Click "Create Backup"
4. Download when ready

---

## 📊 Monitor Your App

### View Logs

1. **Render Dashboard**
2. **Click your Web Service**
3. **"Logs" tab** shows real-time logs
4. See errors, requests, database activity

### Performance Metrics

1. **Render Dashboard**
2. **"Metrics" tab** shows:
   - CPU usage
   - Memory usage
   - Requests per minute
   - Response times

---

## 🆘 Common Issues & Solutions

### Issue: "App crashes after deploy"

**Solution:**
1. Check logs in Render dashboard
2. Common causes:
   - Missing requirements in requirements.txt
   - DATABASE_URL not set
   - Import errors
3. Fix locally, push to GitHub, Render redeploys

### Issue: "Database connection error"

**Solution:**
1. Verify DATABASE_URL is correct
2. Copy exact string from PostgreSQL service
3. Check password doesn't have special characters
4. Restart web service

### Issue: "Static files not loading"

**Solution:**
1. In Flask, static files should be in `/static`
2. Make sure `.gitignore` doesn't exclude static/
3. Rebuild: manually restart service

### Issue: "App takes long to start"

**Solution:**
- First 15 seconds is normal
- If longer, check requirements.txt for large packages
- Consider using smaller dependencies

---

## 🔐 Security Checklist

Before deploying:

- [ ] Remove .env from repository
- [ ] Set FLASK_ENV=production
- [ ] Don't commit database files
- [ ] Use strong database password
- [ ] Keep API keys out of code
- [ ] Use environment variables
- [ ] Test locally first

---

## 📱 Share Your App

### Get your live URL

```
https://medical-cdss.onrender.com
```

### Share features:

- **Home:** `/`
- **Assessment:** `/assessment`
- **History:** `/history`
- **About:** `/about`
- **API:** `/api/health`

### Full URLs to share:

```
Live App: https://medical-cdss.onrender.com
Assessment Form: https://medical-cdss.onrender.com/assessment
API Health: https://medical-cdss.onrender.com/api/health
```

---

## 🔄 Update Your App

**To make changes:**

1. Edit files locally
2. Test on http://localhost:5000
3. Commit changes: `git add .` → `git commit -m "message"`
4. Push to GitHub: `git push origin main`
5. Render automatically deploys!

---

## 💰 Managing Costs

### Free Trial (15 days)
- Costs $0
- After 15 days, Hobby plan starts ($7/mo)

### To avoid charges:
1. Delete app before trial ends (if testing only)
2. Or upgrade to Hobby ($7/month)
3. Hobby is good for 10,000+ daily requests

### Delete App (if needed)
1. Render Dashboard
2. Click Web Service
3. Settings → "Delete Service"
4. Confirm deletion

---

## 📚 Useful Render Features

### Custom Domain
1. Go to Service Settings
2. Add custom domain
3. Point DNS records to Render
4. Your own domain!

### Environment Variables
1. Settings → Environment
2. Add multiple variables
3. All available in Flask app
4. Change without redeploying

### Pull Request Previews
1. Connected to GitHub
2. Every PR gets preview URL
3. Test before merging
4. Delete when done

### Cron Jobs
1. Create scheduled tasks
2. Run database cleanup
3. Send reports
4. Automated maintenance

---

## 🎓 Next Steps After Deploy

1. ✅ Deployed on Render
2. 📊 Share live URL
3. 🗄️ Manage database
4. 📈 Monitor performance
5. 🔄 Make updates via GitHub
6. 💰 Upgrade plan if needed

---

## 📞 Render Support

- **Docs:** https://render.com/docs
- **Status:** https://status.render.com
- **Support:** help@render.com

---

## ✨ You're Done!

Your Medical CDSS is now live on the internet!

**Your live URL:**
```
https://medical-cdss.onrender.com
```

**Share it with:**
- Colleagues
- Friends
- Medical professionals
- Demo to stakeholders

**Anyone can visit and use your app!** 🎉

---

## 📋 Quick Checklist

- [ ] Created Render account
- [ ] Pushed code to GitHub
- [ ] Created Web Service
- [ ] Created PostgreSQL database
- [ ] Set DATABASE_URL environment variable
- [ ] Set FLASK_ENV=production
- [ ] Deployed app
- [ ] Verified app is running
- [ ] Tested assessment form
- [ ] Shared URL with others

**All done? Your app is live!** ✅

