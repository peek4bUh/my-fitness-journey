from flask import Blueprint, render_template, request

from globals import PAGE_LOGIN, PAGE_SIGNUP, METHOD_GET, METHOD_POST, PAGE_DASHBOARD
from ws import WebService

auth_bp = Blueprint('auth', __name__)
webservice = WebService()


@auth_bp.route('/login', methods=[METHOD_GET, METHOD_POST])
def navigate_to_login():
    if request.method == METHOD_GET:
        return render_template(PAGE_LOGIN)

    if request.method == METHOD_POST:
        webservice.post("/api/users/login", json={
            "username": request.form['username'],
            "password": request.form['password']
        })

        client = WebService()
        payload = {"username": "test122221", "password": "Secret123"}
        resp = client.post("/api/users/login", json=payload)
        print(resp)

        return render_template(PAGE_DASHBOARD)


@auth_bp.route('/register')
def navigate_to_signup():
    return render_template(PAGE_SIGNUP)
