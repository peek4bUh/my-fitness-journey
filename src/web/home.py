from flask import Blueprint, render_template

from core.constants.templates import TEMPLATE_INDEX


web_home_bp = Blueprint('home', __name__)


@web_home_bp.route("/")
@web_home_bp.route("/home")
def home_page():
    return render_template(TEMPLATE_INDEX)
