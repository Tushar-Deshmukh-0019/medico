-- ===============================================
-- Medical CDSS Database Setup Script
-- PostgreSQL SQL Script
-- ===============================================
-- Run this script with:
-- psql -U postgres -h localhost -f setup_database.sql

-- Create the database
CREATE DATABASE medical_cdss;

-- Connect to the new database
\c medical_cdss

-- Create the users table
CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(120) UNIQUE NOT NULL,
    email VARCHAR(120) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create the patients table
CREATE TABLE IF NOT EXISTS patients (
    id SERIAL PRIMARY KEY,
    name VARCHAR(120) NOT NULL,
    age INTEGER,
    email VARCHAR(120),
    phone VARCHAR(20),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create the assessments table
CREATE TABLE IF NOT EXISTS assessments (
    id SERIAL PRIMARY KEY,
    patient_id INTEGER NOT NULL REFERENCES patients(id) ON DELETE CASCADE,
    blood_sugar FLOAT NOT NULL,
    bmi FLOAT NOT NULL,
    age INTEGER NOT NULL,
    blood_pressure FLOAT NOT NULL,
    risk_score FLOAT NOT NULL,
    risk_category VARCHAR(50),
    blood_sugar_status VARCHAR(50),
    bmi_category VARCHAR(50),
    bp_category VARCHAR(50),
    recommendations TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create indexes for better query performance
CREATE INDEX idx_assessments_patient_id ON assessments(patient_id);
CREATE INDEX idx_assessments_created_at ON assessments(created_at);
CREATE INDEX idx_patients_created_at ON patients(created_at);

-- Create the medical_cdss user with limited privileges
CREATE USER cdss_user WITH PASSWORD 'Password123!';

-- Grant privileges on database
GRANT CONNECT ON DATABASE medical_cdss TO cdss_user;

-- Grant privileges on schema
GRANT USAGE ON SCHEMA public TO cdss_user;

-- Grant privileges on tables
GRANT SELECT, INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA public TO cdss_user;

-- Grant privileges on sequences (for auto-increment)
GRANT USAGE, SELECT ON ALL SEQUENCES IN SCHEMA public TO cdss_user;

-- Set default privileges for future tables
ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT SELECT, INSERT, UPDATE, DELETE ON TABLES TO cdss_user;
ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT USAGE, SELECT ON SEQUENCES TO cdss_user;

-- Verify setup
\echo '================================'
\echo 'Database Setup Complete!'
\echo '================================'
\echo 'Database: medical_cdss'
\echo 'User: cdss_user'
\echo 'Password: Password123!'
\echo ''
\echo 'Tables created:'
\echo '  - users'
\echo '  - patients'
\echo '  - assessments'
\echo ''
\echo 'Indexes created:'
\echo '  - idx_assessments_patient_id'
\echo '  - idx_assessments_created_at'
\echo '  - idx_patients_created_at'
\echo ''
\echo 'Ready to use!'
\echo '================================'
