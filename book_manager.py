
from book import Book


class BookManager:

    def __init__(self):
        self.__books = []

    # წიგნის დამატება
    def add_book(self, book):
        if not isinstance(book, Book):
            raise TypeError("უნდა დაემატოს Book კლასის ობიექტი.")

        self.__books.append(book)

    # ყველა წიგნის მიღება
    def get_all_books(self):
        return self.__books.copy()

    # ყველა წიგნის ჩვენება
    def show_books(self):
        if not self.__books:
            print("წიგნების სია ცარიელია.")
            return

        for index, book in enumerate(self.__books, start=1):
            print(f"\nწიგნი №{index}")
            book.display_info()
            print("--------------------")

    # წიგნის ძებნა სათაურით
    def search_book(self, title):
        if not isinstance(title, str):
            raise TypeError("სათაური ტექსტური უნდა იყოს.")

        if not title.strip():
            raise ValueError("საძიებო სათაური ცარიელია.")

        return [
            book for book in self.__books
            if book.title.casefold() == title.strip().casefold()
        ]

    # წიგნის წაშლა სათაურით
    def delete_book(self, title):
        if not isinstance(title, str):
            raise TypeError("სათაური ტექსტური უნდა იყოს.")

        if not title.strip():
            raise ValueError("წასაშლელი სათაური ცარიელი არ უნდა იყოს.")

        for book in self.__books:
            if book.title.casefold() == title.strip().casefold():
                self.__books.remove(book)
                return book

        return None
