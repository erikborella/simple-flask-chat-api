from flask_restful import Resource

from utils.auth import auth

class Auth(Resource):

    def post(self):
        return auth()