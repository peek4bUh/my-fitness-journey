from flask import Blueprint, render_template

from core.constants.pages import PAGE_DASHBOARD


web_dashboard_bp = Blueprint('dashboard', __name__)


@web_dashboard_bp.route('/dashboard')
def navigate_to_dashboard():
    return render_template(PAGE_DASHBOARD)
