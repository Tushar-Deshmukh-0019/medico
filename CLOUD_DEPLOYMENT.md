# ☁️ Cloud Deployment Guide - Medical Decision Support System

Complete guide to deploy your Fuzzy Logic Medical Decision Support System to the cloud.

## 🌍 Cloud Platform Options

| Platform | Cost | Difficulty | Recommended For |
|----------|------|------------|-----------------|
| **Heroku** | Free tier available | ⭐ Easy | Quick prototyping |
| **AWS** | Pay-as-you-go | ⭐⭐ Medium | Production apps |
| **Azure** | Free tier available | ⭐⭐ Medium | Enterprise apps |
| **Google Cloud** | Pay-as-you-go | ⭐⭐ Medium | Modern deployments |
| **DigitalOcean** | $4-12/month | ⭐⭐ Medium | Simple deployments |

---

## 🚀 Option 1: Heroku (Easiest - Free to Start)

### Step 1: Install Heroku CLI
```bash
# Windows
Download from: https://devcenter.heroku.com/articles/heroku-cli

# Linux/Mac
brew tap heroku/brew && brew install heroku
```

### Step 2: Create Heroku Account
```bash
# Go to: https://www.heroku.com
# Sign up for free
```

### Step 3: Create Procfile
Create file: `c:\medical_cdss\Procfile`
```
web: gunicorn -w 4 -b 0.0.0.0:$PORT "app:create_app()"
```

### Step 4: Create runtime.txt
Create file: `c:\medical_cdss\runtime.txt`
```
python-3.10.13
```

### Step 5: Update requirements.txt
Add production server:
```bash
pip install gunicorn
pip freeze > requirements.txt
```

### Step 6: Initialize Git
```bash
cd c:\medical_cdss
git init
git add .
git commit -m "Initial commit - Medical CDSS"
```

### Step 7: Deploy to Heroku
```bash
# Login to Heroku
heroku login

# Create Heroku app
heroku create your-app-name

# Set environment variables
heroku config:set DATABASE_URL=sqlite:///medical_cdss.db
heroku config:set FLASK_ENV=production

# Deploy
git push heroku main

# View logs
heroku logs --tail
```

### Step 8: Access Your App
```
https://your-app-name.herokuapp.com
```

**Advantages:**
- ✅ Free tier available
- ✅ Easy deployment
- ✅ Automatic scaling
- ✅ Good for learning

**Limitations:**
- ⚠️ Free dyno sleeps after 30 min inactivity
- ⚠️ Limited to 512MB RAM
- ⚠️ SQLite not persistent (data lost)

---

## 💻 Option 2: AWS (Most Popular - Production)

### Step 1: Install AWS CLI
```bash
# Download from: https://aws.amazon.com/cli/
# Or: pip install awscli
```

### Step 2: Create AWS Account
```
https://aws.amazon.com
Sign up (free tier available 12 months)
```

### Step 3: Configure AWS CLI
```bash
aws configure

# Enter:
# AWS Access Key ID: [from AWS console]
# AWS Secret Access Key: [from AWS console]
# Default region: us-east-1
# Default output format: json
```

### Step 4: Create Elastic Beanstalk Application

#### Option A: Using EB CLI (Recommended)
```bash
# Install EB CLI
pip install awsebcli

# Initialize EB
cd c:\medical_cdss
eb init -p python-3.10 medical-cdss --region us-east-1

# Create environment
eb create medical-cdss-env

# Deploy
eb deploy

# Open application
eb open
```

#### Option B: Using AWS Console
1. Go to Elastic Beanstalk
2. Create application
3. Upload code
4. Configure settings
5. Deploy

### Step 5: Configure Environment Variables
```bash
# Via EB CLI
eb setenv DATABASE_URL=mysql://user:pass@rds-instance.amazonaws.com/medical_cdss
eb setenv FLASK_ENV=production

# Or in AWS Console:
# Elastic Beanstalk → Configuration → Environment properties
```

### Step 6: Set Up RDS Database (MySQL)
```bash
# Via AWS Console:
# 1. Go to RDS
# 2. Create DB instance (MySQL)
# 3. Copy connection string
# 4. Set DATABASE_URL environment variable

# Or via AWS CLI:
aws rds create-db-instance \
  --db-instance-identifier medical-cdss-db \
  --db-instance-class db.t3.micro \
  --engine mysql \
  --master-username admin \
  --master-user-password '<set-in-secret-manager>'
```

### Step 7: Deploy & Monitor
```bash
# Deploy
eb deploy

# Check status
eb status

# View logs
eb logs

# SSH into instance (if needed)
eb ssh

# Scale up/down
eb scale 3  # 3 instances
```

### Step 8: Access Your App
```
https://medical-cdss-env.elasticbeanstalk.com
```

**Advantages:**
- ✅ Production-ready
- ✅ Auto-scaling
- ✅ RDS database support
- ✅ CDN integration
- ✅ Monitoring & alerts

**Cost Estimate:**
- EC2 instance: ~$10/month
- RDS database: ~$15/month
- Data transfer: Variable

---

## 🔵 Option 3: Azure (Enterprise-Ready)

### Step 1: Create Azure Account
```
https://azure.microsoft.com
Sign up (free $200 credit)
```

### Step 2: Install Azure CLI
```bash
# Download from: https://docs.microsoft.com/cli/azure/install-azure-cli
# Or: pip install azure-cli
```

### Step 3: Create Azure App Service

#### Via Azure CLI
```bash
# Login
az login

# Create resource group
az group create --name medical-cdss-rg --location eastus

# Create App Service plan
az appservice plan create \
  --name medical-cdss-plan \
  --resource-group medical-cdss-rg \
  --sku B1 --is-linux

# Create web app
az webapp create \
  --resource-group medical-cdss-rg \
  --plan medical-cdss-plan \
  --name medical-cdss-app \
  --runtime "PYTHON|3.10"

# Deploy code
cd c:\medical_cdss
az webapp up \
  --resource-group medical-cdss-rg \
  --name medical-cdss-app
```

#### Via Azure Portal
1. Go to App Services
2. Create new App Service
3. Configure Python runtime
4. Deploy code

### Step 4: Configure Database
```bash
# Create MySQL Database for Azure
az mysql flexible-server create \
  --resource-group medical-cdss-rg \
  --name medical-cdss-db \
  --admin-user adminuser \
  --admin-password '<set-in-secret-manager>'

# Get connection string
az mysql flexible-server show \
  --resource-group medical-cdss-rg \
  --name medical-cdss-db
```

### Step 5: Set Environment Variables
```bash
# Via CLI
az webapp config appsettings set \
  --resource-group medical-cdss-rg \
  --name medical-cdss-app \
  --settings \
  DATABASE_URL="mysql+pymysql://user:pass@host/dbname" \
  FLASK_ENV="production"

# Or via Portal: Configuration → Application settings
```

### Step 6: Deploy
```bash
# Deploy from local
az webapp up --name medical-cdss-app

# Or connect GitHub repository
# Portal → Deployment Center → GitHub
```

### Step 7: Access Your App
```
https://medical-cdss-app.azurewebsites.net
```

**Advantages:**
- ✅ Enterprise features
- ✅ Excellent documentation
- ✅ Integration with Microsoft services
- ✅ Good free tier
- ✅ Auto-scaling

**Cost Estimate:**
- App Service (B1): ~$13/month
- MySQL Database: ~$29/month

---

## 🟨 Option 4: Google Cloud (Modern)

### Step 1: Create Google Cloud Account
```
https://cloud.google.com
Sign up (free $300 credit)
```

### Step 2: Install Google Cloud SDK
```bash
# Download from: https://cloud.google.com/sdk/docs/install
# Or: pip install google-cloud-deploy
```

### Step 3: Deploy to Cloud Run
```bash
# Initialize project
gcloud config set project YOUR-PROJECT-ID

# Create Dockerfile (see below)
# Create .dockerignore

# Build and deploy
gcloud run deploy medical-cdss \
  --source . \
  --platform managed \
  --region us-central1 \
  --memory 512Mi \
  --timeout 3600 \
  --allow-unauthenticated
```

### Step 4: Create Dockerfile
Create file: `c:\medical_cdss\Dockerfile`
```dockerfile
FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:8080", "app:create_app()"]
```

### Step 5: Create .dockerignore
Create file: `c:\medical_cdss\.dockerignore`
```
__pycache__
*.pyc
.git
.gitignore
.vscode
.env
*.db
```

### Step 6: Access Your App
```
https://medical-cdss-XXXXX-uc.a.run.app
```

**Advantages:**
- ✅ Serverless architecture
- ✅ Pay-per-request pricing
- ✅ Automatic scaling
- ✅ No server management

**Cost Estimate:**
- Cloud Run: Free tier + pay-per-request
- Storage: Minimal

---

## 🔧 Required Files for Deployment

### 1. Procfile (Heroku)
```
web: gunicorn -w 4 -b 0.0.0.0:$PORT "app:create_app()"
```

### 2. runtime.txt (Heroku)
```
python-3.10.13
```

### 3. requirements.txt (All platforms)
```bash
pip freeze > requirements.txt
```

Updated should include:
```
Flask==2.3.3
Flask-SQLAlchemy==3.0.5
gunicorn==21.2.0
PyMySQL==1.1.0
python-dotenv==1.0.0
numpy==1.24.3
pandas==2.0.3
Werkzeug==2.3.7
```

### 4. .env (Local - don't commit)
```
FLASK_ENV=production
SECRET_KEY=your-secret-key-here
DATABASE_URL=mysql+pymysql://user:pass@host/dbname
```

### 5. Dockerfile (Google Cloud/Docker)
```dockerfile
FROM python:3.10-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 8080
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:8080", "app:create_app()"]
```

### 6. .gitignore
```
__pycache__/
*.pyc
.env
*.db
.vscode/
venv/
dist/
build/
*.egg-info/
.DS_Store
```

---

## 🗄️ Database Setup for Cloud

### SQLite (Not Recommended for Production)
- File-based
- Data lost on redeploy
- Use only for testing

### MySQL (Recommended)
```bash
# Connection string format
DATABASE_URL=mysql+pymysql://username:password@host:3306/database_name

# Example
DATABASE_URL=mysql+pymysql://admin:SecurePass123@medical-db.rds.amazonaws.com/medical_cdss
```

### PostgreSQL (Alternative)
```bash
# Connection string format
DATABASE_URL=postgresql://username:password@host:5432/database_name
```

---

## 📝 Environment Variables

Set these in your cloud platform:

```
FLASK_ENV=production
SECRET_KEY=[Generate: python -c "import secrets; print(secrets.token_hex(32))"]
DATABASE_URL=mysql+pymysql://user:pass@host/dbname
FLASK_DEBUG=False
```

---

## 🔒 Security Best Practices

### 1. Secret Management
```bash
# Generate secret key
python -c "import secrets; print(secrets.token_hex(32))"

# Don't commit secrets to git
# Use environment variables or secret managers
```

### 2. Database Security
```bash
# Use strong passwords
# Minimum 12 characters with mixed case and special chars

# Restrict access
# Only allow app to access database
# Use VPC/security groups
```

### 3. HTTPS
```bash
# Enable SSL/TLS
# Most cloud platforms auto-enable
# Heroku: automatic
# AWS: Use CloudFront + ACM certificate
# Azure: automatic
```

### 4. Environment Variables
```bash
# Don't hardcode secrets
# Use cloud platform's secrets manager
# Heroku Config Vars
# AWS Secrets Manager
# Azure Key Vault
```

---

## 📊 Comparison Table

| Feature | Heroku | AWS | Azure | GCP |
|---------|--------|-----|-------|-----|
| Ease of Setup | ⭐⭐⭐⭐⭐ | ⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ |
| Cost | Free tier | $25+/mo | $15+/mo | $0.00/mo* |
| Scalability | Good | Excellent | Excellent | Excellent |
| Support | Good | Excellent | Excellent | Good |
| Free Tier | Yes | Yes (12mo) | Yes ($200) | Yes ($300) |
| Database Support | PostgreSQL | RDS/DynamoDB | MySQL/PostgreSQL | Cloud SQL |
| Best For | Learning | Production | Enterprise | Serverless |

*GCP Cloud Run is free for first 2M invocations

---

## 🚀 Step-by-Step: Heroku (Quickest)

### Complete Setup (15 minutes)

```bash
# 1. Create Procfile
echo 'web: gunicorn -w 4 -b 0.0.0.0:$PORT "app:create_app()"' > Procfile

# 2. Create runtime.txt
echo 'python-3.10.13' > runtime.txt

# 3. Update requirements
pip install gunicorn
pip freeze > requirements.txt

# 4. Git setup
git init
git add .
git commit -m "Initial commit"

# 5. Heroku setup
heroku login
heroku create your-app-name

# 6. Deploy
git push heroku main

# 7. View app
heroku open
```

That's it! Your app is live! 🎉

---

## 🚀 Step-by-Step: AWS (Production)

### Complete Setup (30 minutes)

```bash
# 1. Install tools
pip install awsebcli

# 2. Create Procfile & runtime.txt (same as above)

# 3. Configure AWS
aws configure
# Enter your AWS credentials

# 4. Initialize Elastic Beanstalk
eb init -p python-3.10 medical-cdss --region us-east-1

# 5. Create environment
eb create medical-cdss-prod

# 6. Set environment variables
eb setenv DATABASE_URL=your-rds-url FLASK_ENV=production

# 7. Deploy
eb deploy

# 8. Monitor
eb open
```

---

## 🔍 Troubleshooting Cloud Deployment

### App Won't Start
```bash
# Check logs
heroku logs --tail          # Heroku
eb logs                     # AWS
az webapp log tail          # Azure

# Common issues:
# - Missing requirements
# - Wrong Python version
# - Database connection error
```

### Database Connection Failed
```bash
# Verify connection string
echo $DATABASE_URL

# Check database is running
# Check firewall rules allow access
# Verify credentials

# For MySQL:
mysql -h host -u user -p -D dbname
```

### Performance Issues
```bash
# Scale up instances
heroku ps:scale web=2       # Heroku
eb scale 3                  # AWS
az appservice plan update --sku S2  # Azure

# Check logs for errors
# Monitor database performance
```

---

## 📈 Monitoring & Logs

### Heroku
```bash
heroku logs --tail
heroku logs -n 100
heroku ps
heroku config
```

### AWS
```bash
eb logs
eb status
eb config
aws logs tail /aws/elasticbeanstalk/logs
```

### Azure
```bash
az webapp log tail --resource-group rg --name app
az monitor app-insights metrics list --resource-group rg
```

---

## 💰 Cost Estimates

### Heroku
- Free tier: $0/month (limited)
- Basic dyno: $7/month
- Standard dyno: $50/month

### AWS Elastic Beanstalk
- EC2 (t3.micro): $10/month
- RDS MySQL: $15/month
- Data transfer: Variable
- **Total: ~$25+/month**

### Azure App Service
- B1 plan: $13/month
- MySQL Database: $29/month
- **Total: ~$42+/month**

### Google Cloud Run
- First 2M requests: FREE
- After: $0.40 per 1M requests
- Cloud SQL (MySQL): $4/month
- **Total: ~$4+/month** (usually free tier covers it)

---

## ✅ Pre-Deployment Checklist

- [ ] requirements.txt updated with gunicorn
- [ ] Procfile created (for Heroku)
- [ ] .env file created (not in git)
- [ ] .gitignore configured
- [ ] Database credentials set
- [ ] SECRET_KEY generated and set
- [ ] FLASK_ENV=production
- [ ] All tests passing locally
- [ ] Git initialized and committed
- [ ] Cloud account created
- [ ] Cloud CLI installed
- [ ] Firewall rules configured
- [ ] SSL/HTTPS enabled

---

## 📞 Deployment Support

### Heroku
- https://devcenter.heroku.com/
- https://help.heroku.com/

### AWS
- https://docs.aws.amazon.com/elasticbeanstalk/
- https://aws.amazon.com/getting-started/

### Azure
- https://docs.microsoft.com/azure/app-service/
- https://docs.microsoft.com/azure/app-service/app-service-web-get-started-python

### Google Cloud
- https://cloud.google.com/run/docs/
- https://cloud.google.com/docs/

---

## 🎉 After Deployment

### Test Your App
1. Go to your cloud URL
2. Create an assessment
3. Check if data is saved
4. Verify email notifications (if configured)
5. Check logs for errors

### Monitor Performance
- View dashboard
- Check error rates
- Monitor database
- Review logs

### Scale if Needed
- Increase server size
- Add more instances
- Optimize database

---

## 🚀 Your App is Ready to Deploy!

Choose your platform:
1. **Heroku** - Easiest (free tier)
2. **AWS** - Most popular
3. **Azure** - Enterprise
4. **GCP** - Serverless

Pick one and follow the steps above!

---

**Cloud Deployment Guide Version**: 1.0.0
**Last Updated**: 2024
**Platforms Covered**: Heroku, AWS, Azure, Google Cloud
**Status**: Ready to Deploy ✅
