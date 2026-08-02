# Setup Guide - Medical Decision Support System

Complete step-by-step guide to get the Fuzzy Logic-Based Medical Decision Support System running.

## 📋 Prerequisites

- **Python 3.7 or higher** - [Download here](https://www.python.org/downloads/)
- **pip** (comes with Python)
- **Git** (optional, for version control)
- **Web Browser** (Chrome, Firefox, Edge, Safari)

## 🚀 Quick Start (5 minutes)

### Step 1: Navigate to Project Directory
```bash
cd c:\medical_cdss
```

### Step 2: Create Virtual Environment
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Run the Application
```bash
python app.py
```

### Step 5: Access the Web Interface
Open your browser and navigate to:
```
http://localhost:5000
```

## 📦 What Gets Installed

The `requirements.txt` installs:

| Package | Version | Purpose |
|---------|---------|---------|
| Flask | 2.3.3 | Web framework |
| NumPy | 1.24.3 | Numerical operations |
| scikit-fuzzy | 0.4.2 | Fuzzy logic (optional, included for reference) |
| Pandas | 2.0.3 | Data manipulation |
| Matplotlib | 3.7.2 | Data visualization |
| python-dotenv | 1.0.0 | Environment configuration |

## 🔧 Troubleshooting

### Issue: "Python not found"
**Solution:**
- Ensure Python is installed: `python --version`
- If not installed, download from [python.org](https://www.python.org)
- On Windows, check "Add Python to PATH" during installation

### Issue: "Module not found"
**Solution:**
- Ensure virtual environment is activated
- Reinstall dependencies: `pip install -r requirements.txt --force-reinstall`

### Issue: "Port 5000 already in use"
**Solution:**
- Edit `app.py` line 81:
  ```python
  app.run(debug=True, host='127.0.0.1', port=5001)  # Change 5000 to 5001
  ```
- Or kill the process using port 5000:
  ```bash
  # Windows
  netstat -ano | findstr :5000
  taskkill /PID <PID> /F
  
  # Linux/Mac
  lsof -ti:5000 | xargs kill -9
  ```

### Issue: SSL Certificate Error
**Solution:**
- This is a Flask development server message, not an error
- Simply access the application via: `http://localhost:5000`

### Issue: Browser shows "Connection refused"
**Solution:**
- Ensure Flask is running: `python app.py`
- Check the terminal shows "Running on http://127.0.0.1:5000"
- Wait 10 seconds for the server to fully start

## 📁 Directory Structure

After setup, your project should look like:

```
c:\medical_cdss\
├── venv/                          # Virtual environment (created after setup)
├── app.py                         # Main Flask application
├── config.py                      # Configuration
├── test_system.py                 # Test script
├── requirements.txt               # Dependencies
├── README.md                      # Project documentation
├── SETUP_GUIDE.md                 # This file
│
├── fuzzy/                         # Fuzzy logic engine
│   ├── __init__.py
│   ├── membership.py
│   ├── rules.py
│   ├── inference.py
│   ├── defuzzification.py
│   └── engine.py
│
├── models/
│   └── patient.py
│
├── utils/
│   ├── validators.py
│   └── helpers.py
│
├── static/
│   ├── css/
│   │   └── style.css
│   └── js/
│       └── script.js
│
└── templates/
    ├── base.html
    ├── index.html
    ├── patient_form.html
    ├── history.html
    └── about.html
```

## ✅ Verify Installation

Run the test script to verify everything is working:

```bash
python test_system.py
```

You should see output like:
```
============================================================
FUZZY LOGIC MEDICAL DECISION SUPPORT SYSTEM - TEST
============================================================

✓ Fuzzy Engine initialized successfully
...
✓ ALL TESTS COMPLETED
```

## 🌐 Accessing the Application

### Default Access
- **URL**: http://localhost:5000
- **Pages**:
  - Home: http://localhost:5000/
  - Assessment: http://localhost:5000/assessment
  - History: http://localhost:5000/history
  - About: http://localhost:5000/about

### From Other Devices (Same Network)
1. Find your computer's IP address:
   ```bash
   # Windows
   ipconfig
   # Look for "IPv4 Address"
   
   # Linux/Mac
   ifconfig
   # Look for "inet"
   ```

2. Access from another device:
   ```
   http://<YOUR_IP>:5000
   ```

## 📝 Testing the System

### Test 1: Simple Assessment
1. Go to http://localhost:5000/assessment
2. Fill in the form:
   - Name: John Doe
   - Age: 45
   - Blood Sugar: 150
   - BMI: 28
   - BP: 135
3. Click "Perform Assessment"
4. View the results

### Test 2: API Testing
```bash
# Test the assessment API
curl -X POST http://localhost:5000/api/assess \
  -H "Content-Type: application/json" \
  -d "{\"name\":\"Test\",\"age\":45,\"blood_sugar\":150,\"bmi\":28,\"bp\":135}"

# Check system health
curl http://localhost:5000/api/health
```

## 🐛 Debug Mode

The application runs in debug mode by default. This means:
- Server automatically reloads when you modify code
- Detailed error messages in the browser
- Interactive debugger on errors

To disable debug mode:
```python
# In app.py, change:
app.run(debug=True, ...)
# To:
app.run(debug=False, ...)
```

## 🔐 Production Deployment

For production deployment:

1. **Disable Debug Mode**
   ```python
   app.run(debug=False)
   ```

2. **Set Secret Key**
   ```bash
   export SECRET_KEY="your-secret-key-here"
   ```

3. **Use Production Server**
   ```bash
   pip install gunicorn
   gunicorn -w 4 -b 0.0.0.0:5000 app:create_app()
   ```

4. **Use HTTPS**
   - Set up SSL certificates
   - Configure reverse proxy (nginx/Apache)

## 📊 Database Setup (Optional)

Currently, the system uses in-memory storage. To add persistent storage:

1. **Uncomment database code** in `config.py`
2. **Initialize database**:
   ```bash
   python
   >>> from app import create_app, db
   >>> app = create_app()
   >>> with app.app_context():
   >>>     db.create_all()
   ```

## 🎓 Learning Resources

### Fuzzy Logic
- Zadeh, L.A. (1965). "Fuzzy sets"
- Mamdani & Assilian (1975). "Application of Fuzzy Algorithms for Control of a Simple Dynamic Plant"

### Flask
- [Flask Official Documentation](https://flask.palletsprojects.com/)
- [Flask Mega-Tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world)

### Fuzzy Logic in Medical Systems
- [Medical Fuzzy Logic Systems Overview](https://en.wikipedia.org/wiki/Fuzzy_logic)
- WHO Diabetes Guidelines
- ADA Standards of Medical Care

## 🆘 Common Questions

### Q: Can I modify the fuzzy rules?
**A:** Yes! Edit `fuzzy/rules.py` and add/modify rules in the `evaluate_rules()` method. The system will use the new rules on next run.

### Q: How do I add new input parameters?
**A:** 
1. Add membership function in `fuzzy/membership.py`
2. Create fuzzification method
3. Add new rules using the parameter
4. Update HTML form to accept the new input

### Q: Can I export assessments?
**A:** Currently, assessments are stored locally in browser. Print the report (Ctrl+P) for a PDF, or use the export button (coming soon).

### Q: Is my data secure?
**A:** The application stores assessment history locally in your browser (localStorage). No data is sent to external servers.

### Q: Can I run this on a server?
**A:** Yes! See "Production Deployment" section above for instructions.

## 📞 Support

If you encounter issues:

1. **Check error message** in browser console (F12)
2. **Check terminal output** where Flask is running
3. **Run tests**: `python test_system.py`
4. **Review logs** in the application output

## ✨ Next Steps

After setup:
1. Explore the home page to understand the system
2. Try the assessment form
3. Review the "About" section for technical details
4. Experiment with different patient scenarios
5. Review the code to understand fuzzy logic implementation

## 📚 Additional Resources

- **Project README**: `README.md`
- **API Documentation**: See `app.py` routes
- **Fuzzy Engine**: `fuzzy/engine.py`
- **System Test**: `test_system.py`

---

**Version**: 1.0.0
**Last Updated**: 2024
**Status**: Ready for Educational Use
