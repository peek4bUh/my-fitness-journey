from flask import Blueprint, render_template

from core.constants.pages import PAGE_INDEX


home_bp = Blueprint('home', __name__)


@home_bp.route("/")
@home_bp.route("/home")
def index():
    return render_template(PAGE_INDEX)
