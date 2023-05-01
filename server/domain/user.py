from sqlalchemy.orm import relationship

from server.domain.declarative_base import Base
from sqlalchemy import Column, Integer, Text


class User(Base):
    __tablename__ = "users"

    user_id = Column(
        Integer,
        primary_key=True,
        autoincrement=True,
    )

    username = Column(
        Text,
        unique=True,
        nullable=False,
    )

    name = Column(
        Text,
        nullable=True,
    )

    surname = Column(
        Text,
        nullable=True,
    )

    about = Column(
        Text,
        nullable=True,
    )

    technologies = Column(
        Text,
        nullable=True,
    )

    type_of_activity = Column(
        Text,
        nullable=True
    )

    age = Column(
        Integer,
        nullable=True,
    )

    phone_number = Column(
        Text,
        unique=True,
        nullable=True,
    )

    education = Column(
        Text,
        nullable=True,
    )

    social_networks = Column(
        Text,
        nullable=True,
    )

    email = Column(
        Text,
        unique=True,
        nullable=False
    )

    password = Column(
        Text,
        nullable=True,
    )

    def __str__(self):
        return f'user_id: {self.user_id}, username: {self.username}, email: {self.email}' \
               f' name: {self.name}, surname: {self.surname},' \
               f'about: {self.about}, technologies: {self.technologies}, type_of_activity: {self.type_of_activity} ' \
               f'age: {self.age}, phone_number: {self.phone_number}, education: {self.education},' \
               f' social_networks: {self.social_networks}, password: {self.password}'
