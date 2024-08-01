

from datetime import datetime
from app import db
from sqlalchemy import Enum
import enum

class UserRole(enum.Enum):
    ADMIN = 'ADMIN'
    USER = 'USER'

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    first_name = db.Column(db.String(120), nullable=False)
    last_name = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    role = db.Column(Enum(UserRole), default=UserRole.USER)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    active = db.Column(db.Boolean, default=True)
    reset_token = db.Column(db.String(36), nullable=True)
    reset_token_expires_at = db.Column(db.DateTime, nullable=True)

    def __repr__(self):
        return f'<User {self.username}>'