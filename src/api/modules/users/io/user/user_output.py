from flask_restx import fields

from api.core.namespaces import users_ns


class UserOutput:
    """Output Object for User data."""

    schema = users_ns.model('UserOutput', {
        'username': fields.String(),
        'email': fields.String(),
    })

    def __init__(self, username: str = None, email: str = None):
        self.username = username
        self.email = email

    def get_username(self):
        return self.username

    def set_username(self, username):
        self.username = username

    def get_email(self):
        return self.email

    def set_email(self, email):
        self.email = email
