from flask import request
from flask_restx import Resource

from users.service import UsersService
from core.extensions import api


ns = api.namespace("users", description="Users Operations")
users_service = UsersService()


@ns.route('/users')
class UserCRUD(Resource):

    @api.doc(parser=api.parser())
    def post(self):
        return users_service.create_user()


@ns.route('/users/<username>')
class UserData(Resource):

    @api.doc(parser=api.parser())
    def get(self, username):
        return users_service.get_user_data(username)
