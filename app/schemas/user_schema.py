from app import ma
from app.models.user import User, UserRole
from marshmallow import fields

class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        load_instance = True
        exclude = ('password',)

    role = fields.Enum(UserRole)

user_schema = UserSchema()
users_schema = UserSchema(many=True)