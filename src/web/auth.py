from flask import Blueprint, current_app, redirect, render_template, request, url_for, session

from core.constants.globals import METHOD_GET, METHOD_POST, HTTP_409_CONFLICT, HTTP_200_OK
from core.constants.pages import PAGE_DASHBOARD, PAGE_LOGIN
from core.constants.templates import TEMPLATE_LOGIN, TEMPLATE_SIGNUP
from core.ws import WebService
from core.decorators.auth import redirect_if_authenticated


web_auth_bp = Blueprint('auth', __name__)
ws = WebService()


@web_auth_bp.route('/login', methods=[METHOD_GET, METHOD_POST])
@redirect_if_authenticated()
def login_page():
    if request.method == METHOD_GET:
        return render_template(TEMPLATE_LOGIN)

    if request.method == METHOD_POST:
        http_result = ws.post("/api/auth/login", json={
            "username": request.form['username'],
            "password": request.form['password']
        })

        if http_result.status_code != HTTP_200_OK:
            return render_template(TEMPLATE_LOGIN, error=(http_result.json.get("message")))

        session['username'] = request.form['username']
        session.permanent = True

        return redirect(url_for(PAGE_DASHBOARD))


@web_auth_bp.route('/logout')
def logout_user():
    session.pop('username', None)
    return redirect(url_for(PAGE_LOGIN))


@web_auth_bp.route('/register', methods=[METHOD_GET, METHOD_POST])
def signup_page():
    if request.method == METHOD_GET:
        return render_template(TEMPLATE_SIGNUP)

    if request.method == METHOD_POST:
        resp = ws.post("/api/users", json={
            "username": request.form['username'],
            "email": request.form['email'],
            "password": request.form['password']
        })

        if resp.status_code == HTTP_409_CONFLICT:
            return render_template(TEMPLATE_SIGNUP, error="Username or email already exists.")

        return redirect(url_for(PAGE_LOGIN))
