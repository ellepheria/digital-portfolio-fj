import re
from flask import Flask, jsonify, request
from flask_jwt_extended import create_access_token, JWTManager
from server.domain import db_session
from server.domain.user import User
from server.repository.user_repository import UserRepository
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
jwt = JWTManager(app)
app.config["JWT_SECRET_KEY"] = "super-secret"  # Change this!
jwt = JWTManager(app)
user_repository = UserRepository()


@app.route('/register', methods=['POST'])
def register():
    params = request.json
    user = User(**params)
    token = create_access_token(identity=[user.username, user.password])
    user_repository.add(user)
    return {'access_token': token}


@app.route('/login', methods=['POST'])
def login():
    params = request.json
    pattern = r"^[-\w\.]+@([-\w]+\.)+[-\w]{2,4}$"

    print(params)

    # Проверка на email
    if re.match(pattern, params['login']) is not None:
        user_data = {
            'email': params['login'],
            'password': params['password']
        }
        if user := user_repository.get_user_by_email(User(**user_data).email):
            if params['password'] != user.password:
                raise Exception('No user with this password')
            else:
                token = create_access_token(identity=[user.username, user.password])
                return {'access_token': token}
        else:
            raise Exception('No user with this email')
    else:
        user_data = {
            'username': params['login'],
            'password': params['password']
        }
        if user := user_repository.get_user_by_username(User(**user_data).username):
            if params['password'] != user.password:
                raise Exception('No user with this password')
            else:
                token = create_access_token(identity=[user.username, user.password])
                return {'access_token': token}
        else:
            raise Exception('No user with this username')


if __name__ == '__main__':
    db_session.global_init()
    app.run(debug=True)

