from flask import Response, request
from flask import current_app as app
from . import login_manager
from .models import Goal, User

@login_manager.user_loader
def user_loader(email):
    """Given *user_id*, return the associated User object.

    :param unicode user_id: user_id (email) user to retrieve

    """
    return User.objects(email)

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