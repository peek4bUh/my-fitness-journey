from flask import Blueprint, render_template, request

from core.constants.globals import METHOD_GET, METHOD_POST
from core.constants.pages import PAGE_DASHBOARD, PAGE_LOGIN, PAGE_SIGNUP
from core.ws import WebService


auth_bp = Blueprint('auth', __name__)
ws = WebService()


@auth_bp.route('/login', methods=[METHOD_GET, METHOD_POST])
def login_page():
    if request.method == METHOD_GET:
        return render_template(PAGE_LOGIN)

    if request.method == METHOD_POST:
        ws.post("/api/users/login", json={
            "username": request.form['username'],
            "password": request.form['password']
        })

        return render_template(PAGE_DASHBOARD)


@auth_bp.route('/register')
def signup_page():
    return render_template(PAGE_SIGNUP)
