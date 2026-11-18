from book import Book
import json
import os


class BookManager:

    def __init__(self, filename="books.json"):
        
        current_dir = os.path.dirname(os.path.abspath(__file__))
        
        self.filename = os.path.join(current_dir, filename)
        
        self.__books = []
        self._load_from_file()

    # ფაილიდან წიგნების ჩატვირთვა
    def _load_from_file(self):
        if not os.path.exists(self.filename):
            return
        
        try:
            with open(self.filename, "r", encoding="utf-8") as file:
                data = json.load(file)
                for item in data:
                    book = Book(item["title"], item["author"], item["year"])
                    self.__books.append(book)
        except (json.JSONDecodeError, KeyError):
            print("ფაილის წაკითხვისას მოხდა შეცდომა ან ფაილი დაზიანებულია.")

    # ფაილში წიგნების შენახვა
    def _save_to_file(self):
        data = [
            {
                "title": book.title,
                "author": book.author,
                "year": book.year
            }
            for book in self.__books
        ]
        with open(self.filename, "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

    # წიგნის დამატება
    def add_book(self, book):
        if not isinstance(book, Book):
            raise TypeError("უნდა დაემატოს Book კლასის ობიექტი.")

        self.__books.append(book)
        self._save_to_file()  # ავტომატური შენახვა ფაილში

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
                self._save_to_file() 
                return book

        return None