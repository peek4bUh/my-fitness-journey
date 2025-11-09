import secrets
from flask import Flask, abort, request

from core.config import DevelopmentConfig
from core.extensions import api


def create_app():
    app = Flask(__name__,
                template_folder='./ui/templates',
                static_folder='./ui/static')
    app.config.from_object(DevelopmentConfig())
    app.config['SECRET_KEY'] = secrets.token_urlsafe(32)

    from core.blueprints import BlueprintManager
    BlueprintManager.register_all(app)

    from core.extensions import login_manager
    login_manager.init_app(app)

    from auth.routes import ns as auth_ns
    from users.routes import ns as users_ns
    from programs.routes import ns as programs_ns
    api.add_namespace(auth_ns, path="/auth")
    api.add_namespace(users_ns, path="/users")
    api.add_namespace(programs_ns, path="/programs")
    api.init_app(app)

    from core.extensions import db
    db.init_app(app)

    # Ensure models are imported before creating tables
    import users.model
    with app.app_context():
        db.create_all()

    return app
