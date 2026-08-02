"""
Membership Functions for Fuzzy Sets
Defines triangular and trapezoidal membership functions
"""
import numpy as np

class MembershipFunction:
    """Base membership function class"""
    
    @staticmethod
    def triangular(x, a, b, c):
        """
        Triangular membership function
        a: left corner, b: peak, c: right corner
        """
        if x <= a or x >= c:
            return 0.0
        elif a < x <= b:
            return (x - a) / (b - a)
        else:
            return (c - x) / (c - b)
    
    @staticmethod
    def trapezoidal(x, a, b, c, d):
        """
        Trapezoidal membership function
        a: left corner, b: left peak, c: right peak, d: right corner
        """
        if x <= a or x >= d:
            return 0.0
        elif a < x <= b:
            return (x - a) / (b - a)
        elif b < x < c:
            return 1.0
        else:
            return (d - x) / (d - c)
    
    @staticmethod
    def gaussian(x, mean, sigma):
        """
        Gaussian membership function
        mean: center, sigma: standard deviation
        """
        return np.exp(-((x - mean) ** 2) / (2 * sigma ** 2))


class DiabetesFuzzySets:
    """Fuzzy sets for diabetes risk assessment"""
    
    # Blood Sugar (mg/dL)
    BLOOD_SUGAR_RANGES = {
        'normal': (70, 85, 100),           # Triangular
        'slightly_high': (90, 115, 130),   # Triangular
        'high': (120, 150, 180),           # Triangular
        'very_high': (170, 215, 250)       # Triangular
    }
    
    # BMI (kg/m²)
    BMI_RANGES = {
        'underweight': (0, 12, 18.5),      # Triangular
        'normal': (17, 22, 27),            # Triangular
        'overweight': (25, 28, 31),        # Triangular
        'obese': (30, 35, 45)              # Triangular
    }
    
    # Age (years)
    AGE_RANGES = {
        'young': (0, 20, 35),              # Triangular
        'middle': (30, 45, 60),            # Triangular
        'old': (55, 70, 100)               # Triangular
    }
    
    # Blood Pressure (mmHg) - Systolic
    BP_RANGES = {
        'normal': (60, 90, 120),           # Triangular
        'elevated': (110, 135, 160),       # Triangular
        'high': (150, 175, 200)            # Triangular
    }
    
    # Risk Output
    RISK_RANGES = {
        'low': (0, 15, 30),                # Triangular
        'medium': (20, 50, 80),            # Triangular
        'high': (70, 85, 100)              # Triangular
    }
    
    @staticmethod
    def fuzzify_blood_sugar(value):
        """Convert blood sugar value to fuzzy membership values"""
        return {
            'normal': MembershipFunction.triangular(value, *DiabetesFuzzySets.BLOOD_SUGAR_RANGES['normal']),
            'slightly_high': MembershipFunction.triangular(value, *DiabetesFuzzySets.BLOOD_SUGAR_RANGES['slightly_high']),
            'high': MembershipFunction.triangular(value, *DiabetesFuzzySets.BLOOD_SUGAR_RANGES['high']),
            'very_high': MembershipFunction.triangular(value, *DiabetesFuzzySets.BLOOD_SUGAR_RANGES['very_high'])
        }
    
    @staticmethod
    def fuzzify_bmi(value):
        """Convert BMI value to fuzzy membership values"""
        return {
            'underweight': MembershipFunction.triangular(value, *DiabetesFuzzySets.BMI_RANGES['underweight']),
            'normal': MembershipFunction.triangular(value, *DiabetesFuzzySets.BMI_RANGES['normal']),
            'overweight': MembershipFunction.triangular(value, *DiabetesFuzzySets.BMI_RANGES['overweight']),
            'obese': MembershipFunction.triangular(value, *DiabetesFuzzySets.BMI_RANGES['obese'])
        }
    
    @staticmethod
    def fuzzify_age(value):
        """Convert age value to fuzzy membership values"""
        return {
            'young': MembershipFunction.triangular(value, *DiabetesFuzzySets.AGE_RANGES['young']),
            'middle': MembershipFunction.triangular(value, *DiabetesFuzzySets.AGE_RANGES['middle']),
            'old': MembershipFunction.triangular(value, *DiabetesFuzzySets.AGE_RANGES['old'])
        }
    
    @staticmethod
    def fuzzify_bp(value):
        """Convert blood pressure value to fuzzy membership values"""
        return {
            'normal': MembershipFunction.triangular(value, *DiabetesFuzzySets.BP_RANGES['normal']),
            'elevated': MembershipFunction.triangular(value, *DiabetesFuzzySets.BP_RANGES['elevated']),
            'high': MembershipFunction.triangular(value, *DiabetesFuzzySets.BP_RANGES['high'])
        }
