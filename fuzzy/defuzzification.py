"""
Defuzzification - Convert fuzzy outputs to crisp values
Implements Centroid and other defuzzification methods
"""
import numpy as np

class Defuzzification:
    """Defuzzification methods for converting fuzzy outputs to crisp values"""
    
    @staticmethod
    def centroid_method(fuzzy_output, output_range=(0, 100)):
        """
        Centroid (Center of Mass) defuzzification method
        Commonly used for medical decision support
        
        Args:
            fuzzy_output: Dict with 'low', 'medium', 'high' membership values
            output_range: Tuple (min, max) for output value
        
        Returns:
            Float crisp value between min and max
        """
        # Define the peak values for each output category
        low_peak = output_range[0] + (output_range[1] - output_range[0]) * 0.2
        medium_peak = (output_range[0] + output_range[1]) / 2
        high_peak = output_range[0] + (output_range[1] - output_range[0]) * 0.8
        
        low_strength = max(fuzzy_output.get('low', 0))
        medium_strength = max(fuzzy_output.get('medium', 0))
        high_strength = max(fuzzy_output.get('high', 0))
        
        numerator = (low_strength * low_peak) + (medium_strength * medium_peak) + (high_strength * high_peak)
        denominator = low_strength + medium_strength + high_strength
        
        if denominator == 0:
            return 50.0  # Default to medium if no rules fire
        
        crisp_value = numerator / denominator
        return np.clip(crisp_value, output_range[0], output_range[1])
    
    @staticmethod
    def weighted_average_method(fuzzy_output, output_range=(0, 100)):
        """
        Weighted Average defuzzification method
        
        Args:
            fuzzy_output: Dict with 'low', 'medium', 'high' membership values
            output_range: Tuple (min, max) for output value
        
        Returns:
            Float crisp value between min and max
        """
        low_strength = max(fuzzy_output.get('low', 0))
        medium_strength = max(fuzzy_output.get('medium', 0))
        high_strength = max(fuzzy_output.get('high', 0))
        
        total_strength = low_strength + medium_strength + high_strength
        
        if total_strength == 0:
            return 50.0  # Default to medium if no rules fire
        
        # Normalize strengths
        low_weight = low_strength / total_strength
        medium_weight = medium_strength / total_strength
        high_weight = high_strength / total_strength
        
        # Calculate weighted risk score (0-100)
        risk_score = (low_weight * 20) + (medium_weight * 50) + (high_weight * 80)
        
        return np.clip(risk_score, output_range[0], output_range[1])
    
    @staticmethod
    def max_membership_method(fuzzy_output, output_range=(0, 100)):
        """
        Maximum Membership defuzzification
        Selects the output corresponding to maximum membership
        
        Args:
            fuzzy_output: Dict with 'low', 'medium', 'high' membership values
            output_range: Tuple (min, max) for output value
        
        Returns:
            Float crisp value representing the category with highest membership
        """
        max_membership = 0
        selected_category = 'low'
        
        for category in ['low', 'medium', 'high']:
            category_max = max(fuzzy_output.get(category, [0]))
            if category_max > max_membership:
                max_membership = category_max
                selected_category = category
        
        # Map category to output value
        category_map = {
            'low': output_range[0] + (output_range[1] - output_range[0]) * 0.2,
            'medium': (output_range[0] + output_range[1]) / 2,
            'high': output_range[0] + (output_range[1] - output_range[0]) * 0.8
        }
        
        return category_map[selected_category]
    
    @staticmethod
    def defuzzify(fuzzy_output, method='centroid', output_range=(0, 100)):
        """
        Main defuzzification interface
        
        Args:
            fuzzy_output: Dict with 'low', 'medium', 'high' membership values
            method: 'centroid', 'weighted_average', or 'max_membership'
            output_range: Tuple (min, max) for output value
        
        Returns:
            Float crisp value
        """
        if method == 'centroid':
            return Defuzzification.centroid_method(fuzzy_output, output_range)
        elif method == 'weighted_average':
            return Defuzzification.weighted_average_method(fuzzy_output, output_range)
        elif method == 'max_membership':
            return Defuzzification.max_membership_method(fuzzy_output, output_range)
        else:
            return Defuzzification.centroid_method(fuzzy_output, output_range)
