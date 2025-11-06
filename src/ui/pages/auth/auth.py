from flask import redirect, render_template, request, url_for
from flask_login import login_remembered, login_required, login_user, logout_user

from core.constants.globals import METHOD_GET, METHOD_POST, HTTP_409_CONFLICT, HTTP_200_OK
from core.constants.pages import PAGE_DASHBOARD, PAGE_LOGIN
from core.templates import Templates
from core.ws import WebService
from core.endpoints import Endpoints
from core.blueprints import ui_auth_bp
from dto.user import User


ws = WebService()


@ui_auth_bp.route(Endpoints.LOGIN.value, methods=[METHOD_GET, METHOD_POST])
def login_page():
    if request.method == METHOD_GET:
        if login_remembered():
            return redirect(url_for(PAGE_DASHBOARD))

        return render_template(Templates.LOGIN.value)

    if request.method == METHOD_POST:
        http_result = ws.post("/api/v0/auth/login", json={
            "username": request.form['username'],
            "password": request.form['password']
        })

        if http_result.status_code != HTTP_200_OK:
            return render_template(Templates.LOGIN.value, error=("Invalid username or password."))

        user = User(**http_result.json.get('user'))
        login_user(user, remember=True)

        return redirect(url_for(PAGE_DASHBOARD))


@ui_auth_bp.route(Endpoints.LOGOUT.value)
@login_required
def logout():
    logout_user()
    return redirect(url_for(PAGE_LOGIN))


@ui_auth_bp.route(Endpoints.REGISTER.value)
def signup_page():
    if request.method == METHOD_GET:
        return render_template(Templates.SIGNUP.value)

    if request.method == METHOD_POST:
        resp = ws.post("/api/users", json={
            "username": request.form['username'],
            "email": request.form['email'],
            "password": request.form['password']
        })

        if resp.status_code == HTTP_409_CONFLICT:
            return render_template(Templates.SIGNUP.value, error="Username or email already exists.")

        return redirect(url_for(PAGE_LOGIN))
