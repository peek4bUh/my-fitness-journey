from flask import render_template, request, url_for, redirect
from werkzeug.security import generate_password_hash, check_password_hash
from modules.models.user import UserModel

from flask import Blueprint

auth = Blueprint('auth', __name__)


@auth.route("/login", methods=["GET", "POST"])
def login():
    # if request.method == "POST":
    #     username = request.form.get("username")
    #     password = request.form.get("password")
    #     user = Users.query.filter_by(username=username).first()

    #     if user and check_password_hash(user.password, password):
    #         login_user(user)
    #         return redirect(url_for("dashboard"))
    #     else:
    #         return render_template("login.html", error="Invalid username or password")
    return render_template("auth/login.html")

# @auth.route('/register', methods=["GET", "POST"])
# def register():
#     if request.method == "POST":
#         username = request.form.get("username")
#         password = request.form.get("password")

#         if Users.query.filter_by(username=username).first():
#             return render_template("sign_up.html", error="Username already taken!")

#         hashed_password = generate_password_hash(
#             password, method="pbkdf2:sha256")

#         new_user = UserModel(username=username, password=hashed_password)
#         db.session.add(new_user)
#         db.session.commit()

#         return redirect(url_for("login"))

#   return render_template("auth/signup.html")
