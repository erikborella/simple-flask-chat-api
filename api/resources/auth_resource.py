from flask_restful import Resource

from flask import request, make_response

from utils.auth import auth, token_required, token_required

from config import TOKEN_NAME


"""
post: authenticates the user and return a authenciation token
"""
class Auth(Resource):

    def post(self):        
        token = auth()

        if type(token) == str:

            response = make_response({'message': 'successfuly loged'})

            response.set_cookie(TOKEN_NAME, token, httponly=True)

            return response
        
        else:

            return token, 401


class Logout(Resource):

    @token_required
    def get(self, **kwargs):
        response = make_response({
            'message': 'successfully logout'
        })

        response.set_cookie(TOKEN_NAME, '', expires=0)

        return response