import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-secret-key-change-in-production'
    MONGO_URI = os.environ.get('MONGO_URI') or 'mongodb+srv://239x1a32b0_db_user:a3cTQ*CA6base9A@cluster0.umwhot3.mongodb.net/gate_planner?retryWrites=true&w=majority&appName=Cluster0'
    
    # Date range for GATE preparation
    START_DATE = '2026-01-01'
    END_DATE = '2027-02-15'
    
    # Study goal
    DAILY_HOURS_GOAL = 5

class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False

config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
