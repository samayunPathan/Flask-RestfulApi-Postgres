from flask import Blueprint, request, jsonify
from app.services import user_service
from app.utils.decorators import admin_required, jwt_required

user_bp = Blueprint('user', __name__, url_prefix='/users')

@user_bp.route('/', methods=['GET'])
@jwt_required
def get_users():
    return user_service.get_all_users()

@user_bp.route('/<int:user_id>', methods=['GET'])
@jwt_required
def get_user(user_id):
    return user_service.get_user(user_id)

@user_bp.route('/<int:user_id>', methods=['PUT'])
@jwt_required
def update_user(user_id):
    return user_service.update_user(user_id, request.json)

@user_bp.route('/<int:user_id>', methods=['DELETE'])
@admin_required
def delete_user(user_id):
    return user_service.delete_user(user_id)

@user_bp.route('/<int:user_id>/activate', methods=['PUT'])
@admin_required
def activate_user(user_id):
    return user_service.activate_user(user_id)

@user_bp.route('/<int:user_id>/deactivate', methods=['PUT'])
@admin_required
def deactivate_user(user_id):
    return user_service.deactivate_user(user_id)

@user_bp.route('/<int:user_id>/promote', methods=['PUT'])
@admin_required
def promote_user(user_id):
    return user_service.promote_user(user_id)