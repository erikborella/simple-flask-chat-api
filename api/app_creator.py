from flask import Flask
from extensions import db

"""Create and configure Flask instance"""
def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')

    register_extension(app)
    
    return app

"""Register the flask extensions"""
def register_extension(app):
    #use '[ex].init_app(app)' methods from extensions here
    
    db.init_app(app)