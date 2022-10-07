from app_auth.App_Auth import App_Auth, Search_controller
from users.Client import Client
from utils.Utils import Methods_Utils
from books.Book import Book
from books.book_Auth import Book_Auth

def get_input_from_user(app_auth: App_Auth):
    full_name = input("Enter client name: ")
    age = input("Enter client age: ")
    id_no = input("Enter client id_no: ")
    phone_number = input("Enter client phone_number: ")

    if Methods_Utils.check_value_is_empty(full_name, age, id_no, phone_number):
        print("Invaild inputs")
        return

    clt = Client(full_name=full_name, age=age, id_no=id_no, phone_number=phone_number,
                  id=app_auth.get_last_id_client() + 1)

    app_auth.register_new_Client(clt)


print("Welcome,please add your crediual: ")

user_name = input("Username: ")
password = input("Password: ")

if Methods_Utils.check_value_is_empty(user_name, password):
    print("Empty fields")
    exit()

auth = App_Auth()
search_cont = Search_controller()

if auth.login_librarian(user_name, password):
    print("What you want to do: \n1_Add new student.\n2_ Search for user by id")

print("What you want to do: \n1_Add new student.\n2_ Search for user by id")

emp_choice = input("User choice: ")
if not Methods_Utils.check_value_is_empty(emp_choice):
 if emp_choice == "1":
        get_input_from_user(auth)
 elif emp_choice == "2":
     id_input = input("Enter user id: ")
     if not Methods_Utils.check_value_is_empty(id_input) and id_input.isdigit():
            search_client = search_cont.search_for_client_by_id(int(id_input), auth.get_Clients_list())

            if search_client != None:
              print("Client Name: ", search_client.get_full_name()
                        , "\nClient age: ", search_client.get_age())

     if not Methods_Utils.check_value_is_empty(id_input) and id_input.isdigit():
            search_librarian = search_cont.search_for_librarian_by_id(int(id_input), auth.get_Librarian_list())

            if search_librarian != None:
              print("Librarian Name: ", search_librarian.get_full_name()
                        , "\nLibrarian age: ", search_librarian.get_age())


welcome_msg = '''\n Welcome to the Book’s Library 
        Please choose an option:
        1. Display all the books
        2. Borrow book
        3. Return book
        4. Exit 
        '''
def book_list():
 for item in Book_Auth.list_of_all_books :
    print(item.get_id())
    print(item.get_title())

# def borrowing_book():
#     for item in App_Auth.list_of_all_books:
#         if item is Constants.Active:
#             print(Book.get_title)

print(welcome_msg)
a = int(input("Enter a choice: "))

if a == 1:
 print("Books present in this library are: \n 1.The 7 Habits Of Highly Effective People \n 2.How To Win Friends And Influence People \n 3.How To Win Friends And Influence People\n 4.The Greatest Salesman In The World " )
 print(welcome_msg)
 a = int(input("Enter a choice: "))

if a == 1:
 print("Books present in this library are: \n 1.The 7 Habits Of Highly Effective People \n 2.How To Win Friends And Influence People \n 3.How To Win Friends And Influence People\n 4.The Greatest Salesman In The World " )

elif a == 2:
 print('These are the books we have')
 print(book_list())
 b = int(input("Write the id of the book you want to borrow: "))
 print("Done!,The book is borrowed now, Return it in 30 days.")

elif a == 3:
    print(book_list())
    int(input("Which book id do you want to return: "))
    print("Done!, Thanks for borrowing")

else:
    print("Exit")













