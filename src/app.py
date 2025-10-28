from flask import Flask

from config import DevelopmentConfig


def create_app():
    app = Flask(__name__,
                template_folder='../templates',
                static_folder='../static')
    app.config.from_object(DevelopmentConfig())

    from routes.api import api_bp
    from routes.web import web_bp
    app.register_blueprint(api_bp)
    app.register_blueprint(web_bp)

    from database import db
    db.init_app(app)

    # Ensure models are imported before creating tables
    import models
    with app.app_context():
        db.create_all()

    return app
