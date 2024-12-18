from .db import db
from datetime import datetime


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(255), nullable=True)
    password = db.Column(db.String(20), nullable=False)
    phone = db.Column(db.String(11), nullable=True)
    avatar = db.Column(db.String(255), nullable=True)
    created_time = db.Column(db.TIMESTAMP, nullable=True, default=datetime.now())
    updated_time = db.Column(db.TIMESTAMP, nullable=True, onupdate=datetime.now())

    def __repr__(self):
        return f'<User {self.username}>'