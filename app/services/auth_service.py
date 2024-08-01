


# ----- test ----- 

from app import db, bcrypt
from app.models.user import User, UserRole
from flask_jwt_extended import create_access_token, get_jwt_identity
from app.schemas.user_schema import user_schema
from datetime import datetime, timedelta
from flask import jsonify
import uuid
from config import Config


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
        secret_admin_key = data.get('secret_admin_key')  # Retrieve secret_admin_key from request body
        
        if secret_admin_key == Config.SECRET_ADMIN_KEY:
            role = 'ADMIN'
        else:
            role = 'USER'  # Default to 'USER'

        # Validate the role
        if role not in UserRole.__members__:
            return {"message": "Invalid role"}, 400

        # Check if username or email already exists
        if User.query.filter_by(username=username).first():
            return {"message": "Username already exists"}, 400
        if User.query.filter_by(email=email).first():
            return {"message": "Email already exists"}, 400

        # Hash the password
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

        # Create a new user
        new_user = User(
            username=username,
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=hashed_password,
            role=UserRole[role]  # Convert the role to UserRole enum
        )
        db.session.add(new_user)
        db.session.commit()

        # Generate an access token (optional)
        access_token = create_access_token(identity={'email': email})

# Return success message with details
        return {
            "message": "User registered successfully",
            "details": {
                "username": username,
                "role": role
            },
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

    # Generate reset token
    reset_token = str(uuid.uuid4())
    user.reset_token = reset_token
    user.reset_token_expires_at = datetime.utcnow() + timedelta(hours=1)
    db.session.commit()

    # In a real application, send the reset token to the user's email
    # Send email logic here

    return jsonify({"message": "Password reset token sent to email", "reset_token": reset_token}), 200

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

