


# ---- test z ---- 



# from flask import Blueprint, request, jsonify
# from app.services import user_service
# from flask_jwt_extended import jwt_required, get_jwt_identity

# user_bp = Blueprint('user', __name__, url_prefix='/users')

# @user_bp.route('', methods=['GET'])
# @jwt_required()
# def get_users():
#     return user_service.get_users()

# @user_bp.route('/<int:user_id>', methods=['GET'])
# @jwt_required()
# def get_user(user_id):
#     return user_service.get_user(user_id)

# @user_bp.route('/<int:user_id>', methods=['PUT'])
# @jwt_required()
# def update_user(user_id):
#     return user_service.update_user(user_id, request.json)

# @user_bp.route('/<int:user_id>', methods=['DELETE'])
# @jwt_required()
# def delete_user(user_id):
#     return user_service.delete_user(user_id)

# @user_bp.route('/<int:user_id>/activate', methods=['PUT'])
# @jwt_required()
# def activate_user(user_id):
#     return user_service.activate_user(user_id)

# @user_bp.route('/<int:user_id>/deactivate', methods=['PUT'])
# @jwt_required()
# def deactivate_user(user_id):
#     return user_service.deactivate_user(user_id)

# @user_bp.route('/<int:user_id>/promote', methods=['PUT'])
# @jwt_required()
# def promote_user(user_id):
#     return user_service.promote_user(user_id)



from flask import Blueprint, request, jsonify
from app.services import user_service
from flask_jwt_extended import jwt_required
from flasgger import swag_from

user_bp = Blueprint('user', __name__, url_prefix='/users')

@user_bp.route('', methods=['GET'])
@jwt_required()
@swag_from({
    'summary': 'Get users',
    'description': 'Retrieve all users if the current user is an admin, otherwise retrieve the current user’s details.',
    'responses': {
        200: {
            'description': 'List of users or user details',
            'schema': {
                'type': 'array',
                'items': {
                    'type': 'object',
                    'properties': {
                        'id': {'type': 'integer'},
                        'username': {'type': 'string'},
                        'first_name': {'type': 'string'},
                        'last_name': {'type': 'string'},
                        'email': {'type': 'string'},
                        'role': {'type': 'string'},
                        'active': {'type': 'boolean'}
                    }
                }
            }
        },
        403: {
            'description': 'Unauthorized access',
            'schema': {
                'type': 'object',
                'properties': {
                    'message': {'type': 'string'}
                }
            }
        }
    },
    'operationId': 'get_users'
})
def get_users():
    return user_service.get_users()

@user_bp.route('/<int:user_id>', methods=['GET'])
@jwt_required()
@swag_from({
    'summary': 'Get a user by ID',
    'description': 'Retrieve a specific user by their ID if the current user is an admin or is the same user.',
    'parameters': [
        {
            'name': 'user_id',
            'in': 'path',
            'type': 'integer',
            'required': True,
            'description': 'ID of the user to retrieve'
        }
    ],
    'responses': {
        200: {
            'description': 'User details',
            'schema': {
                'type': 'object',
                'properties': {
                    'id': {'type': 'integer'},
                    'username': {'type': 'string'},
                    'first_name': {'type': 'string'},
                    'last_name': {'type': 'string'},
                    'email': {'type': 'string'},
                    'role': {'type': 'string'},
                    'active': {'type': 'boolean'}
                }
            }
        },
        403: {
            'description': 'Unauthorized access',
            'schema': {
                'type': 'object',
                'properties': {
                    'message': {'type': 'string'}
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
    },
    'operationId': 'get_user'
})
def get_user(user_id):
    return user_service.get_user(user_id)

@user_bp.route('/<int:user_id>', methods=['PUT'])
@jwt_required()
@swag_from({
    'summary': 'Update a user',
    'description': 'Update user details if the current user is an admin or is the same user.',
    'parameters': [
        {
            'name': 'user_id',
            'in': 'path',
            'type': 'integer',
            'required': True,
            'description': 'ID of the user to update'
        },
        {
            'name': 'body',
            'in': 'body',
            'description': 'Updated user details',
            'schema': {
                'type': 'object',
                'properties': {
                    'username': {'type': 'string'},
                    'first_name': {'type': 'string'},
                    'last_name': {'type': 'string'},
                    'email': {'type': 'string'}
                }
            }
        }
    ],
    'responses': {
        200: {
            'description': 'User details updated successfully',
            'schema': {
                'type': 'object',
                'properties': {
                    'id': {'type': 'integer'},
                    'username': {'type': 'string'},
                    'first_name': {'type': 'string'},
                    'last_name': {'type': 'string'},
                    'email': {'type': 'string'},
                    'role': {'type': 'string'},
                    'active': {'type': 'boolean'}
                }
            }
        },
        403: {
            'description': 'Unauthorized access',
            'schema': {
                'type': 'object',
                'properties': {
                    'message': {'type': 'string'}
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
    },
    'operationId': 'update_user'
})
def update_user(user_id):
    return user_service.update_user(user_id, request.json)

@user_bp.route('/<int:user_id>', methods=['DELETE'])
@jwt_required()
@swag_from({
    'summary': 'Delete a user',
    'description': 'Delete a specific user if the current user is an admin.',
    'parameters': [
        {
            'name': 'user_id',
            'in': 'path',
            'type': 'integer',
            'required': True,
            'description': 'ID of the user to delete'
        }
    ],
    'responses': {
        200: {
            'description': 'User deleted successfully'
        },
        403: {
            'description': 'Unauthorized access',
            'schema': {
                'type': 'object',
                'properties': {
                    'message': {'type': 'string'}
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
    },
    'operationId': 'delete_user'
})
def delete_user(user_id):
    return user_service.delete_user(user_id)

@user_bp.route('/<int:user_id>/activate', methods=['PUT'])
@jwt_required()
@swag_from({
    'summary': 'Activate a user',
    'description': 'Activate a specific user if the current user is an admin.',
    'parameters': [
        {
            'name': 'user_id',
            'in': 'path',
            'type': 'integer',
            'required': True,
            'description': 'ID of the user to activate'
        }
    ],
    'responses': {
        200: {
            'description': 'User activated successfully',
            'schema': {
                'type': 'object',
                'properties': {
                    'id': {'type': 'integer'},
                    'username': {'type': 'string'},
                    'first_name': {'type': 'string'},
                    'last_name': {'type': 'string'},
                    'email': {'type': 'string'},
                    'role': {'type': 'string'},
                    'active': {'type': 'boolean'}
                }
            }
        },
        403: {
            'description': 'Unauthorized access',
            'schema': {
                'type': 'object',
                'properties': {
                    'message': {'type': 'string'}
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
    },
    'operationId': 'activate_user'
})
def activate_user(user_id):
    return user_service.activate_user(user_id)

@user_bp.route('/<int:user_id>/deactivate', methods=['PUT'])
@jwt_required()
@swag_from({
    'summary': 'Deactivate a user',
    'description': 'Deactivate a specific user if the current user is an admin.',
    'parameters': [
        {
            'name': 'user_id',
            'in': 'path',
            'type': 'integer',
            'required': True,
            'description': 'ID of the user to deactivate'
        }
    ],
    'responses': {
        200: {
            'description': 'User deactivated successfully',
            'schema': {
                'type': 'object',
                'properties': {
                    'id': {'type': 'integer'},
                    'username': {'type': 'string'},
                    'first_name': {'type': 'string'},
                    'last_name': {'type': 'string'},
                    'email': {'type': 'string'},
                    'role': {'type': 'string'},
                    'active': {'type': 'boolean'}
                }
            }
        },
        403: {
            'description': 'Unauthorized access',
            'schema': {
                'type': 'object',
                'properties': {
                    'message': {'type': 'string'}
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
    },
    'operationId': 'deactivate_user'
})
def deactivate_user(user_id):
    return user_service.deactivate_user(user_id)

@user_bp.route('/<int:user_id>/promote', methods=['PUT'])
@jwt_required()
@swag_from({
    'summary': 'Promote a user to admin',
    'description': 'Promote a specific user to admin if the current user is an admin.',
    'parameters': [
        {
            'name': 'user_id',
            'in': 'path',
            'type': 'integer',
            'required': True,
            'description': 'ID of the user to promote'
        }
    ],
    'responses': {
        200: {
            'description': 'User promoted to admin successfully',
            'schema': {
                'type': 'object',
                'properties': {
                    'id': {'type': 'integer'},
                    'username': {'type': 'string'},
                    'first_name': {'type': 'string'},
                    'last_name': {'type': 'string'},
                    'email': {'type': 'string'},
                    'role': {'type': 'string'},
                    'active': {'type': 'boolean'}
                }
            }
        },
        403: {
            'description': 'Unauthorized access',
            'schema': {
                'type': 'object',
                'properties': {
                    'message': {'type': 'string'}
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
    },
    'operationId': 'promote_user'
})
def promote_user(user_id):
    return user_service.promote_user(user_id)
