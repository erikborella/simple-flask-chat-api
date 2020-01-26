import jwt
import datetime

from config import SECRET_KEY

from models import User

from utils.validators import is_user_valid_or_raise_error, is_authorization_fields_valid

from flask import request

from werkzeug.security import check_password_hash

def __generate_token(user: User):

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


def auth(email=None, password=None):

    if not email or not password:
        if not is_authorization_fields_valid():
            return None
        else:
            email = request.authorization.username
            password = request.authorization.password

    user = User.query.filter_by(email=email).first_or_404("Email or password is invalid")

    print(password)

    if user and check_password_hash(user.password, password):

        token = __generate_token(user)
        token = token.decode('UTF-8')

        return token

    else:

        return None
