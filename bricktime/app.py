import os
from flask import Flask
from database.db import initialize_db
from database.models import Goal
from database.models import User
from resources.goal import goals

app = Flask(__name__)

app.config['MONGODB_SETTINGS'] = {
    'db': 'all_events',
    'host': 'mongodb://localhost/all_events'
    }

initialize_db(app)

app.secret_key = os.environ.get('SECRET_KEY', 'dev')

@login_manager.user_loader
def user_loader(email):
    """Given *user_id*, return the associated User object.

    :param unicode user_id: user_id (email) user to retrieve

    """
    return User.objects(email)

if __name__ == "__main__":
    app.run(debug=True)
