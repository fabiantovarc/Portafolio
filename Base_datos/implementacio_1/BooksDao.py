from Conexion import Conexion
from Book import Book
from logger_base import log
from CursorDelPool import CursorDelPool

class BooksDao:
    '''
    DAO (Data Access Object)
    CRUD (Create-Read-Update-Delete)
    Cuando hablamos de book (en minuscula), hablamos directamente de la tabla.
    '''
    _SELECCIONAR = 'SELECT * FROM book ORDER BY id_books'
    _INSERTAR = 'INSERT INTO book(name, price, genre, user_rating, year, author) VALUES(%s, %s, %s, %s, %s, %s)'
    _ACTUALIZAR = 'UPDATE book SET name=%s, price=%s, genre=%s, user_rating=%s, year=%s, author=%s WHERE id_books=%s'
    _ELIMINAR = 'DELETE FROM book WHERE id_books=%s'

    @classmethod
    def seleccionar(cls):
        with CursorDelPool() as cursor:
            cursor.execute(cls._SELECCIONAR)
            registros = cursor.fetchall()
            books = []
            for registro in registros:
                book = Book(registro[0], registro[1], registro[2], registro[3], registro[4], registro[5], registro[6])
                books.append(book)
            return books

    @classmethod
    def insertar(cls, book):
        with CursorDelPool() as cursor:
            log.debug(f'Insert book: {book}')
            valores = (book.name, book.price, book.genre, book.user_rating, book.year, book.author)
            cursor.execute(cls._INSERTAR, valores)
            log.debug(f'Insert book: {book}')
            return cursor.rowcount

    @classmethod
    def actualizar(cls, book):
        with CursorDelPool() as cursor:
            valores = (book.name, book.price, book.genre, book.user_rating, book.year, book.id_books)
            cursor.execute(cls._ACTUALIZAR, valores)
            log.debug(f'Update book: {Book}')
            return cursor.rowcount
    
    @classmethod
    def eliminar(cls, Book):
        with CursorDelPool() as cursor:
            valores = (Book.id_books,)
            cursor.execute(cls._ELIMINAR, valores)
            log.debug(f'Deleted object: {Book}')
            return cursor.rowcount
    
if __name__ == '__main__':
    #Ingresar un registro
    Book1 = Book(name = 'The Lord of the Rings', price = 19.99 , genre = 'Fantasy', user_rating = 4.5, year = '1954', author = 'J.R.R. Tolkien')
    Insert_Books = BooksDao.insertar(Book1)
    log.debug(f'inserted book: {Insert_Books}')
