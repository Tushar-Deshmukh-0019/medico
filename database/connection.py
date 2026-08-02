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
    
    if not database_url:
        # Default to SQLite for quick start (no PostgreSQL needed)
        # If you want PostgreSQL, set DATABASE_URL environment variable
        database_url = 'sqlite:///medical_cdss.db'
        print("⚠️ No DATABASE_URL set. Using SQLite for quick start.")
        print("   To use PostgreSQL, set: setx DATABASE_URL=postgresql://user:pass@localhost:5432/medical_cdss")
    
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
        db.create_all()
        print("✓ Database initialized successfully")
    
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
