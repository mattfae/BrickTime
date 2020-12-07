from flask import Flask
from flask_mongoengine import MongoEngine

app = Flask(__name__)

# simple example page
@app.route('/hello')
def hello():
    return "Hello, World"

if __name__ == "__main__":
    app.run(debug=True)
