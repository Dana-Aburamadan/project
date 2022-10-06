from users.Client import Client
from users.Librarian import Librarian
from utils.Utils import Constants
from books.Book import Book

class App_Auth:
    Clients_list: list[Client] = [
     Client(1, "Aya", 23, 1234567, 597876434, "Aya", 123),
     Client(2, "Hala", 22, 5678943, 599876543, "Hala",345),
     Client(3, "Asil", 18, 7654321, 599845334, "Asil",678)]

    Librarian_list: list[Librarian] = [
     Librarian(4, "Ali", 33, 1234567, Constants.Full_Time,"Ali", 111),
     Librarian(5, "Abdallah", 32, 5678943, Constants.Full_Time, "Abdallah", 112),
     Librarian(6, "Adham", 28, 7654321, Constants.Part_Time, "Adham",113)]


    def get_last_id_client(self):
         return self.Clients_list[len(self.Clients_list) - 1].get_id()

    def get_last_id_librarian(self):
         return self.Librarian_list[len(self.Librarian_list) - 1].get_id()

    def login_librarian(self, username: str, password: str) -> bool:
        for item in self.Librarian_list:
            if username == item.get_username() and password == item.get_password():
                return True
        return False

    def login_client(self, username: str, password: str) -> bool:
        for item in self.Clients_list:
            if username == item.get_username() and password == item.get_password():
                return True
        return False

    def register_new_Librarian(self, user: Librarian):
        if not self.check_if_librarian_exist(user.get_username()):
            self.Librarian_list.append(user)
        else:
            print("User already Used!")

    def register_new_Client(self, user: Client):
        if not self.check_if_client_exist(user.get_username()):
            self.Clients_list.append(user)
        else:
            print("User already Used!")

        print(len(self.Clients_list))

    def check_if_librarian_exist(self, username: str):
        for item in self.Librarian_list:
            if item.get_username() == username:
                return True
        return False

    def check_if_client_exist(self, username: str):
        for item in self.Clients_list:
            if item.get_username() == username:
                return True
        return False

    def get_Clients_list(self):
        return self.Clients_list

    def get_Librarian_list(self):
        return self.Librarian_list

class Search_controller:

    def search_for_client_by_id(self, id: int, Clients_list: list[Client]):
        if Clients_list == None or len(Clients_list) == 0:
            return None
        else:
            for item in Clients_list:
                if item.get_id() == id:
                    return item

    def search_for_librarian_by_id(self, id: int, Librarian_list: list[Librarian]):
        if Librarian_list == None or len(Librarian_list) == 0:
            return None
        else:
            for item in Librarian_list:
                if item.get_id() == id:
                    return item