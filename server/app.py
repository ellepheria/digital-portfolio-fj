import re
from flask import Flask, request
from flask_jwt_extended import create_access_token, JWTManager, jwt_required, get_jwt_identity
from server.domain import db_session
from server.domain.__all_models import *
from server.repository.__all_repository import *
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
jwt = JWTManager(app)
app.config["JWT_SECRET_KEY"] = "digital-portfolio-fj"
user_repository = UserRepository()


@app.route('/register', methods=['POST'])
def register():
    params = request.json

    user = User(**params)
    print(params)

    token = create_access_token(identity=[user.username, user.email, user.password])
    user.name = params["username"]

    user_repository.add(user)

    return {'access_token': token}


@app.route('/login', methods=['POST'])
def login():
    params = request.json
    pattern = r"^[-\w\.]+@([-\w]+\.)+[-\w]{2,4}$"

    # Проверка на email
    if re.match(pattern, params['login']) is not None:
        user_data = {
            'email': params['login'],
            'password': params['password']
        }
        if user := user_repository.get_user_by_email(User(**user_data).email):
            if params['password'] != user.password:
                return {"error": "No user with this password"}
            else:
                token = create_access_token(identity=[user.username, user.password])
                return {'access_token': token, 'username': user.username}
        else:
            return {"error": "No user with this email in database"}
    else:
        user_data = {
            'username': params['login'],
            'password': params['password']
        }
        if user := user_repository.get_user_by_username(User(**user_data).username):
            if params['password'] != user.password:
                return {"error": "No user with this password"}
            else:
                token = create_access_token(identity=[user.username, user.password])
                return {'access_token': token, 'username': user.username}
        else:
            return {"error": "No user with this username in database"}


@app.route('/get_profile/<username>', methods=['GET'])
def get_profile(username):
    profile = user_repository.get_user_by_username(username)
    return {
        'username': profile.username,
        'name': profile.name,
        'surname': profile.surname,
        'about': profile.about,
        'technologies': profile.technologies,
        'type_of_activity': profile.type_of_activity,
        'age': profile.age,
        'phone_number': profile.phone_number,
        'education': profile.education,
        'social_networks': profile.social_networks
    }


@app.route('/profile_edit', methods=['POST'])
@jwt_required()
def profile_edit():
    user = get_jwt_identity()
    if user is not None:
        params = request.json

        profile = user_repository.get_user_by_username(user[0])
        new_user = User(**params)
        new_user.email = user[1]
        new_user.password = user[2]

        print(new_user)

        user_repository.update(new_user, profile.user_id)
        user[0] = params["username"]

        token = create_access_token(identity=[user[0], user[1], user[2]])

        return {'access_token': token, 'username': user[0]}
    else:
        return {"error": "No user with this token"}


if __name__ == '__main__':
    db_session.global_init()
    app.run(debug=True)
