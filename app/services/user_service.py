from app import db
from app.models.user import User, UserRole
from app.schemas.user_schema import user_schema, users_schema

def get_all_users():
    users = User.query.all()
    return users_schema.dump(users)

def get_user(user_id):
    user = User.query.get_or_404(user_id)
    return user_schema.dump(user)

def update_user(user_id, data):
    user = User.query.get_or_404(user_id)
    # Implement update logic
    pass

def delete_user(user_id):
    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    return '', 204

def activate_user(user_id):
    user = User.query.get_or_404(user_id)
    user.active = True
    db.session.commit()
    return user_schema.dump(user)

def deactivate_user(user_id):
    user = User.query.get_or_404(user_id)
    user.active = False
    db.session.commit()
    return user_schema.dump(user)

def promote_user(user_id):
    user = User.query.get_or_404(user_id)
    user.role = UserRole.ADMIN
    db.session.commit()
    return user_schema.dump(user)