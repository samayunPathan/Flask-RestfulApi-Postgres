from flask import Blueprint, request, jsonify
from app.services import user_service
from flask_jwt_extended import jwt_required
from flasgger import swag_from

user_bp = Blueprint('user', __name__, url_prefix='/users')

@user_bp.route('', methods=['GET'])
@jwt_required()
@swag_from({
    'tags': ['User Management'],
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
    'security': [{'Bearer': ['Bearer']}]
  
})
def get_users():
    return user_service.get_users()

@user_bp.route('/<int:user_id>', methods=['GET'])
@jwt_required()
@swag_from({
    'tags': ['User Management'],
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
    'security': [{'Bearer': ['Bearer']}]
})


def get_user(user_id):
    return user_service.get_user(user_id)



@user_bp.route('/<int:user_id>', methods=['PUT'])
@jwt_required()
@swag_from({
    'tags': ['User Management'],
    'summary': 'Update, activate, deactivate, or promote a user',
    'description': 'Update user details, activate, deactivate, or promote a user if the current user is an admin, or is the same user for updates.',
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
            'description': 'Updated user details or action (activate, deactivate, promote)',
            'schema': {
                'type': 'object',
                'properties': {
                    'username': {'type': 'string'},
                    'first_name': {'type': 'string'},
                    'last_name': {'type': 'string'},
                    'email': {'type': 'string'},
                    'role': {'type': 'string'},
                    'active': {'type': 'boolean'}
                }
            }
        }
    ],
    'responses': {
        200: {
            'description': 'User updated successfully',
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
    'security': [{'Bearer': ['Bearer']}]
})
def update_user(user_id):
    return user_service.update_user(user_id, request.json)


@user_bp.route('/<int:user_id>', methods=['DELETE'])
@jwt_required()
@swag_from({
    'tags': ['User Management'],
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
    'security': [{'Bearer': ['Bearer']}]
})
def delete_user(user_id):
    return user_service.delete_user(user_id)


