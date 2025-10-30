from flask import session


class AuthRepository:

    def login_user(self, user_id: int, username: str = None):
        session['user'] = {"id": user_id, "username": username}

    def logout_user(self):
        session.pop('user', None)
