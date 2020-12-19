from flask_login import LoginManager
from .database.models import User

login_manager = LoginManager()

@login_manager.user_loader
def user_loader(email):
    """Given *user_id*, return the associated User object.

    :param unicode user_id: user_id (email) user to retrieve

    """
    return User.objects(email)