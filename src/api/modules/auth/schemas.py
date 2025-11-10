from flask_restx import fields

from api.core.namespaces import auth_ns


login_input_schema = auth_ns.model('AuthLogin', {
    'username': fields.String(required=True, description='The user name'),
    'password': fields.String(required=True, description='The user password')
})
