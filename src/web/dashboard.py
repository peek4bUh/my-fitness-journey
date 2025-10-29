from flask import Blueprint, render_template

from core.constants.pages import PAGE_DASHBOARD


dashboard_bp = Blueprint('dashboard', __name__)


@dashboard_bp.route('/dashboard')
def navigate_to_dashboard():
    return render_template(PAGE_DASHBOARD)
