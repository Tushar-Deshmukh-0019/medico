"""
Helper Functions
"""
import json
from datetime import datetime

def calculate_bmi(height_cm, weight_kg):
    """
    Calculate BMI from height and weight
    
    Args:
        height_cm: Height in centimeters
        weight_kg: Weight in kilograms
    
    Returns:
        BMI value rounded to 2 decimal places
    """
    if height_cm <= 0 or weight_kg <= 0:
        return None
    
    height_m = height_cm / 100
    bmi = weight_kg / (height_m ** 2)
    return round(bmi, 2)


def get_bmi_category(bmi):
    """
    Get BMI category
    
    Args:
        bmi: BMI value
    
    Returns:
        Category string
    """
    if bmi < 18.5:
        return 'Underweight'
    elif bmi < 25:
        return 'Normal Weight'
    elif bmi < 30:
        return 'Overweight'
    else:
        return 'Obese'


def get_bp_category(systolic):
    """
    Get blood pressure category
    
    Args:
        systolic: Systolic pressure value
    
    Returns:
        Category string
    """
    if systolic < 120:
        return 'Normal'
    elif systolic < 130:
        return 'Elevated'
    elif systolic < 140:
        return 'High BP Stage 1'
    else:
        return 'High BP Stage 2'


def format_timestamp(dt=None):
    """
    Format timestamp for display
    
    Args:
        dt: datetime object (defaults to now)
    
    Returns:
        Formatted timestamp string
    """
    if dt is None:
        dt = datetime.now()
    
    return dt.strftime('%Y-%m-%d %H:%M:%S')


def format_risk_report(assessment_result):
    """
    Format assessment result for display
    
    Args:
        assessment_result: Dict with assessment results
    
    Returns:
        Formatted report string
    """
    report = f"""
    {'='*60}
    DIABETES RISK ASSESSMENT REPORT
    {'='*60}
    
    Patient: {assessment_result.get('patient_data', {}).get('name', 'N/A')}
    Assessment Date: {format_timestamp()}
    
    {'─'*60}
    INPUT DATA
    {'─'*60}
    Blood Sugar: {assessment_result.get('patient_data', {}).get('blood_sugar', 0)} mg/dL
    BMI: {assessment_result.get('patient_data', {}).get('bmi', 0)} kg/m²
    Age: {assessment_result.get('patient_data', {}).get('age', 0)} years
    Blood Pressure: {assessment_result.get('patient_data', {}).get('bp', 0)} mmHg
    
    {'─'*60}
    RISK ASSESSMENT
    {'─'*60}
    Risk Score: {assessment_result.get('risk_percentage', '0%')}
    Risk Category: {assessment_result.get('risk_label', 'N/A')}
    
    {'─'*60}
    RECOMMENDATIONS
    {'─'*60}
    """
    
    for i, rec in enumerate(assessment_result.get('recommendations', []), 1):
        report += f"{i}. {rec}\n"
    
    report += f"{'='*60}\n"
    
    return report


def get_color_for_risk(risk_score):
    """
    Get color code for risk visualization
    
    Args:
        risk_score: Risk score (0-100)
    
    Returns:
        Color code (hex or CSS color)
    """
    if risk_score < 30:
        return '#4CAF50'  # Green
    elif risk_score < 60:
        return '#FFC107'  # Amber
    else:
        return '#F44336'  # Red


def get_emoji_for_risk(risk_category):
    """
    Get emoji for risk category
    
    Args:
        risk_category: 'low', 'medium', or 'high'
    
    Returns:
        Emoji string
    """
    emoji_map = {
        'low': '✓',
        'medium': '⚠',
        'high': '🔴'
    }
    return emoji_map.get(risk_category, '•')


def calculate_health_metrics(blood_sugar, bmi, bp, age):
    """
    Calculate additional health metrics for display
    
    Args:
        blood_sugar: Blood sugar level
        bmi: BMI value
        bp: Blood pressure
        age: Age in years
    
    Returns:
        Dict with calculated metrics
    """
    return {
        'bmi_category': get_bmi_category(bmi),
        'bp_category': get_bp_category(bp),
        'blood_sugar_status': 'High' if blood_sugar > 126 else 'Normal' if blood_sugar < 100 else 'Slightly High',
        'age_group': 'Senior' if age >= 60 else 'Middle-Aged' if age >= 40 else 'Young Adult'
    }


def generate_json_response(status, data=None, error=None):
    """
    Generate standardized JSON response
    
    Args:
        status: 'success' or 'error'
        data: Response data
        error: Error message
    
    Returns:
        Dict for JSON serialization
    """
    return {
        'status': status,
        'data': data or {},
        'error': error,
        'timestamp': format_timestamp()
    }
