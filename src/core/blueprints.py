from flask import Blueprint

from users.routes import api_user_bp
from auth.routes import api_auth_bp
from web import web_home_bp, web_auth_bp, web_dashboard_bp

api_bp = Blueprint('api', __name__, url_prefix='/api')
api_bp.register_blueprint(api_user_bp, url_prefix='/users')
api_bp.register_blueprint(api_auth_bp, url_prefix='/auth')

web_bp = Blueprint('web', __name__)
web_bp.register_blueprint(web_home_bp)
web_bp.register_blueprint(web_auth_bp)
web_bp.register_blueprint(web_dashboard_bp)
