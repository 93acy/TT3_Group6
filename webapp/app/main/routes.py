import resource
from flask import request
from flask_restx import Resource
from werkzeug.exceptions import Unauthorized

from app import db
from app.main import api
from app.auth import login, generate_token, login_required
from app.models import Post, LikedPost


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
                return {"token": token}, 200
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

@api.route('/get-user-posts')
class GetUserPost(Resource):
    @api.doc(responses={200: 'OK', 400: 'Errors'})
    @login_required
    def get(payload, self):
        current_user_id = payload['User_ID']
        a = LikedPost.query.filter_by(User_ID=current_user_id)
        list = []
        for likedpost in a:
            p = Post.query.filter_by(Post_ID=likedpost.Post_ID).first()
            list.append(p.to_dict())
        return list, 200

@api.route('/create-post')
class CreatePost(Resource):
    @api.doc(responses={200: 'OK', 400: 'Errors'})
    @login_required
    def post(payload, self):
        current_user_id = payload['User_ID']
        data = request.json
        
        if 'Post_Title' not in data or 'Post_Description' not in data or 'Post_image' not in data:
            return {"message": "Post_Title, Post_Descriptionor Post_image not provided"}, 400

        p = Post(Post_Title=data['Post_Title'], Post_Description=data['Post_Description'], Post_image=data['Post_image'])
        session = db.session()
        session.add(p)
        session.commit()

        lp = LikedPost(User_ID=current_user_id, Post_ID=p.Post_ID)
        session = db.session()
        session.add(lp)
        session.commit()
        return {"message": "post created", "post_id": p.Post_ID}, 201