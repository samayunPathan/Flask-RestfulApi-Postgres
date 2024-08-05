import uuid
from datetime import datetime, timedelta
from flask import jsonify, current_app, url_for
from flask_mail import Message
from werkzeug.security import generate_password_hash
from app import db, bcrypt
from flask_jwt_extended import create_access_token, get_jwt_identity
from app.models.user import User, UserRole
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

<<<<<<< HEAD
=======

>>>>>>> 9761ea6250fbb498607682041185ca47ca089a61
# Return success message with details
        return {
            "message": "User registered successfully",
            "details": {
                "username": username,
                "role": role
            }
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
    format_token=f"Bearer {access_token}"
<<<<<<< HEAD
    return jsonify(access_token=format_token), 200


def send_reset_email(user, reset_token):
    from app import mail  # Importing within the app context

    reset_url = url_for('auth.reset_password', _external=True)
    
    msg = Message('Password Reset Request',
                  sender=current_app.config['MAIL_DEFAULT_SENDER'],
                  recipients=[user.email])
    msg.body = f'''To reset your password, use the following token:
{reset_token}

Submit a POST request to {reset_url} with the following JSON body:
{{
    "email": "{user.email}",
    "reset_token": "{reset_token}",
    "new_password": "your_new_password"
}}

If you did not make this request then simply ignore this email and no changes will be made.
'''
    mail.send(msg)
=======
    return jsonify(format_token=format_token), 200
   
>>>>>>> 9761ea6250fbb498607682041185ca47ca089a61

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
    

    # return jsonify(reset_token=reset_token) # ........  for testing purpose  u can comment it .....
    # Send email
    try:
        send_reset_email(user, reset_token)
        return jsonify({"message": "Password reset token sent to email"},reset_token=reset_token), 200
    except Exception as e:
        # Log the error here
        print(f"Failed to send email: {str(e)}")
        return jsonify({"message": "Failed to send reset email. Please try again later."}), 500

def reset_password(data):
    """
    Reset a user's password.
    """
    email = data.get('email')
    reset_token = data.get('reset_token')
    new_password = data.get('new_password')
    
    user = User.query.filter_by(email=email, reset_token=reset_token).first()
    
    if not user or user.reset_token_expires_at < datetime.utcnow():
        return jsonify({"message": "Invalid or expired reset token"}), 400
    
    hashed_password = generate_password_hash(new_password)
    user.password = hashed_password
    user.reset_token = None
    user.reset_token_expires_at = None
    db.session.commit()
    
    return jsonify({"message": "Password reset successfully"}), 200



