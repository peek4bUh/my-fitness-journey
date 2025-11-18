from flask import render_template

from ui.core.enums import Template
from ui.core.blueprints import ui_home_bp


@ui_home_bp.route('/')
@ui_home_bp.route('/home')
def home_page():
    return render_template(Template.INDEX.value)
