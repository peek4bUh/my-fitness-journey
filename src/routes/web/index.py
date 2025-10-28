from flask import Blueprint, render_template

from globals import PAGE_INDEX


index_bp = Blueprint('index', __name__)


@index_bp.route("/")
@index_bp.route("/home")
def index():
    return render_template(PAGE_INDEX)
