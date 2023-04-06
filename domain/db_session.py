from sqlalchemy import create_engine
import sqlalchemy.orm as orm
from __all_models import *
from declarative_base import Base

__factory = None

DATABASE = {
    "user": "postgres",
    "password": "",
    "database_name": "db",
    "url": "localhost",
}


def global_init(database: dict):
    global __factory

    if __factory:
        return

    if not check_dict_to_correctness(dictionary):
        raise Exception("Неправильное подключение к базе данных")

    engine = create_engine(f"postgresql+psycopg2://"
                           f"{dictionary['user']}:"
                           f"{dictionary['password']}@"
                           f"{dictionary['url']}/"
                           f"{dictionary['database_name']}", echo=True)
    engine.connect()

    Base.metadata.create_all(engine)
    __factory = orm.sessionmaker(bind=engine)


def create_session() -> orm.sessionmaker:
    global __factory
    return __factory


def check_dict_to_correctness(dictionary: dict):
    correct_keys = ["user", "password", "database_name", "url"]
    keys = set(dictionary.keys())
    if len(keys) == 4:
        for key in keys:
            if key in correct_keys:
                continue
            return False
        return True
    return False


if __name__ == "__main__":
    dictionary = DATABASE = {
        "user": "postgres",
        "password": "",
        "database_name": "db",
        "url": "localhost",
    }
    global_init(dictionary)
