from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class Note(db.Model):
    # Change this to the format of a post later
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    data = db.Column(db.DateTime(timezone=True), default=func.now())
    # Get the user id out of the database part of the user, foreign keys use lowercase
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    # 150 is the max String length, and it should be an unique email
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    # The notes that a user has created, relationships use capital
    notes = db.relationship('Note')
