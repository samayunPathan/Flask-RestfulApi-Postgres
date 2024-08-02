
# ------ test ----- 

from app import db
from app.models.user import User, UserRole
from app.schemas.user_schema import user_schema, users_schema
from flask import jsonify
from flask_jwt_extended import get_jwt_identity

def get_current_user():
    current_user_id = get_jwt_identity()
    return User.query.get_or_404(current_user_id)

def get_users():
    current_user = get_current_user()
    if current_user.role == UserRole.ADMIN:
        users = User.query.all()
        return jsonify(users_schema.dump(users)), 200
    else:
        return jsonify(user_schema.dump(current_user)), 200

def get_user(user_id):
    current_user = get_current_user()
    if current_user.role == UserRole.ADMIN or current_user.id == user_id:
        user = User.query.get_or_404(user_id)
        return jsonify(user_schema.dump(user)), 200
    else:
        return jsonify({"message": "Unauthorized"}), 403



def delete_user(user_id):
    current_user = get_current_user()
    if current_user.role == UserRole.ADMIN:
        user = User.query.get_or_404(user_id)
        db.session.delete(user)
        db.session.commit()
        return jsonify({"message": "User deleted successfully"}), 200
    else:
        return jsonify({"message": "Unauthorized"}), 403


def update_user(user_id, data):
    current_user = get_current_user()
    user = User.query.get_or_404(user_id)

    if current_user.role != UserRole.ADMIN and current_user.id != user_id:
        return jsonify({"message": "Unauthorized"}), 403

    # Admin can update all fields
    if current_user.role == UserRole.ADMIN:
        user.username = data.get('username', user.username)
        user.first_name = data.get('first_name', user.first_name)
        user.last_name = data.get('last_name', user.last_name)
        user.email = data.get('email', user.email)
        user.role = data.get('role', user.role)
        user.active = data.get('active', user.active)
    
    # Regular user can update only their own non-role and non-active fields
    elif current_user.id == user_id:
        if 'role' in data or 'active' in data:
            return jsonify({"message": "Unauthorized to change role or active status"}), 403
        user.username = data.get('username', user.username)
        user.first_name = data.get('first_name', user.first_name)
        user.last_name = data.get('last_name', user.last_name)
        user.email = data.get('email', user.email)
    
    db.session.commit()
    return jsonify(user_schema.dump(user)), 200




