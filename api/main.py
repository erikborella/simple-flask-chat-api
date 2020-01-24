from app_creator import create_app
from flask_restful import Api

from resources.user_resource import Users, GetOneUser


app = create_app()
api = Api(app)

api.add_resource(Users, '/api/user')
api.add_resource(GetOneUser, '/api/user/<user_id>')

if __name__ == "__main__":
    app.run()