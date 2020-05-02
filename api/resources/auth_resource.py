from flask_restful import Resource

from flask import request, make_response

from utils.auth import auth, token_required, token_required


"""
post: authenticates the user and return a authenciation token
"""
class Auth(Resource):

    def post(self):        
        token = auth()

        response = make_response({'message': 'successfuly loged'})

        response.set_cookie('access_token', token, httponly=True)

        return response


class Logout(Resource):

    @token_required
    def get(self, **kwargs):
        response = make_response({
            'message': 'successfully logout'
        })

        response.set_cookie('access_token', '', expires=0)

        return response