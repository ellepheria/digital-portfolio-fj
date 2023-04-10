from domain import db_session
from domain.user import User
from repository.user_repository import UserRepository

if __name__ == '__main__':
    user_repository = UserRepository()
    db_session.global_init()
    user = User(username="fearppen", email="antoncahchylin@gmail.com", surname="", password="123")
    user_repository.add(user)
    for user in user_repository.get_all():
        print(user)
