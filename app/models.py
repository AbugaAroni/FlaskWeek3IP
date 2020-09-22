from . import db
from werkzeug.security import generate_password_hash,check_password_hash

class Pitch:

    all_pitches = []

    def __init__(self,pitch_id,pitch_title,pitch_description,pitch_category):
        self.id = pitch_id
        self.title = pitch_title
        self.category = pitch_category
        self.description = pitch_description

    def save_pitches(self):
        Pitch.all_pitches.append(self)


    @classmethod
    def clear_pitches(cls):
        Pitch.all_pitches.clear()

    @classmethod
    def get_pitches(cls,category):

        response = []

        for pitches in cls.all_pitches:
            if pitch.pitch_category == category:
                response.append(pitch)

        return response

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)


    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))
    role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))
    pass_secure = db.Column(db.String(255))


    def __repr__(self):
        return f'User {self.username}'

class Role(db.Model):
    __tablename__ = 'roles'

    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(255))
    users = db.relationship('User',backref = 'role',lazy="dynamic")


    def __repr__(self):
        return f'User {self.name}'
