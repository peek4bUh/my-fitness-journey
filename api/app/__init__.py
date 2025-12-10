import secrets
from flask import Flask

from app.core.config_profile import DevelopmentConfig
from app.core.config import api_restx


def create_app():
    app = Flask(__name__)
    app.config.from_object(DevelopmentConfig())
    app.config['SECRET_KEY'] = secrets.token_urlsafe(32)

    # from app.core.extensions import login_manager
    # login_manager.init_app(app)

    from app.core.namespaces import NamespaceManager
    NamespaceManager.register_all(api_restx)
    api_restx.init_app(app)

    from app.core.extensions import db
    db.init_app(app)

    # Ensure models are imported before creating tables
    from app.domain import entity
    with app.app_context():
        db.create_all()

    return app


create_app()
