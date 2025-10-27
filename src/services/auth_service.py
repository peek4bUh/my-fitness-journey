from flask import jsonify, redirect, render_template, request, url_for
from werkzeug.security import generate_password_hash, check_password_hash

from models.user import UserModel
from config.constants.pages import PAGE_DASHBOARD, PAGE_LOGIN, PAGE_SIGNUP
from config.constants.messages import MSG_ERROR_INVALID_CREDENTIALS, MSG_ERROR_USER_TAKEN
from config.constants.globals import METHOD_GET, METHOD_POST


class AuthService:

    @staticmethod
    def login_user():
        if request.method == METHOD_GET:
            return render_template(PAGE_LOGIN)

        if request.method == METHOD_POST:
            request_username = request.form.get("username")
            request_password = request.form.get("password")
            user = UserModel.query.filter_by(username=request_username).first()

            if user and check_password_hash(user.password, request_password):
                return redirect(url_for(PAGE_DASHBOARD))
            else:
                return render_template(PAGE_LOGIN, error=MSG_ERROR_INVALID_CREDENTIALS)

    @staticmethod
    def register_user():
        if request.method == METHOD_GET:
            return render_template(PAGE_SIGNUP)

        if request.method == METHOD_POST:
            data = request.get_json()
            request_username = data.get("username")
            request_password = data.get("password")
            request_email = data.get("email")

            if UserModel.query.filter_by(username=request_username).first():
                return render_template(PAGE_SIGNUP, error=MSG_ERROR_USER_TAKEN)

            # hashed_password = generate_password_hash(password, method="pbkdf2:sha256")
            new_user = UserModel(username=request_username,
                                 password=request_password,
                                 email=request_email)

            from database import db
            db.session.add(new_user)
            db.session.commit()

            return jsonify({"message": "OK"}), 200
