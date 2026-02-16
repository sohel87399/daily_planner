# Deployment Guide

## Prerequisites
- Git installed
- GitHub account (for Render/Railway)
- MongoDB Atlas connection (already configured)

## Deploy to Render (Recommended)

### Step 1: Prepare Your Code
```bash
# Make sure all files are committed
git add .
git commit -m "Initial commit"
git push origin main
```

### Step 2: Create Render Account
1. Go to https://render.com
2. Sign up with GitHub

### Step 3: Create New Web Service
1. Click "New +" button
2. Select "Web Service"
3. Connect your GitHub repository
4. Click "Connect" next to your repo

### Step 4: Configure Service
- **Name**: `gate-planner-2026`
- **Region**: Choose closest to you
- **Branch**: `main`
- **Root Directory**: Leave empty
- **Environment**: `Python 3`
- **Build Command**: `pip install -r requirements.txt`
- **Start Command**: `gunicorn app:app`
- **Instance Type**: Free

### Step 5: Add Environment Variables
Click "Advanced" → "Add Environment Variable":
- **Key**: `SECRET_KEY`
- **Value**: Generate using: `python -c "import secrets; print(secrets.token_hex(32))"`

### Step 6: Deploy
1. Click "Create Web Service"
2. Wait 2-3 minutes for deployment
3. Your app will be live at: `https://gate-planner-2026.onrender.com`

---

## Deploy to Railway

### Step 1: Create Railway Account
1. Go to https://railway.app
2. Sign up with GitHub

### Step 2: Create New Project
1. Click "New Project"
2. Select "Deploy from GitHub repo"
3. Choose your repository

### Step 3: Configure
Railway auto-detects Flask. Just add:
- Environment Variable: `SECRET_KEY` = (generate random key)

### Step 4: Deploy
- Railway automatically deploys
- Get your URL from the dashboard

---

## Deploy to Heroku

### Step 1: Install Heroku CLI
Download from: https://devcenter.heroku.com/articles/heroku-cli

### Step 2: Login
```bash
heroku login
```

### Step 3: Create App
```bash
heroku create gate-planner-2026
```

### Step 4: Set Environment Variables
```bash
heroku config:set SECRET_KEY=$(python -c "import secrets; print(secrets.token_hex(32))")
```

### Step 5: Deploy
```bash
git push heroku main
```

### Step 6: Open App
```bash
heroku open
```

---

## Post-Deployment Checklist

✅ Test login with both users
✅ Add a sample entry
✅ Check calendar view
✅ Verify analytics page
✅ Test on mobile device
✅ Check MongoDB connection
✅ Verify all features work

---

## Custom Domain (Optional)

### For Render:
1. Go to Settings → Custom Domain
2. Add your domain
3. Update DNS records as shown

### For Railway:
1. Go to Settings → Domains
2. Add custom domain
3. Update DNS records

---

## Monitoring

### Render:
- View logs in Dashboard → Logs
- Monitor usage in Dashboard → Metrics

### Railway:
- View logs in Deployments tab
- Monitor in Metrics tab

---

## Updating Your App

```bash
# Make changes to code
git add .
git commit -m "Update message"
git push origin main
```

Render/Railway will auto-deploy the changes.

---

## Troubleshooting Deployment

### Issue: Build Failed
- Check requirements.txt has all dependencies
- Verify Python version compatibility

### Issue: App Crashes on Start
- Check logs for errors
- Verify MongoDB connection string
- Ensure SECRET_KEY is set

### Issue: Can't Access App
- Wait 2-3 minutes after deployment
- Check if service is running
- Verify no build errors

---

## Production Checklist

Before going live:
1. ✅ Change SECRET_KEY to secure random value
2. ✅ Update default passwords
3. ✅ Test all features
4. ✅ Enable HTTPS (automatic on Render/Railway)
5. ✅ Monitor logs for errors
6. ✅ Set up error tracking (optional)

---

Your GATE Daily Planner is now live! 🚀
