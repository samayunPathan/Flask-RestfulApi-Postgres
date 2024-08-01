
# from flask import Blueprint, request, jsonify
# from app.services import auth_service

# auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

# @auth_bp.route('/register', methods=['POST'])
# def register():
#     return auth_service.register_user(request.json)

# @auth_bp.route('/login', methods=['GET','POST'])
# def login():
#     return auth_service.login_user(request.json)

# @auth_bp.route('/forgot-password', methods=['POST'])
# def forgot_password():
#     return auth_service.forgot_password(request.json)

# @auth_bp.route('/reset-password', methods=['POST'])
# def reset_password():
#     return auth_service.reset_password(request.json)



from flask import Blueprint, request, jsonify
from app.services import auth_service
from flasgger import swag_from

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

@auth_bp.route('/register', methods=['POST'])
@swag_from({
    'summary': 'Register a new user',
    'description': 'Register a new user with the provided details.',
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'description': 'User registration details',
            'schema': {
                'type': 'object',
                'properties': {
                    'username': {'type': 'string', 'description': 'Username of the user'},
                    'first_name': {'type': 'string', 'description': 'First name of the user'},
                    'last_name': {'type': 'string', 'description': 'Last name of the user'},
                    'email': {'type': 'string', 'description': 'Email address of the user'},
                    'password': {'type': 'string', 'description': 'Password of the user'},
                    'secret_admin_key': {'type': 'string', 'description': 'Optional admin key for admin role'}
                },
                'required': ['username', 'email', 'password']
            }
        }
    ],
    'responses': {
        201: {
            'description': 'User registered successfully',
            'schema': {
                'type': 'object',
                'properties': {
                    'message': {'type': 'string', 'example': 'User registered successfully'},
                    'details': {
                        'type': 'object',
                        'properties': {
                            'username': {'type': 'string'},
                            'role': {'type': 'string'}
                        }
                    },
                    'access_token': {'type': 'string', 'example': 'JWT_TOKEN_HERE'}
                }
            }
        },
        400: {
            'description': 'Invalid input or user already exists',
            'schema': {
                'type': 'object',
                'properties': {
                    'message': {'type': 'string'}
                }
            }
        },
        500: {
            'description': 'Internal server error',
            'schema': {
                'type': 'object',
                'properties': {
                    'message': {'type': 'string'},
                    'error': {'type': 'string'}
                }
            }
        }
    }
})
def register():
    return auth_service.register_user(request.json)

@auth_bp.route('/login', methods=['POST'])
@swag_from({
    'summary': 'Login user',
    'description': 'Login a user and return a JWT token.',
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'description': 'User login details',
            'schema': {
                'type': 'object',
                'properties': {
                    'email': {'type': 'string', 'description': 'Email address of the user'},
                    'password': {'type': 'string', 'description': 'Password of the user'}
                },
                'required': ['email', 'password']
            }
        }
    ],
    'responses': {
        200: {
            'description': 'Login successful',
            'schema': {
                'type': 'object',
                'properties': {
                    'access_token': {'type': 'string', 'example': 'JWT_TOKEN_HERE'}
                }
            }
        },
        401: {
            'description': 'Invalid email or password',
            'schema': {
                'type': 'object',
                'properties': {
                    'message': {'type': 'string'}
                }
            }
        }
    }
})
def login():
    return auth_service.login_user(request.json)

@auth_bp.route('/forgot-password', methods=['POST'])
@swag_from({
    'summary': 'Forgot password',
    'description': 'Request a password reset link.',
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'description': 'Email address for password reset',
            'schema': {
                'type': 'object',
                'properties': {
                    'email': {'type': 'string', 'description': 'Email address of the user'}
                },
                'required': ['email']
            }
        }
    ],
    'responses': {
        200: {
            'description': 'Password reset token sent',
            'schema': {
                'type': 'object',
                'properties': {
                    'message': {'type': 'string', 'example': 'Password reset token sent to email'},
                    'reset_token': {'type': 'string', 'example': 'RESET_TOKEN_HERE'}
                }
            }
        },
        404: {
            'description': 'User not found',
            'schema': {
                'type': 'object',
                'properties': {
                    'message': {'type': 'string'}
                }
            }
        }
    }
})
def forgot_password():
    return auth_service.forgot_password(request.json)

@auth_bp.route('/reset-password', methods=['POST'])
@swag_from({
    'summary': 'Reset password',
    'description': 'Reset user password using provided token and new password.',
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'description': 'Password reset details',
            'schema': {
                'type': 'object',
                'properties': {
                    'reset_token': {'type': 'string', 'description': 'Password reset token'},
                    'new_password': {'type': 'string', 'description': 'New password for the user'}
                },
                'required': ['reset_token', 'new_password']
            }
        }
    ],
    'responses': {
        200: {
            'description': 'Password successfully reset',
            'schema': {
                'type': 'object',
                'properties': {
                    'message': {'type': 'string', 'example': 'Password reset successfully'}
                }
            }
        },
        400: {
            'description': 'Invalid or expired reset token',
            'schema': {
                'type': 'object',
                'properties': {
                    'message': {'type': 'string'}
                }
            }
        }
    }
})
def reset_password():
    return auth_service.reset_password(request.json)
