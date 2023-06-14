from server.domain import db_session
from server.repository.__all_repository import *
from server.domain.__all_models import *

if __name__ == '__main__':
    db_session.global_init()
    user_repository = UserRepository()
    project_repository = ProjectRepository()
    comment_repository = CommentRepository()
    liked_project_repository = LikedProjectRepository()
    profile_file_repository = ProfileFileRepository()
    project_file_repository = ProjectFileRepository()
    user = User(username="0", name='0', email="0@gmail.com", surname="", password="0",
                technologies="aaa")
    #user1 = User(username="12", name='12', email="12@gmail.com", surname="", password="123",
    #            type_of_activity="a")

    #user_repository.add(user)
    #user_repository.add(user1)
    # print(user_repository.get_user_by_username('fearppen'))
    # project1 = Project(title="DigitalPortfolio", user_id=2, rating=1, description="1234", cover_path='repository/project1')
    # project_repository.add(project1)

    #project2 = Project(title="Lego", user_id=2, rating=2, description="1234", cover_path='repository/project2')
    #project_repository.add(project2)
    # comment = Comment(project_id=1, text='good', user_id=1, username='fearppen')
    # comment_repository.add(comment)
    # liked = LikedProject(user_id=1, liked_project_id=1)
    # liked_project_repository.add(liked)
    # profile_file = ProfileFile(profile_id=1, photo_path="repository/profile_repository.py", cover_path='1234567')
    # profile_file_repository.add(profile_file)
    # project_file = ProjectFile(project_id=1, file_path='.1py4')
    # project_file_repository.add(project_file)

    #print(project2.serialize)
    for i in user_repository.get_users_with_names('ауууу'):
        print(i)
