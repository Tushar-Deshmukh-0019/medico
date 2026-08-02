"""
Fuzzy Inference Module
Handles the inference logic and rule evaluation
"""
import numpy as np

class FuzzyInference:
    """Fuzzy inference operations"""
    
    @staticmethod
    def and_operation(values):
        """
        AND operation in fuzzy logic (minimum)
        
        Args:
            values: List of membership values
        
        Returns:
            Minimum value
        """
        if not values:
            return 0
        return min(values)
    
    @staticmethod
    def or_operation(values):
        """
        OR operation in fuzzy logic (maximum)
        
        Args:
            values: List of membership values
        
        Returns:
            Maximum value
        """
        if not values:
            return 0
        return max(values)
    
    @staticmethod
    def not_operation(value):
        """
        NOT operation in fuzzy logic (complement)
        
        Args:
            value: Membership value
        
        Returns:
            Complement value (1 - value)
        """
        return 1 - value
    
    @staticmethod
    def implication(antecedent, consequent):
        """
        Implication in fuzzy logic (Mamdani: minimum)
        
        Args:
            antecedent: Antecedent membership value
            consequent: Consequent membership value
        
        Returns:
            Minimum of antecedent and consequent
        """
        return min(antecedent, consequent)
    
    @staticmethod
    def aggregation(rule_outputs):
        """
        Aggregate multiple rule outputs (maximum)
        
        Args:
            rule_outputs: List of rule output membership values
        
        Returns:
            Maximum membership value
        """
        if not rule_outputs:
            return 0
        return max(rule_outputs)
    
    @staticmethod
    def evaluate_fuzzy_proposition(fuzzy_dict, propositions):
        """
        Evaluate a fuzzy proposition like "is high" or "is low"
        
        Args:
            fuzzy_dict: Dictionary of membership values {category: value}
            propositions: List of proposition names to extract
        
        Returns:
            Combined membership value
        """
        values = [fuzzy_dict.get(prop, 0) for prop in propositions]
        return FuzzyInference.or_operation(values)
    
    @staticmethod
    def hedge_very(membership_value):
        """
        Linguistic hedge 'very' - concentrates membership
        Formula: value^2
        
        Args:
            membership_value: Original membership value
        
        Returns:
            Concentrated membership value
        """
        return membership_value ** 2
    
    @staticmethod
    def hedge_somewhat(membership_value):
        """
        Linguistic hedge 'somewhat' - dilutes membership
        Formula: sqrt(value)
        
        Args:
            membership_value: Original membership value
        
        Returns:
            Diluted membership value
        """
        return np.sqrt(membership_value)
    
    @staticmethod
    def hedge_not_very(membership_value):
        """
        Linguistic hedge 'not very' - negates and concentrates
        Formula: (1 - value)^2
        
        Args:
            membership_value: Original membership value
        
        Returns:
            Not very membership value
        """
        return FuzzyInference.hedge_very(FuzzyInference.not_operation(membership_value))
    
    @staticmethod
    def similarity_measure(fuzzy_set1, fuzzy_set2):
        """
        Calculate similarity between two fuzzy sets
        Uses Jaccard similarity
        
        Args:
            fuzzy_set1: Dict of membership values
            fuzzy_set2: Dict of membership values
        
        Returns:
            Similarity measure between 0 and 1
        """
        if not fuzzy_set1 or not fuzzy_set2:
            return 0
        
        all_keys = set(fuzzy_set1.keys()) | set(fuzzy_set2.keys())
        
        min_sum = sum(min(fuzzy_set1.get(k, 0), fuzzy_set2.get(k, 0)) for k in all_keys)
        max_sum = sum(max(fuzzy_set1.get(k, 0), fuzzy_set2.get(k, 0)) for k in all_keys)
        
        if max_sum == 0:
            return 0
        
        return min_sum / max_sum
