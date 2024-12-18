from .db import db
from datetime import datetime


class Bot(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, nullable=False)
    avatar = db.Column(db.String(255), nullable=True)
    name = db.Column(db.String(20), nullable=False)
    created_time = db.Column(db.TIMESTAMP, nullable=True, default=datetime.now())
    updated_time = db.Column(db.TIMESTAMP, nullable=True, onupdate=datetime.now())

    def __repr__(self):
        return f'<Bot id={self.id}, user_id={self.user_id}, name={self.name}>'