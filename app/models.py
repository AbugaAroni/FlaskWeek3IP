from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager
from datetime import datetime

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

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

class User(UserMixin,db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255),index = True)
    email = db.Column(db.String(255),unique = True,index = True)
    role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    pass_secure = db.Column(db.String(255))

    pitches = db.relationship('Pitch',backref = 'user',lazy = "dynamic")

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)


    def verify_password(self,password):
        self.pass_secure = generate_password_hash(password)
        return check_password_hash(self.pass_secure,password)

    def __repr__(self):
        return f'User {self.username}'

class Role(db.Model):
    __tablename__ = 'roles'

    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(255))
    users = db.relationship('User',backref = 'role',lazy="dynamic")


    def __repr__(self):
        return f'User {self.name}'

class Pitch(db.Model):

    __tablename__='pitches'

    id = db.Column(db.Integer,primary_key = True)
    pitch_title = db.Column(db.String)
    pitch_category = db.Column(db.String)
    pitch_description = db.Column(db.String)
    posted = db.Column(db.DateTime,default=datetime.utcnow)
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))

    def save_pitch(self):
        db.session.add(self)
        db.session.commit()

    #get pitches according to persons id
    @classmethod
    def get_userpitch(cls,id):
        pitches = Pitch.query.filter_by(user_id=id).all()
        return pitches

    #get pitches according to persons id
    @classmethod
    def get_pitchcat(cls,cat):
        pitches = Pitch.query.filter_by(pitch_category=cat).all()
        return pitches

    #get all pitches
    @classmethod
    def get_pitches(cls):
        pitches = Pitch.query.all()
        return pitches
