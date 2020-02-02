from flask_restful import Resource

from flask import request

from utils.auth import auth, token_required


"""
post: authenticates the user and return a authenciation token
"""
class Auth(Resource):

    def post(self):
        return {
            'token': auth()
        }