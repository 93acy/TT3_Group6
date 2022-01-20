from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy 
from flask_marshmallow import Marshmallow 
import os

# Init app
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
# Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Init db
db = SQLAlchemy(app)
# Init ma
ma = Marshmallow(app)

# Class/Model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(200))
    # posts = db.relationship('Post', backref='user', lazy=True)

    def __init__(self, username, password):
        self.username = username
        self.password = password

# class Post(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(100), unique=True)
#     description = db.Column(db.String(200))
#     image = db.Column(db.Integer, db.ForeignKey('user.id', nullable=False))

#     def __init__(self, username, password):
#         self.username = username
#         self.password = password

# Schemas
class UserSchema(ma.Schema):
    class Meta:
        fields = ('id', 'username', 'password', 'posts')

# class PostSchema(ma.Schema):
#     class Meta:
#         fields = ('id', 'title', 'description', 'image')

# Init schema
user_schema = UserSchema()
# post_schema = PostSchema()
# posts_schema = PostSchema(many=True)

# Create a User
@app.route('/user', methods=['POST'])
def add_user():
    username = request.json['username']
    password = request.json['password']

    new_user = User(username, password)

    db.session.add(new_user)
    db.session.commit()
    return user_schema.jsonify(new_user)

# Login
@app.route('/login', methods=['POST'])
def login():
    username = request.json['username']
    #   user = User.query.get(username)
    return "{'message': 'True'}"

# @app.route('/post', methods=['POST'])
# def add_post():
#     title = request.json['title']
#     description = request.json['description']
#     image = request.json['image']

#     new_post = Post(title, description, image)

#     db.session.add(new_post)
#     db.session.commit()
#     return user_schema.jsonify(new_post)

# # Get All posts
# @app.route('/post', methods=['GET'])
# def get_post():
#     all_posts = Post.query.all()
#     result = posts_schema.dump(all_posts)
#     print(result)
#     return jsonify(result)

# # Get Single Post
# @app.route('/post/<id>', methods=['GET'])
# def get_post(id):
#     post = Post.query.get(id)
#     print(post)
#     return post_schema.jsonify(post)

# # Update a Post
# @app.route('/post/<id>', methods=['PUT'])
# def update_post(id):
#     post = Post.query.get(id)

#     title = request.json['title']
#     description = request.json['description']
#     image = request.json['image']

#     post.name = title
#     post.description = description
#     post.price = image

#     db.session.commit()
#     return post_schema.jsonify(post)

# # Delete Post
# @app.route('/post/<id>', methods=['DELETE'])
# def delete_post(id):
#     post = Post.query.get(id)
#     db.session.delete(post)
#     db.session.commit()

#     return post_schema.jsonify(post)

# Run Server
if __name__ == '__main__':
    app.run(debug=True)
