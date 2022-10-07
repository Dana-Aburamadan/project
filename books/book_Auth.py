from books.Book import Book
from utils.Utils import Constants

class Book_Auth:
 list_of_all_books = [
    Book(1, "The 7 Habits Of Highly Effective People", "motivational", "Stephen Covey", Constants.Active),
    Book(2, "How To Win Friends And Influence People", "Best seller", "Dale Carnegie", Constants.Inactive),
    Book(3, "Think And Grow Rich Written", "Most Effective", "Napoleon Hill", Constants.Active),
    Book(4, "The Greatest Salesman In The World", "Educational", "Og Mandino", Constants.Inactive)]

 def append_to_books_list(self):
     self.list_of_all_books.append()

