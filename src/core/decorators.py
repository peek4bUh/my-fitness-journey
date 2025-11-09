from functools import wraps
from flask import g, request, abort


def require_api_key(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        from core.extensions import db
        from users.model import UserModel

        api_key = request.headers.get('X-API-KEY')
        if not api_key:
            abort(401, 'Missing API key')

        user = UserModel.query.filter_by(api_token=api_key).first()
        if not user.api_token:
            abort(401, 'Invalid API key')

        g.user_id = user.user_id
        g.api_key = user.api_token

        return f(*args, **kwargs)
    return decorated
