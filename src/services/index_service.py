from flask import render_template

from config.constants.pages import PAGE_INDEX


class IndexService:

    def index(self):
        return render_template(PAGE_INDEX)
