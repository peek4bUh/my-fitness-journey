from routes.blueprints import index_bp
from services.index_service import IndexService


@index_bp.route("/")
@index_bp.route("/index")
def index():
    return IndexService.index()
