from flask import Flask, jsonify, request
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
    token = user.get_token()
    return {'access_token': token}


@app.route('/login', methods=['POST'])
def login():
    params = request.json
    user = User.authenticate(**params)
    token = user.get_token()
    return {'access_token': token}


if __name__ == '__main__':
    db_session.global_init()
    app.run(debug=True)