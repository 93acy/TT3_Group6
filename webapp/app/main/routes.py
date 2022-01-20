import resource
from flask import request
from flask_restx import Resource
from werkzeug.exceptions import Unauthorized

from app.main import api
from app.auth import login, generate_token, login_required
from app.models import Post


@api.route('/health')
class HealthCheck(Resource):
    @api.doc(responses={200: 'OK', 400: 'Errors'})
    def get(self):
        token = generate_token('asdasd')
        return {'status': 'service is up and running', 'token': token}, 200

@api.route('/login')
class Login(Resource):
    @api.doc(responses={200: 'OK', 400: 'Errors'})
    def post(self):
        data = request.json
        if not data:
            raise Unauthorized('username or password not provided')
        if 'username' in data and 'password' in data:
            valid, user_id = login(data['username'], data['password'])
            if valid:
                token = generate_token(data['username'], user_id)
                return {"token": token, "boolean" : True}, 200
            else:
                raise Unauthorized('invalid username or password')
        else:
            raise Unauthorized('username or password not provided')

@api.route('/get-post')
class GetAllPosts(Resource):
    @api.doc(responses={200: 'OK', 400: 'Errors'})
    def get(self):
        a = Post.query.all()
        list =[]
        for x in a:
            list.append(x.to_dict())
        return list, 200
