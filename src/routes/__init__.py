from .blueprints import auth_bp, api_bp, index_bp

import controllers.index_controller
import controllers.user_controller
import controllers.auth_controller


blueprints = [auth_bp, api_bp, index_bp]
