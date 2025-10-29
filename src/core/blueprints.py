from flask import Blueprint

from users.routes import user_bp
from web import home_bp, auth_bp, dashboard_bp

api_bp = Blueprint('api', __name__, url_prefix='/api')
api_bp.register_blueprint(user_bp, url_prefix='/users')

web_bp = Blueprint('web', __name__)
web_bp.register_blueprint(home_bp)
web_bp.register_blueprint(auth_bp)
web_bp.register_blueprint(dashboard_bp)
