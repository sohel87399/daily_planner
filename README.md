# GATE 2026-2027 Daily Planner

A full-stack web application for tracking daily 5-hour study sessions for GATE exam preparation.

## Features

- 🔐 Secure login system for Sohel and Anju
- 📅 Calendar view with color-coded study tracking
- 📊 Analytics and progress tracking
- 🔥 Streak counter and motivation system
- 🏆 Friendly competition between users
- 📈 Subject-wise study distribution
- 🎯 Daily goal tracking (5 hours)

## Tech Stack

- **Backend**: Python Flask
- **Database**: MongoDB Atlas
- **Frontend**: HTML, CSS, JavaScript
- **Charts**: Chart.js

## Project Structure

```
gate_planner/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── templates/            # HTML templates
│   ├── base.html
│   ├── login.html
│   ├── dashboard.html
│   ├── calendar.html
│   ├── add_entry.html
│   ├── edit_entry.html
│   └── analytics.html
├── static/              # Static files
│   ├── css/
│   │   └── style.css
│   └── js/
│       └── main.js
└── README.md
```

## Setup Instructions

### Prerequisites

- Python 3.8 or higher
- MongoDB Atlas account (already configured)

### Local Installation

1. Clone or download the project

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
python app.py
```

4. Open your browser and navigate to:
```
http://localhost:5000
```

### Default Login Credentials

- **User 1**: 
  - Username: `sohel`
  - Password: `sohel123`

- **User 2**:
  - Username: `anju`
  - Password: `anju123`

## MongoDB Configuration

The application is pre-configured to connect to your MongoDB Atlas cluster:

```
mongodb+srv://239x1a32b0_db_user:a3cTQ*CA6base9A@cluster0.umwhot3.mongodb.net/gate_planner
```

Database: `gate_planner`

Collections:
- `users` - User authentication data
- `daily_logs` - Study entry records

## Usage

1. **Login**: Use the credentials above to log in
2. **Dashboard**: View your statistics and progress
3. **Add Entry**: Click "Add Today's Entry" to log your study session
4. **Calendar**: View all your entries in calendar format
5. **Analytics**: See detailed charts and subject-wise breakdown
6. **Competition**: Compare your progress with your study partner

## Date Range

Study entries are only allowed between:
- Start: January 1, 2026
- End: February 15, 2027

## Deployment

### Deploy to Render

1. Create a new Web Service on Render
2. Connect your GitHub repository
3. Set the following:
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `gunicorn app:app`
4. Add environment variable:
   - `SECRET_KEY`: Generate a secure random key
5. Deploy!

### Deploy to Railway

1. Create a new project on Railway
2. Connect your GitHub repository
3. Railway will auto-detect Flask and deploy
4. Add environment variable for `SECRET_KEY`

## Security Notes

⚠️ **Important**: Before deploying to production:

1. Change the `SECRET_KEY` in `app.py` to a secure random string
2. Consider using environment variables for sensitive data
3. Enable HTTPS in production
4. Update default passwords for users

## Features Breakdown

### Core Features
- ✅ Two-user authentication system
- ✅ Date range validation (01/01/2026 - 15/02/2027)
- ✅ Daily 5-hour study tracking
- ✅ Subject categorization
- ✅ Mood tracking
- ✅ Completion status

### Dashboard Features
- ✅ Total days logged
- ✅ Completion percentage
- ✅ Total hours studied
- ✅ Current streak counter
- ✅ Longest streak
- ✅ Progress bar
- ✅ Friendly competition view

### Calendar Features
- ✅ Color-coded days (Green/Yellow/Red)
- ✅ Click to add/edit entries
- ✅ Monthly navigation

### Analytics
- ✅ Monthly study hours graph
- ✅ Subject-wise pie chart
- ✅ Detailed breakdown table

### Extra Features
- ✅ Daily motivational quotes
- ✅ Responsive design
- ✅ Clean modern UI
- ✅ Smooth animations

## Support

For issues or questions, please check the code comments or modify as needed.

## License

Personal use for GATE preparation 2026-2027
