import jwt
import datetime

from config import SECRET_KEY

from models import User

from utils.validators import is_user_valid_or_raise_error, is_authorization_fields_valid

from flask import request

from werkzeug.security import check_password_hash

def generate_token(user: User):

    is_user_valid_or_raise_error(user)

    token = jwt.encode(
        {
            'name': user.name,
            'email': user.email,
            'image': user.image,
            'exp': datetime.datetime.now() + datetime.timedelta(hours=12)
        },
        SECRET_KEY
    )

    return token

def authentication_error():
    return {
            'error': 'could not verify', 
            'WWW-Authenticate': 'Basic auth="Login required"'
        }, 401

def auth():

    if not is_authorization_fields_valid():
        return authentication_error()
    
    auth = request.authorization

    user = user = User.query.filter_by(email=auth.username).first_or_404("User id cannot be find")

    if user and check_password_hash(user.password, auth.password):

        token = generate_token(user)
        token = token.decode('UTF-8')

        return {
            'message': 'Successfully authenticate',
            'token': token,
            'exp': str(datetime.datetime.now() + datetime.timedelta(hours=12))
        }

    else:

        return authentication_error()
