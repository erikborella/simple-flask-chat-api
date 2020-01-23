import sys
from functools import wraps

from flask import request

def check_fields(fields=()):

    def decorator(f):

        @wraps(f)
        def wrap(*args, **kwargs):
            if not fields:
                raise Exception("Expected at least 1 field")

            error_message = {
                "error": "Invalid payload",
                "detail": {}
            }

            has_missing_fields: bool = False

            for field in fields:
                if field not in request.form:
                    error_message['detail'][field] = "This field is required"
                    has_missing_fields = True

            if has_missing_fields:
                return error_message, 400
            else:
                return f(*args, **kwargs)

        return wrap
    return decorator