import re
from datetime import timedelta

from flask import Flask, request, make_response
from flask_jwt_extended import create_access_token, JWTManager, jwt_required, get_jwt_identity
from server.domain import db_session
from server.domain.__all_models import *
from server.repository.__all_repository import *
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
jwt = JWTManager(app)
app.config["JWT_SECRET_KEY"] = "digital-portfolio-fj"
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(days=30)
app.config["JWT_REFRESH_TOKEN_EXPIRES"] = timedelta(days=30)
UPLOAD_FOLDER = 'server/files'
user_repository = UserRepository()
profile_file_repository = ProfileFileRepository()


@app.route('/register', methods=['POST'])
def register():
    params = request.json

    user = User(**params)

    token = create_access_token(identity=[user.username, user.email, user.password])
    user.name = params["username"]

    user_repository.add(user)
    id_ = user_repository.get_user_by_username(params["username"]).user_id
    profile_file = ProfileFile(user_id=id_)

    profile_file_repository.add(profile_file)

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
                return {'error': 'No user with this password'}
            else:
                token = create_access_token(identity=[user.username, user.email, user.password])
                return {'access_token': token, 'username': user.username}
        else:
            return {'error': 'No user with this email in database'}
    else:
        user_data = {
            'username': params['login'],
            'password': params['password']
        }
        if user := user_repository.get_user_by_username(User(**user_data).username):
            if params['password'] != user.password:
                return {'error': 'No user with this password'}
            else:
                token = create_access_token(identity=[user.username, user.email, user.password])
                return {'access_token': token, 'username': user.username}
        else:
            return {'error': 'No user with this username in database'}


@app.route('/get_profile/<username>', methods=['GET'])
def get_profile(username):
    profile = user_repository.get_user_by_username(username)
    profile_file = profile_file_repository.get_profile_files(profile.user_id)

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
        'social_networks': profile.social_networks,
        'cover': profile_file.cover_path,
        'profile_picture': profile_file.photo_path
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
        profile_file = ProfileFile(user_id=profile.user_id)

        user_repository.update(new_user, profile.user_id)
        user[0] = params["username"]
        profile_file_repository.update(user_id=user_repository.get_user_by_username(user[0]).user_id,
                                       new_profile_file=profile_file)

        token = create_access_token(identity=[new_user.username, new_user.email, new_user.password])

        return {'access_token': token, 'username': user[0]}
    else:
        return {'error': 'No user with this token'}


@app.route('/download', methods=['POST'])
def download():
    path = request.json['path']
    file = None
    with app.open_resource(app.root_path + path, mode="rb") as f:
        file = f.read()

    if not file:
        return {'error': 'file not found'}

    res = make_response(file)
    res.headers['Content-Type'] = 'image'
    return res


@app.route('/upload_profile_files', methods=['POST'])
@jwt_required()
def upload_profile_files():
    user = get_jwt_identity()
    if user is not None:
        cover = request.files['cover']
        profile_picture = request.files['profile_picture']

        type_of_cover = cover.filename.split('.')[1]
        type_of_profile_picture = profile_picture.filename.split(".")[1]

        cover_file_name = f'files/cover/{user[0]}_cover.{type_of_cover}'
        profile_picture_name = f'files/profile_picture/{user[0]}_profile_picture.{type_of_profile_picture}'

        profile_picture.save(profile_picture_name)
        cover.save(cover_file_name)

        profile_file = ProfileFile(user_id=user_repository.get_user_by_username(user[0]).user_id,
                                   photo_path=profile_picture_name,
                                   cover_path=cover_file_name)

        profile_file_repository.update(profile_file.user_id, profile_file)

        return {'status': 'success'}
    else:
        return {'error': 'No user with this token'}


if __name__ == '__main__':
    db_session.global_init()
    app.run(debug=True)