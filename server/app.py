import re
from flask import Flask, jsonify, request
from flask_jwt_extended import create_access_token, JWTManager, jwt_required, get_jwt_identity
from server.domain import db_session
from server.domain.user import User
from server.domain.profile import Profile
from server.repository.user_repository import UserRepository
from server.repository.profile_repository import ProfileRepository
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
jwt = JWTManager(app)
app.config["JWT_SECRET_KEY"] = "super-secret"  # Change this!
user_repository = UserRepository()
profile_repository = ProfileRepository()


@app.route('/register', methods=['POST'])
def register():
    params = request.json

    user = User(**params)

    token = create_access_token(identity=[user.username, user.password])

    user_repository.add(user)

    new_user = user_repository.get_user_by_username(params['username'])
    profile = Profile(user_id=new_user.id, username=params['username'], name=params['username'])
    profile_repository.add(profile)

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
    profile = profile_repository.get_profile_by_username(username)
    return {
        'username': profile.username,
        'name': profile.name,
        'surname': profile.surname,
        'about': profile.about,
        'technologies' : profile.technologies,
        'type_of_activity' : profile.type_of_activity,
        'age' : profile.age,
        'phone_number' : profile.phone_number,
        'education' : profile.education,
        'social_networks' : profile.social_networks
    }

@app.route('/profile_edit', methods=['POST'])
@jwt_required()
def profile_edit():
    user = get_jwt_identity()
    if user is not None:
        params = request.json

        profile = profile_repository.get_profile_by_username(user[0])

        profile_repository.update(profile.user_id, Profile(**params))
        return {"status":"success"}
    else:
        return {"error": "No user with this token"}


if __name__ == '__main__':
    db_session.global_init()
    app.run(debug=True)

