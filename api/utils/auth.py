import jwt
import datetime

import sys
from functools import wraps

from config import SECRET_KEY, DEBUG

from models import User

from utils.validators import is_user_valid_or_raise_error, is_authorization_fields_valid

from flask import request

from werkzeug.security import check_password_hash


def __generate_token(user: User):

    is_user_valid_or_raise_error(user)

    if DEBUG:

        token = jwt.encode(
            {
                'email': user.email,
                "debug token": True
            },
            SECRET_KEY
        )
        
    else:

        token = jwt.encode(
            {
                'email': user.email,
                'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=12)
            },
            SECRET_KEY
        )

    return token


def auth(email=None, password=None):

    if not email or not password:
        if not is_authorization_fields_valid():
            return {
                'error': 'Invalid payload',
                'detail': 'There are fields missing'
            }
        else:
            email = request.authorization.username
            password = request.authorization.password

    user = User.query.filter_by(email=email).first_or_404("Email or password is invalid")

    if user and check_password_hash(user.password, password):

        token = __generate_token(user)
        token = token.decode('UTF-8')

        return token

    else:

        return {
            'error': 'Email or passowrd is invalid'
        }


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):

        token = request.headers.get('Authorization')

        if not token:
            return {
                'error': 'Token is missing'
            }, 401

        token = token.replace("Bearer ", "")

        try:
            data = jwt.decode(token, SECRET_KEY)
            user: User = User.query.filter_by(email=data['email']).first()

        except:
            return {
                'error': 'Token is invalid or expired'
            }, 401

        kwargs['user'] = user
        return f(*args, **kwargs)
    return decorated