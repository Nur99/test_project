from copy import deepcopy, copy
from functools import wraps
from rest_framework.status import is_success
from utils import codes
import json


def response_wrapper():
    """
    Decorator to make a view only accept request with required http method.
    :param required http method.
    """

    def decorator(func):
        @wraps(func)
        def inner(request, *args, **kwargs):
            response = func(request, *args, **kwargs)
            if is_success(response.status_code):
                if hasattr(response, 'data'):
                    data = deepcopy(response.data)
                    response.data = {'result': data, 'code': codes.OK}
                else:
                    content = json.loads(
                        deepcopy(response.content.decode('utf-8'))) if response.content else None
                    response.content = json.dumps(
                        {'result': content, 'code': codes.OK})
            return response

        return inner

    return decorator
