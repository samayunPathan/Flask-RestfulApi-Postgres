from functools import wraps
from flask_jwt_extended import verify_jwt_in_request, get_jwt_identity
from app.models.user import User, UserRole

def jwt_required(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        verify_jwt_in_request()
        return fn(*args, **kwargs)
    return wrapper

def admin_required(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        verify_jwt_in_request()
        current_user = User.query.get(get_jwt_identity())
        if current_user.role != UserRole.ADMIN:
            return {'message': 'Admin access required'}, 403
        return fn(*args, **kwargs)
    return wrapper