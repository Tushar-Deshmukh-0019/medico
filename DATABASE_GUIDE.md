# 🗄️ Database Guide - Medical Decision Support System

Complete guide to the database system for the Fuzzy Logic Medical Decision Support System.

## 📊 Database Overview

The system now includes a **full-featured database layer** with two options:

### SQLite (Default)
- ✅ No setup required
- ✅ File-based storage
- ✅ Perfect for development
- ✅ Automatic initialization
- ✅ Default: `medical_cdss.db` in project root

### MySQL (Optional)
- ✅ Production-ready
- ✅ Multi-user support
- ✅ Advanced features
- ✅ Requires setup
- ✅ Better for large-scale deployments

---

## 🗂️ Database Schema

### Patient Table
```sql
CREATE TABLE patients (
    id INTEGER PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE,
    phone VARCHAR(20),
    date_of_birth DATE,
    gender VARCHAR(10),
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP
);
```

**Fields:**
- `id` - Unique patient identifier
- `name` - Patient full name
- `email` - Patient email (optional, unique)
- `phone` - Patient phone number (optional)
- `date_of_birth` - Patient DOB (optional)
- `gender` - Patient gender (optional)
- `created_at` - Record creation date
- `updated_at` - Last update date

### Assessment Table
```sql
CREATE TABLE assessments (
    id INTEGER PRIMARY KEY,
    patient_id INTEGER NOT NULL FOREIGN KEY,
    blood_sugar FLOAT NOT NULL,
    bmi FLOAT NOT NULL,
    age INTEGER NOT NULL,
    blood_pressure FLOAT NOT NULL,
    risk_score FLOAT NOT NULL,
    risk_category VARCHAR(20) NOT NULL,
    blood_sugar_status VARCHAR(50),
    bmi_category VARCHAR(50),
    bp_category VARCHAR(50),
    clinical_notes TEXT,
    recommendations TEXT,
    assessment_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (patient_id) REFERENCES patients(id)
);
```

**Fields:**
- `id` - Unique assessment identifier
- `patient_id` - Reference to patient
- `blood_sugar` - Blood sugar level (mg/dL)
- `bmi` - Body Mass Index
- `age` - Patient age
- `blood_pressure` - Systolic pressure (mmHg)
- `risk_score` - Calculated risk (0-100%)
- `risk_category` - low/medium/high
- `blood_sugar_status` - Categorized blood sugar status
- `bmi_category` - BMI category
- `bp_category` - BP category
- `clinical_notes` - Additional clinical notes
- `recommendations` - Clinical recommendations (JSON)
- `assessment_date` - When assessment was made
- `created_at` - Record creation date
- `updated_at` - Last update date

---

## 🚀 Setup & Configuration

### SQLite (Default - No Setup Needed)
Database initializes automatically on first run:
```
medical_cdss.db is created in project root
Tables are created automatically
Data persists across sessions
```

### MySQL Setup

#### 1. Install MySQL
```bash
# Windows
# Download from mysql.com or use: choco install mysql

# Linux
sudo apt-get install mysql-server

# Mac
brew install mysql
```

#### 2. Create Database
```sql
CREATE DATABASE medical_cdss;
CREATE USER 'cdss_user'@'localhost' IDENTIFIED BY 'your_password';
GRANT ALL PRIVILEGES ON medical_cdss.* TO 'cdss_user'@'localhost';
FLUSH PRIVILEGES;
```

#### 3. Set Environment Variable
```bash
# Windows (Command Prompt)
set DATABASE_URL=mysql+pymysql://cdss_user:your_password@localhost:3306/medical_cdss

# Windows (PowerShell)
$env:DATABASE_URL = "mysql+pymysql://cdss_user:your_password@localhost:3306/medical_cdss"

# Linux/Mac
export DATABASE_URL="mysql+pymysql://cdss_user:your_password@localhost:3306/medical_cdss"
```

#### 4. Start Application
```bash
python app.py
```

---

## 💻 Query Functions

### Patient Operations

#### Create Patient
```python
from database.queries import create_patient

patient = create_patient(
    name="John Doe",
    email="john@example.com",
    phone="123-456-7890",
    gender="M"
)
```

#### Get Patient
```python
from database.queries import get_patient, get_patient_by_email

# By ID
patient = get_patient(1)

# By Email
patient = get_patient_by_email("john@example.com")
```

#### Get All Patients
```python
from database.queries import get_all_patients

patients = get_all_patients()
for patient in patients:
    print(f"{patient.name} - {patient.email}")
```

#### Update Patient
```python
from database.queries import update_patient

updated = update_patient(
    patient_id=1,
    phone="987-654-3210",
    gender="M"
)
```

#### Delete Patient
```python
from database.queries import delete_patient

success = delete_patient(patient_id=1)
```

#### Search Patients
```python
from database.queries import search_patients

results = search_patients("John")
# Searches by name or email
```

### Assessment Operations

#### Create Assessment
```python
from database.queries import create_assessment

assessment = create_assessment(
    patient_id=1,
    blood_sugar=150,
    bmi=28,
    age=45,
    blood_pressure=135,
    risk_score=62.5,
    risk_category="high",
    blood_sugar_status="High",
    bmi_category="Overweight",
    bp_category="Elevated",
    clinical_notes="Patient shows elevated risk factors",
    recommendations="[recommendation1, recommendation2]"
)
```

#### Get Patient Assessments
```python
from database.queries import get_patient_assessments

assessments = get_patient_assessments(patient_id=1)
for assessment in assessments:
    print(f"Risk: {assessment.risk_score}% - {assessment.assessment_date}")
```

#### Get Latest Assessment
```python
from database.queries import get_latest_assessment

latest = get_latest_assessment(patient_id=1)
if latest:
    print(f"Latest Risk Score: {latest.risk_score}%")
```

#### Get All Assessments
```python
from database.queries import get_all_assessments

all_assessments = get_all_assessments()
print(f"Total assessments: {len(all_assessments)}")
```

#### Update Assessment
```python
from database.queries import update_assessment

updated = update_assessment(
    assessment_id=1,
    clinical_notes="Updated clinical notes"
)
```

#### Delete Assessment
```python
from database.queries import delete_assessment

success = delete_assessment(assessment_id=1)
```

### Analytics Operations

#### Risk Statistics
```python
from database.queries import get_risk_statistics

stats = get_risk_statistics()
print(f"Total: {stats['total']}")
print(f"Low Risk: {stats['low']} ({stats['low_percent']}%)")
print(f"Medium Risk: {stats['medium']} ({stats['medium_percent']}%)")
print(f"High Risk: {stats['high']} ({stats['high_percent']}%)")
```

#### Average Risk Score
```python
from database.queries import get_average_risk_score

avg = get_average_risk_score()
print(f"Average Risk Score: {avg}%")
```

#### Assessment Count
```python
from database.queries import get_assessment_count

count = get_assessment_count()
print(f"Total Assessments: {count}")
```

#### Patient Count
```python
from database.queries import get_patient_count

count = get_patient_count()
print(f"Total Patients: {count}")
```

#### Recent Assessments
```python
from database.queries import get_recent_assessments

recent = get_recent_assessments(limit=10)
for assessment in recent:
    print(f"{assessment.patient.name}: {assessment.risk_score}%")
```

#### Assessments by Date Range
```python
from database.queries import get_assessments_by_date_range
from datetime import datetime, timedelta

start = datetime.now() - timedelta(days=30)
end = datetime.now()

assessments = get_assessments_by_date_range(start, end)
print(f"Assessments in last 30 days: {len(assessments)}")
```

#### High Risk Patients
```python
from database.queries import get_high_risk_patients

high_risk = get_high_risk_patients()
print(f"High Risk Patients: {len(high_risk)}")
for patient in high_risk:
    print(f"- {patient.name}")
```

---

## 📱 API Endpoints with Database

### Create Assessment (with Database Save)
```bash
curl -X POST http://localhost:5000/api/assess \
  -H "Content-Type: application/json" \
  -d '{
    "name": "John Doe",
    "age": 45,
    "blood_sugar": 150,
    "bmi": 28,
    "bp": 135
  }'
```

**Response includes:**
- `assessment_id` - Database ID of assessment
- `patient_id` - Database ID of patient
- All assessment results

### System Info (with Database Stats)
```bash
curl http://localhost:5000/api/system-info
```

**Response includes:**
```json
{
  "database": {
    "total_assessments": 42,
    "total_patients": 15,
    "average_risk_score": 58.3,
    "risk_distribution": {
      "low": 10,
      "medium": 15,
      "high": 17,
      "low_percent": 23.81,
      "medium_percent": 35.71,
      "high_percent": 40.48
    }
  }
}
```

### Health Check (includes Database)
```bash
curl http://localhost:5000/api/health
```

**Response:**
```json
{
  "status": "healthy",
  "fuzzy_engine": "ready",
  "database": "connected"
}
```

---

## 🔧 Advanced Configuration

### Environment Variables

Create `.env` file in project root:

```bash
# Database
DATABASE_URL=sqlite:///./medical_cdss.db
# Or for MySQL:
# DATABASE_URL=mysql+pymysql://user:password@localhost:3306/medical_cdss

# Flask
FLASK_ENV=development
FLASK_DEBUG=True
SECRET_KEY=your-secret-key-here

# Application
APP_NAME=Medical CDSS
LOG_LEVEL=INFO
```

### Config File (config.py)
```python
class Config:
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
                              'sqlite:///medical_cdss.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False  # Set to True for SQL logging
```

---

## 📊 Database Maintenance

### Backup Database

#### SQLite
```bash
# Simple copy
copy medical_cdss.db medical_cdss_backup.db

# Or use sqlite3
sqlite3 medical_cdss.db ".backup medical_cdss_backup.db"
```

#### MySQL
```bash
# Full backup
mysqldump -u cdss_user -p medical_cdss > backup.sql

# Restore
mysql -u cdss_user -p medical_cdss < backup.sql
```

### Clear Database

```python
from app import create_app, db

app = create_app()
with app.app_context():
    db.drop_all()
    db.create_all()
    print("Database cleared and recreated")
```

### Export Data to CSV

```python
from database.queries import get_all_assessments, get_all_patients
import csv

# Export assessments
with open('assessments.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['ID', 'Patient', 'Blood Sugar', 'BMI', 'Age', 'BP', 'Risk Score', 'Category'])
    
    for assessment in get_all_assessments():
        writer.writerow([
            assessment.id,
            assessment.patient.name,
            assessment.blood_sugar,
            assessment.bmi,
            assessment.age,
            assessment.blood_pressure,
            assessment.risk_score,
            assessment.risk_category
        ])

print("Data exported to assessments.csv")
```

### Check Database Status

```python
from app import create_app, db
from database.connection import get_database_info

app = create_app()
with app.app_context():
    info = get_database_info()
    print(f"Database Driver: {info['drivername']}")
    print(f"Database: {info['database']}")
    print(f"Host: {info['host']}")
    print(f"Port: {info['port']}")
```

---

## 🧪 Testing Database

### Test Database Operations

```python
from app import create_app, db
from database.queries import *
from datetime import datetime

app = create_app()

with app.app_context():
    # Create patient
    print("Creating patient...")
    patient = create_patient(
        name="Test Patient",
        email="test@example.com",
        phone="555-1234"
    )
    print(f"✓ Patient created: ID {patient.id}")
    
    # Create assessment
    print("Creating assessment...")
    assessment = create_assessment(
        patient_id=patient.id,
        blood_sugar=150,
        bmi=28,
        age=45,
        blood_pressure=135,
        risk_score=62.5,
        risk_category="high"
    )
    print(f"✓ Assessment created: ID {assessment.id}")
    
    # Get assessments
    print("Retrieving assessments...")
    assessments = get_patient_assessments(patient.id)
    print(f"✓ Found {len(assessments)} assessments")
    
    # Get stats
    print("Getting statistics...")
    stats = get_risk_statistics()
    print(f"✓ Total assessments: {stats['total']}")
    print(f"✓ Risk distribution: Low {stats['low_percent']}%, Medium {stats['medium_percent']}%, High {stats['high_percent']}%")
    
    print("\n✓ All tests passed!")
```

---

## 📈 Performance Tips

### Indexing

Add indexes for common queries:

```python
from database.connection import db
from database.queries import Patient, Assessment

# Indexes are automatically created on:
# - Patient.id (primary key)
# - Patient.email (unique)
# - Assessment.patient_id (foreign key)
# - Assessment.assessment_date (for sorting)
# - Assessment.risk_category (for filtering)
```

### Query Optimization

```python
# ✓ Good - Uses eager loading
assessments = db.session.query(Assessment).options(
    db.joinedload(Assessment.patient)
).all()

# ✗ Bad - N+1 query problem
for assessment in get_all_assessments():
    print(assessment.patient.name)  # Separate query for each
```

### Connection Pooling

```python
# Automatically configured in Flask-SQLAlchemy
# Adjustable via:
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {
    'pool_size': 10,
    'pool_recycle': 3600,
    'pool_pre_ping': True,
}
```

---

## 🔒 Security Considerations

### SQL Injection Prevention
- ✅ All queries use parameterized statements
- ✅ SQLAlchemy ORM prevents SQL injection
- ✅ User input is never directly in queries

### Data Validation
```python
# Input validation before saving
from utils.validators import PatientDataValidator

is_valid, errors = PatientDataValidator.validate_all(data)
if is_valid:
    create_assessment(...)
```

### Password Security (MySQL)
```bash
# Use strong passwords
CREATE USER 'cdss_user'@'localhost' 
IDENTIFIED BY 'complex_password_123!@#';

# Don't hardcode in code - use environment variables
DATABASE_URL=mysql+pymysql://user:password@host/dbname
```

---

## 📚 Examples

### Complete Workflow Example

```python
from app import create_app, db
from database.queries import *

app = create_app()

with app.app_context():
    # Step 1: Create patient
    patient = create_patient(
        name="Alice Johnson",
        email="alice@example.com",
        phone="555-0123",
        gender="F"
    )
    
    # Step 2: Create multiple assessments
    assessments_data = [
        {
            'blood_sugar': 100, 'bmi': 24, 'age': 35,
            'blood_pressure': 120, 'risk_score': 15, 'risk_category': 'low'
        },
        {
            'blood_sugar': 130, 'bmi': 27, 'age': 35,
            'blood_pressure': 125, 'risk_score': 45, 'risk_category': 'medium'
        },
        {
            'blood_sugar': 180, 'bmi': 31, 'age': 35,
            'blood_pressure': 140, 'risk_score': 75, 'risk_category': 'high'
        }
    ]
    
    for data in assessments_data:
        assessment = create_assessment(
            patient_id=patient.id,
            **data
        )
    
    # Step 3: Analyze
    patient_assessments = get_patient_assessments(patient.id)
    print(f"Patient {patient.name} has {len(patient_assessments)} assessments")
    
    for i, assessment in enumerate(patient_assessments, 1):
        print(f"  {i}. Risk {assessment.risk_score}% ({assessment.risk_category})")
    
    # Step 4: Get overall stats
    stats = get_risk_statistics()
    print(f"\nOverall Statistics:")
    print(f"  Total Assessments: {stats['total']}")
    print(f"  Average Risk: {get_average_risk_score()}%")
```

---

## 🆘 Troubleshooting

### "No such table: patients"
```
Solution: Database not initialized
Run: python -c "from app import create_app, db; app = create_app(); db.create_all()"
```

### "Operational Error: connection refused"
```
Solution: Database server not running
For MySQL: Start MySQL server
For SQLite: Check file permissions
```

### "Foreign key constraint failed"
```
Solution: Patient doesn't exist for assessment
Ensure patient is created before assessment:
patient = create_patient(...)
assessment = create_assessment(patient_id=patient.id, ...)
```

---

## 📞 Support

For database issues:
1. Check DATABASE_GUIDE.md (this file)
2. Review example code above
3. Check Flask logs for errors
4. Verify database is running

---

**Database System Version**: 1.0.0
**Last Updated**: 2024
**Status**: Fully Functional
