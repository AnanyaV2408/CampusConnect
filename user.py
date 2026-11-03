
from abc import ABC, abstractmethod


class User(ABC):

    def __init__(self, user_id, name, email, password):
        self.__user_id = user_id
        self.__name = name
        self.__email = email
        self.__password = password

    # Getter methods
    @property
    def user_id(self):
        return self.__user_id

    @property
    def name(self):
        return self.__name

    @property
    def email(self):
        return self.__email

    def check_password(self, password):
        return self.__password == password

    @abstractmethod
    def display_dashboard(self):
        pass
