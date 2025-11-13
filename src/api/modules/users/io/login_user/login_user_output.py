from flask_restx import fields

from api.core.namespaces import auth_ns


class LoginUserOutput:
    """LoginUser Output Object for Login User data."""

    schema = auth_ns.model('AuthLoginOutput', {
        'username': fields.String(required=True, description='The user name'),
        'password': fields.String(required=True, description='The user password')
    })

    def __init__(self, id: int = None, username: str = None, email: str = None):
        self.id = id
        self.username = username
        self.email = email

    def get_id(self):
        return self.username

    def set_id(self, id):
        self.id = id

    def get_username(self):
        return self.username

    def set_username(self, username):
        self.username = username

    def get_email(self):
        return self.email

    def set_email(self, email):
        self.email = email
