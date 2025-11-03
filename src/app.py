import secrets
from flask import Flask

from core.config import DevelopmentConfig
from core.extensions import api


def create_app():
    app = Flask(__name__,
                template_folder='../templates',
                static_folder='../static')
    app.config.from_object(DevelopmentConfig())
    app.config['SECRET_KEY'] = secrets.token_urlsafe(32)

    from core.blueprints import web_bp
    app.register_blueprint(web_bp)

    from auth.routes import ns as auth_ns
    from users.routes import ns as users_ns
    api.add_namespace(auth_ns, path="/auth")
    api.add_namespace(users_ns, path="/users")
    api.init_app(app)

    from core.extensions import db
    db.init_app(app)

    # Ensure models are imported before creating tables
    import users.model
    with app.app_context():
        db.create_all()

    return app
