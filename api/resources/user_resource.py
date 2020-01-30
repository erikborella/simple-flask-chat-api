import os
import urllib.request

from flask_restful import Resource, reqparse
from flask import request

import werkzeug

from werkzeug.security import generate_password_hash
from werkzeug.utils import secure_filename

from extensions import db

from models import User
from models_schemas import user_schema, users_schemas

from utils.validators import check_fields
from utils import auth

from config import ALLOWED_EXTENSIONS, UPLOAD_FOLDER

import datetime

"""
get: return all users
post: create a new user
    *required fileds
    - name
    - password
    - email
"""
class Users(Resource):

    def is_email_already_in_use(self, email: str) -> bool:
        return User.query.filter(User.email == email).first() is not None

    @auth.token_required
    def get(self, **kwargs):
        user = kwargs.get('user')
        return {
            'message': 'User successfuly find',
            'data': user_schema.dump(user)
        }

    
    # check if all the fields are correct
    @check_fields(fields=("name", "email", "password"))
    # create a new user
    def post(self, **kwargs):

        # get the fields dict content all fields value 
        # injected by 'check_fields' decorator
        fields = kwargs.get('fields')

        name = fields.get('name')
        email = fields.get('email')
        password = fields.get('password')
    
        if self.is_email_already_in_use(email):
            return {'error': 'Email already in use'}, 400

        user = User(name, email, generate_password_hash(password))

        # Try to create a new user
        try:
            db.session.add(user)
            db.session.commit()

            token = auth.auth(email=email, password=password)
            
            return {
                'message': 'New user successfully created', 
                'data': user_schema.dump(user),
                'token': token,
                'exp': str(datetime.datetime.now() + datetime.timedelta(hours=12))
                }, 201

        except:
                
            return {'message': 'Internal error'}, 500

"""
get: get one specific user
"""
class GetOneUser(Resource):
    def get(self, user_id):
        user = User.query.filter_by(id=user_id).first_or_404("User id cannot be find")
        return {
            'message': 'User successfully find',
            'data': user_schema.dump(user)
        }


class GetAllUsers(Resource):
    # return a list with all users
    def get(self):
        users = User.query.all()
        return {
            'message': 'Users successufully find',
            'data': users_schemas.dump(users)
        }


class Image(Resource):

    def allowed_file(self, filename: str) -> bool:
        return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
    
    def get_file_extension(self, filename: str) -> str:
        return filename.split('.')[-1]

    def remove_email_domain(self, filename: str) -> str:
        return filename.replace('.com', '')


    @auth.token_required
    def post(self, **kwargs):
        user: User = kwargs.get('user')

        if 'file' not in request.files:
            return {
                'error': 'No file part in the request'
            }, 400

        file = request.files['file']

        if file.filename == '':
            return{
                'error': 'No file selected for uploading'
            }, 400

        if file and self.allowed_file(file.filename):

            filename = "%s.%s" % (user.email, self.get_file_extension(file.filename))
            filename = self.remove_email_domain(filename)
            filename = secure_filename(filename)

            file.save(os.path.join(UPLOAD_FOLDER, filename))

            user.image = "public/%s" % filename
            db.session.commit()

            return {
                'message': 'File successfully uploaded'
            }, 201

        else:
            return {
                'error': 'allowed file types are jpg, jpeg and png'
            }, 400