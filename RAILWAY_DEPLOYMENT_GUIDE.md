# 🚂 Railway Deployment Guide - Medical CDSS

Complete step-by-step guide to deploy your Medical CDSS application to Railway.

---

## 📋 What is Railway?

**Railway** is a modern cloud platform for deploying applications:
- ✅ Easy deployment (just push code)
- ✅ Automatic PostgreSQL database
- ✅ Built-in monitoring
- ✅ Free tier available ($5/month credit)
- ✅ No credit card required for trial
- ✅ Perfect for Flask applications

**Website:** https://railway.app



---

## 🎯 Prerequisites

Before starting, make sure you have:

✅ **Git installed** - For version control  
✅ **GitHub account** - To push your code  
✅ **Railway account** - Free at railway.app  
✅ **Code ready** - Your Medical CDSS project  

---

## 📝 Step 1: Install Required Tools

### Install Git (if not already installed)

1. Download from: https://git-scm.com/download/win
2. Run installer with default settings
3. Verify installation:
   ```cmd
   git --version
   ```

### Create GitHub Account

1. Go to: https://github.com/signup
2. Create free account
3. Verify email

### Create Railway Account

1. Go to: https://railway.app
2. Click "Get Started" or "Sign Up"
3. Sign up with GitHub (recommended)
4. Create new project

---

## 🔧 Step 2: Prepare Your Project for Deployment

### Update requirements.txt

Your current `requirements.txt` should include:
```
Flask==3.0.3
Flask-SQLAlchemy==3.0.5
psycopg2-binary==2.9.9
python-dotenv==1.0.1
gunicorn==22.0.0
SQLAlchemy==2.0.39
```

Verify it has everything. Run:
```cmd
pip freeze > requirements.txt
```

### Create Procfile (if not exists)

Create file: `c:\medical_cdss\Procfile`

```
web: gunicorn app:app
```

This tells Railway how to run your app.

### Create runtime.txt (if not exists)

Create file: `c:\medical_cdss\runtime.txt`

```
python-3.10.13
```

Specifies Python version for Railway.

### Update environment variables

Your `.env` file has:
```
DATABASE_URL=<your managed PostgreSQL connection string>
FLASK_ENV=development
```

Railway will automatically provide DATABASE_URL. You just need to set FLASK_ENV.

---

## 🔐 Step 3: Push Code to GitHub

### Initialize Git Repository

```cmd
cd c:\medical_cdss
git init
git config user.name "Your Name"
git config user.email "your.email@example.com"
```

### Add Files to Git

```cmd
git add .
git status
```

You should see all your files.

### Create Initial Commit

```cmd
git commit -m "Initial commit: Medical CDSS with fuzzy logic"
```

### Create GitHub Repository

1. Go to: https://github.com/new
2. Create repository: `medical-cdss` (or any name)
3. Don't initialize with README (we have one)
4. Click "Create repository"

### Push to GitHub

Copy the commands from GitHub and run:

```cmd
git remote add origin https://github.com/YOUR_USERNAME/medical-cdss.git
git branch -M main
git push -u origin main
```

Replace `YOUR_USERNAME` with your actual GitHub username.

---

## 🚀 Step 4: Deploy to Railway

### Method 1: Dashboard (Easiest)

1. **Go to Railway:** https://railway.app/dashboard
2. **Click "Create New Project"**
3. **Select "Deploy from GitHub"**
4. **Authorize Railway to access GitHub**
5. **Select your repository** (`medical-cdss`)
6. **Select main branch**
7. **Railway starts deploying!**

### Method 2: Railway CLI

If you prefer command line:

```cmd
npm install -g @railway/cli
railway login
cd c:\medical_cdss
railway init
railway up
```

---

## 🗄️ Step 5: Set Up PostgreSQL Database

### Add PostgreSQL to Railway

1. **In Railway Dashboard**
2. **Click your project**
3. **Click "Add Service"**
4. **Select "PostgreSQL"**
5. **Railway creates database automatically**

### Connect Database to App

1. **In Railway Dashboard**
2. **Click your Flask app service**
3. **Go to "Variables"**
4. **Railway automatically adds DATABASE_URL** from PostgreSQL

### Verify Connection

1. Check "PostgreSQL" service in Railway
2. It shows connection details automatically
3. Your app uses the connection string

---

## 🌍 Step 6: Configure Environment Variables

### Set Variables in Railway

1. **Click your Flask app service**
2. **Go to "Variables"**
3. **Add these variables:**

| Variable | Value |
|----------|-------|
| `FLASK_ENV` | `production` |
| `FLASK_DEBUG` | `False` |

DATABASE_URL is set automatically by Railway.

---

## ✅ Step 7: Deploy and Test

### Railway Deploys Automatically

When you pushed to GitHub, Railway:
1. ✅ Detects your code
2. ✅ Reads Procfile
3. ✅ Installs dependencies
4. ✅ Creates PostgreSQL database
5. ✅ Starts your app
6. ✅ Assigns a public URL

### Get Your Public URL

1. **In Railway Dashboard**
2. **Click your Flask app**
3. **Look for "Public URL"** (something like: `medical-cdss-production-xxxxx.railway.app`)
4. **Click the URL** to open your app

### Test Your Deployment

1. **Visit your public URL**
2. You should see the Medical CDSS home page
3. Click "Assessment" 
4. Create a test assessment
5. Check if it saves successfully

---

## 📊 Step 8: Monitor and Debug

### View Logs

1. **In Railway Dashboard**
2. **Click your app service**
3. **Go to "Deployments"**
4. **Click latest deployment**
5. **View real-time logs**

### Check Database

1. **In Railway, click PostgreSQL service**
2. **Go to "Connect"**
3. **Use connection details to connect with pgAdmin**
4. **Verify your tables and data**

### View Metrics

1. **Click your app service**
2. **Go to "Metrics"**
3. **See CPU, memory, requests**

---

## 🔄 Step 9: Deploy Updates

### Make Changes and Push

```cmd
cd c:\medical_cdss
# Make your changes
git add .
git commit -m "Updated assessment logic"
git push origin main
```

### Railway Auto-Deploys

Railway automatically:
1. Detects new push
2. Rebuilds your app
3. Deploys new version
4. **No downtime!**

---

## 🎯 Complete Deployment Checklist

- [ ] Git installed
- [ ] GitHub account created
- [ ] Code pushed to GitHub
- [ ] Railway account created
- [ ] Project connected to GitHub
- [ ] PostgreSQL added to Railway
- [ ] DATABASE_URL configured
- [ ] FLASK_ENV set to production
- [ ] App deployed successfully
- [ ] Public URL working
- [ ] Can create assessments
- [ ] Data saved to database
- [ ] Logs show no errors

---

## 📚 Quick Command Reference

### Git Commands

```cmd
# Initialize repo
git init

# Add all files
git add .

# Commit
git commit -m "Your message"

# Push to GitHub
git push origin main

# Check status
git status

# View logs
git log
```

### Railway CLI

```cmd
# Login to Railway
railway login

# Initialize Railway
railway init

# Deploy
railway up

# View logs
railway logs

# View variables
railway variables
```

---

## 🆘 Troubleshooting

### Problem: "DATABASE_URL not found"

**Solution:**
1. Add PostgreSQL service to Railway project
2. Wait for it to initialize
3. DATABASE_URL appears automatically
4. Redeploy your app

### Problem: "ModuleNotFoundError"

**Solution:**
1. Check requirements.txt is in root directory
2. All modules are listed
3. Run: `pip freeze > requirements.txt`
4. Push and redeploy

### Problem: "App crashes on startup"

**Solution:**
1. Check logs: Railway Dashboard → Deployments → View logs
2. Look for error messages
3. Fix the issue locally
4. Commit and push
5. Railway auto-redeploys

### Problem: "Can't connect to database"

**Solution:**
1. Verify PostgreSQL service exists in Railway
2. Check DATABASE_URL is set
3. Check Procfile uses gunicorn
4. View logs for connection errors

### Problem: "Static files not loading"

**Solution:**
1. Flask handles static files automatically
2. Check static folder exists
3. Check paths in templates
4. Run locally to verify

---

## 🔐 Security Notes

### For Production

✅ **Do:**
- Set FLASK_ENV=production
- Use strong database password
- Enable HTTPS (Railway does this)
- Monitor logs for errors
- Keep dependencies updated

❌ **Don't:**
- Commit .env file (already in .gitignore)
- Use debug mode in production
- Hardcode secrets in code
- Expose sensitive info in logs

### Environment Variables

Your sensitive data (DATABASE_URL) is:
- ✅ Managed by Railway
- ✅ Never exposed in logs
- ✅ Encrypted in transit
- ✅ Secure

---

## 📈 Scaling Your App

### Railway Auto-Scaling

Railway automatically handles:
- ✅ Load balancing
- ✅ Auto-restart on crash
- ✅ Database backups
- ✅ Monitoring

### Manual Scaling

If needed:
1. Go to Railway Dashboard
2. Click your app service
3. Adjust resources (RAM, CPU)
4. Click "Update"

---

## 💾 Database Backups

### Railway Automatic Backups

Railway automatically:
- ✅ Daily backups
- ✅ 7-day retention
- ✅ One-click restore

### Manual Backup

1. Click PostgreSQL service
2. Go to "Connect"
3. Use pgAdmin to backup

---

## 📱 Custom Domain (Optional)

To use your own domain:

1. **In Railway Dashboard**
2. **Click your app service**
3. **Go to "Settings"**
4. **Add custom domain**
5. **Update DNS records** with your provider

---

## 🎓 Next Steps After Deployment

### Monitor Regularly
1. Check Railway Dashboard daily
2. Review logs for errors
3. Monitor performance metrics

### Continue Development
1. Make improvements locally
2. Test thoroughly
3. Commit and push
4. Railway auto-deploys

### Add Features
1. Improve fuzzy rules
2. Add user authentication
3. Add data analytics
4. Deploy updates

---

## 📞 Getting Help

### Railway Documentation
- **Official Docs:** https://docs.railway.app
- **GitHub Integration:** https://docs.railway.app/guides/github
- **PostgreSQL:** https://docs.railway.app/databases/postgresql

### Your Code
- **Repository:** Your GitHub repo
- **Issues:** GitHub Issues for tracking
- **Deployments:** Railway Dashboard

---

## 🎉 You're Live!

Once deployed, your Medical CDSS is:
- ✅ Publicly accessible
- ✅ Using PostgreSQL database
- ✅ Auto-scaling
- ✅ Backed up
- ✅ Monitored
- ✅ Production-ready

**Share your public URL with others to use your system!**

---

## 💡 Tips and Tricks

### View Live Logs
```cmd
railway logs -f
```
Shows real-time logs.

### Set Variables from CLI
```cmd
railway variables set FLASK_ENV production
```

### Connect to Database Remotely
```cmd
psql [DATABASE_URL from Railway]
```

### Restart App
In Railway Dashboard → Click app → "Restart"

### View Resource Usage
Railway Dashboard → Metrics tab

---

## ✨ Final Checklist

Before going live:

- [ ] Code works locally
- [ ] All tests pass
- [ ] requirements.txt updated
- [ ] Procfile created
- [ ] .env configured (not committed)
- [ ] Pushed to GitHub
- [ ] Railway project created
- [ ] PostgreSQL added
- [ ] DATABASE_URL configured
- [ ] Environment variables set
- [ ] App deployed
- [ ] Public URL working
- [ ] Can create assessments
- [ ] Data saves correctly
- [ ] No errors in logs

---

## 🚀 You're Ready to Deploy!

Follow these steps and your Medical CDSS will be live on Railway in minutes!

**Next steps:**
1. Push code to GitHub
2. Create Railway account
3. Connect GitHub repository
4. Add PostgreSQL
5. Deploy!

**Your app will be live and accessible worldwide!**

---

**Happy deployment! 🚂🌍**
