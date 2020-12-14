from flask_mongoengine import MongoEngine

db = MongoEngine()

def initialize_db(app):
    print('mongo db init')
    db.init_app(app)