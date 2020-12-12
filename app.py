from flask import Flask, request, Response
from database.db import initialize_db
from database.models import Goal

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

app.config['MONGODB_SETTINGS'] = {
    'host': 'mongodb://localhost/movie-bag'
    }

initialize_db(app)


@app.route('/goals')
def get_goals():
   goals = Goal.objects().to_json()
   return Response(goals, mimetype="application/json", status=200)


@app.route('/goals', methods=['POST'])
def add_goal():
    body = request.get_json()
    goal = Goal(**body).save()
    id = goal.id
    return {'id': str(id)}, 200


@app.route('/movies/<id>')
def get_goal(id):
    movies = Movie.objects.get(id=id).to_json()
    return Response(movies, mimetype="application/json", status=200)


if __name__ == "__main__":
    app.run(debug=True)
