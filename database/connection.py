"""
Database Connection Module
Handles database initialization and connection setup
Supports PostgreSQL, SQLite, and MySQL
"""
import os
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Initialize SQLAlchemy
db = SQLAlchemy()

def init_db(app):
    """
    Initialize database with Flask app
    
    Args:
        app: Flask application instance
    """
    # Configure database based on environment
    database_url = os.environ.get('DATABASE_URL')
    is_render = os.environ.get('RENDER') is not None
    is_production = os.environ.get('FLASK_ENV') == 'production'
    
    # If no DATABASE_URL set, handle appropriately
    if not database_url:
        if is_render or is_production:
            # On Render/production, DATABASE_URL is REQUIRED
            error_msg = (
                "❌ CRITICAL ERROR: DATABASE_URL environment variable not set!\n"
                "   This is required for Render deployment.\n"
                "   \n"
                "   ACTION NEEDED:\n"
                "   1. Go to https://render.com/dashboard\n"
                "   2. Click your Web Service (medical-cdss)\n"
                "   3. Click Settings tab\n"
                "   4. Scroll to Environment section\n"
                "   5. Click 'Add Environment Variable'\n"
                "   6. Key: DATABASE_URL\n"
                "   7. Value: [Your Render PostgreSQL connection string]\n"
                "   8. Click Save and Redeploy\n"
            )
            print(error_msg)
            raise RuntimeError(error_msg)
        else:
            # Local development - use SQLite
            database_url = 'sqlite:///medical_cdss.db'
            print("✓ Local development mode: Using SQLite database")
    else:
        print(f"✓ Using database from environment variable")
        if is_render:
            print("  ✓ Render deployment detected")
    
    # Handle heroku postgres:// URLs (convert to postgresql://)
    if database_url.startswith('postgres://'):
        database_url = database_url.replace('postgres://', 'postgresql://', 1)
    
    app.config['SQLALCHEMY_DATABASE_URI'] = database_url
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {
        'pool_size': 10,
        'pool_recycle': 3600,
        'pool_pre_ping': True,
    }
    
    # Initialize database
    db.init_app(app)
    
    # Create tables
    with app.app_context():
        try:
            db.create_all()
            print("✓ Database initialized successfully")
        except Exception as e:
            print(f"⚠️  Database initialization warning: {str(e)[:100]}")
    
    return db

def get_database_info():
    """Get database information"""
    uri = db.engine.url
    return {
        'drivername': uri.drivername,
        'database': uri.database,
        'host': uri.host or 'localhost',
        'port': uri.port or 'default'
    }

# Database utility functions
def commit_changes():
    """Commit database changes"""
    try:
        db.session.commit()
        return True
    except Exception as e:
        db.session.rollback()
        print(f"Database error: {e}")
        return False

def rollback_changes():
    """Rollback database changes"""
    db.session.rollback()

