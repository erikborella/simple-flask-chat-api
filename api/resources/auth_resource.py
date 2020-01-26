from flask_restful import Resource

from flask import request

from utils.auth import auth, token_required

class Auth(Resource):

    def post(self):
        return {
            'token': auth()
        }