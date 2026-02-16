from flask import Flask, render_template, request, redirect, url_for, session, jsonify, flash
from flask_pymongo import PyMongo
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime, timedelta
from functools import wraps
import os
from bson import ObjectId

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key-change-in-production'
app.config['MONGO_URI'] = 'mongodb+srv://239x1a32b0_db_user:a3cTQ*CA6base9A@cluster0.umwhot3.mongodb.net/gate_planner?retryWrites=true&w=majority&appName=Cluster0'

mongo = PyMongo(app)

# Date range constants
START_DATE = datetime(2026, 1, 1)
END_DATE = datetime(2027, 2, 15)

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'username' not in session:
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

@app.route('/')
def index():
    if 'username' in session:
        return redirect(url_for('dashboard'))
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username', '').lower()
        password = request.form.get('password', '')
        
        user = mongo.db.users.find_one({'username': username})
        
        if user and check_password_hash(user['password_hash'], password):
            session['username'] = username
            session['gender'] = user['gender']
            flash('Login successful!', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid username or password', 'error')
    
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear()
    flash('Logged out successfully', 'success')
    return redirect(url_for('login'))

@app.route('/dashboard')
@login_required
def dashboard():
    username = session['username']
    
    # Get all logs for user
    logs = list(mongo.db.daily_logs.find({'username': username}).sort('date', -1))
    
    # Calculate statistics
    total_days = len(logs)
    completed_days = len([log for log in logs if log.get('completed')])
    total_hours = sum([log.get('hours_studied', 0) for log in logs])
    completion_percentage = (completed_days / total_days * 100) if total_days > 0 else 0
    
    # Calculate streak
    current_streak, longest_streak = calculate_streaks(logs)
    
    # Get partner stats
    partner = 'anju' if username == 'sohel' else 'sohel'
    partner_logs = list(mongo.db.daily_logs.find({'username': partner}))
    partner_completed = len([log for log in partner_logs if log.get('completed')])
    partner_total = len(partner_logs)
    partner_percentage = (partner_completed / partner_total * 100) if partner_total > 0 else 0
    
    stats = {
        'total_days': total_days,
        'completed_days': completed_days,
        'total_hours': total_hours,
        'completion_percentage': round(completion_percentage, 1),
        'current_streak': current_streak,
        'longest_streak': longest_streak,
        'partner': partner.capitalize(),
        'partner_percentage': round(partner_percentage, 1)
    }
    
    return render_template('dashboard.html', stats=stats, username=username)

@app.route('/calendar')
@login_required
def calendar():
    username = session['username']
    year = request.args.get('year', datetime.now().year, type=int)
    month = request.args.get('month', datetime.now().month, type=int)
    
    # Handle month overflow/underflow
    if month > 12:
        month = 1
        year += 1
    elif month < 1:
        month = 12
        year -= 1
    
    # Get logs for the month
    start = datetime(year, month, 1)
    if month == 12:
        end = datetime(year + 1, 1, 1)
    else:
        end = datetime(year, month + 1, 1)
    
    logs = list(mongo.db.daily_logs.find({
        'username': username,
        'date': {'$gte': start, '$lt': end}
    }))
    
    # Create a dictionary for quick lookup
    log_dict = {log['date'].strftime('%Y-%m-%d'): log for log in logs}
    
    # Calculate first day of month (0=Monday, 6=Sunday)
    first_day = datetime(year, month, 1)
    first_weekday = (first_day.weekday() + 1) % 7  # Convert to Sunday=0
    
    # Days in month
    if month == 12:
        days_in_month = (datetime(year + 1, 1, 1) - datetime(year, month, 1)).days
    else:
        days_in_month = (datetime(year, month + 1, 1) - datetime(year, month, 1)).days
    
    return render_template('calendar.html', 
                         year=year, 
                         month=month, 
                         logs=log_dict,
                         first_weekday=first_weekday,
                         days_in_month=days_in_month,
                         start_date=START_DATE, 
                         end_date=END_DATE)

@app.route('/add_entry', methods=['GET', 'POST'])
@login_required
def add_entry():
    if request.method == 'POST':
        username = session['username']
        date_str = request.form.get('date')
        date = datetime.strptime(date_str, '%Y-%m-%d')
        
        # Validate date range
        if date < START_DATE or date > END_DATE:
            flash('Date must be between 01/01/2026 and 15/02/2027', 'error')
            return redirect(url_for('add_entry'))
        
        # Check if entry already exists
        existing = mongo.db.daily_logs.find_one({'username': username, 'date': date})
        if existing:
            flash('Entry for this date already exists. Please edit it instead.', 'error')
            return redirect(url_for('calendar'))
        
        entry = {
            'username': username,
            'date': date,
            'hours_studied': float(request.form.get('hours_studied', 5)),
            'subject': request.form.get('subject'),
            'topics': request.form.get('topics'),
            'description': request.form.get('description'),
            'mood': request.form.get('mood'),
            'completed': request.form.get('completed') == 'yes',
            'created_at': datetime.now()
        }
        
        mongo.db.daily_logs.insert_one(entry)
        flash('Entry added successfully!', 'success')
        return redirect(url_for('calendar'))
    
    return render_template('add_entry.html', start_date=START_DATE, end_date=END_DATE)

@app.route('/edit_entry/<entry_id>', methods=['GET', 'POST'])
@login_required
def edit_entry(entry_id):
    username = session['username']
    entry = mongo.db.daily_logs.find_one({'_id': ObjectId(entry_id), 'username': username})
    
    if not entry:
        flash('Entry not found', 'error')
        return redirect(url_for('calendar'))
    
    if request.method == 'POST':
        update_data = {
            'hours_studied': float(request.form.get('hours_studied', 5)),
            'subject': request.form.get('subject'),
            'topics': request.form.get('topics'),
            'description': request.form.get('description'),
            'mood': request.form.get('mood'),
            'completed': request.form.get('completed') == 'yes'
        }
        
        mongo.db.daily_logs.update_one({'_id': ObjectId(entry_id)}, {'$set': update_data})
        flash('Entry updated successfully!', 'success')
        return redirect(url_for('calendar'))
    
    return render_template('edit_entry.html', entry=entry)

@app.route('/analytics')
@login_required
def analytics():
    username = session['username']
    logs = list(mongo.db.daily_logs.find({'username': username}).sort('date', 1))
    
    # Monthly study hours
    monthly_data = {}
    for log in logs:
        month_key = log['date'].strftime('%Y-%m')
        monthly_data[month_key] = monthly_data.get(month_key, 0) + log.get('hours_studied', 0)
    
    # Subject-wise distribution
    subject_data = {}
    for log in logs:
        subject = log.get('subject', 'Other')
        subject_data[subject] = subject_data.get(subject, 0) + log.get('hours_studied', 0)
    
    return render_template('analytics.html', 
                         monthly_data=monthly_data, 
                         subject_data=subject_data)

@app.route('/api/quote')
def get_quote():
    quotes = [
        "Success is the sum of small efforts repeated day in and day out.",
        "The expert in anything was once a beginner.",
        "Don't watch the clock; do what it does. Keep going.",
        "The secret of getting ahead is getting started.",
        "Study hard, stay focused, and make it happen!"
    ]
    import random
    return jsonify({'quote': random.choice(quotes)})

@app.route('/api/save-theme', methods=['POST'])
@login_required
def save_theme():
    """Save user's theme preference to database"""
    try:
        username = session['username']
        data = request.get_json()
        
        theme_data = {
            'theme_color': data.get('primary_color', '#2563EB'),
            'hover_color': data.get('hover_color', '#1E40AF'),
            'theme_name': data.get('theme_name', 'Professional Blue'),
            'theme_mode': data.get('mode', 'light')
        }
        
        # Update user document
        mongo.db.users.update_one(
            {'username': username},
            {'$set': theme_data}
        )
        
        return jsonify({'success': True, 'message': 'Theme saved successfully'})
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)}), 500

@app.route('/api/get-theme')
@login_required
def get_theme():
    """Get user's saved theme preference"""
    try:
        username = session['username']
        user = mongo.db.users.find_one({'username': username})
        
        if user and 'theme_color' in user:
            return jsonify({
                'theme_color': user.get('theme_color'),
                'hover_color': user.get('hover_color'),
                'theme_name': user.get('theme_name'),
                'theme_mode': user.get('theme_mode', 'light')
            })
        else:
            return jsonify({
                'theme_color': '#2563EB',
                'hover_color': '#1E40AF',
                'theme_name': 'Professional Blue',
                'theme_mode': 'light'
            })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

def calculate_streaks(logs):
    if not logs:
        return 0, 0
    
    # Sort by date descending
    sorted_logs = sorted(logs, key=lambda x: x['date'], reverse=True)
    
    current_streak = 0
    longest_streak = 0
    temp_streak = 0
    
    for i, log in enumerate(sorted_logs):
        if log.get('completed'):
            temp_streak += 1
            if i == 0:
                current_streak = temp_streak
        else:
            if temp_streak > longest_streak:
                longest_streak = temp_streak
            temp_streak = 0
    
    longest_streak = max(longest_streak, temp_streak)
    
    return current_streak, longest_streak

def init_db():
    """Initialize database with default users"""
    if mongo.db.users.count_documents({}) == 0:
        users = [
            {
                'username': 'sohel',
                'password_hash': generate_password_hash('sohel123'),
                'gender': 'male',
                'theme_color': '#2563EB',
                'hover_color': '#1E40AF',
                'theme_name': 'Professional Blue',
                'theme_mode': 'light'
            },
            {
                'username': 'anju',
                'password_hash': generate_password_hash('anju123'),
                'gender': 'female',
                'theme_color': '#2563EB',
                'hover_color': '#1E40AF',
                'theme_name': 'Professional Blue',
                'theme_mode': 'light'
            }
        ]
        mongo.db.users.insert_many(users)
        print("Default users created!")

if __name__ == '__main__':
    with app.app_context():
        init_db()
    app.run(debug=True, host='0.0.0.0', port=5000)
