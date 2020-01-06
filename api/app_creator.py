from flask import Flask

"""Create and configure Flask instance"""
def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    
    return app

"""Register the flask extensions"""
def register_extension(app):
    #use '[ex].init_app(app)' methods from extensions here
    pass