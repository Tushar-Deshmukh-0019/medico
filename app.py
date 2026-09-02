"""
Flask Application - Medical Decision Support System
"""
from flask import Flask, render_template, request, jsonify
import os
from config import config
from fuzzy import FuzzyEngine
from utils.validators import PatientDataValidator
from utils.helpers import generate_json_response, get_color_for_risk, calculate_health_metrics
from database.connection import init_db, db
from database.queries import (
    create_assessment, get_patient_assessments, create_patient,
    get_patient, get_all_assessments, get_risk_statistics,
    get_average_risk_score, get_recent_assessments, get_assessment_count,
    get_patient_count
)

def create_app(config_name='development'):
    """Application factory"""
    # Auto-detect production environment
    if os.environ.get('RENDER') or os.environ.get('FLASK_ENV') == 'production':
        config_name = 'production'
    
    app = Flask(__name__, 
                template_folder='templates',
                static_folder='static')
    
    app.config.from_object(config[config_name])
    
    # Initialize database
    init_db(app)
    
    # Create tables safely (don't crash if they already exist)
    with app.app_context():
        try:
            db.create_all()
            print("✓ Database tables created/verified successfully")
        except Exception as e:
            print(f"⚠️  Database tables might already exist: {str(e)[:100]}")
            # Don't crash on existing tables - this is normal on redeployment
    
    # Initialize fuzzy engine
    fuzzy_engine = FuzzyEngine()
    
    # Store in app context for routes
    app.fuzzy_engine = fuzzy_engine
    
    # Register routes
    @app.route('/')
    @app.route('/home')
    def home():
        """Home page"""
        return render_template('index.html')
    
    @app.route('/assessment')
    def assessment_page():
        """Assessment form page"""
        return render_template('patient_form.html')
    
    @app.route('/about')
    def about():
        """About page"""
        return render_template('about.html')
    
    @app.route('/history')
    def history():
        """Assessment history page"""
        return render_template('history.html')
    
    # API Routes
    @app.route('/api/assess', methods=['POST'])
    def api_assess():
        """API endpoint for diabetes risk assessment"""
        try:
            data = request.get_json()
            
            # Validate input
            is_valid, errors = PatientDataValidator.validate_all(data)
            if not is_valid:
                return jsonify(generate_json_response('error', error=errors)), 400
            
            # Prepare patient data
            patient_data = {
                'blood_sugar': float(data.get('blood_sugar', 100)),
                'bmi': float(data.get('bmi', 25)),
                'age': float(data.get('age', 40)),
                'bp': float(data.get('bp', 120))
            }
            
            # Validate using fuzzy engine
            is_valid, engine_errors = app.fuzzy_engine.validate_inputs(patient_data)
            if not is_valid:
                return jsonify(generate_json_response('error', error=engine_errors)), 400
            
            # Perform assessment
            result = app.fuzzy_engine.assess_diabetes_risk(patient_data)
            
            if result.get('status') == 'error':
                return jsonify(generate_json_response('error', error=result.get('message'))), 500
            
            # Enhance result with additional information
            result['color'] = get_color_for_risk(result['risk_score'])
            result['health_metrics'] = calculate_health_metrics(
                patient_data['blood_sugar'],
                patient_data['bmi'],
                patient_data['bp'],
                patient_data['age']
            )
            result['patient_name'] = data.get('name', 'Patient')
            
            # Save to database
            try:
                # Create or get patient
                patient = get_patient(data.get('patient_id')) if data.get('patient_id') else None
                if not patient:
                    patient = create_patient(result['patient_name'])
                
                if patient:
                    # Create assessment record
                    assessment = create_assessment(
                        patient_id=patient.id,
                        blood_sugar=patient_data['blood_sugar'],
                        bmi=patient_data['bmi'],
                        age=int(patient_data['age']),
                        blood_pressure=patient_data['bp'],
                        risk_score=result['risk_score'],
                        risk_category=result['risk_category'],
                        blood_sugar_status=result['health_metrics'].get('blood_sugar_status'),
                        bmi_category=result['health_metrics'].get('bmi_category'),
                        bp_category=result['health_metrics'].get('bp_category'),
                        recommendations=str(result.get('recommendations', []))
                    )
                    
                    if assessment:
                        result['assessment_id'] = assessment.id
                        result['patient_id'] = patient.id
            except Exception as db_error:
                print(f"Database error (non-critical): {db_error}")
                # Continue even if database save fails
            
            return jsonify(generate_json_response('success', data=result)), 200
        
        except Exception:
            return jsonify(generate_json_response('error', error='Internal server error')), 500
    
    @app.route('/api/system-info', methods=['GET'])
    def api_system_info():
        """Get fuzzy system information"""
        info = app.fuzzy_engine.get_system_info()
        
        # Add database stats
        try:
            info['database'] = {
                'total_assessments': get_assessment_count(),
                'total_patients': get_patient_count(),
                'average_risk_score': get_average_risk_score(),
                'risk_distribution': get_risk_statistics()
            }
        except:
            pass
        
        return jsonify(generate_json_response('success', data=info)), 200
    
    @app.route('/api/validate', methods=['POST'])
    def api_validate():
        """Validate patient input"""
        try:
            data = request.get_json()
            is_valid, errors = PatientDataValidator.validate_all(data)
            
            return jsonify(generate_json_response(
                'success',
                data={
                    'is_valid': is_valid,
                    'errors': errors
                }
            )), 200
        
        except Exception:
            return jsonify(generate_json_response('error', error='Internal server error')), 500
    
    @app.route('/api/health', methods=['GET'])
    def api_health():
        """Health check endpoint"""
        health_status = {
            'status': 'healthy',
            'fuzzy_engine': 'ready',
            'database': 'connected'
        }
        
        try:
            # Test database connection
            db.session.execute('SELECT 1')
        except:
            health_status['database'] = 'disconnected'
            health_status['status'] = 'degraded'
        
        return jsonify(generate_json_response('success', data=health_status)), 200
    
    # Error handlers
    @app.errorhandler(404)
    def not_found(error):
        return jsonify(generate_json_response('error', error='Resource not found')), 404
    
    @app.errorhandler(500)
    def server_error(error):
        return jsonify(generate_json_response('error', error='Internal server error')), 500
    
    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, host='127.0.0.1', port=5000)
