# GATE 2026-2027 Daily Planner - Setup Guide

## Quick Start (Local Development)

### Step 1: Install Python Dependencies

```bash
pip install -r requirements.txt
```

### Step 2: Run the Application

```bash
python app.py
```

### Step 3: Access the Application

Open your browser and go to: `http://localhost:5000`

### Step 4: Login

Use these credentials:
- **Sohel**: username: `sohel`, password: `sohel123`
- **Anju**: username: `anju`, password: `anju123`

---

## MongoDB Setup (Already Configured)

Your MongoDB connection is already set up in `app.py`:

```
mongodb+srv://239x1a32b0_db_user:a3cTQ*CA6base9A@cluster0.umwhot3.mongodb.net/gate_planner
```

The application will automatically:
1. Connect to MongoDB Atlas
2. Create the `gate_planner` database
3. Create two collections: `users` and `daily_logs`
4. Initialize default users (Sohel and Anju)

---

## Database Schema

### Collection: users
```json
{
  "_id": ObjectId,
  "username": "sohel",
  "password_hash": "hashed_password",
  "gender": "male"
}
```

### Collection: daily_logs
```json
{
  "_id": ObjectId,
  "username": "sohel",
  "date": ISODate("2026-01-15"),
  "hours_studied": 5.0,
  "subject": "Data Structures",
  "topics": "Binary Trees, AVL Trees",
  "description": "Studied tree traversal algorithms...",
  "mood": "Productive",
  "completed": true,
  "created_at": ISODate("2026-01-15T20:30:00Z")
}
```

---

## Deployment Options

### Option 1: Deploy to Render

1. Create account on [Render.com](https://render.com)

2. Click "New +" → "Web Service"

3. Connect your GitHub repository

4. Configure:
   - **Name**: gate-planner
   - **Environment**: Python 3
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app`

5. Add Environment Variable:
   - Key: `SECRET_KEY`
   - Value: Generate a random string (e.g., use `python -c "import secrets; print(secrets.token_hex(32))"`)

6. Click "Create Web Service"

7. Your app will be live at: `https://gate-planner.onrender.com`

### Option 2: Deploy to Railway

1. Create account on [Railway.app](https://railway.app)

2. Click "New Project" → "Deploy from GitHub repo"

3. Select your repository

4. Railway auto-detects Flask and deploys

5. Add Environment Variable:
   - `SECRET_KEY`: Generate a secure random key

6. Your app will be live at: `https://your-app.railway.app`

### Option 3: Deploy to Heroku

1. Install Heroku CLI

2. Login to Heroku:
```bash
heroku login
```

3. Create a new app:
```bash
heroku create gate-planner
```

4. Set environment variable:
```bash
heroku config:set SECRET_KEY=your-secret-key-here
```

5. Deploy:
```bash
git push heroku main
```

6. Open your app:
```bash
heroku open
```

---

## Changing Default Passwords

To change the default passwords, modify the `init_db()` function in `app.py`:

```python
users = [
    {
        'username': 'sohel',
        'password_hash': generate_password_hash('YOUR_NEW_PASSWORD'),
        'gender': 'male'
    },
    {
        'username': 'anju',
        'password_hash': generate_password_hash('YOUR_NEW_PASSWORD'),
        'gender': 'female'
    }
]
```

Then delete the users collection in MongoDB and restart the app to recreate users.

---

## Testing the Application

### Test Login
1. Go to `http://localhost:5000`
2. Login with `sohel` / `sohel123`
3. You should see the dashboard

### Test Adding Entry
1. Click "Add Today's Entry"
2. Fill in the form with:
   - Date: Any date between 01/01/2026 and 15/02/2027
   - Hours: 5
   - Subject: Data Structures
   - Topics: Binary Trees
   - Description: Studied tree algorithms
   - Mood: Productive
   - Status: Completed
3. Click "Save Entry"

### Test Calendar
1. Click "Calendar" in navigation
2. You should see your entry marked in green
3. Click on the date to edit

### Test Analytics
1. Click "Analytics" in navigation
2. View charts and statistics

---

## Troubleshooting

### Issue: Can't connect to MongoDB
- Check your internet connection
- Verify the MongoDB URI is correct
- Ensure your IP is whitelisted in MongoDB Atlas (or use 0.0.0.0/0 for all IPs)

### Issue: Module not found
```bash
pip install -r requirements.txt
```

### Issue: Port already in use
Change the port in `app.py`:
```python
app.run(debug=True, host='0.0.0.0', port=5001)
```

### Issue: Can't login
- Check that users were created (check console output)
- Try deleting the users collection and restarting

---

## Security Recommendations for Production

1. **Change SECRET_KEY**: Use a strong random key
2. **Use HTTPS**: Enable SSL/TLS
3. **Change Passwords**: Update default user passwords
4. **Enable CSRF Protection**: Add Flask-WTF
5. **Rate Limiting**: Add Flask-Limiter
6. **Input Validation**: Already implemented
7. **Session Security**: Configure secure cookies

---

## Features Checklist

✅ Two-user authentication (Sohel & Anju)
✅ Date range validation (01/01/2026 - 15/02/2027)
✅ Daily 5-hour study tracking
✅ Subject categorization (11 subjects)
✅ Mood tracking (Productive/Average/Bad)
✅ Completion status
✅ Dashboard with statistics
✅ Calendar view (color-coded)
✅ Streak counter
✅ Progress bar
✅ Friendly competition
✅ Analytics with charts
✅ Monthly study hours graph
✅ Subject-wise distribution
✅ Daily motivational quotes
✅ Responsive design
✅ Clean modern UI
✅ MongoDB integration
✅ Password hashing (bcrypt)
✅ Session management
✅ Add/Edit/View entries

---

## Support

For any issues:
1. Check the console output for errors
2. Verify MongoDB connection
3. Check browser console for JavaScript errors
4. Review the README.md for additional info

---

## Next Steps

1. Run the app locally and test all features
2. Customize the UI colors/theme if needed
3. Add more subjects if required
4. Deploy to your preferred platform
5. Share the URL with Sohel and Anju
6. Start tracking your GATE preparation!

Good luck with your GATE 2027 preparation! 🎯📚
