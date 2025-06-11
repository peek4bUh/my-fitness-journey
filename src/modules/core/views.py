from flask import Blueprint, render_template, request, url_for, redirect

core = Blueprint('core', __name__)


@core.route("/")
@core.route("/index")
def login():
    return render_template("core/index.html")
