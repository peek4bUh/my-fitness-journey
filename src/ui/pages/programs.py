from ui.core.httpclient import HttpClient
from flask import current_app, redirect, url_for, flash
from flask import render_template, session
from flask_login import login_required
import requests

from ui.core.enums import Template
from ui.core.blueprints import ui_dashboard_bp


@ui_dashboard_bp.route('/dashboard/programs')
@login_required
def dashboard_programs_page():
    response = requests.get("http://localhost:7777/api/v0/programs",
                            headers={"X-API-KEY": session['api_key']})

    return render_template(Template.PROGRAMS.value, programs=response.json())


@ui_dashboard_bp.route('/dashboard/programs/<int:programId>')
@login_required
def dashboard_programs_by_id_page(programId):
    response = requests.get(f"http://localhost:7777/api/v0/programs/{programId}",
                            headers={"X-API-KEY": session['api_key']})

    return render_template(Template.PROGRAM.value, program=response.json())


@ui_dashboard_bp.route('/dashboard/programs/<int:program_id>/delete', methods=['POST'])
@login_required
def delete_program(program_id: int):
    response = requests.delete(
        f"http://localhost:7777/api/v0/programs/{program_id}",
        headers={"X-API-KEY": session['api_key']})

    if response.status_code == 200:
        flash("Program deleted.", "success")
    else:
        current_app.logger.error(f"Failed to delete program: {program_id}")
        flash("Failed to delete program.", "error")

    return redirect(url_for('ui.dashboard.dashboard_programs_page'))
