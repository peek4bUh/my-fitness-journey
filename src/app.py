from flask import Flask

from config import DevelopmentConfig


def create_app():
    app = Flask(__name__)
    app.config.from_object(DevelopmentConfig())

    app = Flask(__name__,
                template_folder='../templates',
                static_folder='../static')
    app.config.from_object(DevelopmentProfile())

    from controllers import blueprints
    [app.register_blueprint(bp) for bp in blueprints]

    from database import db
    db.init_app(app)

    # Ensure models are imported before creating tables
    import models
    with app.app_context():
        db.create_all()

    return app
