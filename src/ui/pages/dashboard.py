from flask import render_template
from flask_login import current_user, login_required

from ui.core.enums import Template
from ui.core.blueprints import ui_dashboard_bp


@ui_dashboard_bp.route('/dashboard')
@login_required
def navigate_to_dashboard():
    return render_template(Template.DASHBOARD.value, username=current_user.username)
