from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from flask_marshmallow import Marshmallow
from flask_bcrypt import Bcrypt
from config import Config

db = SQLAlchemy()
migrate = Migrate()
jwt = JWTManager()
ma = Marshmallow()
bcrypt = Bcrypt()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)
    ma.init_app(app)
    bcrypt.init_app(app)

    from app.routes import auth_routes, user_routes
    app.register_blueprint(auth_routes.auth_bp)
    app.register_blueprint(user_routes.user_bp)

    return app

# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate
# from flask_jwt_extended import JWTManager
# from flask_marshmallow import Marshmallow
# from flask_bcrypt import Bcrypt
# from config import Config

# db = SQLAlchemy()
# migrate = Migrate()
# jwt = JWTManager()
# ma = Marshmallow()
# bcrypt = Bcrypt()

# def create_app():
#     app = Flask(__name__)
#     app.config.from_object(Config)

#     db.init_app(app)
#     migrate.init_app(app, db)
#     jwt.init_app(app)
#     ma.init_app(app)
#     bcrypt.init_app(app)

#     from app.routes.auth_routes import auth_bp
#     app.register_blueprint(auth_bp)

#     return app
