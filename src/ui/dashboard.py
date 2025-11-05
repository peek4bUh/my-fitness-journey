from flask import render_template
from flask_login import current_user, login_required

from core.templates import Templates
from core.endpoints import Endpoints
from core.blueprints import ui_dashboard_bp


@ui_dashboard_bp.route(Endpoints.DASHBOARD.value)
@login_required
def navigate_to_dashboard():
    return render_template(Templates.DASHBOARD.value, username=current_user.username)
