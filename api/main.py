from app_creator import create_app
from flask_restful import Api

from resources.HelloWorld import HelloWorld

app = create_app()
api = Api(app)

api.add_resource(HelloWorld, '/')

if __name__ == "__main__":
    app.run()