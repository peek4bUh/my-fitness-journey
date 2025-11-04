from flask import Blueprint, render_template

from core.templates import Templates
from core.endpoints import Endpoints


ui_home_bp = Blueprint('home', __name__)


@ui_home_bp.route(Endpoints.INDEX.value)
@ui_home_bp.route(Endpoints.HOME.value)
def home_page():
    return render_template(Templates.INDEX.value)
