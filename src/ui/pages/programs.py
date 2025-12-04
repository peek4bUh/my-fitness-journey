from flask import render_template, request
from flask_login import login_required

from ui.core.enums import Template
from ui.core.blueprints import ui_dashboard_bp
from ui.core.httpclient import HttpClient


@ui_dashboard_bp.route('/dashboard/programs')
@login_required
def dashboard_programs_page():
    # programs = HttpClient().post("/api/v0/programs", json={
    #     "username": request.form['username'],
    #     "email": request.form['email'],
    #     "password": request.form['password']
    # })

    return render_template(Template.PROGRAMS.value)
