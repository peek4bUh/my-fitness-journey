from flask import Blueprint

from services.index_service import IndexService


index_bp = Blueprint('index', __name__)


@index_bp.route("/")
@index_bp.route("/index")
def index():
    return IndexService.index()
