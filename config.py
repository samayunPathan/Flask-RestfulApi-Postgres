import os
from dotenv import load_dotenv
load_dotenv()

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI =os.getenv('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY', 'your_jwt_secret_key')
    SECRET_ADMIN_KEY=os.getenv('SECRET_ADMIN_KEY')

    MAIL_SERVER=os.getenv('MAIL_SERVER')
    MAIL_PORT=os.getenv('MAIL_PORT')
    MAIL_USE_TLS=os.getenv('MAIL_USE_TLS')
    MAIL_USERNAME=os.getenv('MAIL_USERNAME')
    MAIL_PASSWORD=os.getenv('MAIL_PASSWORD')
    MAIL_DEFAULT_SENDER=pos.getenv('MAIL_DEFAULT_SENDER')


