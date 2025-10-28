class UserDto:
    """Data Transfer Object for User data."""

    def __init__(self):
        self.username = ""
        self.password = ""
        self.email = ""

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
