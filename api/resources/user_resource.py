from flask_restful import Resource
from flask import request

from werkzeug.security import generate_password_hash

from extensions import db

from models import User
from models_schemas import user_schema, users_schemas

from utils import check_fields


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

    # return a list with all users
    def get(self):
        users = User.query.all()
        return {
            'message': 'Users successufully find',
            'data': users_schemas.dump(users)
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
    
        password = generate_password_hash(password)

        if self.is_email_already_in_use(email):
            return {'error': 'Email already in use'}, 400

        user = User(name, email, password)

        # Try to create a new user
        try:
            db.session.add(user)
            db.session.commit()

            return {
                'message': 'New user successfully created', 
                'data': user_schema.dump(user)
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