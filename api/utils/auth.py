import jwt
import datetime

from config import SECRET_KEY

from models import User

from utils.validators import is_user_valid_or_raise_error

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
