from flask import Flask

from config.profiles import DevelopmentProfile


def create_app():

    app = Flask(__name__,
                template_folder='../templates',
                static_folder='../static')
    app.config.from_object(DevelopmentProfile())

    from controllers.index_controller import index_bp
    from controllers.auth_controller import auth_bp
    from controllers.user_controller import api_bp
    app.register_blueprint(index_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(api_bp)

    from database import db
    db.init_app(app)

    # Ensure models are imported before creating tables
    import models
    with app.app_context():
        db.create_all()

    return app
