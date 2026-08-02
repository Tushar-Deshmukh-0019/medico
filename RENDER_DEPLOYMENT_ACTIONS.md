# Render Deployment - Complete Action Guide

## Current Status
✅ Code is ready for production deployment  
✅ Database connection configured correctly  
✅ All dependencies listed in requirements.txt  

## What's Fixed in This Update

1. **Procfile Updated**: Now correctly passes `'production'` config to Flask app factory
2. **connection.py Enhanced**: Clear error messages when DATABASE_URL is missing
3. **app.py Improved**: Auto-detects production environment on Render
4. **.env Updated**: Better documentation and setup instructions

---

## Step-by-Step Render Deployment

### Step 1: Create PostgreSQL Database (5 minutes)

1. Go to [Render Dashboard](https://render.com/dashboard)
2. Click **"New"** button → **"PostgreSQL"**
3. Fill in:
   - **Name**: `medical-cdss-db`
   - **Database**: `medical_cdss`
   - **User**: `postgres`
   - **Region**: Select closest to you
   - **PostgreSQL Version**: 15 (or latest)
   - **Plan**: Free tier is fine
4. Click **"Create Database"**
5. Wait 2-3 minutes for creation to complete
6. **Copy the Internal Database URL** (starts with `postgresql://`)
   - You'll need this for Step 3

### Step 2: Push Code to GitHub

1. Open terminal in project folder
2. Run:
   ```bash
   git add .
   git commit -m "Ready for Render deployment"
   git push -u origin main
   ```

### Step 3: Create Web Service (5 minutes)

1. Go to [Render Dashboard](https://render.com/dashboard)
2. Click **"New"** → **"Web Service"**
3. Click **"Connect a repository"**
   - Search for `medical_cdss` repo
   - Click **"Connect"**
4. Fill in Web Service settings:
   - **Name**: `medical-cdss`
   - **Environment**: `Python 3`
   - **Region**: Same as database
   - **Branch**: `main`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn -w 4 -b 0.0.0.0:$PORT "app:create_app('production')"`
5. Scroll down to **Environment** section
6. Click **"Add Environment Variable"** for each:

   | Key | Value |
   |-----|-------|
   | `DATABASE_URL` | Paste from Step 1 (PostgreSQL Internal URL) |
   | `FLASK_ENV` | `production` |
   | `FLASK_DEBUG` | `False` |
   | `SECRET_KEY` | Generate random: `python -c "import os; print(os.urandom(16).hex())"` |

7. Select **Free Plan** (or Pro if you want)
8. Click **"Create Web Service"**
9. Wait 5-10 minutes for deployment

### Step 4: Verify Deployment

1. After deployment completes, Render shows your URL: `https://medical-cdss.onrender.com`
2. Click the link to test the app
3. Try the assessment to verify database connection
4. Check health endpoint: `https://medical-cdss.onrender.com/api/health`

---

## Expected Deployment Logs

```
⠋ Deploying...
✓ Building image
  Build started...
  Building image from Dockerfile
  ✓ Built successfully
  Pushing image to registry
  ✓ Pushed
✓ Updating service...
  Service deployed successfully
✓ Started
✓ Running
  Starting gunicorn 21.2.0
  ✓ Listening at: http://0.0.0.0:8080
  ✓ Using worker: sync
  ✓ Booting worker with pid
  ✓ Database initialized successfully
  ✓ Using database from environment variable
  ✓ Render deployment detected
```

---

## Troubleshooting

### Error: "DATABASE_URL not set"
**Solution**: 
1. Go to Web Service Settings
2. Check Environment section has DATABASE_URL set
3. Verify value starts with `postgresql://`
4. Click "Save" and "Redeploy"

### Error: "Connection refused" to localhost:5432
**Cause**: App trying to use local PostgreSQL instead of Render's  
**Solution**: Ensure DATABASE_URL is set in Environment variables (see Step 3, Step 6)

### App doesn't start
1. Check Build Logs tab
2. Look for Python errors
3. Verify all imports work: `pip install -r requirements.txt`
4. Check .gitignore doesn't exclude needed files

### Database tables not created
**This is normal** - tables auto-create on first request to `/api/assess`

---

## Post-Deployment

### Monitor Your App
- **Render Dashboard**: Check resource usage and logs
- **Health Check**: `https://medical-cdss.onrender.com/api/health`
- **System Info**: `https://medical-cdss.onrender.com/api/system-info`

### Updating Code
1. Make changes locally
2. Test: `python app.py`
3. Commit: `git add . && git commit -m "message" && git push`
4. Render auto-deploys within 1-2 minutes

### Free Tier Limits
- Web Service: Sleeps after 15 minutes inactivity (30 sec startup)
- Database: 256 MB storage
- Upgrade anytime for persistent service

---

## Important Notes

- **Don't commit .env** to GitHub - it's in .gitignore
- **SECRET_KEY must be random** in production
- **Database auto-creates tables** on first request
- **Connection pooling** is configured for production

---

## Quick Reference Commands

```bash
# Generate SECRET_KEY
python -c "import os; print(os.urandom(16).hex())"

# Test local before deploying
python app.py
# Visit http://localhost:5000

# Push changes
git add .
git commit -m "message"
git push
```

---

**Need help?** Check logs in Render Dashboard → Web Service → Logs tab

**App URL**: `https://medical-cdss.onrender.com`  
**Time to deploy**: 5-10 minutes total
