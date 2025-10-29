from flask import Blueprint

from .index import index_bp
from .auth import auth_bp
from .dashboard import dashboard_bp


web_bp = Blueprint('web', __name__)
web_bp.register_blueprint(index_bp)
web_bp.register_blueprint(auth_bp)
web_bp.register_blueprint(dashboard_bp)
