from flask_restx import Resource

from app.main import api
from app.auth import generate_token
from app.models import User

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