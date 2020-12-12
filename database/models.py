from .db import db

class Goal(db.Document):
    description = db.StringField(required=True, unique=True)
    start = db.StringField(required=True, unique=True)
    finish = db.StringField(required=True, unique=True)
