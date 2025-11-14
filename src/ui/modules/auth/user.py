from flask_login import UserMixin


class ApiUser(UserMixin):

    def __init__(self, id, username, email):
        self.id = id
        self.username = username
