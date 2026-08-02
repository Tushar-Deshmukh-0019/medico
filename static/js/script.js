/**
 * Main Application Script
 * Handles client-side interactions and animations
 */

// ============================================
// Utility Functions
// ============================================

/**
 * Smoothly scroll to element
 */
function scrollToElement(selector) {
    const element = document.querySelector(selector);
    if (element) {
        element.scrollIntoView({ behavior: 'smooth' });
    }
}

/**
 * Add active class to navigation links
 */
function updateActiveNav() {
    const currentLocation = location.pathname;
    const menuItems = document.querySelectorAll('.nav-link');

    menuItems.forEach(item => {
        item.classList.remove('active');
        if (item.getAttribute('href') === currentLocation) {
            item.classList.add('active');
        }
    });
}

/**
 * Format number with commas
 */
function formatNumber(num) {
    return num.toFixed(2);
}

/**
 * Show notification
 */
function showNotification(message, type = 'info', duration = 5000) {
    const notification = document.createElement('div');
    notification.className = `alert alert-${type}`;
    notification.textContent = message;
    notification.style.position = 'fixed';
    notification.style.top = '100px';
    notification.style.right = '20px';
    notification.style.zIndex = '9999';
    notification.style.maxWidth = '400px';
    notification.style.animation = 'slideInLeft 0.3s ease';

    document.body.appendChild(notification);

    setTimeout(() => {
        notification.style.animation = 'slideInLeft 0.3s ease reverse';
        setTimeout(() => notification.remove(), 300);
    }, duration);
}

/**
 * Format date and time
 */
function formatDateTime(date) {
    const options = {
        year: 'numeric',
        month: 'short',
        day: 'numeric',
        hour: '2-digit',
        minute: '2-digit'
    };
    return new Date(date).toLocaleDateString('en-US', options);
}

// ============================================
// Animations on Scroll
// ============================================

/**
 * Observe elements and add animation class when they come into view
 */
function observeElements() {
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('fade-in');
                observer.unobserve(entry.target);
            }
        });
    }, observerOptions);

    document.querySelectorAll('.card, .process-step, .info-card').forEach(el => {
        observer.observe(el);
    });
}

// ============================================
// Validation Functions
// ============================================

/**
 * Validate email format
 */
function isValidEmail(email) {
    const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return re.test(email);
}

/**
 * Validate blood sugar range
 */
function isValidBloodSugar(value) {
    const num = parseFloat(value);
    return num >= 0 && num <= 600;
}

/**
 * Validate BMI range
 */
function isValidBMI(value) {
    const num = parseFloat(value);
    return num >= 10 && num <= 60;
}

/**
 * Validate age range
 */
function isValidAge(value) {
    const num = parseFloat(value);
    return num >= 0 && num <= 120;
}

/**
 * Validate blood pressure range
 */
function isValidBP(value) {
    const num = parseFloat(value);
    return num >= 40 && num <= 250;
}

// ============================================
// API Functions
// ============================================

/**
 * Fetch assessment from API
 */
async function fetchAssessment(data) {
    try {
        const response = await fetch('/api/assess', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        });

        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }

        return await response.json();
    } catch (error) {
        console.error('Assessment error:', error);
        throw error;
    }
}

/**
 * Fetch system information
 */
async function fetchSystemInfo() {
    try {
        const response = await fetch('/api/system-info');
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        return await response.json();
    } catch (error) {
        console.error('System info error:', error);
    }
}

/**
 * Validate patient data
 */
async function validatePatientData(data) {
    try {
        const response = await fetch('/api/validate', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        });

        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }

        return await response.json();
    } catch (error) {
        console.error('Validation error:', error);
    }
}

// ============================================
// Chart Functions
// ============================================

/**
 * Create a simple bar chart for risk visualization
 */
function createRiskChart(context, riskScore) {
    const canvas = document.getElementById(context);
    if (!canvas) return;

    const ctx = canvas.getContext('2d');
    const width = canvas.width;
    const height = canvas.height;

    // Clear canvas
    ctx.clearRect(0, 0, width, height);

    // Draw background
    ctx.fillStyle = '#f5f5f5';
    ctx.fillRect(0, 0, width, height);

    // Determine color based on risk score
    let color;
    if (riskScore < 30) {
        color = '#4CAF50'; // Green
    } else if (riskScore < 60) {
        color = '#FFC107'; // Amber
    } else {
        color = '#F44336'; // Red
    }

    // Draw risk bar
    const barWidth = (riskScore / 100) * (width - 40);
    ctx.fillStyle = color;
    ctx.fillRect(20, 30, barWidth, 40);

    // Draw border
    ctx.strokeStyle = '#333';
    ctx.lineWidth = 2;
    ctx.strokeRect(20, 30, width - 40, 40);

    // Draw percentage text
    ctx.fillStyle = '#333';
    ctx.font = 'bold 16px Arial';
    ctx.textAlign = 'center';
    ctx.fillText(riskScore.toFixed(1) + '%', width / 2, 85);

    // Draw labels
    ctx.font = '12px Arial';
    ctx.textAlign = 'left';
    ctx.fillStyle = '#666';
    ctx.fillText('0%', 20, 110);
    ctx.textAlign = 'right';
    ctx.fillText('100%', width - 20, 110);
}

/**
 * Create fuzzification visualization
 */
function createFuzzificationChart(context, fuzzifiedValues) {
    const container = document.getElementById(context);
    if (!container) return;

    container.innerHTML = '';

    Object.entries(fuzzifiedValues).forEach(([variable, values]) => {
        const row = document.createElement('div');
        row.style.marginBottom = '20px';

        const title = document.createElement('h4');
        title.textContent = variable.toUpperCase().replace('_', ' ');
        row.appendChild(title);

        Object.entries(values).forEach(([category, value]) => {
            const percentage = (value * 100).toFixed(1);

            const barContainer = document.createElement('div');
            barContainer.style.marginBottom = '10px';

            const label = document.createElement('span');
            label.textContent = `${category}: ${percentage}%`;
            label.style.display = 'block';
            label.style.marginBottom = '5px';
            label.style.fontSize = '12px';

            const bar = document.createElement('div');
            bar.style.width = '100%';
            bar.style.height = '20px';
            bar.style.background = '#e0e0e0';
            bar.style.borderRadius = '10px';
            bar.style.overflow = 'hidden';

            const fill = document.createElement('div');
            fill.style.width = percentage + '%';
            fill.style.height = '100%';
            fill.style.background = 'linear-gradient(90deg, #667eea 0%, #764ba2 100%)';
            fill.style.transition = 'width 0.5s ease';

            bar.appendChild(fill);

            barContainer.appendChild(label);
            barContainer.appendChild(bar);
            row.appendChild(barContainer);
        });

        container.appendChild(row);
    });
}

// ============================================
// DOM Ready
// ============================================

document.addEventListener('DOMContentLoaded', () => {
    // Update active navigation
    updateActiveNav();

    // Observe elements for animation
    observeElements();

    // Add keyboard shortcuts
    document.addEventListener('keydown', (e) => {
        // Alt + A = Go to assessment
        if (e.altKey && e.key === 'a') {
            window.location.href = '/assessment';
        }
        // Alt + H = Go to home
        if (e.altKey && e.key === 'h') {
            window.location.href = '/';
        }
    });

    // Log system ready
    console.log('Medical CDSS Application Loaded');
});

// ============================================
// Export Functions
// ============================================

/**
 * Print page
 */
function printPage() {
    window.print();
}

/**
 * Export to JSON
 */
function exportToJSON(data, filename = 'assessment.json') {
    const json = JSON.stringify(data, null, 2);
    const blob = new Blob([json], { type: 'application/json' });
    downloadFile(blob, filename);
}

/**
 * Download file
 */
function downloadFile(blob, filename) {
    const url = window.URL.createObjectURL(blob);
    const link = document.createElement('a');
    link.href = url;
    link.download = filename;
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
    window.URL.revokeObjectURL(url);
}

// ============================================
// Dark Mode Support
// ============================================

/**
 * Check for dark mode preference
 */
function checkDarkModePreference() {
    const prefersDark = window.matchMedia('(prefers-color-scheme: dark)');
    if (prefersDark.matches) {
        document.body.classList.add('dark-mode');
    }
}

// Call on load
checkDarkModePreference();

// ============================================
// Mobile Menu Toggle (if needed)
// ============================================

/**
 * Toggle mobile menu
 */
function toggleMobileMenu() {
    const menu = document.querySelector('.nav-menu');
    if (menu) {
        menu.classList.toggle('active');
    }
}
