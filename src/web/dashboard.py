from flask import Blueprint, current_app, render_template, session, redirect, url_for

from core.constants.pages import PAGE_LOGIN
from core.constants.templates import TEMPLATE_DASHBOARD

web_dashboard_bp = Blueprint('dashboard', __name__)


@web_dashboard_bp.route('/dashboard')
def navigate_to_dashboard():
    user = session.get('username')
    if user is None:
        return redirect(url_for(PAGE_LOGIN))
    return render_template(TEMPLATE_DASHBOARD, user=user)
