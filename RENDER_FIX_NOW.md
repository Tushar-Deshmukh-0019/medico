# 🚨 RENDER DEPLOYMENT - CRITICAL FIX

**Your deployment is failing because DATABASE_URL environment variable is NOT set on Render!**

---

## ❌ WHAT'S HAPPENING

App is trying to connect to `localhost:5432` on Render (which doesn't exist):

```
⚠️ No DATABASE_URL environment variable found.
Use the deployment-provided PostgreSQL connection string through `DATABASE_URL`.
```

**This ONLY works on your local machine, not on Render!**

---

## ✅ FIX IN 5 STEPS

### Step 1: Get Your PostgreSQL Connection String

1. Go to: https://render.com/dashboard
2. Click your **PostgreSQL database** (e.g., `medical-cdss-db`)
3. Copy the connection string (looks like):
   ```
   postgresql://postgres:XXXXXXXXXXXXX@dpg-xxxxx.oregon-postgres.render.com:5432/medical_cdss
   ```
4. **Save this!**

---

### Step 2: Set Environment Variable on Render

1. Go to: https://render.com/dashboard
2. Click your **Web Service** (e.g., `medical-cdss`)
3. Go to **Settings** tab
4. Scroll to **Environment** section
5. Click **Add Environment Variable**

---

### Step 3: Add DATABASE_URL Variable

**Add EXACTLY this:**

```
Key: DATABASE_URL

Value: [PASTE YOUR CONNECTION STRING FROM STEP 1]
```

**Example value (replace with yours):**
```
postgresql://postgres:<your-password>@<render-endpoint>:5432/medical_cdss
```

⚠️ **Make sure you copy the ENTIRE connection string, including the password!**

---

### Step 4: Add Other Environment Variables

While you're at it, add these too:

```
Key: FLASK_ENV
Value: production

Key: FLASK_DEBUG
Value: False
```

---

### Step 5: Redeploy

1. Go to Web Service
2. Click **"Redeploy"** button (or push new code to GitHub)
3. **Wait 5-10 minutes**
4. **Watch logs** for:
   - ✅ "Worker ready"
   - ✅ "Listening at: http://0.0.0.0:8080"

---

## 🎯 WHAT TO LOOK FOR IN LOGS

### ✅ SUCCESS (You'll see):
```
✓ Using PostgreSQL for Render deployment
✓ Database connection established
✓ Worker ready
✓ Running on http://0.0.0.0:8080
```

### ❌ STILL FAILING (You'll see):
```
⚠️ No DATABASE_URL environment variable found.
sqlalchemy.exc.OperationalError: connection to server failed
```

**If you see this, the environment variable didn't save. Go back to Step 3!**

---

## 🔍 VERIFY ENVIRONMENT VARIABLES ARE SET

**In Render Dashboard:**

1. Web Service → Settings
2. Scroll to Environment
3. You should see:
   ```
   DATABASE_URL = postgresql://postgres:xxxxx...
   FLASK_ENV = production
   FLASK_DEBUG = False
   ```

**If you DON'T see these, they're not saved!**

---

## 📋 STEP-BY-STEP SCREENSHOT GUIDE

### Screenshot 1: Render Dashboard
```
[Dashboard] → [Services] → [medical-cdss] → [Settings]
```

### Screenshot 2: Environment Section
```
Environment Variables
├─ DATABASE_URL = postgresql://postgres:...
├─ FLASK_ENV = production
└─ FLASK_DEBUG = False

[Add Environment Variable] button
```

### Screenshot 3: Add Variable Form
```
Key: DATABASE_URL
Value: [your connection string]
[Add Variable] button
```

---

## 🆘 STILL NOT WORKING?

### Check 1: Is DATABASE_URL saved?
- Render Dashboard → Web Service → Settings
- Scroll to Environment
- DATABASE_URL should be listed

### Check 2: Is it the right format?
- Should start with: `postgresql://`
- Should have: `postgres:password@host:port/database`
- Should have password (not blank)

### Check 3: Did you redeploy?
- Push new code: `git push origin main`
- Or click Redeploy button
- Wait 5-10 minutes
- Check logs

### Check 4: Check logs for DATABASE_URL
- Render Dashboard → Logs
- Search for "DATABASE_URL"
- Should see it being used

---

## 🎯 QUICK CHECKLIST

```
[ ] Got PostgreSQL connection string from Render
[ ] Went to Web Service Settings
[ ] Added DATABASE_URL environment variable
[ ] Pasted correct connection string (with password)
[ ] Added FLASK_ENV = production
[ ] Added FLASK_DEBUG = False
[ ] Clicked Save/Add
[ ] Redeployed (push or redeploy button)
[ ] Waited 5-10 minutes
[ ] Checked logs for success
[ ] Tested app at https://medical-cdss.onrender.com
```

---

## ✨ WHAT HAPPENS AFTER FIX

Once DATABASE_URL is set correctly:

1. App starts
2. Connects to Render's PostgreSQL
3. Creates tables (if needed)
4. Ready to accept requests
5. Your app goes LIVE!

---

## 📞 IF STILL BROKEN

1. **Check connection string format:**
   - `postgresql://postgres:PASSWORD@HOST:5432/medical_cdss`
   - PASSWORD should be your PostgreSQL password
   - HOST should be from Render (not localhost!)

2. **Verify PostgreSQL database exists:**
   - Render Dashboard → PostgreSQL
   - Should show "Available"
   - Database name: `medical_cdss`

3. **Check logs for exact error:**
   - Render Dashboard → Logs
   - Read error carefully
   - Common: connection string typo

4. **Restart everything:**
   - Delete web service
   - Create new web service
   - Start fresh with correct environment variables

---

## 🎉 WHEN IT WORKS

You'll see in logs:
```
[2026-08-02 15:06:07 +0000] [1] [INFO] Listening at: http://0.0.0.0:8080 (1)
[2026-08-02 15:06:07 +0000] [7] [INFO] Booting worker with pid: 7
[2026-08-02 15:06:07 +0000] [8] [INFO] Booting worker with pid: 8
[2026-08-02 15:06:07 +0000] [9] [INFO] Booting worker with pid: 9
[2026-08-02 15:06:07 +0000] [10] [INFO] Booting worker with pid: 10
✓ Database connection established
✓ Using PostgreSQL for Render deployment
```

Then visit: **https://medical-cdss.onrender.com**

✅ App is LIVE!

---

## 🔑 KEY TAKEAWAY

**DATABASE_URL must be set in Render environment variables!**

Without it, the app tries to use localhost PostgreSQL (which doesn't exist on Render).

Set it now and your app will work! 🚀
