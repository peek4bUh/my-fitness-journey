from flask import redirect, render_template, request, url_for
from flask_login import login_remembered, login_required, login_user, logout_user

from shared.enum.http import HTTP
from ui.core.enums import Endpoint, Template, View
from ui.core.httpclient import HttpClient
from ui.core.blueprints import ui_auth_bp
from ui.modules.auth.user import ApiUser


http_client = HttpClient()


@ui_auth_bp.route(
    rule=Endpoint.LOGIN.value,
    methods=[HTTP.Method.GET.value, HTTP.Method.POST.value])
def login_page():
    if request.method == HTTP.Method.GET.value:
        if login_remembered():
            return redirect(url_for(View.DASHBOARD.value))

        return render_template(Template.LOGIN.value)

    if request.method == HTTP.Method.POST.value:
        http_result = http_client.post("/api/v0/auth/login", json={
            "username": request.form['username'],
            "password": request.form['password']
        })

        if http_result.status_code != HTTP.Status.OK.value:
            return render_template(Template.LOGIN.value, error=("Invalid username or password."))

        user = ApiUser(**http_result.json.get('user'))
        login_user(user, remember=True)

        return redirect(url_for(View.DASHBOARD.value))


@ui_auth_bp.route(rule=Endpoint.LOGOUT.value)
@login_required
def logout():
    logout_user()
    return redirect(url_for(View.LOGIN.value))


@ui_auth_bp.route(
    rule=Endpoint.REGISTER.value,
    methods=[HTTP.Method.GET.value, HTTP.Method.POST.value])
def signup_page():
    if request.method == HTTP.Method.GET.value:
        return render_template(Template.SIGNUP.value)

    if request.method == HTTP.Method.POST.value:
        resp = http_client.post("/api/users", json={
            "username": request.form['username'],
            "email": request.form['email'],
            "password": request.form['password']
        })

        if resp.status_code == HTTP.Status.CONFLICT.value:
            return render_template(Template.SIGNUP.value, error="Username or email already exists.")

        return redirect(url_for(View.DASHBOARD.value))
