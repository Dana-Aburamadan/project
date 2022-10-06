from utils.Utils import Constants
class Book:
    def __init__(self, id, title, description, author, status=0):
        self.__id = id
        self.__title = title
        self.__description = description
        self.__author = author
        self.__status = status

    def get_id(self):
        return self.__id

    def get_title(self):
        return self.__title

    def get_description(self):
        return self.__description

    def get_author(self):
        return self.__author

    def get_status(self):
        return self.__status




