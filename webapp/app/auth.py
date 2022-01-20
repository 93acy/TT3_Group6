import json
import requests
from functools import wraps
from datetime import datetime, timedelta

import jwt
from flask import request
from flask_bcrypt import Bcrypt
from werkzeug.exceptions import Unauthorized

from app.models import User, UserPassword
from config import Config


bcrypt = Bcrypt()

PAYLOAD_TEMPLATE = '{{ "username": "{username}", "User_ID": {User_ID}, "Name": "{Name}", "Age": {Age}, "Birthday": "{Birthday}", "Email": "{Email}", "Phone": "{Phone}", "City": "{City}", "Country": "{Country}", "iat": {iat}, "exp": {exp} }}'

def login(username, password):
    up = UserPassword.query.filter_by(username=username).first()
    if bcrypt.check_password_hash(up.password_hash, password):
        return True, up.User_ID
    else:
        return False, None

def generate_token(username, user_id):
    current_time = datetime.now()

    u = User.query.filter_by(User_ID=user_id).first()
    token = jwt.encode(
        json.loads(PAYLOAD_TEMPLATE.format(
            username=username,
            User_ID=u.User_ID,
            Name=u.Name,
            Age=u.Age,
            Birthday=u.Birthday,
            Email=u.Email,
            Phone=u.Phone,
            City=u.City,
            Country=u.Country,
            iat=int(current_time.timestamp()),
            exp=int((current_time + timedelta(minutes=30)).timestamp())
            )),
        Config.SECRET,
        algorithm='HS256'
    )
    return token

def validate_token(token):
    return jwt.decode(token, Config.SECRET, algorithms='HS256')

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not 'Authorization' in request.headers:
            raise Unauthorized('token not provided')

        data = request.headers['Authorization']
        token = str.replace(data, 'Bearer ','')
        try:
            print(token)
            payload = validate_token(token)
        except Exception as e:
            raise Unauthorized(str(e))

        return f(payload, *args, **kwargs)
    return decorated_function


