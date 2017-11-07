from .wrappers import *


def user_is_login(request):
    return get_session(request, 'username') and get_session(request, 'uid')
