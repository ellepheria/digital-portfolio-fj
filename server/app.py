import re
from datetime import timedelta
from flask import Flask, jsonify, request
from flask_jwt_extended import create_access_token
from passlib.hash import bcrypt
from server.domain import db_session
from server.domain.user import User
from server.repository.user_repository import UserRepository
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
user_repository = UserRepository()


@app.route('/register', methods=['POST'])
def register():
    params = request.json
    user = User(**params)
    user_repository.add(user)
    token = create_access_token(identity=[user.username, user.password], expire_delta=timedelta(24))
    return {'access_token': token}


@app.route('/login', methods=['POST'])
def login():
    params = request.json
    pattern = r"^[-\w\.]+@([-\w]+\.)+[-\w]{2,4}$"

    # Проверка на email
    if re.match(pattern, params.login) is not None:
        user = user_repository.get_user_by_email(User(**params).email)
        if not bcrypt.verify(params.password, user.password):
            raise Exception('No user with this password')
        else:
            token = create_access_token(identity=[user.username, user.password], expire_delta=timedelta(24))
            return {'access_token': token}
    else:
        user = user_repository.get_user_by_username(User(**params).username)
        if not bcrypt.verify(params.password, user.password):
            raise Exception('No user with this password')
        else:
            token = create_access_token(identity=[user.username, user.password], expire_delta=timedelta(24))
            return {'access_token': token}


if __name__ == '__main__':
    db_session.global_init()
    app.run(debug=True)