
class Librarian:

    def __init__(self, id, full_name, age, id_no, user_name="", password=""):
        self.__id = id
        self.__full_name = full_name
        self.__age = age
        self.__id_no = id_no
        self.__user_name = user_name
        self.__password = password


    def get_id(self):
        return self.__id

    def get_full_name(self):
        return self.__full_name

    def get_age(self):
        return self.__age

    def get_id_no(self):
        return self.__id_no

    def get_username(self):
        return self.__user_name

    def get_password(self):
        return self.__password