from flask import Blueprint, redirect, render_template, request, url_for, session

from core.constants.globals import METHOD_GET, METHOD_POST, HTTP_409_CONFLICT
from core.constants.pages import PAGE_DASHBOARD, PAGE_LOGIN
from core.constants.templates import TEMPLATE_LOGIN, TEMPLATE_SIGNUP
from core.ws import WebService
from core.decorators.auth import is_user_logged, redirect_if_authenticated


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

        if http_result.status_code != 200:
            return render_template(TEMPLATE_LOGIN, error=(http_result.json or {}).get("message"))

        body = http_result.json or {}
        session['user'] = {
            "id": body.get("id") or body.get("user_id"),
            "username": body.get("username")
        }
        session.permanent = True

        return redirect(url_for(PAGE_DASHBOARD))


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
