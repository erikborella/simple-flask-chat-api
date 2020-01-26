from flask_restful import Resource

from flask import request

from utils.auth import auth, token_required

class Auth(Resource):

    def post(self):
        return auth()

    @token_required
    def get(self, **kwargs):
        user = kwargs.get('user')
        return user.name