from ui.core.user import ApiUser
from ui.core.blueprints import ui_auth_bp
from ui.core.httpclient import HttpClient
from ui.core.enums import Template, View
from shared.enum.http import Method, Status
from flask_login import login_remembered, login_required, login_user, logout_user
from flask import redirect, render_template, request, url_for


@ui_auth_bp.route(
    rule='/login',
    methods=[Method.GET.value, Method.POST.value])
def login_page():
    if request.method == Method.GET.value:
        if login_remembered():
            return redirect(url_for(View.DASHBOARD_OVERVIEW.value))

        return render_template(Template.LOGIN.value)

    if request.method == Method.POST.value:
        http_result = HttpClient().post("/api/v0/auth/login", json={
            "username": request.form['username'],
            "password": request.form['password']
        })

        if http_result.status_code != Status.OK.value:
            return render_template(Template.LOGIN.value, error=("Invalid username or password."))

        user = ApiUser(**http_result.json.get('user'))
        login_user(user, remember=True)

        return redirect(url_for(View.DASHBOARD_OVERVIEW.value))


@ui_auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for(View.LOGIN.value))


@ui_auth_bp.route(
    rule='/register',
    methods=[Method.GET.value, Method.POST.value])
def signup_page():
    if request.method == Method.GET.value:
        return render_template(Template.SIGNUP.value)

    if request.method == Method.POST.value:
        resp = HttpClient().post("/api/users", json={
            "username": request.form['username'],
            "email": request.form['email'],
            "password": request.form['password']
        })

        if resp.status_code == Status.CONFLICT.value:
            return render_template(Template.SIGNUP.value, error="Username or email already exists.")

        return redirect(url_for(View.DASHBOARD_OVERVIEW.value))
