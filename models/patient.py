"""
Patient Data Model
"""
from datetime import datetime

class PatientAssessment:
    """Model for patient diabetes risk assessment"""
    
    def __init__(self, name, age, blood_sugar, bmi, bp, assessment_date=None):
        self.name = name
        self.age = age
        self.blood_sugar = blood_sugar
        self.bmi = bmi
        self.bp = bp
        self.assessment_date = assessment_date or datetime.now()
        self.risk_score = None
        self.risk_category = None
        self.recommendations = []
    
    def to_dict(self):
        """Convert to dictionary"""
        return {
            'name': self.name,
            'age': self.age,
            'blood_sugar': self.blood_sugar,
            'bmi': self.bmi,
            'bp': self.bp,
            'assessment_date': self.assessment_date.isoformat(),
            'risk_score': self.risk_score,
            'risk_category': self.risk_category,
            'recommendations': self.recommendations
        }
    
    def validate(self):
        """Validate patient data"""
        errors = []
        
        if not self.name or len(self.name.strip()) == 0:
            errors.append('Patient name is required')
        
        if not isinstance(self.age, (int, float)) or self.age < 0 or self.age > 120:
            errors.append('Age must be between 0-120 years')
        
        if not isinstance(self.blood_sugar, (int, float)) or self.blood_sugar < 0 or self.blood_sugar > 600:
            errors.append('Blood sugar must be between 0-600 mg/dL')
        
        if not isinstance(self.bmi, (int, float)) or self.bmi < 10 or self.bmi > 60:
            errors.append('BMI must be between 10-60 kg/m²')
        
        if not isinstance(self.bp, (int, float)) or self.bp < 40 or self.bp > 250:
            errors.append('Blood pressure must be between 40-250 mmHg')
        
        return len(errors) == 0, errors
    
    def calculate_bmi(height_cm, weight_kg):
        """Calculate BMI from height and weight"""
        if height_cm <= 0:
            return None
        height_m = height_cm / 100
        return round(weight_kg / (height_m ** 2), 2)
