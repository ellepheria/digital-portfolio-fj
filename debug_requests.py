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
    user = User(username="den1234", name='den1234', email="den11233@gmail.com", surname="", password="123")

    #user_repository.add(user)
    # print(user_repository.get_user_by_username('fearppen'))
    # project = Project(title="DigitalPortfolio", user_id=1, rating=1, description="1234", cover_path='repository/project')
    # project_repository.add(project)
    # comment = Comment(project_id=1, text='good', user_id=1, username='fearppen')
    # comment_repository.add(comment)
    # liked = LikedProject(user_id=1, liked_project_id=1)
    # liked_project_repository.add(liked)
    # profile_file = ProfileFile(profile_id=1, photo_path="repository/profile_repository.py", cover_path='1234567')
    # profile_file_repository.add(profile_file)
    # project_file = ProjectFile(project_id=1, file_path='.1py4')
    # project_file_repository.add(project_file)

    for i in user_repository.get_all():
        print(i)

