import os
import re
from datetime import timedelta

from flask import Flask, request, jsonify
from flask_jwt_extended import create_access_token, JWTManager, jwt_required, get_jwt_identity
from server.domain import db_session
from server.domain.__all_models import *
from server.repository.__all_repository import *
from flask_cors import CORS

app = Flask(__name__, static_folder='files')
CORS(app)
jwt = JWTManager(app)
app.config["JWT_SECRET_KEY"] = "digital-portfolio-fj"
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(days=30)
app.config["JWT_REFRESH_TOKEN_EXPIRES"] = timedelta(days=30)
UPLOAD_FOLDER = 'server/files'
user_repository = UserRepository()
profile_file_repository = ProfileFileRepository()
project_repository = ProjectRepository()
project_file_repository = ProjectFileRepository()


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
        'email': profile.email,
        'name': profile.name,
        'surname': profile.surname,
        'about': profile.about,
        'technologies': profile.technologies,
        'type_of_activity': profile.type_of_activity,
        'age': profile.age,
        'phone_number': profile.phone_number,
        'education': profile.education,
        'social_networks': profile.social_networks,
        'cover_path': profile_file.cover_path,
        'profile_picture_path': profile_file.photo_path
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

        user_repository.update(new_user, profile.user_id)
        user[0] = params["username"]

        token = create_access_token(identity=[new_user.username, new_user.email, new_user.password])

        return {'access_token': token, 'username': user[0]}
    else:
        return {'error': 'No user with this token'}


@app.route('/upload_profile_cover', methods=['POST'])
@jwt_required()
def upload_profile_cover():
    user_data = get_jwt_identity()
    if user_data:
        user_id = user_repository.get_user_by_username(user_data[0]).user_id
        current_profile_files = profile_file_repository.get_profile_files(user_id)
        cover = request.files['cover']
        type_of_cover = cover.filename.split('.')[1]
        cover_file_name = f'files/cover/{user_data[0]}_cover.{type_of_cover}'
        cover.save(cover_file_name)

        profile_file = ProfileFile(user_id=user_id,
                                   photo_path=current_profile_files.photo_path,
                                   cover_path=cover_file_name)

        profile_file_repository.update(profile_file.user_id, profile_file)

        return {'cover_path': cover_file_name}
    else:
        return {'error': 'No user with this token'}


@app.route('/upload_profile_picture', methods=['POST'])
@jwt_required()
def upload_profile_picture():
    user_data = get_jwt_identity()
    if user_data:
        user_id = user_repository.get_user_by_username(user_data[0]).user_id
        current_profile_files = profile_file_repository.get_profile_files(user_id)
        profile_picture = request.files['profile_picture']
        type_of_profile_picture = profile_picture.filename.split('.')[1]
        profile_picture_name = f'files/profile_picture/{user_data[0]}_profile_picture.{type_of_profile_picture}'
        profile_picture.save(profile_picture_name)

        profile_file = ProfileFile(user_id=user_id,
                                   photo_path=profile_picture_name,
                                   cover_path=current_profile_files.cover_path)

        profile_file_repository.update(profile_file.user_id, profile_file)

        return {'profile_picture_path': profile_picture_name}
    else:
        return {'error': 'No user with this token'}


@app.route('/create_project', methods=['POST'])
@jwt_required()
def create_project():
    user_data = get_jwt_identity()
    if user_data:
        params = request.json

        project = Project(**params)
        user_id = user_repository.get_user_by_username(user_data[0]).user_id
        project.user_id = user_id
        projects = project_repository.get_all_user_projects_by_id(user_id)

        for elem in projects:
            if elem.title == params['title']:
                return {'Error': 'Project with this title already exists'}
        project_repository.add(project)

        return {'status': 'success'}
    else:
        return {'error': 'No user with this token'}


@app.route('/projects/<project_id>/edit', methods=['POST'])
@jwt_required()
def project_edit(project_id):
    user_data = get_jwt_identity()
    params = request.json
    project = project_repository.get_project(project_id)
    projects = project_repository.get_all_user_projects_by_id(project.user_id)
    user = user_repository.get_user(project.user_id)

    if user_data and params['owner'] == user.username:
        for p in projects:
            if p.title == params['title'] and p.id != int(project_id):
                return {'Error': 'Project with this title already exists'}

        project.title = params['title']
        project.short_description = params['short_description']
        project.description = params['description']
        project.added_links = params['added_links']

        project_repository.update(new_project=project,
                                  project_id=project.id)

        return {'project_id': project.id}
    else:
        return {'error': 'No user with this token or user not owner'}


@app.route('/projects/<project_id>', methods=['GET'])
def get_project(project_id):
    project = project_repository.get_project(project_id)
    if not project:
        return {'error': 'project not found'}

    user = user_repository.get_user(project.user_id)
    project_file = project_file_repository.get_all_project_files(project_id)

    images = {}
    for i in range(len(project_file)):
        images[i] = project_file[i].file_path

    return {
        'title': project.title,
        'short_description': project.short_description,
        'description': project.description,
        'added_links': project.added_links,
        'cover_path': project.cover_path,
        'images': images,
        'owner': user.username
    }


@app.route('/projects/<project_id>/card', methods=['GET'])
def get_card(project_id):
    project = project_repository.get_project(project_id)
    user = user_repository.get_user(project.user_id)
    return {
        'title': project.title,
        'short_description': project.short_description,
        'cover': project.cover_path,
        'owner': user.username
    }


@app.route('/get_user_projects/<username>')
def get_cards(username):
    card_count = int(request.args.get('count'))
    page = int(request.args.get('page'))
    user = user_repository.get_user_by_username(username)
    projects = project_repository.get_all_user_projects_by_id(user.user_id)

    if len(projects) <= card_count and page == 0:
        # return jsonify(projects.query.paginate(page=page+1, per_page=card_count).items)
        return jsonify(json_list=[project.serialize for project in projects])

    if len(projects) > card_count:
        return jsonify(json_list=[project.serialize for project in projects[page * card_count:(page + 1) * card_count]])
    return {'error': 'нет проектов'}


@app.route('/<project_id>/upload_cover', methods=['POST'])
@jwt_required()
def upload_cover(project_id):
    user_data = get_jwt_identity()
    if user_data:
        cover = request.files['cover']

        project = project_repository.get_project(project_id)
        if project.cover_path:
            os.remove(project.cover_path)

        type_of_cover = cover.filename.split('.')[1]

        path = f'files/projects/{project_id}_project/cover'
        try:
            os.makedirs(path)
        except OSError as e:
            print(e)

        project_cover_file_name = f'files/projects/{project_id}_project/cover/{hash(cover)}_cover.{type_of_cover}'
        cover.save(project_cover_file_name)

        updated_project = project_repository.get_project(project_id)
        updated_project.cover_path = project_cover_file_name

        project_repository.update(new_project=updated_project,
                                  project_id=project_id)

        return {'cover_path': project_cover_file_name}
    else:
        return {'error': 'No user with this token'}


@app.route('/<project_id>/upload_photos', methods=['POST'])
@jwt_required()
def upload_photos(project_id):
    user_data = get_jwt_identity()
    if user_data:
        project_files = project_file_repository.get_all_project_files(project_id)
        files = request.files
        if project_files:
            for file in project_files:
                os.remove(file.file_path)
                project_file_repository.delete(file.id)

        path = f'files/projects/{project_id}_project/photos/'
        try:
            os.makedirs(path)
        except OSError as e:
            print(e)

        images = {}
        for i in range(len(files)):
            photo = files[f'{i}']
            type_of_photo = photo.filename.split('.')[1]
            photo_file_name = f'files/projects/{project_id}_project/photos/{i}_{hash(photo)}.{type_of_photo}'
            images[f'{i}'] = photo_file_name
            # Add file to folder
            photo.save(photo_file_name)

            updated_project_files = ProjectFile(project_id=project_id, file_path=photo_file_name)

            project_file_repository.add(updated_project_files)
        #     добавить в ответ массив картинок
        return images
    else:
        return {'error': 'No user with this token'}


@app.route('/search_users')
def search_users():
    profile_card_count = int(request.args.get('count'))
    page = int(request.args.get('page'))
    search_query = request.args.get('search_query')
    users = []
    user_by_username = user_repository.get_user_by_username(search_query)
    if user_by_username is not None:
        users.append(user_by_username)
    user_by_names = user_repository.get_users_with_names(search_query)
    if len(user_by_names) > 0:
        users += user_by_names
    users_by_technologies = user_repository.get_users_with_technologies(search_query)
    if len(users_by_technologies) > 0:
        users += users_by_technologies
    users_by_activities = user_repository.get_users_with_type_of_activities(search_query)
    if len(users_by_activities) > 0:
        users += users_by_activities
    users_by_description = user_repository.get_users_with_description(search_query)
    if len(users_by_description) > 0:
        users += users_by_description

    result = []
    usernames = []

    for user in users:
        if user is not None:
            if user.username not in usernames:
                result.append(user)
                usernames.append(user.username)

    return get_profile_cards_by_pages(result, profile_card_count, page)


@app.route('/get_profile_cards', methods=['GET'])
def get_profile_cards():
    profile_card_count = int(request.args.get('count'))
    page = int(request.args.get('page'))
    users = user_repository.get_all()

    return get_profile_cards_by_pages(users, profile_card_count, page)


def get_profile_cards_by_pages(users, profile_card_count, page):
    if len(users) <= profile_card_count and page == 0:
        json = []
        for user in users[0 : len(users)]:
            profile_file = profile_file_repository.get_profile_files(user.user_id)
            json.append({
                'name': user.name,
                'type_of_activity': user.type_of_activity,
                'about': user.about,
                'images': {
                    'profile_picture_path': profile_file.photo_path,
                    'cover_path': profile_file.cover_path,
                },
                'username': user.username
            })

        return json

    if len(users) > profile_card_count:
        json = []
        for user in users[(page * profile_card_count) : ((page + 1) * profile_card_count)]:
            profile_file = profile_file_repository.get_profile_files(user.user_id)
            json.append({
                'name': user.name,
                'type_of_activity': user.type_of_activity,
                'about': user.about,
                'images': {
                    'profile_picture_path': profile_file.photo_path,
                    'cover_path': profile_file.cover_path,
                },
                'username': user.username
            })

        return json
    return {'error': 'нет профилей'}


if __name__ == '__main__':
    db_session.global_init()
    app.run(debug=True)