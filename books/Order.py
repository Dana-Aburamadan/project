class order:
    def __init__(self, id, date, client_id, book_id):
        self.__id = id
        self.__date = date
        self.__client_id = client_id
        self.__book_id = book_id

    def get_id(self):
        return self.__id

    def get_date(self):
        return self.__date

    def get_client_id(self):
        return self.__client_id

    def get_book_id(self):
        return self.__book_id