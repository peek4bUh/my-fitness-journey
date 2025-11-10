from flask import Flask, Blueprint


ui_bp = Blueprint('ui', __name__)
ui_auth_bp = Blueprint('auth', __name__)
ui_dashboard_bp = Blueprint('dashboard', __name__)
ui_home_bp = Blueprint('home', __name__)


class BlueprintManager:
    """Class to manage all blueprints."""

    _blueprints = {
        ui_bp: [ui_auth_bp, ui_dashboard_bp, ui_home_bp],
    }

    @classmethod
    def register_all(cls, app: Flask):
        """Register all blueprints to the Flask app."""
        from ui import modules

        for parent_bp, child_bps in cls._blueprints.items():
            for child_bp in child_bps:
                parent_bp.register_blueprint(child_bp)
            app.register_blueprint(parent_bp)
