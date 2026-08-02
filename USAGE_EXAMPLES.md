# Usage Examples - Medical Decision Support System

Practical examples and scenarios for using the Fuzzy Logic Medical Decision Support System.

## 🎯 Quick Examples

### Example 1: Assessment Through Web Interface

1. **Start Application**
   ```bash
   python app.py
   ```

2. **Navigate to Assessment**
   ```
   http://localhost:5000/assessment
   ```

3. **Fill in Patient Data**
   - Name: Sarah Johnson
   - Age: 52
   - Blood Sugar: 145 mg/dL
   - BMI: 31 (or calculate from height/weight)
   - Blood Pressure: 138 mmHg

4. **Submit Form**
   - Click "Perform Assessment"
   - Wait for results

5. **Review Results**
   - Risk Score: 72%
   - Category: High Risk
   - Recommendations: Follow clinical guidance
   - Save to history automatically

### Example 2: Programmatic Assessment

```python
from fuzzy.engine import FuzzyEngine

# Initialize engine
engine = FuzzyEngine()

# Patient data
patient_data = {
    'blood_sugar': 145,
    'bmi': 31,
    'age': 52,
    'bp': 138
}

# Perform assessment
result = engine.assess_diabetes_risk(patient_data)

# Print results
print(f"Risk Score: {result['risk_score']}%")
print(f"Category: {result['risk_label']}")
print(f"Recommendations:")
for rec in result['recommendations']:
    print(f"  - {rec}")
```

**Output:**
```
Risk Score: 72.0%
Category: High Risk
Recommendations:
  - 🔴 High diabetes risk detected
  - • Urgent: Consult an endocrinologist or internist
  - • Comprehensive metabolic panel required
  - • Structured weight loss program (5-10% target)
  - • Diabetes prevention program enrollment suggested
  - ... and more
```

## 📊 Patient Scenarios

### Scenario 1: Young Healthy Patient
**Profile**: 28-year-old with normal parameters

```python
patient_young = {
    'blood_sugar': 85,
    'bmi': 22,
    'age': 28,
    'bp': 110
}

result = engine.assess_diabetes_risk(patient_young)
```

**Expected Output:**
- Risk Score: ~15%
- Category: Low Risk
- Recommendations: Maintain lifestyle

### Scenario 2: Middle-Aged with Slight Elevation
**Profile**: 45-year-old with slightly elevated parameters

```python
patient_moderate = {
    'blood_sugar': 120,
    'bmi': 27,
    'age': 45,
    'bp': 125
}

result = engine.assess_diabetes_risk(patient_moderate)
```

**Expected Output:**
- Risk Score: ~50%
- Category: Medium Risk
- Recommendations: Schedule physician consultation, lifestyle modifications

### Scenario 3: Senior with Multiple Risk Factors
**Profile**: 68-year-old with multiple elevated parameters

```python
patient_senior = {
    'blood_sugar': 200,
    'bmi': 35,
    'age': 68,
    'bp': 155
}

result = engine.assess_diabetes_risk(patient_senior)
```

**Expected Output:**
- Risk Score: ~85%
- Category: High Risk
- Recommendations: Urgent medical attention

## 🔍 API Usage Examples

### Using cURL

#### Basic Assessment
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

#### Validation Only
```bash
curl -X POST http://localhost:5000/api/validate \
  -H "Content-Type: application/json" \
  -d '{
    "name": "John Doe",
    "age": 45,
    "blood_sugar": 150,
    "bmi": 28,
    "bp": 135
  }'
```

#### System Info
```bash
curl http://localhost:5000/api/system-info
```

#### Health Check
```bash
curl http://localhost:5000/api/health
```

### Using Python Requests

```python
import requests
import json

BASE_URL = "http://localhost:5000/api"

# Perform assessment
patient_data = {
    "name": "Jane Smith",
    "age": 52,
    "blood_sugar": 165,
    "bmi": 30,
    "bp": 140
}

response = requests.post(
    f"{BASE_URL}/assess",
    json=patient_data,
    headers={"Content-Type": "application/json"}
)

result = response.json()

if result['status'] == 'success':
    data = result['data']
    print(f"Risk Score: {data['risk_score']}%")
    print(f"Category: {data['risk_label']}")
else:
    print(f"Error: {result['error']}")
```

### Using JavaScript/Fetch

```javascript
const patientData = {
    name: "Michael Johnson",
    age: 55,
    blood_sugar: 180,
    bmi: 32,
    bp: 145
};

fetch('/api/assess', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json'
    },
    body: JSON.stringify(patientData)
})
.then(response => response.json())
.then(data => {
    if (data.status === 'success') {
        console.log(`Risk Score: ${data.data.risk_score}%`);
        console.log(`Category: ${data.data.risk_label}`);
        console.log('Recommendations:');
        data.data.recommendations.forEach(rec => {
            console.log(`  - ${rec}`);
        });
    }
})
.catch(error => console.error('Error:', error));
```

## 🧪 Testing Different Risk Levels

### Create Low Risk Case
```python
# Normal all parameters
low_risk = {'blood_sugar': 90, 'bmi': 22, 'age': 30, 'bp': 110}
result = engine.assess_diabetes_risk(low_risk)
assert result['risk_category'] == 'low', "Expected low risk"
```

### Create Medium Risk Case
```python
# Some elevated parameters
medium_risk = {'blood_sugar': 130, 'bmi': 27, 'age': 50, 'bp': 130}
result = engine.assess_diabetes_risk(medium_risk)
assert result['risk_category'] == 'medium', "Expected medium risk"
```

### Create High Risk Case
```python
# Multiple elevated parameters
high_risk = {'blood_sugar': 200, 'bmi': 35, 'age': 65, 'bp': 150}
result = engine.assess_diabetes_risk(high_risk)
assert result['risk_category'] == 'high', "Expected high risk"
```

## 📈 Batch Processing

Process multiple patients at once:

```python
from fuzzy.engine import FuzzyEngine
import csv

# Initialize engine
engine = FuzzyEngine()

# Sample patient list
patients = [
    {"name": "Patient A", "blood_sugar": 100, "bmi": 23, "age": 40, "bp": 120},
    {"name": "Patient B", "blood_sugar": 160, "bmi": 30, "age": 55, "bp": 140},
    {"name": "Patient C", "blood_sugar": 220, "bmi": 35, "age": 70, "bp": 155},
]

# Process all patients
results = []
for patient in patients:
    patient_data = {
        'blood_sugar': patient['blood_sugar'],
        'bmi': patient['bmi'],
        'age': patient['age'],
        'bp': patient['bp']
    }
    
    result = engine.assess_diabetes_risk(patient_data)
    
    results.append({
        'name': patient['name'],
        'risk_score': result['risk_score'],
        'risk_category': result['risk_category'],
        'risk_label': result['risk_label']
    })

# Display results
for result in results:
    print(f"{result['name']}: {result['risk_score']}% ({result['risk_label']})")
```

**Output:**
```
Patient A: 20.0% (Low Risk)
Patient B: 65.0% (High Risk)
Patient C: 80.0% (High Risk)
```

## 🔧 Customization Examples

### Modify Risk Thresholds

Edit `fuzzy/rules.py` and adjust the risk categorization:

```python
@staticmethod
def get_risk_category(risk_score):
    """Categorize risk based on score"""
    if risk_score < 25:  # Changed from 30
        return 'low', 'Low Risk'
    elif risk_score < 50:  # Changed from 60
        return 'medium', 'Medium Risk'
    else:
        return 'high', 'High Risk'
```

### Add Custom Recommendations

Edit `fuzzy/rules.py` in the `get_recommendations()` method:

```python
recommendations.append('• Custom recommendation based on your profile')
```

### Add New Fuzzy Rule

Edit `fuzzy/rules.py` and add to `evaluate_rules()`:

```python
# New rule example
rule_new = min(bs['high'], bmi['obese'], age['old'], bp['high'])
rules_output['high'].append(rule_new)
```

## 📊 Integration Examples

### With Database (SQLAlchemy)

```python
from datetime import datetime
from app import create_app, db

class AssessmentRecord(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    patient_name = db.Column(db.String(100))
    blood_sugar = db.Column(db.Float)
    bmi = db.Column(db.Float)
    age = db.Column(db.Float)
    bp = db.Column(db.Float)
    risk_score = db.Column(db.Float)
    risk_category = db.Column(db.String(20))
    date = db.Column(db.DateTime, default=datetime.now)

# Save assessment
app = create_app()
with app.app_context():
    result = engine.assess_diabetes_risk(patient_data)
    record = AssessmentRecord(
        patient_name=patient_data['name'],
        blood_sugar=patient_data['blood_sugar'],
        bmi=patient_data['bmi'],
        age=patient_data['age'],
        bp=patient_data['bp'],
        risk_score=result['risk_score'],
        risk_category=result['risk_category']
    )
    db.session.add(record)
    db.session.commit()
```

### Generate PDF Report

```python
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Table, TableStyle, Spacer
from reportlab.lib.styles import getSampleStyleSheet

def generate_pdf_report(result, filename):
    doc = SimpleDocTemplate(filename, pagesize=letter)
    story = []
    styles = getSampleStyleSheet()
    
    # Title
    story.append(Paragraph("Diabetes Risk Assessment Report", styles['Heading1']))
    story.append(Spacer(1, 12))
    
    # Patient info table
    data = [
        ['Patient', result['patient_name']],
        ['Risk Score', f"{result['risk_score']}%"],
        ['Category', result['risk_label']],
    ]
    
    table = Table(data)
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (0, -1), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, -1), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (0, -1), 14),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 12),
        ('BACKGROUND', (1, 0), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black)
    ]))
    story.append(table)
    
    # Build PDF
    doc.build(story)

# Usage
result = engine.assess_diabetes_risk(patient_data)
generate_pdf_report(result, 'assessment_report.pdf')
```

## 🎓 Learning Scenarios

### Understanding Fuzzy Membership

```python
from fuzzy.membership import DiabetesFuzzySets

# Get membership values for a specific blood sugar level
blood_sugar = 125  # mg/dL
memberships = DiabetesFuzzySets.fuzzify_blood_sugar(blood_sugar)

print(f"Blood Sugar: {blood_sugar} mg/dL")
print(f"Membership Values:")
for category, value in memberships.items():
    print(f"  {category}: {value:.3f}")
```

**Output:**
```
Blood Sugar: 125 mg/dL
Membership Values:
  normal: 0.333
  slightly_high: 0.630
  high: 0.370
  very_high: 0.000
```

### Understanding Rule Evaluation

```python
from fuzzy.rules import FuzzyRules
from fuzzy.membership import DiabetesFuzzySets

# Get fuzzified inputs
patient_data = {'blood_sugar': 150, 'bmi': 28, 'age': 45, 'bp': 135}
fuzzified = {
    'blood_sugar': DiabetesFuzzySets.fuzzify_blood_sugar(patient_data['blood_sugar']),
    'bmi': DiabetesFuzzySets.fuzzify_bmi(patient_data['bmi']),
    'age': DiabetesFuzzySets.fuzzify_age(patient_data['age']),
    'bp': DiabetesFuzzySets.fuzzify_bp(patient_data['bp'])
}

# Evaluate rules
rules_output = FuzzyRules.evaluate_rules(fuzzified)

print(f"Low Risk Rules Fired: {len([r for r in rules_output['low'] if r > 0])}")
print(f"Medium Risk Rules Fired: {len([r for r in rules_output['medium'] if r > 0])}")
print(f"High Risk Rules Fired: {len([r for r in rules_output['high'] if r > 0])}")
```

## 📝 Practical Workflow

### Day-to-Day Usage

1. **Start Application**
   ```bash
   python app.py
   ```

2. **Patient Arrives**
   - Navigate to /assessment
   - Fill in patient information
   - Click "Perform Assessment"

3. **Review Results**
   - Check risk score and category
   - Read recommendations
   - Print report if needed

4. **Follow Up**
   - Store assessment information
   - Schedule follow-up appointments
   - Document in medical records

5. **Track History**
   - View previous assessments
   - Compare results over time
   - Monitor risk progression

---

**For more information, refer to README.md and SETUP_GUIDE.md**
