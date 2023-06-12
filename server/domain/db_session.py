from sqlalchemy import create_engine
import sqlalchemy.orm as orm
from server.domain.declarative_base import Base
from sqlalchemy.orm import Session

__factory = None

DATABASE = {
    "user": "postgres",
    "password": "posgres",
    "database_name": "db",
    "url": "localhost",
}


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


def global_init():
    global __factory
    if not check_dict_to_correctness(DATABASE):
        raise Exception("Неправильное подключение к базе данных")

    engine = create_engine(f"postgresql+psycopg2://"
                           f"{DATABASE['user']}:"
                           f"{DATABASE['password']}@"
                           f"{DATABASE['url']}/"
                           f"{DATABASE['database_name']}",
                           echo=True)

    Base.metadata.create_all(engine)
    __factory = orm.sessionmaker(bind=engine)


def create_session() -> Session:
    global __factory
    return __factory()


if __name__ == "__main__":
    global_init()
