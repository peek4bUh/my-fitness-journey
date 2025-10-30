from flask import Blueprint, render_template, session, redirect, url_for

from core.constants.templates import TEMPLATE_DASHBOARD

web_dashboard_bp = Blueprint('dashboard', __name__)


@web_dashboard_bp.route('/dashboard')
def navigate_to_dashboard():
    user = session.get('user')
    if not user:
        return redirect(url_for('web.auth.login_page'))
    return render_template(TEMPLATE_DASHBOARD, user=user)
