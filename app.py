from flask import Flask, request, Response
from database.db import initialize_db
from database.models import Goal

app = Flask(__name__)
print("initializing app")

app.config['MONGODB_SETTINGS'] = {
    'host': 'mongodb://localhost/all_events'
    }

db = initialize_db(app)
print("initializing db in app.py")


@app.route('/goals')
def get_goals():
    print("starting get_goals")
    goals = Goal.objects().to_json()
    return Response(goals, mimetype="application/json", status=200)


@app.route('/goals', methods=['POST'])
def add_goal():
    print("starting add_goal")
    body = request.get_json()
    goal = Goal(**body).save()
    id = goal.id
    return {'id': str(id)}, 200


@app.route('/goals/<id>')
def get_goal(id):
    goals = Goal.objects.get(id=id).to_json()
    return Response(goals, mimetype="application/json", status=200)


if __name__ == "__main__":
    app.run(debug=True)
