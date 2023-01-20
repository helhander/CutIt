import random
import string
from flask import request
import re
LINK_ID_DEFAULT_SYMBOLS = string.ascii_letters + string.digits


def get_unique_short_id():
    return ''.join(random.sample(LINK_ID_DEFAULT_SYMBOLS, 6))


def validate_id(id):
    return bool(re.fullmatch(f'[{LINK_ID_DEFAULT_SYMBOLS}]*', id))


def get_service_url(param):
    domain = '/'.join(request.base_url.split('/')[:3])
    return f'{domain}/{param}'