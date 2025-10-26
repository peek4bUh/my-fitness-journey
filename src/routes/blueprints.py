from flask import Blueprint


auth_bp = Blueprint('auth', __name__)
api_bp = Blueprint('api', __name__, url_prefix='/api')
index_bp = Blueprint('index', __name__)
