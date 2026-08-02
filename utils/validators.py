"""
Input Validators
"""
import re

class PatientDataValidator:
    """Validates patient input data"""
    
    @staticmethod
    def validate_name(name):
        """Validate patient name"""
        if not name or len(name.strip()) == 0:
            return False, "Name cannot be empty"
        
        if len(name.strip()) < 2:
            return False, "Name must be at least 2 characters"
        
        if len(name.strip()) > 100:
            return False, "Name must be less than 100 characters"
        
        # Allow letters, spaces, hyphens, and apostrophes
        if not re.match(r"^[a-zA-Z\s\-']+$", name):
            return False, "Name contains invalid characters"
        
        return True, ""
    
    @staticmethod
    def validate_age(age):
        """Validate age"""
        try:
            age_num = float(age)
            if age_num < 0 or age_num > 120:
                return False, "Age must be between 0-120 years"
            return True, ""
        except (ValueError, TypeError):
            return False, "Age must be a valid number"
    
    @staticmethod
    def validate_blood_sugar(value):
        """Validate blood sugar level (mg/dL)"""
        try:
            bs = float(value)
            if bs < 0 or bs > 600:
                return False, "Blood sugar must be between 0-600 mg/dL"
            return True, ""
        except (ValueError, TypeError):
            return False, "Blood sugar must be a valid number"
    
    @staticmethod
    def validate_bmi(value):
        """Validate BMI (kg/m²)"""
        try:
            bmi = float(value)
            if bmi < 10 or bmi > 60:
                return False, "BMI must be between 10-60 kg/m²"
            return True, ""
        except (ValueError, TypeError):
            return False, "BMI must be a valid number"
    
    @staticmethod
    def validate_bp(value):
        """Validate blood pressure (mmHg)"""
        try:
            bp = float(value)
            if bp < 40 or bp > 250:
                return False, "Blood pressure must be between 40-250 mmHg"
            return True, ""
        except (ValueError, TypeError):
            return False, "Blood pressure must be a valid number"
    
    @staticmethod
    def validate_all(patient_data):
        """Validate all patient data"""
        validators = {
            'name': PatientDataValidator.validate_name,
            'age': PatientDataValidator.validate_age,
            'blood_sugar': PatientDataValidator.validate_blood_sugar,
            'bmi': PatientDataValidator.validate_bmi,
            'bp': PatientDataValidator.validate_bp
        }
        
        errors = {}
        for field, validator in validators.items():
            is_valid, error_msg = validator(patient_data.get(field, ''))
            if not is_valid:
                errors[field] = error_msg
        
        return len(errors) == 0, errors
