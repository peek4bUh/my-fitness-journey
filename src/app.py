from flask import Flask
from config import DevelopmentConfig
from modules.database.db import db
from modules.api.users import api
from modules.core.views import core
from modules.auth.views import auth

app = Flask(__name__,
            template_folder='../templates',
            static_folder='../static')
app.config.from_object(DevelopmentConfig())

app.register_blueprint(api)
app.register_blueprint(auth)
app.register_blueprint(core)


# db.init_app(app)
