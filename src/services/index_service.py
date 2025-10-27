from flask import render_template

from globals import PAGE_INDEX


class IndexService:

    def index(self):
        return render_template(PAGE_INDEX)
