import streamlit as st
from pymongo import MongoClient
from werkzeug.security import check_password_hash, generate_password_hash
from datetime import datetime, timedelta
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from bson import ObjectId

# Page config
st.set_page_config(
    page_title="GATE Daily Planner 2026",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="expanded"
)

# MongoDB connection
@st.cache_resource
def init_connection():
    return MongoClient('mongodb+srv://239x1a32b0_db_user:a3cTQ*CA6base9A@cluster0.umwhot3.mongodb.net/gate_planner?retryWrites=true&w=majority&appName=Cluster0')

client = init_connection()
db = client.gate_planner

# Date range constants
START_DATE = datetime(2026, 1, 1)
END_DATE = datetime(2027, 2, 15)

# Initialize session state
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
if 'username' not in st.session_state:
    st.session_state.username = None
if 'gender' not in st.session_state:
    st.session_state.gender = None

# Custom CSS
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        color: #2563EB;
        text-align: center;
        margin-bottom: 2rem;
    }
    .stat-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 1.5rem;
        border-radius: 10px;
        color: white;
        text-align: center;
    }
    .stat-value {
        font-size: 2rem;
        font-weight: bold;
    }
    .stat-label {
        font-size: 0.9rem;
        opacity: 0.9;
    }
</style>
""", unsafe_allow_html=True)

def login_page():
    st.markdown('<div class="main-header">📚 GATE Daily Planner 2026</div>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        st.subheader("Login")
        username = st.text_input("Username", key="login_username").lower()
        password = st.text_input("Password", type="password", key="login_password")
        
        if st.button("Login", use_container_width=True):
            user = db.users.find_one({'username': username})
            
            if user and check_password_hash(user['password_hash'], password):
                st.session_state.logged_in = True
                st.session_state.username = username
                st.session_state.gender = user['gender']
                st.success("Login successful!")
                st.rerun()
            else:
                st.error("Invalid username or password")

def calculate_streaks(logs):
    if not logs:
        return 0, 0
    
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

def dashboard_page():
    st.markdown('<div class="main-header">📊 Dashboard</div>', unsafe_allow_html=True)
    
    username = st.session_state.username
    logs = list(db.daily_logs.find({'username': username}).sort('date', -1))
    
    # Calculate statistics
    total_days = len(logs)
    completed_days = len([log for log in logs if log.get('completed')])
    total_hours = sum([log.get('hours_studied', 0) for log in logs])
    completion_percentage = (completed_days / total_days * 100) if total_days > 0 else 0
    current_streak, longest_streak = calculate_streaks(logs)
    
    # Partner stats
    partner = 'anju' if username == 'sohel' else 'sohel'
    partner_logs = list(db.daily_logs.find({'username': partner}))
    partner_completed = len([log for log in partner_logs if log.get('completed')])
    partner_total = len(partner_logs)
    partner_percentage = (partner_completed / partner_total * 100) if partner_total > 0 else 0
    
    # Display stats
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Total Days", total_days)
        st.metric("Completed Days", completed_days)
    
    with col2:
        st.metric("Total Hours", f"{total_hours:.1f}")
        st.metric("Completion %", f"{completion_percentage:.1f}%")
    
    with col3:
        st.metric("Current Streak", f"{current_streak} days")
        st.metric("Longest Streak", f"{longest_streak} days")
    
    with col4:
        st.metric(f"{partner.capitalize()}'s Progress", f"{partner_percentage:.1f}%")
    
    # Recent entries
    st.subheader("Recent Entries")
    if logs:
        for log in logs[:5]:
            with st.expander(f"{log['date'].strftime('%Y-%m-%d')} - {log.get('subject', 'N/A')}"):
                st.write(f"**Hours Studied:** {log.get('hours_studied', 0)}")
                st.write(f"**Topics:** {log.get('topics', 'N/A')}")
                st.write(f"**Mood:** {log.get('mood', 'N/A')}")
                st.write(f"**Completed:** {'✅' if log.get('completed') else '❌'}")
                st.write(f"**Description:** {log.get('description', 'N/A')}")
    else:
        st.info("No entries yet. Add your first entry!")

def calendar_page():
    st.markdown('<div class="main-header">📅 Calendar</div>', unsafe_allow_html=True)
    
    username = st.session_state.username
    
    col1, col2 = st.columns([3, 1])
    with col1:
        selected_date = st.date_input("Select Month", datetime.now(), min_value=START_DATE, max_value=END_DATE)
    
    year = selected_date.year
    month = selected_date.month
    
    # Get logs for the month
    start = datetime(year, month, 1)
    if month == 12:
        end = datetime(year + 1, 1, 1)
    else:
        end = datetime(year, month + 1, 1)
    
    logs = list(db.daily_logs.find({
        'username': username,
        'date': {'$gte': start, '$lt': end}
    }))
    
    # Create calendar view
    if logs:
        df = pd.DataFrame(logs)
        df['date_str'] = df['date'].dt.strftime('%Y-%m-%d')
        df['status'] = df['completed'].apply(lambda x: '✅ Completed' if x else '❌ Incomplete')
        
        st.dataframe(
            df[['date_str', 'subject', 'hours_studied', 'topics', 'mood', 'status']].rename(columns={
                'date_str': 'Date',
                'subject': 'Subject',
                'hours_studied': 'Hours',
                'topics': 'Topics',
                'mood': 'Mood',
                'status': 'Status'
            }),
            use_container_width=True,
            hide_index=True
        )
    else:
        st.info("No entries for this month")

def add_entry_page():
    st.markdown('<div class="main-header">➕ Add Entry</div>', unsafe_allow_html=True)
    
    username = st.session_state.username
    
    with st.form("add_entry_form"):
        date = st.date_input("Date", datetime.now(), min_value=START_DATE, max_value=END_DATE)
        hours_studied = st.number_input("Hours Studied", min_value=0.0, max_value=24.0, value=5.0, step=0.5)
        subject = st.selectbox("Subject", ["Mathematics", "Physics", "Chemistry", "Computer Science", "Other"])
        topics = st.text_input("Topics Covered")
        description = st.text_area("Description")
        mood = st.select_slider("Mood", options=["😢 Bad", "😐 Okay", "😊 Good", "😄 Great", "🤩 Excellent"])
        completed = st.checkbox("Mark as Completed")
        
        submitted = st.form_submit_button("Add Entry", use_container_width=True)
        
        if submitted:
            date_obj = datetime.combine(date, datetime.min.time())
            
            # Check if entry exists
            existing = db.daily_logs.find_one({'username': username, 'date': date_obj})
            if existing:
                st.error("Entry for this date already exists. Please edit it instead.")
            else:
                entry = {
                    'username': username,
                    'date': date_obj,
                    'hours_studied': hours_studied,
                    'subject': subject,
                    'topics': topics,
                    'description': description,
                    'mood': mood,
                    'completed': completed,
                    'created_at': datetime.now()
                }
                
                db.daily_logs.insert_one(entry)
                st.success("Entry added successfully!")
                st.balloons()

def analytics_page():
    st.markdown('<div class="main-header">📈 Analytics</div>', unsafe_allow_html=True)
    
    username = st.session_state.username
    logs = list(db.daily_logs.find({'username': username}).sort('date', 1))
    
    if not logs:
        st.info("No data available for analytics")
        return
    
    df = pd.DataFrame(logs)
    
    # Monthly study hours
    df['month'] = df['date'].dt.strftime('%Y-%m')
    monthly_hours = df.groupby('month')['hours_studied'].sum().reset_index()
    
    fig1 = px.bar(monthly_hours, x='month', y='hours_studied', 
                  title='Monthly Study Hours',
                  labels={'month': 'Month', 'hours_studied': 'Hours Studied'})
    st.plotly_chart(fig1, use_container_width=True)
    
    # Subject-wise distribution
    subject_hours = df.groupby('subject')['hours_studied'].sum().reset_index()
    
    fig2 = px.pie(subject_hours, values='hours_studied', names='subject',
                  title='Subject-wise Study Distribution')
    st.plotly_chart(fig2, use_container_width=True)
    
    # Completion rate over time
    df['week'] = df['date'].dt.strftime('%Y-W%U')
    weekly_completion = df.groupby('week')['completed'].mean().reset_index()
    weekly_completion['completion_rate'] = weekly_completion['completed'] * 100
    
    fig3 = px.line(weekly_completion, x='week', y='completion_rate',
                   title='Weekly Completion Rate (%)',
                   labels={'week': 'Week', 'completion_rate': 'Completion Rate (%)'})
    st.plotly_chart(fig3, use_container_width=True)

def main():
    if not st.session_state.logged_in:
        login_page()
    else:
        # Sidebar
        with st.sidebar:
            st.title(f"Welcome, {st.session_state.username.capitalize()}! 👋")
            
            page = st.radio("Navigation", 
                          ["Dashboard", "Calendar", "Add Entry", "Analytics"],
                          label_visibility="collapsed")
            
            st.divider()
            
            if st.button("Logout", use_container_width=True):
                st.session_state.logged_in = False
                st.session_state.username = None
                st.session_state.gender = None
                st.rerun()
        
        # Main content
        if page == "Dashboard":
            dashboard_page()
        elif page == "Calendar":
            calendar_page()
        elif page == "Add Entry":
            add_entry_page()
        elif page == "Analytics":
            analytics_page()

if __name__ == "__main__":
    main()
