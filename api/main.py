from app_creator import create_app
from flask_restful import Api

from flask import send_from_directory

from resources.user_resource import Users, GetOneUser, Image
from resources.auth_resource import Auth


app = create_app()
api = Api(app)

api.add_resource(Users, '/api/user')
api.add_resource(GetOneUser, '/api/user/<user_id>')
api.add_resource(Image, '/api/user/image')

api.add_resource(Auth, '/api/auth')

if __name__ == "__main__":
    app.run()