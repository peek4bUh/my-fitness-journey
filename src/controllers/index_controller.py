from flask import Blueprint

from services.index_service import IndexService


index_bp = Blueprint('index', __name__)
index_service = IndexService()


@index_bp.route("/")
def index():
    return index_service.index()
