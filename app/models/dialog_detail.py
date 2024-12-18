from .db import db
from datetime import datetime


class DialogDetail(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    dialog_id = db.Column(db.Integer, nullable=False)
    content = db.Column(db.Text, nullable=True)
    type = db.Column(db.SmallInteger, nullable=False)
    created_time = db.Column(db.TIMESTAMP, nullable=True, default=datetime.now())
    updated_time = db.Column(db.TIMESTAMP, nullable=True, onupdate=datetime.now())

    def __repr__(self):
        return f'<DialogDetail id={self.id}, dialog_id={self.dialog_id}, type={self.type}>'