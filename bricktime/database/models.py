from .db import db
from datetime import datetime

class Goal(db.Document):
    description = db.StringField(required=True)
    categories = db.ListField(db.StringField())
    start = db.DateTimeField(required=True, default=datetime.datetime.utcnow)
    finish = db.DateTimeField(required=True, default=datetime.datetime.utcnow)

class User(db.Document):
    email = db.StringField(required=True, unique=True)
    password = db.StringField()
    authenticated = db.BooleanField(default=False)

    def is_active(self):
        return True

    def get_id(self):
        """Return the email address to satisfy Flask-Login's requirements."""
        return self.email

    def is_authenticated(self):
        """Return True if the user is authenticated."""
        return self.authenticated

    def is_anonymous(self):
        """False, as anonymous users aren't supported."""
        return False