"""
Fuzzy Inference Engine - Main orchestration for fuzzy logic operations
Implements the Mamdani Fuzzy Inference System
"""
from .membership import DiabetesFuzzySets
from .rules import FuzzyRules
from .defuzzification import Defuzzification
from .inference import FuzzyInference

class FuzzyEngine:
    """Main fuzzy inference engine for diabetes risk assessment"""
    
    def __init__(self):
        self.fuzzification_engine = DiabetesFuzzySets()
        self.rule_engine = FuzzyRules()
        self.defuzzification_engine = Defuzzification()
        self.inference_engine = FuzzyInference()
    
    def assess_diabetes_risk(self, patient_data):
        """
        Complete fuzzy inference pipeline for diabetes risk assessment
        
        Args:
            patient_data: Dict with 'blood_sugar', 'bmi', 'age', 'bp'
        
        Returns:
            Dict with risk_score, risk_category, recommendations, and details
        """
        try:
            # Step 1: Fuzzification
            fuzzified_inputs = self._fuzzify_inputs(patient_data)
            
            # Step 2: Rule Evaluation
            rules_output = self.rule_engine.evaluate_rules(fuzzified_inputs)
            
            # Step 3: Defuzzification
            risk_score = self.defuzzification_engine.defuzzify(
                rules_output,
                method='centroid',
                output_range=(0, 100)
            )
            
            # Step 4: Risk Categorization
            risk_category, risk_label = self.rule_engine.get_risk_category(risk_score)
            
            # Step 5: Generate Recommendations
            recommendations = self.rule_engine.get_recommendations(
                risk_category,
                risk_score,
                patient_data
            )
            
            # Step 6: Prepare detailed output
            result = {
                'risk_score': round(risk_score, 2),
                'risk_category': risk_category,
                'risk_label': risk_label,
                'risk_percentage': f"{round(risk_score)}%",
                'recommendations': recommendations,
                'fuzzified_inputs': self._format_fuzzified_for_display(fuzzified_inputs),
                'rules_fired': self._count_fired_rules(rules_output),
                'patient_data': patient_data,
                'status': 'success'
            }
            
            return result
        
        except Exception as e:
            return {
                'status': 'error',
                'message': str(e),
                'risk_score': 0,
                'recommendations': ['Error processing patient data']
            }
    
    def _fuzzify_inputs(self, patient_data):
        """Convert crisp inputs to fuzzy membership values"""
        return {
            'blood_sugar': DiabetesFuzzySets.fuzzify_blood_sugar(patient_data.get('blood_sugar', 100)),
            'bmi': DiabetesFuzzySets.fuzzify_bmi(patient_data.get('bmi', 25)),
            'age': DiabetesFuzzySets.fuzzify_age(patient_data.get('age', 40)),
            'bp': DiabetesFuzzySets.fuzzify_bp(patient_data.get('bp', 120))
        }
    
    def _format_fuzzified_for_display(self, fuzzified_inputs):
        """Format fuzzified values for display"""
        return {
            'blood_sugar': {k: round(v, 3) for k, v in fuzzified_inputs['blood_sugar'].items()},
            'bmi': {k: round(v, 3) for k, v in fuzzified_inputs['bmi'].items()},
            'age': {k: round(v, 3) for k, v in fuzzified_inputs['age'].items()},
            'bp': {k: round(v, 3) for k, v in fuzzified_inputs['bp'].items()}
        }
    
    def _count_fired_rules(self, rules_output):
        """Count how many rules fired with meaningful strength"""
        count = 0
        for category in rules_output.values():
            for strength in category:
                if strength > 0.01:  # Threshold for meaningful firing
                    count += 1
        return count
    
    def validate_inputs(self, patient_data):
        """
        Validate patient data before assessment
        
        Args:
            patient_data: Dict with patient measurements
        
        Returns:
            Tuple (is_valid, error_messages)
        """
        errors = []
        
        blood_sugar = patient_data.get('blood_sugar')
        if blood_sugar is None or blood_sugar < 0 or blood_sugar > 600:
            errors.append('Blood sugar must be between 0-600 mg/dL')
        
        bmi = patient_data.get('bmi')
        if bmi is None or bmi < 10 or bmi > 60:
            errors.append('BMI must be between 10-60 kg/m²')
        
        age = patient_data.get('age')
        if age is None or age < 0 or age > 120:
            errors.append('Age must be between 0-120 years')
        
        bp = patient_data.get('bp')
        if bp is None or bp < 40 or bp > 250:
            errors.append('Blood pressure must be between 40-250 mmHg')
        
        return len(errors) == 0, errors
    
    def get_system_info(self):
        """Get information about the fuzzy system"""
        return {
            'system_name': 'Fuzzy Logic Diabetes Risk Assessment',
            'version': '1.0.0',
            'inference_method': 'Mamdani',
            'defuzzification_method': 'Centroid',
            'total_rules': 25,
            'input_variables': ['blood_sugar', 'bmi', 'age', 'blood_pressure'],
            'output_variable': 'diabetes_risk',
            'risk_categories': ['low', 'medium', 'high']
        }
