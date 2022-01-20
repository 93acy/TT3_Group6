import json
from datetime import datetime, timedelta

import jwt

from config import Config


PAYLOAD_TEMPLATE = '{{ "username": "{username}", "iat": "{iat}", "exp": "{exp}" }}'

def generate_token(username):
    current_time = datetime.now()
    token = jwt.encode(
        json.loads(PAYLOAD_TEMPLATE.format(
            username=username, 
            iat=int(current_time.timestamp()),
            exp=int((current_time + timedelta(minutes=30)).timestamp())
            )),
        'asdasd',
        algorithm='HS256'
    )
    return token

def validate_token(token):
    return jwt.decode(token, "asdasd", algorithms='HS256')

# def login_required():



