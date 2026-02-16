# 🚀 Quick Start Guide

## For Windows Users

### Option 1: Double-click to run
1. Double-click `run.bat`
2. Wait for installation to complete
3. Open browser: `http://localhost:5000`
4. Login with:
   - Username: `sohel` or `anju`
   - Password: `sohel123` or `anju123`

### Option 2: Manual commands
```cmd
pip install -r requirements.txt
python app.py
```

---

## For Mac/Linux Users

```bash
# Install dependencies
pip install -r requirements.txt

# Run the app
python app.py
```

Then open: `http://localhost:5000`

---

## Default Login Credentials

### User 1: Sohel
- Username: `sohel`
- Password: `sohel123`

### User 2: Anju
- Username: `anju`
- Password: `anju123`

---

## First Steps After Login

1. ✅ View your dashboard
2. ✅ Click "Add Today's Entry"
3. ✅ Fill in your study details
4. ✅ Check the calendar view
5. ✅ Explore analytics

---

## Need Help?

- Read `README.md` for full documentation
- Check `SETUP.md` for detailed setup
- See `DEPLOYMENT.md` for hosting online
- Review `PROJECT_OVERVIEW.md` for technical details

---

## MongoDB Connection

Already configured! The app connects to:
```
MongoDB Atlas Cloud Database
Database: gate_planner
Collections: users, daily_logs
```

No additional setup needed!

---

## Troubleshooting

### Can't install dependencies?
```bash
# Try upgrading pip first
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### Port 5000 already in use?
Edit `app.py` line at the bottom:
```python
app.run(debug=True, host='0.0.0.0', port=5001)
```

### Can't connect to MongoDB?
- Check your internet connection
- The MongoDB URI is already configured
- No additional setup needed

---

## What's Next?

1. Test all features locally
2. Customize if needed
3. Deploy to Render/Railway (see DEPLOYMENT.md)
4. Share with Sohel and Anju
5. Start tracking GATE preparation!

---

**Happy Studying! 📚🎯**
