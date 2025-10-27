from controllers.index_controller import index_bp
from controllers.auth_controller import auth_bp
from controllers.user_controller import api_bp

blueprints = [index_bp, auth_bp, api_bp]
