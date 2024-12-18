from .db import db
from datetime import datetime


class Dialog(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, nullable=False)
    title = db.Column(db.String(50), nullable=False, default='New Chat')
    created_time = db.Column(db.TIMESTAMP, nullable=True, default=datetime.now())
    updated_time = db.Column(db.TIMESTAMP, nullable=True, onupdate=datetime.now())

    def __repr__(self):
        return f'<Dialog id={self.id}, user_id={self.user_id}, title={self.title}>'