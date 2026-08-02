# Fuzzy Logic-Based Medical Decision Support System

A comprehensive web-based diabetes risk assessment system using advanced fuzzy logic inference with an interactive, animated user interface.

## 🎯 Overview

This system implements a **Mamdani Fuzzy Inference Engine** to assess diabetes risk by analyzing patient health metrics (blood sugar, BMI, age, and blood pressure). The fuzzy logic approach better mimics clinical reasoning where parameters don't have sharp boundaries.

### Key Features

- **25 Fuzzy Rules**: Comprehensive rule set based on medical knowledge
- **Triangular Membership Functions**: Smooth transitions between fuzzy sets
- **Centroid Defuzzification**: Converts fuzzy output to crisp risk scores
- **Interactive UI**: Animated forms, real-time validation, and engaging visualizations
- **Mobile Responsive**: Fully responsive design for all devices
- **Assessment History**: Browser-based storage of previous assessments
- **Clinical Recommendations**: Context-aware medical guidance based on risk level

## 🏗️ System Architecture

```
Patient Data
    ↓
[FUZZIFICATION]
Convert crisp values to fuzzy membership values
    ↓
[RULE EVALUATION]
Apply 25+ medical fuzzy rules
    ↓
[AGGREGATION]
Combine rule outputs
    ↓
[DEFUZZIFICATION]
Convert fuzzy output to risk score (0-100%)
    ↓
Risk Score + Clinical Recommendations
```

## 📋 Input Parameters

| Parameter | Range | Unit | Clinical Significance |
|-----------|-------|------|----------------------|
| Blood Sugar | 0-600 | mg/dL | Primary diabetes indicator |
| BMI | 10-60 | kg/m² | Body composition indicator |
| Age | 0-120 | years | Risk factor with age |
| Blood Pressure | 40-250 | mmHg | Cardiovascular health indicator |

## 📊 Fuzzy Sets

### Blood Sugar
- **Normal**: 70-100 mg/dL
- **Slightly High**: 90-130 mg/dL
- **High**: 120-180 mg/dL
- **Very High**: 170-250 mg/dL

### BMI
- **Underweight**: 0-18.5 kg/m²
- **Normal**: 17-27 kg/m²
- **Overweight**: 25-31 kg/m²
- **Obese**: 30-60 kg/m²

### Age
- **Young**: 0-35 years
- **Middle-aged**: 30-60 years
- **Old**: 55-100 years

### Blood Pressure
- **Normal**: 60-120 mmHg
- **Elevated**: 110-160 mmHg
- **High**: 150-200 mmHg

## 🎓 Risk Categories

- **Low Risk (0-30%)**: Maintain healthy lifestyle
- **Medium Risk (30-60%)**: Consult healthcare provider
- **High Risk (60-100%)**: Immediate medical attention recommended

## 📦 Installation

### Prerequisites
- Python 3.7+
- pip (Python package manager)

### Setup Instructions

1. **Clone the repository**
```bash
cd c:\medical_cdss
```

2. **Create virtual environment (recommended)**
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Run the application**
```bash
python app.py
```

5. **Access the web interface**
Open your browser and go to: `http://localhost:5000`

## 📁 Project Structure

```
medical_cdss/
├── app.py                          # Flask application and routes
├── config.py                       # Configuration settings
├── requirements.txt                # Python dependencies
│
├── fuzzy/                          # Fuzzy logic engine
│   ├── __init__.py                # Module initialization
│   ├── membership.py              # Membership functions and fuzzy sets
│   ├── rules.py                   # Fuzzy rules (25+ rules)
│   ├── inference.py               # Inference operations
│   ├── defuzzification.py         # Defuzzification methods
│   └── engine.py                  # Main fuzzy engine orchestration
│
├── models/                         # Data models
│   └── patient.py                 # Patient assessment model
│
├── utils/                          # Utility functions
│   ├── validators.py              # Input validators
│   └── helpers.py                 # Helper functions
│
├── static/                         # Frontend assets
│   ├── css/
│   │   └── style.css              # Main stylesheet with animations
│   └── js/
│       └── script.js              # Client-side JavaScript
│
└── templates/                      # HTML templates
    ├── base.html                  # Base template
    ├── index.html                 # Home page
    ├── patient_form.html          # Assessment form with results
    ├── history.html               # Assessment history
    └── about.html                 # About and technical details
```

## 🔧 Fuzzy Rules Examples

The system includes 25 fuzzy rules such as:

1. **IF** Blood Sugar is Normal **AND** BMI is Normal **AND** Age is Young **THEN** Risk is Low
2. **IF** Blood Sugar is High **AND** BMI is Obese **THEN** Risk is High
3. **IF** Blood Sugar is Very High **THEN** Risk is High
4. **IF** Blood Sugar is Slightly High **AND** BMI is Obese **AND** Age is Old **THEN** Risk is High
5. And 21 more rules...

## 🎨 User Interface Features

- **Responsive Design**: Works on desktop, tablet, and mobile devices
- **Smooth Animations**: CSS animations for engaging user experience
- **Real-time Validation**: Input validation with helpful error messages
- **Interactive Forms**: BMI calculator, tooltips, and helper text
- **Visual Results**: Color-coded risk circles, membership bars, and charts
- **Print/Export**: Print assessments for medical records
- **Assessment History**: Local storage of previous assessments

## 📡 API Endpoints

### POST `/api/assess`
Performs diabetes risk assessment

**Request:**
```json
{
    "name": "John Doe",
    "age": 45,
    "blood_sugar": 150,
    "bmi": 28,
    "bp": 135
}
```

**Response:**
```json
{
    "status": "success",
    "data": {
        "risk_score": 62.5,
        "risk_category": "high",
        "risk_label": "High Risk",
        "risk_percentage": "62%",
        "recommendations": [...],
        "fuzzified_inputs": {...},
        "rules_fired": 18,
        "color": "#F44336"
    }
}
```

### GET `/api/system-info`
Returns system information

### POST `/api/validate`
Validates patient input data

### GET `/api/health`
Health check endpoint

## 🔬 Fuzzy Logic Implementation

### Membership Functions
- **Triangular**: Three-point membership functions for all input variables
- **Smooth Transitions**: Overlapping fuzzy sets allow gradual transitions between categories

### Inference Method
- **Mamdani Inference**: Most common for medical decision support
- **Min-Max Composition**: Minimum operator for AND, maximum for aggregation

### Defuzzification
- **Centroid Method**: Center of Mass (CoM) calculation
- **Weighted Average**: Alternative defuzzification method included

## 🧪 Example Scenarios

### Scenario 1: Low Risk Patient
```
Input:
- Blood Sugar: 95 mg/dL (Normal)
- BMI: 23 kg/m² (Normal)
- Age: 30 (Young)
- BP: 115 mmHg (Normal)

Output:
- Risk Score: 18%
- Category: Low Risk
- Recommendation: Maintain healthy lifestyle
```

### Scenario 2: High Risk Patient
```
Input:
- Blood Sugar: 220 mg/dL (Very High)
- BMI: 34 kg/m² (Obese)
- Age: 65 (Old)
- BP: 155 mmHg (High)

Output:
- Risk Score: 88%
- Category: High Risk
- Recommendation: Immediate physician consultation required
```

## ⚖️ Important Disclaimer

⚠️ **IMPORTANT**: This system is for educational purposes only. It should NOT be used as a substitute for professional medical diagnosis or treatment. Always consult with qualified healthcare professionals for medical decisions.

## 📚 Technologies Used

**Backend:**
- Python 3.7+
- Flask 2.3.3
- NumPy 1.24.3

**Frontend:**
- HTML5
- CSS3 (with animations and transitions)
- Vanilla JavaScript
- Font Awesome Icons

**Algorithms:**
- Mamdani Fuzzy Inference System
- Triangular Membership Functions
- Centroid Defuzzification

## 📖 How to Use

1. **Navigate to Home**: Start at the homepage to understand the system
2. **Begin Assessment**: Click "Start Assessment" to access the form
3. **Enter Data**: Fill in patient information (name, age, blood sugar, BMI, BP)
4. **Calculate BMI**: Use the built-in BMI calculator if needed
5. **Submit**: Click "Perform Assessment"
6. **View Results**: See risk score, category, and recommendations
7. **Print/Export**: Print the report for medical records
8. **History**: View previous assessments

## 🔍 Troubleshooting

### Application won't start
- Ensure Python 3.7+ is installed
- Activate virtual environment
- Install requirements: `pip install -r requirements.txt`

### Port 5000 already in use
- Edit `app.py` and change port number
- Or kill process on port 5000

### Animations not working
- Check browser compatibility (all modern browsers supported)
- Disable browser extensions that might interfere

## 📝 Development

### Adding New Fuzzy Rules
Edit `fuzzy/rules.py` and add rules in the `evaluate_rules()` method:

```python
# New rule example
rule_new = min(bs['high'], bmi['obese'], age['old'])
rules_output['high'].append(rule_new)
```

### Modifying Membership Functions
Edit fuzzy sets in `fuzzy/membership.py` to adjust ranges:

```python
BLOOD_SUGAR_RANGES = {
    'new_category': (lower, peak, upper)
}
```

## 📧 Support

For issues or questions, please refer to the technical documentation in the "About" section of the application.

## 📄 License

This project is developed for educational purposes in the context of medical decision support systems and fuzzy logic.

## 🙏 Acknowledgments

- Fuzzy logic principles by Lotfi Zadeh
- Mamdani inference system
- Medical knowledge from WHO and ADA guidelines

---

**Version**: 1.0.0
**Last Updated**: 2024
**Status**: Educational/Research Project
