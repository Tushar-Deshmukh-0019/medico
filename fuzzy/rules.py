"""
Fuzzy Rules for Diabetes Risk Assessment
Implements a comprehensive set of fuzzy rules based on medical knowledge
"""

class FuzzyRules:
    """Medical fuzzy rules for diabetes risk assessment"""
    
    @staticmethod
    def evaluate_rules(fuzzified_inputs):
        """
        Evaluate all fuzzy rules and return aggregated outputs
        
        Args:
            fuzzified_inputs: Dict with fuzzified blood_sugar, bmi, age, bp
        
        Returns:
            Dict with rule outputs for low, medium, high risk
        """
        rules_output = {
            'low': [],
            'medium': [],
            'high': []
        }
        
        bs = fuzzified_inputs['blood_sugar']
        bmi = fuzzified_inputs['bmi']
        age = fuzzified_inputs['age']
        bp = fuzzified_inputs['bp']
        
        # Rule 1: Normal blood sugar + Normal BMI + Young age → Low Risk
        rule_1 = min(bs['normal'], bmi['normal'], age['young'])
        rules_output['low'].append(rule_1)
        
        # Rule 2: Normal blood sugar + Normal BMI → Low Risk
        rule_2 = min(bs['normal'], bmi['normal'])
        rules_output['low'].append(rule_2)
        
        # Rule 3: Slightly High blood sugar + Normal BMI + Young age → Low Risk
        rule_3 = min(bs['slightly_high'], bmi['normal'], age['young'])
        rules_output['low'].append(rule_3)
        
        # Rule 4: Normal blood sugar + Overweight → Medium Risk
        rule_4 = min(bs['normal'], bmi['overweight'])
        rules_output['medium'].append(rule_4)
        
        # Rule 5: Slightly High blood sugar + Normal BMI + Middle age → Medium Risk
        rule_5 = min(bs['slightly_high'], bmi['normal'], age['middle'])
        rules_output['medium'].append(rule_5)
        
        # Rule 6: Slightly High blood sugar + Overweight → Medium Risk
        rule_6 = min(bs['slightly_high'], bmi['overweight'])
        rules_output['medium'].append(rule_6)
        
        # Rule 7: High blood sugar + Normal BMI + Young age → Medium Risk
        rule_7 = min(bs['high'], bmi['normal'], age['young'])
        rules_output['medium'].append(rule_7)
        
        # Rule 8: High blood sugar + Overweight + Middle age → Medium Risk
        rule_8 = min(bs['high'], bmi['overweight'], age['middle'])
        rules_output['medium'].append(rule_8)
        
        # Rule 9: Normal blood sugar + Obese + Old age → Medium Risk
        rule_9 = min(bs['normal'], bmi['obese'], age['old'])
        rules_output['medium'].append(rule_9)
        
        # Rule 10: Slightly High blood sugar + Overweight + Old age → Medium Risk
        rule_10 = min(bs['slightly_high'], bmi['overweight'], age['old'])
        rules_output['medium'].append(rule_10)
        
        # Rule 11: High blood sugar + Normal BMI → High Risk
        rule_11 = min(bs['high'], bmi['normal'])
        rules_output['high'].append(rule_11)
        
        # Rule 12: Very High blood sugar + Any BMI → High Risk
        rule_12 = bs['very_high']
        rules_output['high'].append(rule_12)
        
        # Rule 13: High blood sugar + Overweight → High Risk
        rule_13 = min(bs['high'], bmi['overweight'])
        rules_output['high'].append(rule_13)
        
        # Rule 14: High blood sugar + Obese → High Risk
        rule_14 = min(bs['high'], bmi['obese'])
        rules_output['high'].append(rule_14)
        
        # Rule 15: Slightly High blood sugar + Obese + Old age → High Risk
        rule_15 = min(bs['slightly_high'], bmi['obese'], age['old'])
        rules_output['high'].append(rule_15)
        
        # Rule 16: Normal blood sugar + Obese + High BP → High Risk
        rule_16 = min(bs['normal'], bmi['obese'], bp['high'])
        rules_output['high'].append(rule_16)
        
        # Rule 17: Very High blood sugar + Obese → Very High Risk
        rule_17 = min(bs['very_high'], bmi['obese'])
        rules_output['high'].append(rule_17)
        
        # Rule 18: Very High blood sugar + High BP → Very High Risk
        rule_18 = min(bs['very_high'], bp['high'])
        rules_output['high'].append(rule_18)
        
        # Rule 19: High blood sugar + Obese + Old age + High BP → Very High Risk
        rule_19 = min(bs['high'], bmi['obese'], age['old'], bp['high'])
        rules_output['high'].append(rule_19)
        
        # Rule 20: Elevated BP + High blood sugar + Overweight → High Risk
        rule_20 = min(bp['elevated'], bs['high'], bmi['overweight'])
        rules_output['high'].append(rule_20)
        
        # Rule 21: Slightly High blood sugar + Obese → Medium Risk
        rule_21 = min(bs['slightly_high'], bmi['obese'])
        rules_output['medium'].append(rule_21)
        
        # Rule 22: High blood sugar + Elevated BP + Middle age → High Risk
        rule_22 = min(bs['high'], bp['elevated'], age['middle'])
        rules_output['high'].append(rule_22)
        
        # Rule 23: Slightly High blood sugar + High BP + Old age → Medium Risk
        rule_23 = min(bs['slightly_high'], bp['high'], age['old'])
        rules_output['medium'].append(rule_23)
        
        # Rule 24: Normal blood sugar + High BP + Old age → Medium Risk
        rule_24 = min(bs['normal'], bp['high'], age['old'])
        rules_output['medium'].append(rule_24)
        
        # Rule 25: Very High blood sugar + High BP + Obese → High Risk
        rule_25 = min(bs['very_high'], bp['high'], bmi['obese'])
        rules_output['high'].append(rule_25)
        
        return rules_output
    
    @staticmethod
    def get_risk_category(risk_score):
        """
        Categorize risk based on score
        
        Args:
            risk_score: Float between 0-100
        
        Returns:
            Tuple of (category, description)
        """
        if risk_score < 30:
            return 'low', 'Low Risk'
        elif risk_score < 60:
            return 'medium', 'Medium Risk'
        else:
            return 'high', 'High Risk'
    
    @staticmethod
    def get_recommendations(risk_category, risk_score, patient_data):
        """
        Generate clinical recommendations based on risk category
        
        Args:
            risk_category: 'low', 'medium', or 'high'
            risk_score: Float between 0-100
            patient_data: Dict with blood_sugar, bmi, age, bp
        
        Returns:
            List of recommendation strings
        """
        recommendations = []
        
        if risk_category == 'low':
            recommendations.append('✓ Low diabetes risk detected')
            recommendations.append('• Maintain current lifestyle habits')
            recommendations.append('• Continue regular physical activity (150 min/week)')
            recommendations.append('• Balanced diet with fiber-rich foods')
            recommendations.append('• Annual health check-ups recommended')
        
        elif risk_category == 'medium':
            recommendations.append('⚠ Medium diabetes risk detected')
            recommendations.append('• Schedule appointment with primary care physician')
            recommendations.append('• Fasting blood glucose test recommended')
            recommendations.append('• HbA1c test recommended (screens last 3 months)')
            recommendations.append('• Increase physical activity to 30 min daily')
            recommendations.append('• Reduce sugar and refined carbohydrate intake')
            recommendations.append('• Weight management program recommended')
            recommendations.append('• Monitor blood pressure regularly')
        
        else:  # High risk
            recommendations.append('🔴 High diabetes risk detected')
            recommendations.append('• Urgent: Consult an endocrinologist or internist')
            recommendations.append('• Comprehensive metabolic panel required')
            recommendations.append('• HbA1c test (urgent)')
            recommendations.append('• Oral glucose tolerance test (OGTT) recommended')
            recommendations.append('• Structured weight loss program (5-10% target)')
            recommendations.append('• Diabetes prevention program enrollment suggested')
            recommendations.append('• Intensive lifestyle modification needed')
            recommendations.append('• Regular monitoring (every 3-6 months)')
            recommendations.append('• Family history screening recommended')
        
        # Additional specific recommendations based on patient data
        if patient_data.get('blood_sugar', 0) > 180:
            recommendations.append('• Blood sugar levels are significantly elevated - immediate medical attention needed')
        
        if patient_data.get('bmi', 0) > 30:
            recommendations.append('• BMI indicates obesity - weight management is critical')
        
        if patient_data.get('bp', 0) > 140:
            recommendations.append('• Blood pressure is elevated - may indicate hypertension')
        
        if patient_data.get('age', 0) > 60:
            recommendations.append('• Age is a risk factor - more frequent monitoring needed')
        
        return recommendations
