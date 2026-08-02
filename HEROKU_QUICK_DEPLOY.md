# 🚀 Heroku Quick Deploy (5 Minutes)

Deploy your Medical Decision Support System to Heroku in 5 minutes!

## ✅ Prerequisites

1. **Heroku Account** (Free)
   - Go to: https://www.heroku.com
   - Sign up
   - Verify email

2. **Heroku CLI**
   - Download from: https://devcenter.heroku.com/articles/heroku-cli
   - Or: `npm install -g heroku`

3. **Git**
   - Download from: https://git-scm.com
   - Or: `choco install git`

4. **Internet Connection**
   - Needed for deployment

---

## 🎯 5-Minute Deployment

### Step 1: Open Command Prompt (30 seconds)
```bash
cd c:\medical_cdss
```

### Step 2: Initialize Git (30 seconds)
```bash
git init
git add .
git commit -m "Initial commit - Medical CDSS"
```

### Step 3: Login to Heroku (1 minute)
```bash
heroku login
# Browser opens
# Login with your credentials
# Approve
# Return to terminal
```

### Step 4: Create Heroku App (1 minute)
```bash
heroku create your-unique-app-name

# Example: heroku create medical-cdss-myname
# Heroku checks name availability
```

### Step 5: Deploy (1 minute)
```bash
git push heroku main
# Deployment starts
# Watch the logs
# Wait for completion
```

### Step 6: Open Your App (30 seconds)
```bash
heroku open
# Your app opens in browser!
# OR manually go to:
# https://your-unique-app-name.herokuapp.com
```

**Total Time: ~5 minutes** ⏱️

---

## 📋 What Happens Automatically

1. Heroku reads `Procfile` - knows how to run your app
2. Heroku reads `requirements.txt` - installs Python packages
3. Heroku reads `runtime.txt` - uses Python 3.10
4. App starts on dyno (server)
5. Database (SQLite) created automatically
6. App is live!

---

## ✅ Verify It's Working

1. Open browser
2. Go to: `https://your-app-name.herokuapp.com`
3. You should see the home page
4. Click "Assessment"
5. Fill form and submit
6. See results
7. Data is saved!

---

## 📊 What You Get (Free Tier)

- ✓ 1 web dyno (server)
- ✓ 512 MB RAM
- ✓ SQLite database
- ✓ Up to 1000 rows in database
- ✓ Free while active
- ⚠️ Sleeps after 30 min of inactivity
- ⚠️ Takes 5 seconds to wake up

---

## 🔄 Making Changes

After deployment, if you make changes:

```bash
# Make changes to code
# Save file

# Commit changes
git add .
git commit -m "Description of changes"

# Deploy
git push heroku main

# View changes
heroku open
```

---

## 📝 Useful Heroku Commands

```bash
# View logs
heroku logs --tail

# View app configuration
heroku config

# Set environment variables
heroku config:set DATABASE_URL=mysql://...

# Scale app (add more servers)
heroku ps:scale web=2

# Check app status
heroku ps

# Restart app
heroku restart

# Stop app
heroku dyno:stop web

# Open app
heroku open

# Open logs (in browser)
heroku logs --tail

# Get app info
heroku apps:info
```

---

## 🆘 Troubleshooting

### "App won't load" or "503 error"
```bash
# Check logs
heroku logs --tail

# Look for errors
# Common issues:
# - Module not found → pip install missing package
# - Port error → Procfile uses wrong port
# - Database error → Check database connection
```

### "Connection refused"
```bash
# Might be starting up
# Wait 10 seconds
# Try again

# If persists:
heroku logs --tail
# Check for errors
```

### "Permission denied"
```bash
# If git issue:
heroku auth:login

# If Procfile issue:
# Verify Procfile content:
type Procfile

# Should show:
# web: gunicorn -w 4 -b 0.0.0.0:$PORT "app:create_app()"
```

### Database issues
```bash
# SQLite database created automatically
# Data stored on dyno filesystem
# Data persists between deploys
# Data lost if you rebuild dyno (rare)

# To upgrade to PostgreSQL (paid):
heroku addons:create heroku-postgresql:basic
# Automatically sets DATABASE_URL
```

---

## 💾 Optional: Upgrade to PostgreSQL (Paid)

SQLite works great for learning, but for production:

```bash
# Add PostgreSQL database
heroku addons:create heroku-postgresql:basic

# Verify it's set
heroku config | grep DATABASE_URL

# Deploy
git push heroku main
```

Cost: ~$9/month (much more reliable)

---

## 🔐 Security Notes

### Don't Commit Secrets
```bash
# .env file should NOT be in git
# But it's in .gitignore (already done)

# If you need environment variables:
heroku config:set SECRET_KEY=your-secret-key
heroku config:set API_KEY=your-api-key
```

### HTTPS Automatic
- All Heroku apps get free HTTPS
- Your URL: `https://your-app-name.herokuapp.com`
- SSL certificate automatic

---

## 📈 Monitoring Your App

### View Logs
```bash
# Last 100 lines
heroku logs -n 100

# Follow logs in real-time
heroku logs --tail

# Logs by process
heroku logs -p web
heroku logs -p worker
```

### Check Performance
```bash
# View current process status
heroku ps

# View app metrics (in browser)
# Heroku Dashboard → Metrics
```

---

## 🎯 Next Steps

1. **After successful deployment:**
   - Test all features
   - Try assessments
   - Check history
   - Verify API endpoints

2. **Monitor your app:**
   - Watch logs: `heroku logs --tail`
   - Check metrics in Heroku Dashboard
   - Monitor performance

3. **Make changes:**
   - Edit code locally
   - Commit to git
   - Push to Heroku: `git push heroku main`

4. **Scale up (if needed):**
   - Add more dyos
   - Upgrade dyno size
   - Add database

5. **Custom domain (optional):**
   - https://devcenter.heroku.com/articles/custom-domains

---

## 📊 Free Tier Limitations

| Feature | Free Tier | Pro Tier |
|---------|-----------|----------|
| Dyos | 1 | Unlimited |
| RAM | 512 MB | 512 MB - 8GB |
| Database Rows | 10K | Unlimited |
| Sleep | Sleeps @ 30min | Always on |
| Cost | $0/month | $50+/month |

---

## 💡 Tips & Tricks

### Keep dyno awake (free way)
```bash
# Add uptimerobot.com
# Free service pings your app
# Prevents sleep
# Must be free account
```

### Custom app name
```bash
heroku create medical-cdss-company-name
# Use numbers, dashes, lowercase only
```

### Transfer app to team
```bash
# Heroku Dashboard → Settings → Transfer → Change owner
```

### Export data
```bash
# Via web UI: http://localhost:5000/api/assess
# Via database tools
# Via Heroku backup
```

---

## ✅ Deployment Checklist

Before deploying:
- [x] requirements.txt has gunicorn
- [x] Procfile exists
- [x] runtime.txt exists
- [x] .gitignore exists
- [x] Code committed to git
- [x] Heroku account created
- [x] Heroku CLI installed
- [x] No secrets in code

---

## 🎉 You're Live!

Your Medical Decision Support System is now accessible at:

```
https://your-unique-app-name.herokuapp.com
```

Share this URL with anyone and they can:
- ✓ View the system
- ✓ Create assessments
- ✓ See results
- ✓ Access history

**Congratulations!** 🚀

---

## 📞 Support Links

- Heroku Docs: https://devcenter.heroku.com/
- Python Support: https://devcenter.heroku.com/articles/python-support
- Troubleshooting: https://devcenter.heroku.com/articles/deploying-python
- Community Help: https://help.heroku.com/

---

## 🆘 Need Help?

### Common Issues

**"remote: ! Push rejected"**
- Ensure you did: `git add .` and `git commit`
- Push again: `git push heroku main`

**"Application error"**
- Check logs: `heroku logs --tail`
- Look for Python errors
- Common: Missing import or typo

**"Module not found"**
- Add to requirements.txt
- Run: `pip install package_name` locally
- Run: `pip freeze > requirements.txt`
- Commit and push

**"Connection timeout"**
- App might be starting
- Wait 30 seconds
- Try again

---

**Heroku Deployment Guide Version**: 1.0.0
**Status**: Ready to Deploy ✅
**Time to Deploy**: 5 minutes
**Cost**: Free (with limitations)

Happy deploying! 🎉
