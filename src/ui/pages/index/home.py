from flask import render_template

from core.templates import Templates
from core.endpoints import Endpoints
from core.blueprints import ui_home_bp


@ui_home_bp.route(Endpoints.INDEX.value)
@ui_home_bp.route(Endpoints.HOME.value)
def home_page():
    return render_template(Templates.INDEX.value)
