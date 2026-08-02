"""
Database Query Functions
Handles all database operations for assessments and patients
"""
from datetime import datetime
from .connection import db, commit_changes, rollback_changes
from sqlalchemy import func

class Patient(db.Model):
    """Patient model for database"""
    __tablename__ = 'patients'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=True)
    phone = db.Column(db.String(20), nullable=True)
    date_of_birth = db.Column(db.Date, nullable=True)
    gender = db.Column(db.String(10), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)
    
    # Relationships
    assessments = db.relationship('Assessment', backref='patient', lazy=True, cascade='all, delete-orphan')
    
    def to_dict(self):
        """Convert to dictionary"""
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'phone': self.phone,
            'date_of_birth': self.date_of_birth.isoformat() if self.date_of_birth else None,
            'gender': self.gender,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        }

class Assessment(db.Model):
    """Assessment model for storing diabetes risk assessments"""
    __tablename__ = 'assessments'
    
    id = db.Column(db.Integer, primary_key=True)
    patient_id = db.Column(db.Integer, db.ForeignKey('patients.id'), nullable=False)
    
    # Patient measurements
    blood_sugar = db.Column(db.Float, nullable=False)
    bmi = db.Column(db.Float, nullable=False)
    age = db.Column(db.Integer, nullable=False)
    blood_pressure = db.Column(db.Float, nullable=False)
    
    # Assessment results
    risk_score = db.Column(db.Float, nullable=False)
    risk_category = db.Column(db.String(20), nullable=False)  # low, medium, high
    
    # Additional metrics
    blood_sugar_status = db.Column(db.String(50), nullable=True)
    bmi_category = db.Column(db.String(50), nullable=True)
    bp_category = db.Column(db.String(50), nullable=True)
    
    # Notes and recommendations
    clinical_notes = db.Column(db.Text, nullable=True)
    recommendations = db.Column(db.Text, nullable=True)  # JSON serialized
    
    # Metadata
    assessment_date = db.Column(db.DateTime, default=datetime.now)
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)
    
    def to_dict(self):
        """Convert to dictionary"""
        return {
            'id': self.id,
            'patient_id': self.patient_id,
            'blood_sugar': self.blood_sugar,
            'bmi': self.bmi,
            'age': self.age,
            'blood_pressure': self.blood_pressure,
            'risk_score': self.risk_score,
            'risk_category': self.risk_category,
            'blood_sugar_status': self.blood_sugar_status,
            'bmi_category': self.bmi_category,
            'bp_category': self.bp_category,
            'clinical_notes': self.clinical_notes,
            'recommendations': self.recommendations,
            'assessment_date': self.assessment_date.isoformat(),
            'created_at': self.created_at.isoformat()
        }

# Patient Query Functions

def create_patient(name, email=None, phone=None, date_of_birth=None, gender=None):
    """Create a new patient"""
    patient = Patient(
        name=name,
        email=email,
        phone=phone,
        date_of_birth=date_of_birth,
        gender=gender
    )
    db.session.add(patient)
    
    if commit_changes():
        return patient
    return None

def get_patient(patient_id):
    """Get patient by ID"""
    return Patient.query.get(patient_id)

def get_patient_by_email(email):
    """Get patient by email"""
    return Patient.query.filter_by(email=email).first()

def get_all_patients():
    """Get all patients"""
    return Patient.query.all()

def update_patient(patient_id, **kwargs):
    """Update patient information"""
    patient = get_patient(patient_id)
    if patient:
        for key, value in kwargs.items():
            if hasattr(patient, key):
                setattr(patient, key, value)
        patient.updated_at = datetime.now()
        
        if commit_changes():
            return patient
    
    return None

def delete_patient(patient_id):
    """Delete patient and all related assessments"""
    patient = get_patient(patient_id)
    if patient:
        db.session.delete(patient)
        return commit_changes()
    return False

# Assessment Query Functions

def create_assessment(patient_id, blood_sugar, bmi, age, blood_pressure, 
                     risk_score, risk_category, blood_sugar_status=None,
                     bmi_category=None, bp_category=None, clinical_notes=None,
                     recommendations=None):
    """Create a new assessment"""
    assessment = Assessment(
        patient_id=patient_id,
        blood_sugar=blood_sugar,
        bmi=bmi,
        age=age,
        blood_pressure=blood_pressure,
        risk_score=risk_score,
        risk_category=risk_category,
        blood_sugar_status=blood_sugar_status,
        bmi_category=bmi_category,
        bp_category=bp_category,
        clinical_notes=clinical_notes,
        recommendations=recommendations
    )
    db.session.add(assessment)
    
    if commit_changes():
        return assessment
    return None

def get_assessment(assessment_id):
    """Get assessment by ID"""
    return Assessment.query.get(assessment_id)

def get_patient_assessments(patient_id):
    """Get all assessments for a patient"""
    return Assessment.query.filter_by(patient_id=patient_id).order_by(
        Assessment.assessment_date.desc()
    ).all()

def get_latest_assessment(patient_id):
    """Get latest assessment for a patient"""
    return Assessment.query.filter_by(patient_id=patient_id).order_by(
        Assessment.assessment_date.desc()
    ).first()

def get_all_assessments():
    """Get all assessments"""
    return Assessment.query.order_by(Assessment.assessment_date.desc()).all()

def update_assessment(assessment_id, **kwargs):
    """Update assessment"""
    assessment = get_assessment(assessment_id)
    if assessment:
        for key, value in kwargs.items():
            if hasattr(assessment, key):
                setattr(assessment, key, value)
        assessment.updated_at = datetime.now()
        
        if commit_changes():
            return assessment
    
    return None

def delete_assessment(assessment_id):
    """Delete assessment"""
    assessment = get_assessment(assessment_id)
    if assessment:
        db.session.delete(assessment)
        return commit_changes()
    return False

# Analytics Functions

def get_risk_statistics():
    """Get risk distribution statistics"""
    total = Assessment.query.count()
    
    if total == 0:
        return {
            'total': 0,
            'low': 0,
            'medium': 0,
            'high': 0,
            'low_percent': 0,
            'medium_percent': 0,
            'high_percent': 0
        }
    
    low_count = Assessment.query.filter_by(risk_category='low').count()
    medium_count = Assessment.query.filter_by(risk_category='medium').count()
    high_count = Assessment.query.filter_by(risk_category='high').count()
    
    return {
        'total': total,
        'low': low_count,
        'medium': medium_count,
        'high': high_count,
        'low_percent': round((low_count / total) * 100, 2),
        'medium_percent': round((medium_count / total) * 100, 2),
        'high_percent': round((high_count / total) * 100, 2)
    }

def get_average_risk_score():
    """Get average risk score"""
    result = db.session.query(func.avg(Assessment.risk_score)).scalar()
    return round(result, 2) if result else 0

def get_assessment_count():
    """Get total number of assessments"""
    return Assessment.query.count()

def get_patient_count():
    """Get total number of patients"""
    return Patient.query.count()

def get_recent_assessments(limit=10):
    """Get recent assessments"""
    return Assessment.query.order_by(Assessment.assessment_date.desc()).limit(limit).all()

def search_patients(search_term):
    """Search patients by name or email"""
    return Patient.query.filter(
        db.or_(
            Patient.name.ilike(f'%{search_term}%'),
            Patient.email.ilike(f'%{search_term}%')
        )
    ).all()

def get_assessments_by_date_range(start_date, end_date):
    """Get assessments within date range"""
    return Assessment.query.filter(
        Assessment.assessment_date.between(start_date, end_date)
    ).order_by(Assessment.assessment_date.desc()).all()

def get_high_risk_patients():
    """Get patients with high risk assessments"""
    high_risk_assessments = Assessment.query.filter_by(risk_category='high').all()
    return list(set([a.patient for a in high_risk_assessments]))
