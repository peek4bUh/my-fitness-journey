from flask import Blueprint

from web import web_home_bp, web_auth_bp, web_dashboard_bp


web_bp = Blueprint('web', __name__)
web_bp.register_blueprint(web_home_bp)
web_bp.register_blueprint(web_auth_bp)
web_bp.register_blueprint(web_dashboard_bp)
