from flask import Blueprint

from ui import ui_home_bp, ui_auth_bp, ui_dashboard_bp


ui_bp = Blueprint('ui', __name__)
ui_bp.register_blueprint(ui_home_bp)
ui_bp.register_blueprint(ui_auth_bp)
ui_bp.register_blueprint(ui_dashboard_bp)
