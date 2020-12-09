from flask import Flask, jsonify, request
from flask_mongoengine import MongoEngine

app = Flask(__name__)


my_goals = [
    {
        "description": "flask app backend",
        "start": "342984203",
        "finish": "2342342344"
    },
    {
        "description": "flask app frontend",
        "start": "342984203",
        "finish": "2342342344"
    },
]


# simple example page
@app.route('/goals')
def return_goals():
    return jsonify(my_goals)

@app.route('/goals', methods=['POST'])
def add_goal():
    goal = request.get_json()
    my_goals.append(goal)
    return {'id': len(my_goals)}, 200


if __name__ == "__main__":
    app.run(debug=True)
