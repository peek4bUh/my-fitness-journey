from flask_restx import fields

from api.core.namespaces import users_ns


class UserDto:
    """Data Transfer Object for User data."""

    def __init__(self, username: str, password: str, email: str):
        self.username = username
        self.password = password
        self.email = email

    def get_username(self):
        return self.username

    def set_username(self, username):
        self.username = username

    def get_password(self):
        return self.password

    def set_password(self, password):
        self.password = password

    def get_email(self):
        return self.email

    def set_email(self, email):
        self.email = email


class UserInput:
    """Input Object for User data."""

    schema = users_ns.model('UserInput', {
        'username': fields.String(
            required=True,
            description='The user name',
            example='test'),
        'email': fields.String(required=True,
                               description='The user email',
                               example='test@email.com'),
        'password': fields.String(required=True, description='The user password', example='test')
    })

    def __init__(self, username: str = None, email: str = None, password: str = None):
        self.username = username
        self.email = email
        self.password = password

    def get_username(self):
        return self.username

    def set_username(self, username):
        self.username = username

    def get_email(self):
        return self.email

    def set_email(self, email):
        self.email = email

    def get_password(self):
        return self.password

    def set_password(self, password):
        self.password = password


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


class LoginUserOutput:
    """Output Object for Login User data."""

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
