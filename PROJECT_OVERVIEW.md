# GATE 2026-2027 Daily Planner - Complete Project Overview

## 🎯 Project Summary

A full-stack web application for Sohel and Anju to track their daily 5-hour GATE exam preparation from January 1, 2026 to February 15, 2027.

## 📁 Project Structure

```
gate_planner/
│
├── app.py                      # Main Flask application (all routes & logic)
├── config.py                   # Configuration settings
├── requirements.txt            # Python dependencies
├── runtime.txt                 # Python version for deployment
├── Procfile                    # Heroku deployment config
├── .env.example                # Environment variables template
├── .gitignore                  # Git ignore rules
│
├── templates/                  # HTML templates
│   ├── base.html              # Base template with navbar
│   ├── login.html             # Login page
│   ├── dashboard.html         # Main dashboard with stats
│   ├── calendar.html          # Calendar view
│   ├── add_entry.html         # Add new study entry
│   ├── edit_entry.html        # Edit existing entry
│   └── analytics.html         # Charts and analytics
│
├── static/                     # Static files
│   ├── css/
│   │   └── style.css          # All CSS styles
│   └── js/
│       └── main.js            # JavaScript functionality
│
└── docs/                       # Documentation
    ├── README.md              # Main documentation
    ├── SETUP.md               # Setup instructions
    └── DEPLOYMENT.md          # Deployment guide
```

## 🔧 Tech Stack

### Backend
- **Framework**: Flask 3.0.0
- **Database**: MongoDB Atlas (Cloud)
- **ODM**: Flask-PyMongo 2.3.0
- **Authentication**: Werkzeug (password hashing)
- **Server**: Gunicorn (production)

### Frontend
- **HTML5**: Semantic markup
- **CSS3**: Modern styling with gradients, animations
- **JavaScript**: Vanilla JS (no frameworks)
- **Charts**: Chart.js (for analytics)

### Database
- **MongoDB Collections**:
  - `users`: User authentication data
  - `daily_logs`: Study entry records

## 🎨 Design Features

### Color Scheme
- Primary: Blue (#667eea) & Purple (#764ba2)
- Success: Green (#4caf50)
- Warning: Orange (#ff9800)
- Error: Red (#f44336)
- Background: Gradient (Blue to Purple)

### UI Components
- Modern card-based layout
- Smooth animations and transitions
- Responsive grid system
- Color-coded calendar
- Progress bars and charts
- Clean forms with validation

## 🔐 Authentication System

### Users
1. **Sohel** (Male)
   - Username: `sohel`
   - Default Password: `sohel123`

2. **Anju** (Female)
   - Username: `anju`
   - Default Password: `anju123`

### Security Features
- Password hashing using Werkzeug
- Session-based authentication
- Login required decorators
- User isolation (can only see own data)
- CSRF protection ready

## 📊 Core Features

### 1. Dashboard
- Total days logged
- Completed days count
- Total hours studied
- Completion percentage
- Current streak 🔥
- Longest streak 🏆
- Progress bar to GATE
- Friendly competition view
- Daily motivational quote

### 2. Calendar View
- Monthly calendar grid
- Color-coded days:
  - Green: Completed (5 hours)
  - Yellow: Partial (3-4.9 hours)
  - Red: Missed/Not completed
  - Gray: Future dates
- Click to add/edit entries
- Month navigation
- Legend for clarity

### 3. Study Entry Form
Fields:
- Date (validated: 01/01/2026 - 15/02/2027)
- Hours Studied (default: 5)
- Subject Category (13 options)
- Topics Covered
- Description (What I did today)
- Mood (Productive/Average/Bad)
- Completion Status (Yes/No)

### 4. Analytics Page
- Monthly study hours bar chart
- Subject-wise pie chart
- Detailed breakdown table
- Study consistency tracking

### 5. Competition Feature
- See partner's completion percentage
- Friendly leaderboard
- Motivational comparison

## 📅 Date Range Control

- **Start Date**: January 1, 2026
- **End Date**: February 15, 2027
- **Total Days**: 411 days
- **Daily Goal**: 5 hours
- **Total Goal**: 2,055 hours

Entries outside this range are blocked.

## 🎓 Subject Categories

1. Mathematics
2. Data Structures
3. Algorithms
4. Computer Organization
5. Operating Systems
6. DBMS
7. Computer Networks
8. Theory of Computation
9. Compiler Design
10. Digital Logic
11. Programming
12. Aptitude
13. Mixed Topics

## 🗄️ Database Schema

### Collection: users
```javascript
{
  _id: ObjectId,
  username: String,        // "sohel" or "anju"
  password_hash: String,   // Hashed password
  gender: String          // "male" or "female"
}
```

### Collection: daily_logs
```javascript
{
  _id: ObjectId,
  username: String,        // User who created entry
  date: Date,             // Study date
  hours_studied: Number,  // Hours (0-24)
  subject: String,        // Subject category
  topics: String,         // Topics covered
  description: String,    // Detailed description
  mood: String,          // "Productive", "Average", "Bad"
  completed: Boolean,    // true if 5 hours done
  created_at: Date       // Entry creation timestamp
}
```

## 🔄 Application Flow

1. **User visits site** → Redirected to login
2. **Login** → Validates credentials → Creates session
3. **Dashboard** → Shows statistics and progress
4. **Add Entry** → Form validation → Save to MongoDB
5. **Calendar** → View all entries → Click to edit
6. **Analytics** → Fetch data → Generate charts
7. **Logout** → Clear session → Redirect to login

## 🚀 API Endpoints

### Authentication
- `GET /` - Home (redirects to dashboard or login)
- `GET /login` - Login page
- `POST /login` - Process login
- `GET /logout` - Logout user

### Main Features
- `GET /dashboard` - Main dashboard
- `GET /calendar` - Calendar view
- `GET /add_entry` - Add entry form
- `POST /add_entry` - Save new entry
- `GET /edit_entry/<id>` - Edit entry form
- `POST /edit_entry/<id>` - Update entry
- `GET /analytics` - Analytics page

### API
- `GET /api/quote` - Random motivational quote

## 📈 Statistics Calculation

### Completion Percentage
```python
(completed_days / total_days) * 100
```

### Current Streak
Count consecutive completed days from today backwards

### Longest Streak
Maximum consecutive completed days in entire history

### Total Hours
Sum of all hours_studied values

## 🎯 Key Functions

### `login_required` Decorator
Protects routes requiring authentication

### `calculate_streaks(logs)`
Calculates current and longest study streaks

### `init_db()`
Initializes database with default users

## 🌐 Deployment Options

1. **Render** (Recommended)
   - Free tier available
   - Auto-deploy from GitHub
   - Easy setup

2. **Railway**
   - Modern platform
   - Auto-detection
   - Simple deployment

3. **Heroku**
   - Classic platform
   - CLI-based
   - Reliable

## 📱 Responsive Design

- Desktop: Full layout with sidebar
- Tablet: Adjusted grid
- Mobile: Single column, stacked cards

## ⚡ Performance Features

- Efficient MongoDB queries
- Indexed date fields
- Minimal JavaScript
- Optimized CSS
- Fast page loads

## 🔒 Security Measures

1. Password hashing (Werkzeug)
2. Session management
3. User data isolation
4. Input validation
5. Date range validation
6. SQL injection prevention (NoSQL)
7. XSS protection (template escaping)

## 🎨 UI/UX Features

- Smooth animations
- Hover effects
- Color-coded feedback
- Auto-hiding alerts
- Form validation
- Loading states
- Responsive design
- Clean typography

## 📝 Future Enhancements (Optional)

- Email notifications for missed days
- Weekly summary emails
- PDF report generation
- Study timer (Pomodoro)
- Dark mode toggle
- Mobile app
- Push notifications
- Study reminders
- Goal setting
- Notes section
- File uploads
- Video links

## 🐛 Error Handling

- Invalid login attempts
- Duplicate date entries
- Out-of-range dates
- Missing required fields
- Database connection errors
- Session expiration

## 📊 Success Metrics

- Daily login rate
- Entry completion rate
- Average study hours
- Streak maintenance
- Subject distribution
- Mood trends

## 🎓 GATE Preparation Timeline

- **Start**: January 1, 2026
- **End**: February 15, 2027
- **Exam Date**: ~February 2027
- **Total Preparation**: 13.5 months
- **Target**: 5 hours/day consistently

## 💡 Tips for Users

1. Log entries daily
2. Be honest about hours
3. Track mood patterns
4. Review analytics weekly
5. Maintain streaks
6. Compete healthily
7. Adjust study plans based on data

## 🔧 Maintenance

- Regular MongoDB backups
- Monitor server logs
- Update dependencies
- Check security patches
- Review user feedback

## 📞 Support

For issues:
1. Check SETUP.md
2. Review error logs
3. Verify MongoDB connection
4. Check browser console
5. Review documentation

---

## Quick Start Commands

```bash
# Install dependencies
pip install -r requirements.txt

# Run locally
python app.py

# Access app
http://localhost:5000

# Login
Username: sohel or anju
Password: sohel123 or anju123
```

---

**Built with ❤️ for GATE 2027 Success!** 🎯📚🚀
