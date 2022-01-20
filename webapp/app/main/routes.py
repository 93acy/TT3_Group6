from typing import Dict
from flask_restx import Resource

from app.main import api
from app.auth import generate_token
from app.models import Post, User
import json

@api.route('/health')
class HealthCheck(Resource):
    @api.doc(responses={200: 'OK', 400: 'Errors'})
    def get(self):
        token = generate_token('asdasd')
        return {'status': 'service is up and running', 'token': token}, 200

@api.route('/test')
class Test(Resource):
    @api.doc(responses={200: 'OK', 400: 'Errors'})
    def get(self):
        a = User.query.filter_by(Name='Brose McCreery').first()
        print(a)
        print(type(a))
        print(type(a.to_dict))
        print(type(a.to_dict()))
        print(a.to_dict())
        return a.to_dict(), 200

@api.route('/get_post')
class getAllPosts(Resource):
    @api.doc(responses={200: 'OK', 400: 'Errors'})
    def get(self):
        a = Post.query.all()
        list =[]
        for x in a:
            list.append(x.to_dict())
            # print(x.to_dict())
       
        return list, 200
