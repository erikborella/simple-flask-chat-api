from app_creator import create_app
from flask_restful import Api

from resources.HelloWorld import HelloWorld
from resources.auth import CreateUser

app = create_app()
api = Api(app)

api.add_resource(HelloWorld, '/')
api.add_resource(CreateUser, '/api/user')

if __name__ == "__main__":
    app.run()