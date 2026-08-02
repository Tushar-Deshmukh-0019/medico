-- ===============================================
-- Medical CDSS Database Creation Script
-- Run this as superuser (postgres)
-- ===============================================

-- Create the database
CREATE DATABASE medical_cdss;

-- Connect to the database
\c medical_cdss

-- Create tables automatically (Flask-SQLAlchemy will do this)
-- But we can verify the connection works

-- Verify database creation
\echo 'Database medical_cdss created successfully!'
\echo ''
\echo 'Next steps:'
\echo '1. Run the Flask application: python app.py'
\echo '2. Flask will automatically create all tables'
\echo '3. Visit: http://localhost:5000'
