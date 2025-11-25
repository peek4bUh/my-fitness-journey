from flask import render_template
from flask_login import current_user, login_required

from ui.core.enums import Template
from ui.core.blueprints import ui_dashboard_bp


@ui_dashboard_bp.route('/dashboard/overview')
@login_required
def dashboard_overview_page():
    return render_template(Template.OVERVIEW.value, username=current_user.username)
