from flask import render_template

from ui.core.enums import Endpoint, Template
from ui.core.blueprints import ui_home_bp


@ui_home_bp.route(Endpoint.INDEX.value)
@ui_home_bp.route(Endpoint.HOME.value)
def home_page():
    return render_template(Template.INDEX.value)
