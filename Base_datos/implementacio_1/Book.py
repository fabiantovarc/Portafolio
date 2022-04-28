from logger_base import log

class Book:
    def __init__(self, id_books=None, name= None, price = None, genre = None, user_rating = None, year = None, author = None):
        self._id_books      = id_books
        self._name          = name
        self._price         = price
        self._genre         = genre
        self._user_rating   = user_rating
        self._year          = year
        self._author        = author

    def __str__(self):
        return f'''
        ID Book: {self._id_books}
        Name: {self._name}, Price: {self._price}, 
        Author: {self._author}, Genre: {self._genre}, 
        User raiting: {self._user_rating}, Year: {self._year}
        '''

    @property
    def id_books(self):
        return self._id_books

    @id_books.setter
    def id_books(self, id_books):
        self._id_books = id_books
    
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name
    
    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, price):
        self._price = price

    @property
    def genre(self):
        return self._genre
    
    @genre.setter
    def genre(self, genre):
        self._genre = genre

    @property
    def user_rating(self):
        return self._user_rating

    @user_rating.setter
    def user_rating(self, user_rating):
        self._user_rating = user_rating
    
    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, year):
        self._year = year
    
    @property
    def author(self):
        return self._author
    
    @author.setter
    def author(self, author):
        self._author = author


    
if __name__ == '__main__':
    book1 = Book(name = 'The Lord of the Rings', price = 19.99, genre = 'Fantasy', user_rating = 4.5, year = '1954', author = 'J.R.R. Tolkien')
    log.debug(book1)