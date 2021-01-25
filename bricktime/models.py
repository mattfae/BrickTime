from . import db
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

# pylint: disable=no-member
class Goal(db.Document):
    description = db.StringField(required=True)
    categories = db.ListField(db.StringField())

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

    def set_password(self, password):
        self.password = generate_password_hash(
            password,
            method='sha256'
        )

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def __repr__(self):
        return '<User {}>'.format(self.username)
