from app import db


class UserPassword(db.Model):
    User_ID = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32))
    password_hash = db.Column(db.String(128))

    def to_dict(self):
        return {
            'User_ID': self.User_ID,
            'username': self.username,
            'password': self.password_hash
        }
    
    def __repr__(self):
        return '<UserPassword {}>'.format(self.username)

class User(db.Model):
    User_ID = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(50), index=True, unique=True)
    Age = db.Column(db.Integer, index=True, unique=True)
    Birthday = db.Column(db.Date)
    Email = db.Column(db.String(50), unique=True)
    Phone = db.Column(db.String(50), unique=True)
    City = db.Column(db.String(50))
    Country = db.Column(db.String(50))
    # password_hash = db.Column(db.String(128))

    def to_dict(self):
        return {
            'User_ID': self.User_ID,
            'Name': self.Name,
            'Age': self.Age,
            'Birthday': str(self.Birthday),
            'Email': self.Email,
            'Phone': self.Phone,
            'City': self.City,
            'Country': self.Country
        }

    def __repr__(self):
        return '<User {}>'.format(self.User_ID)


class Post(db.Model):
    Post_ID = db.Column(db.Integer, primary_key=True)
    Post_Title = db.Column(db.String(50))
    Post_Description = db.Column(db.String(200))
    Post_image = db.Column(db.String(200))


    def to_dict(self):
        return {
            'Post_ID': self.Post_ID,
            'Post_Title': self.Post_Title,
            'Post_Description': self.Post_Description,
            'Post_image': self.Post_image
        }

    def __repr__(self):
        return '<Post {}>'.format(self.Post_ID)

class LikedPost:
    User_ID = db.Column(db.Integer, primary_key=True)
    Post_ID = db.Column(db.Integer, primary_key=True)

    def to_dict(self):
        return {
            'User_ID': self.User_ID,
            'Post_ID': self.Post_ID
        }

    def __repr__(self):
        return '<LikedPost {}, {}>'.format(self.User_ID, self.Post_ID)

class PostComment:
    Comment_ID = db.Column(db.Integer, primary_key=True)
    User_ID = db.Column(db.Integer)
    Post_ID = db.Column(db.Integer)
    Comment = db.Column(db.Text)

    def to_dict(self):
        return {
            'Comment_ID': self.Comment_ID,
            'User_ID': self.User_ID,
            'Post_ID': self.Post_ID,
            'Comment': self.Comment
        }

    def __repr__(self):
        return '<PostComment {}>'.format(self.Comment_ID)



