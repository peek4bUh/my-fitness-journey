from flask import render_template, session, redirect, url_for

from core.constants.pages import PAGE_LOGIN
from core.templates import Templates
from core.endpoints import Endpoints
from core.blueprints import ui_dashboard_bp


@ui_dashboard_bp.route(Endpoints.DASHBOARD.value)
def navigate_to_dashboard():
    user = session.get('username')
    if user is None:
        return redirect(url_for(PAGE_LOGIN))
    return render_template(Templates.DASHBOARD.value, user=user)
