from functools import wraps
from flask import request


def is_json_content_type():
    """
    Middleware to check if the body received is JSON type
    """
    def _is_json_content_type(f):
        @wraps(f)
        def __is_json_content_type(*args, **kwargs):
            content_type = request.headers.get('Content-Type')

            if (content_type != "application/json"):
                return 'Content-Type Not Supported!'
            return f(*args, **kwargs)
        return __is_json_content_type
    return _is_json_content_type
