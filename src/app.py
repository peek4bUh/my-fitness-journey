import secrets
from flask import Flask

from config import DevelopmentConfig
from api.config import api_restx


def create_app():
    app = Flask(__name__,
                template_folder='./ui/templates',
                static_folder='../static')
    app.config.from_object(DevelopmentConfig())
    app.config['SECRET_KEY'] = secrets.token_urlsafe(32)

    from ui.core.blueprints import BlueprintManager
    BlueprintManager.register_all(app)

    from api.core.extensions import login_manager
    login_manager.init_app(app)

    from api.core.namespaces import NamespaceManager
    NamespaceManager.register_all(api_restx)
    api_restx.init_app(app)

    from api.core.extensions import db
    db.init_app(app)

    # Ensure models are imported before creating tables
    import api.modules.users.model
    with app.app_context():
        db.create_all()

    return app
