from flask_restx import fields

from api.core.namespaces import users_ns


user_input_schema = users_ns.model('User', {
    'username': fields.String(
        required=True,
        description='The user name',
        example='test'),
    'email': fields.String(required=True,
                           description='The user email',
                           example='test@email.com'),
    'password': fields.String(required=True, description='The user password', example='test')
})
