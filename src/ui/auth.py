from flask import Blueprint, redirect, render_template, request, url_for, session

from core.constants.globals import METHOD_GET, METHOD_POST, HTTP_409_CONFLICT, HTTP_200_OK
from core.constants.pages import PAGE_DASHBOARD, PAGE_LOGIN
from core.templates import Templates
from core.ws import WebService
from core.decorators.auth import redirect_if_authenticated
from core.endpoints import Endpoints


web_auth_bp = Blueprint('auth', __name__)
ws = WebService()


@web_auth_bp.route(Endpoints.LOGIN.value, methods=[METHOD_GET, METHOD_POST])
@redirect_if_authenticated()
def login_page():
    if request.method == METHOD_GET:
        return render_template(Templates.LOGIN.value)

    if request.method == METHOD_POST:
        http_result = ws.post("/api/v0/auth/login", json={
            "username": request.form['username'],
            "password": request.form['password']
        })

        if http_result.status_code != HTTP_200_OK:
            return render_template(Templates.LOGIN.value, error=("Invalid username or password."))

        session['username'] = request.form['username']
        session.permanent = True

        return redirect(url_for(PAGE_DASHBOARD))


@web_auth_bp.route(Endpoints.LOGOUT.value)
def logout_user():
    session.pop('username', None)
    return redirect(url_for(PAGE_LOGIN))


@web_auth_bp.route(Endpoints.REGISTER.value)
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
