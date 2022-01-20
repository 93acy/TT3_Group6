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
    posts = db.relationship('Post', backref='user', lazy=True)

    def __init__(self, username, password):
        self.username = username
        self.password = password

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), unique=True)
    description = db.Column(db.String(200))
    image = db.Column(db.String(200))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __init__(self, title, description, image, user_id):
        self.title = title
        self.description = description
        self.image = image
        self.user_id = user_id

# Schema
class UserSchema(ma.Schema):
    class Meta:
        fields = ('id', 'username', 'password')

class PostSchema(ma.Schema):
    class Meta:
        fields = ('id', 'title', 'description', 'image', 'user_id')

# Init schema
user_schema = UserSchema()
post_schema = PostSchema()
posts_schema = PostSchema(many=True)

with app.app_context():
    db.create_all()

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
    password = request.json['password']
    user = User.query.filter(User.username == username).one_or_none()
    if user.password == password:
        return "{'message': 'True'}"
    return "{'message': 'False'}"

# # Get Single User
# @app.route('/user/<id>', methods=['GET'])
# def get_user(id):
#     user = User.query.get(id)
#     return user_schema.jsonify(user)

# Get All posts
@app.route('/post', methods=['GET'])
def get_post():
    all_posts = Post.query.all()
    result = posts_schema.dump(all_posts)
    print(result)
    return jsonify(result)

# Create new post
@app.route('/post', methods=['POST'])
def add_post():
    title = request.json['title']
    description = request.json['description']
    image = request.json['image']
    user_id = request.json['user_id']

    new_post = Post(title, description, image, user_id)
    print(new_post)
    db.session.add(new_post)
    db.session.commit()
    return post_schema.jsonify(new_post)

# Update a Post
@app.route('/post/<id>', methods=['PUT'])
def update_post(id):
    post = Post.query.get(id)

    title = request.json['title']
    description = request.json['description']
    image = request.json['image']
    user_id = request.json['user_id']

    post.title = title
    post.description = description
    post.image = image
    post.user_id = user_id

    db.session.commit()
    return post_schema.jsonify(post)

# Delete Post
@app.route('/post/<id>', methods=['DELETE'])
def delete_post(id):
    post = Post.query.get(id)
    db.session.delete(post)
    db.session.commit()
    return "{'code': 200}"

#     return post_schema.jsonify(post)
# Run Server
if __name__ == '__main__':
    app.run(debug=True)