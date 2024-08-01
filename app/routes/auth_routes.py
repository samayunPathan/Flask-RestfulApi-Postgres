
from flask import Blueprint, request, jsonify
from app.services import auth_service

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

@auth_bp.route('/register', methods=['POST'])
def register():
    return auth_service.register_user(request.json)

@auth_bp.route('/login', methods=['GET','POST'])
def login():
    return auth_service.login_user(request.json)

@auth_bp.route('/forgot-password', methods=['POST'])
def forgot_password():
    return auth_service.forgot_password(request.json)

@auth_bp.route('/reset-password', methods=['POST'])
def reset_password():
    return auth_service.reset_password(request.json)
