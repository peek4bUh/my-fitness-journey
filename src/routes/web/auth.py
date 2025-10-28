from flask import Blueprint, render_template

from globals import PAGE_LOGIN, PAGE_SIGNUP


auth_bp = Blueprint('auth', __name__)


@auth_bp.route('/login')
def navigate_to_login():
    return render_template(PAGE_LOGIN)


@auth_bp.route('/register')
def navigate_to_signup():
    return render_template(PAGE_SIGNUP)
