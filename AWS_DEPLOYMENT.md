# ☁️ AWS Deployment Guide (Production-Ready)

Deploy your Medical Decision Support System to AWS for production.

## 📋 Prerequisites

1. **AWS Account**
   - Go to: https://aws.amazon.com
   - Sign up (free tier 12 months)
   - Add payment method

2. **AWS CLI**
   ```bash
   pip install awscli
   # Or download from: https://aws.amazon.com/cli/
   ```

3. **EB CLI (Elastic Beanstalk)**
   ```bash
   pip install awsebcli
   ```

4. **Git**
   - Required for deployment

5. **AWS Credentials**
   - Create IAM user in AWS console
   - Get Access Key ID
   - Get Secret Access Key

---

## 🚀 30-Minute Deployment

### Step 1: Configure AWS CLI (3 minutes)
```bash
aws configure

# When prompted, enter:
# AWS Access Key ID: [your key]
# AWS Secret Access Key: [your secret]
# Default region: us-east-1
# Default output format: json
```

### Step 2: Initialize Elastic Beanstalk (2 minutes)
```bash
cd c:\medical_cdss

eb init -p python-3.10 medical-cdss --region us-east-1

# When prompted:
# Application name: medical-cdss
# Default region: us-east-1 (or your choice)
# Create SSH key: y
```

### Step 3: Create Elastic Beanstalk Environment (15 minutes)
```bash
eb create medical-cdss-prod

# This creates:
# - EC2 instance
# - Load balancer
# - Security groups
# - RDS database (optional, we'll skip for now)
```

### Step 4: Deploy Application (5 minutes)
```bash
git add .
git commit -m "Deploy to AWS"

eb deploy

# Deployment starts
# Monitor progress in terminal
# Wait for completion
```

### Step 5: Open Your App (2 minutes)
```bash
eb open

# App opens in browser!
# OR manually go to environment URL
```

---

## 🗄️ Optional: Add RDS Database (MySQL)

### Step 1: Create RDS Instance
```bash
# Via AWS Console:
# 1. Go to RDS
# 2. Create database
# 3. MySQL
# 4. Free tier template
# 5. Storage: 20GB
# 6. DB instance identifier: medical-cdss-db
# 7. Master username: admin
# 8. Master password: choose a strong secret in the AWS console

# Or via CLI:
aws rds create-db-instance \
  --db-instance-identifier medical-cdss-db \
  --db-instance-class db.t3.micro \
  --engine mysql \
  --allocated-storage 20 \
  --master-username admin \
  --master-user-password '<set-in-secret-manager>'
```

### Step 2: Get Connection String
```bash
# Copy the Endpoint from RDS console
# Format: medical-cdss-db.c123456.us-east-1.rds.amazonaws.com

# Connection string:
mysql+pymysql://admin:<your-password>@<rds-endpoint>:3306/medical_cdss
```

### Step 3: Set Environment Variable
```bash
eb setenv \
  DATABASE_URL="<your managed database connection string>"

# Deploy
eb deploy
```

---

## 🔧 Configuration Files

### .ebextensions/python.config
Create: `c:\medical_cdss\.ebextensions\python.config`

```yaml
option_settings:
  aws:elasticbeanstalk:container:python:
    WSGIPath: "app:create_app()"
    NumProcesses: 4
    NumThreads: 2
  aws:elasticbeanstalk:application:environment:
    PYTHONPATH: "/var/app/current"
```

### .ebextensions/django.config (Alternative)
```yaml
option_settings:
  aws:elasticbeanstalk:container:python:
    WSGIPath: "app:create_app()"
  aws:elasticbeanstalk:application:environment:
    FLASK_ENV: "production"
```

---

## 📊 AWS Resources Created

| Resource | Type | Cost |
|----------|------|------|
| EC2 Instance (t3.micro) | Compute | $10/month |
| Elastic IP | Network | $0 (unused) / $3/month |
| RDS MySQL (t3.micro) | Database | $15/month |
| Load Balancer | Load Balancing | $16/month |
| Data Transfer | Data | Variable |
| **Total** | | **~$41+/month** |

---

## 🎯 Useful EB Commands

```bash
# Deploy
eb deploy

# Open app in browser
eb open

# Check status
eb status

# View logs
eb logs

# SSH into instance
eb ssh

# Configuration
eb config

# Environment variables
eb setenv KEY=value
eb printenv

# Scale (add/remove instances)
eb scale 2

# Terminate environment (WARNING)
eb terminate

# Swap CNAME (blue-green deployment)
eb swap
```

---

## 🔍 Monitoring

### CloudWatch Dashboard
```bash
# Via AWS Console:
# Services → CloudWatch → Dashboards
# Create dashboard
# Add metrics for:
# - EC2 CPU usage
# - Network in/out
# - RDS connections
```

### Logs
```bash
# View EB logs
eb logs

# Follow logs in real-time
eb logs --stream

# Via CloudWatch
# Services → CloudWatch → Log Groups
# /aws/elasticbeanstalk/medical-cdss-prod
```

### Alarms
```bash
# Set up alerts for:
# - High CPU usage
# - Database connections
# - Failed deployments
# - HTTP errors

# Via CloudWatch Console
```

---

## 🔐 Security Configuration

### 1. Security Groups
```bash
# Allow inbound:
# HTTP (80)
# HTTPS (443)
# SSH (22) - for admin only

# Restrict database access to app server only
```

### 2. Environment Variables
```bash
# Store secrets in EB environment variables:
eb setenv \
  SECRET_KEY="your-secret-key-here" \
  DATABASE_PASSWORD="your-db-password"

# NOT in code or git
```

### 3. HTTPS/SSL
```bash
# Request SSL certificate in ACM
# Apply to Load Balancer
# Redirect HTTP to HTTPS

# Via EB Console:
# Configuration → Load Balancer → HTTPS
```

### 4. Database Security
```bash
# Create security group for RDS
# Allow inbound 3306 from app security group only
# Disable public access
# Use strong passwords
# Enable encryption
```

---

## 📈 Scaling Configuration

### Auto Scaling
```bash
# Via EB Console:
# Configuration → Auto Scaling

# Settings:
# Min instances: 1
# Max instances: 4
# Trigger: CPU > 70%
# Action: Add instance
```

### Manual Scaling
```bash
# Scale to 3 instances
eb scale 3

# Scale to 1 instance
eb scale 1
```

---

## 🚀 Deployment Best Practices

### 1. Testing Before Deploy
```bash
# Test locally
python app.py

# Run tests
python test_system.py

# Commit changes
git add .
git commit -m "Ready to deploy"
```

### 2. Zero-Downtime Deployment
```bash
# Create second environment
eb create medical-cdss-staging

# Deploy to staging
eb deploy -e medical-cdss-staging

# Test thoroughly

# Swap when ready
eb swap -n medical-cdss-prod
```

### 3. Monitoring Deployments
```bash
# Check status
eb status

# View recent logs
eb logs

# Monitor metrics
# AWS Console → CloudWatch
```

---

## 🔄 CI/CD with AWS CodePipeline

### Automated Deployment
```yaml
# Create buildspec.yml

version: 0.2

phases:
  install:
    runtime-versions:
      python: 3.10
  build:
    commands:
      - pip install -r requirements.txt
      - python test_system.py
artifacts:
  files:
    - '**/*'
```

---

## 🆘 Troubleshooting

### App won't deploy
```bash
# Check logs
eb logs --all

# Common issues:
# - Dependencies missing (pip install locally, pip freeze > requirements.txt)
# - Syntax error (check Python code)
# - Missing files (Procfile, requirements.txt)

# Fix locally, commit, and deploy again
git add .
git commit -m "Fix"
eb deploy
```

### 503 Service Unavailable
```bash
# App crashed during deployment
# Check logs
eb logs

# SSH into instance
eb ssh

# Check logs manually
cat /var/log/eb-engine.log
```

### Database connection failed
```bash
# Verify security group rules
# Database security group should allow app server

# Check RDS endpoint
# Should be: database-name.xxxxx.us-east-1.rds.amazonaws.com

# Test connection locally
mysql -h host -u user -p dbname

# Check environment variable
eb printenv | grep DATABASE_URL
```

### High costs
```bash
# Review:
# - EC2 instance type (scale down if possible)
# - RDS instance type
# - Data transfer
# - Unused resources

# Reduce costs:
# eb scale 1  (reduce instances)
# Delete unused resources
# Use Reserved Instances (cheaper)
```

---

## 📊 Cost Optimization

### 1. Right-Size Instances
```bash
# t3.micro: $10/month (1 vCPU, 512MB RAM)
# t3.small: $20/month (1 vCPU, 2GB RAM)
# t3.medium: $34/month (1 vCPU, 4GB RAM)

# Start small, scale if needed
```

### 2. Use Reserved Instances
```bash
# 1-year commitment: ~30% discount
# 3-year commitment: ~50% discount

# Via AWS Console:
# EC2 → Reserved Instances → Purchase
```

### 3. RDS Optimization
```bash
# db.t3.micro: $15/month
# db.t3.small: $30/month

# Use db.t3.micro for learning
# Upgrade if needed
```

### 4. Clean Up Unused Resources
```bash
# Terminate unused environments
eb terminate

# Delete unused RDS instances
# Delete unused Elastic IPs
# Delete unused Security Groups
```

---

## ✅ AWS Deployment Checklist

- [x] AWS account created
- [x] AWS CLI configured
- [x] EB CLI installed
- [x] Procfile created
- [x] requirements.txt updated
- [x] .gitignore configured
- [x] Code committed to git
- [x] EB environment initialized
- [x] EB environment created
- [x] App deployed
- [x] App verified working
- [x] RDS database created (optional)
- [x] Environment variables set
- [x] Monitoring configured
- [x] Security groups configured

---

## 📞 AWS Support

### Free Tier Support
- AWS Basic Support (included)
- Community forums
- AWS documentation

### Paid Support
- AWS Developer Support: $29/month
- AWS Business Support: $100/month
- AWS Enterprise Support: Custom

### Resources
- AWS Documentation: https://docs.aws.amazon.com/
- Elastic Beanstalk: https://docs.aws.amazon.com/elasticbeanstalk/
- RDS: https://docs.aws.amazon.com/rds/
- CloudWatch: https://docs.aws.amazon.com/cloudwatch/

---

## 🎉 Your App is Live!

```
Environment URL: medical-cdss-prod.elasticbeanstalk.com
Database: Configured with RDS
Monitoring: CloudWatch enabled
Scaling: Auto-scaling configured
```

**Congratulations!** Your production-ready app is deployed on AWS! 🚀

---

**AWS Deployment Guide Version**: 1.0.0
**Status**: Production-Ready ✅
**Time to Deploy**: 30 minutes
**Cost**: ~$41+/month
