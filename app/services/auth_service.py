from app import db, bcrypt
from app.models.user import User
from flask_jwt_extended import create_access_token
from app.schemas.user_schema import user_schema
from datetime import datetime
from flask import jsonify
import uuid

# def register_user(data):
#     """
#     Register a new user.
#     """
#     username = data.get('username')
#     first_name = data.get('first_name')
#     last_name = data.get('last_name')
#     email = data.get('email')
#     password = data.get('password')

#     # Check if user already exists
#     if User.query.filter_by(email=email).first():
#         return jsonify({"message": "User already exists"}), 400

#     # Hash the password
#     hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

#     new_user = User(
#         username=username,
#         first_name=first_name,
#         last_name=last_name,
#         email=email,
#         password=hashed_password
#     )

#     db.session.add(new_user)
#     db.session.commit()

#     return jsonify({"message": "User registered successfully"}), 201

from app import db, bcrypt
from app.models.user import User
from flask_jwt_extended import create_access_token
from app.schemas.user_schema import user_schema

def register_user(data):
    if not data:
        return {"message": "No data provided"}, 400
    
    try:
        # Extract data from the request
        username = data.get('username')
        first_name = data.get('first_name')
        last_name = data.get('last_name')
        email = data.get('email')
        password = data.get('password')
        role = data.get('role', 'user')  # default to 'user'

        # Check if user already exists
        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            return {"message": "User already exists"}, 400

        # Hash the password
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

        # Create a new user
        new_user = User(
            username=username,
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=hashed_password,
            role=role
        )
        db.session.add(new_user)
        db.session.commit()

        # Generate an access token (optional)
        access_token = create_access_token(identity={'email': email})

        return {
            "message": "User registered successfully",
            "access_token": access_token
        }, 201

    except Exception as e:
        # Log the error
        print(f"Error during registration: {str(e)}")
        return {"message": "An error occurred during registration", "error": str(e)}, 500


def login_user(data):
    """
    Login a user.
    """
    email = data.get('email')
    password = data.get('password')

    user = User.query.filter_by(email=email).first()

    if not user or not bcrypt.check_password_hash(user.password, password):
        return jsonify({"message": "Invalid email or password"}), 401

    access_token = create_access_token(identity=user.id)
    return jsonify(access_token=access_token), 200

def forgot_password(data):
    """
    Handle forgot password.
    """
    email = data.get('email')

    user = User.query.filter_by(email=email).first()

    if not user:
        return jsonify({"message": "User not found"}), 404

    # In a real application, send a reset token to the user's email
    reset_token = str(uuid.uuid4())
    user.reset_token = reset_token
    user.reset_token_expires_at = datetime.utcnow() + timedelta(hours=1)
    db.session.commit()

    # Send email logic here
    return jsonify({"message": "Password reset token sent to email"}), 200

def reset_password(data):
    """
    Reset a user's password.
    """
    reset_token = data.get('reset_token')
    new_password = data.get('new_password')

    user = User.query.filter_by(reset_token=reset_token).first()

    if not user or user.reset_token_expires_at < datetime.utcnow():
        return jsonify({"message": "Invalid or expired reset token"}), 400

    hashed_password = bcrypt.generate_password_hash(new_password).decode('utf-8')
    user.password = hashed_password
    user.reset_token = None
    user.reset_token_expires_at = None
    db.session.commit()

    return jsonify({"message": "Password reset successfully"}), 200
