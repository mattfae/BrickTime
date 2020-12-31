from flask import Blueprint, request

auth_bp = Blueprint(
    'auth.bp', __name__,
)


@auth_bp.route('/login', methods=['GET', 'POST'])
def login():

@auth_bp.route('/signup', methods=['GET', 'POST'])
def signup():
    