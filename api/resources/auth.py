from flask_restful import Resource
from flask import request

from werkzeug.security import generate_password_hash

from extensions import db

from models import User
from models_schemas import user_schema


"""
Create a new user

    form fields:
        -name
        -email
        -password
"""

class CreateUser(Resource):
    
    def is_email_already_in_use(self, email: str) -> bool:
        return User.query.filter(User.email == email).first() is not None
    
    def post(self):
        
        if not 'name' in request.form or \
           not 'email' in request.form or \
           not 'password' in request.form:

            return {'message': 'there are fields missing'}, 400

        else:
            
            name = request.form['name']
            email = request.form['email']

            password = request.form['password']
            password = generate_password_hash(password)

            if self.is_email_already_in_use(email):
                return {'message': 'Email already in use'}, 400

            user = User(name, email, password)

            try:
                db.session.add(user)
                db.session.commit()

                return {
                    'message': 'New user successfully created', 
                    'data': user_schema.dump(user)
                    }, 201
            except:
                
                return {'message': 'Internal error'}, 500