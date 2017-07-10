"""
Models for the flask application.
"""

from app import db
from datetime import datetime


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer , primary_key=True)
    username = db.Column(db.String(20), unique=True , index=True)
    password = db.Column(db.String(10))
    email = db.Column(db.String(50),unique=True , index=True)
    registered_on = db.Column(db.DateTime)
 
    def __init__(self , username ,password , email):
        self.username = username
        self.password = password
        self.email = email
        self.registered_on = datetime.utcnow()
 
    def is_authenticated(self):
        return True
 
    def is_active(self):
        return True
 
    def is_anonymous(self):
        return False
 
    def get_id(self):
        return unicode(self.id)
 
    def __repr__(self):
        return '<User %r>' % (self.username)