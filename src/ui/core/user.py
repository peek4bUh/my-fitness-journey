from flask_login import UserMixin


class ApiUser(UserMixin):

    def __init__(self, id, username, email, api_token):
        self.id = id
        self.username = username
        self.email = email
        self.api_token = api_token
