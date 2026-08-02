#!/usr/bin/env python
"""
Test script for the Fuzzy Logic Medical Decision Support System
"""

from fuzzy.engine import FuzzyEngine
from utils.validators import PatientDataValidator

def test_fuzzy_engine():
    """Test the fuzzy engine with sample data"""
    print("=" * 60)
    print("FUZZY LOGIC MEDICAL DECISION SUPPORT SYSTEM - TEST")
    print("=" * 60)
    
    # Initialize the engine
    engine = FuzzyEngine()
    print("\n✓ Fuzzy Engine initialized successfully")
    
    # Get system info
    sys_info = engine.get_system_info()
    print(f"\n📊 System Information:")
    print(f"  - System: {sys_info['system_name']}")
    print(f"  - Version: {sys_info['version']}")
    print(f"  - Inference Method: {sys_info['inference_method']}")
    print(f"  - Total Rules: {sys_info['total_rules']}")
    
    # Test cases
    test_cases = [
        {
            'name': 'Low Risk Patient',
            'data': {'blood_sugar': 95, 'bmi': 23, 'age': 30, 'bp': 115}
        },
        {
            'name': 'Medium Risk Patient',
            'data': {'blood_sugar': 130, 'bmi': 28, 'age': 45, 'bp': 130}
        },
        {
            'name': 'High Risk Patient',
            'data': {'blood_sugar': 200, 'bmi': 34, 'age': 60, 'bp': 150}
        }
    ]
    
    print("\n" + "=" * 60)
    print("TEST CASES")
    print("=" * 60)
    
    for i, test in enumerate(test_cases, 1):
        print(f"\n[Test {i}] {test['name']}")
        print("-" * 60)
        
        patient_data = test['data']
        
        # Validate input
        is_valid, errors = engine.validate_inputs(patient_data)
        if not is_valid:
            print(f"✗ Validation failed: {errors}")
            continue
        
        # Perform assessment
        result = engine.assess_diabetes_risk(patient_data)
        
        if result['status'] == 'success':
            print(f"✓ Assessment successful")
            print(f"  Input Data:")
            print(f"    - Blood Sugar: {patient_data['blood_sugar']} mg/dL")
            print(f"    - BMI: {patient_data['bmi']} kg/m²")
            print(f"    - Age: {patient_data['age']} years")
            print(f"    - BP: {patient_data['bp']} mmHg")
            print(f"\n  Results:")
            print(f"    - Risk Score: {result['risk_score']}%")
            print(f"    - Risk Category: {result['risk_label']}")
            print(f"    - Rules Fired: {result['rules_fired']}")
            print(f"\n  Recommendations (first 3):")
            for j, rec in enumerate(result['recommendations'][:3], 1):
                print(f"    {j}. {rec}")
        else:
            print(f"✗ Assessment failed: {result.get('message', 'Unknown error')}")
    
    # Test input validation
    print("\n" + "=" * 60)
    print("INPUT VALIDATION TESTS")
    print("=" * 60)
    
    invalid_inputs = [
        {'name': 'Invalid - High Blood Sugar', 'data': {'name': 'Test', 'age': 45, 'blood_sugar': 700, 'bmi': 25, 'bp': 120}},
        {'name': 'Invalid - High BMI', 'data': {'name': 'Test', 'age': 45, 'blood_sugar': 100, 'bmi': 80, 'bp': 120}},
        {'name': 'Invalid - Age Out of Range', 'data': {'name': 'Test', 'age': 150, 'blood_sugar': 100, 'bmi': 25, 'bp': 120}},
    ]
    
    for test in invalid_inputs:
        print(f"\n[Validation] {test['name']}")
        is_valid, errors = PatientDataValidator.validate_all(test['data'])
        if is_valid:
            print(f"✓ Valid")
        else:
            print(f"✗ Invalid - Errors: {errors}")
    
    print("\n" + "=" * 60)
    print("✓ ALL TESTS COMPLETED")
    print("=" * 60)

if __name__ == '__main__':
    test_fuzzy_engine()
