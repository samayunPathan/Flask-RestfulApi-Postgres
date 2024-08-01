


# ---- test z ---- 



from flask import Blueprint, request, jsonify
from app.services import user_service
from flask_jwt_extended import jwt_required, get_jwt_identity

user_bp = Blueprint('user', __name__, url_prefix='/users')

@user_bp.route('', methods=['GET'])
@jwt_required()
def get_users():
    return user_service.get_users()

@user_bp.route('/<int:user_id>', methods=['GET'])
@jwt_required()
def get_user(user_id):
    return user_service.get_user(user_id)

@user_bp.route('/<int:user_id>', methods=['PUT'])
@jwt_required()
def update_user(user_id):
    return user_service.update_user(user_id, request.json)

@user_bp.route('/<int:user_id>', methods=['DELETE'])
@jwt_required()
def delete_user(user_id):
    return user_service.delete_user(user_id)

@user_bp.route('/<int:user_id>/activate', methods=['PUT'])
@jwt_required()
def activate_user(user_id):
    return user_service.activate_user(user_id)

@user_bp.route('/<int:user_id>/deactivate', methods=['PUT'])
@jwt_required()
def deactivate_user(user_id):
    return user_service.deactivate_user(user_id)

@user_bp.route('/<int:user_id>/promote', methods=['PUT'])
@jwt_required()
def promote_user(user_id):
    return user_service.promote_user(user_id)