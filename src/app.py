from flask import Flask

from config import DevelopmentConfig


def create_app():

    app = Flask(__name__,
                template_folder='../templates',
                static_folder='../static')
    app.config.from_object(DevelopmentConfig())

    from database import db
    db.init_app(app)

    # with app.app_context():
    #     db.drop_all()
    #     db.create_all()
    #     db.session.commit()

    from routes import blueprints
    [app.register_blueprint(bp) for bp in blueprints]

    return app
