
from book import Book
from book_manager import BookManager


class BookInterface:

    def __init__(self):
        self.manager = BookManager()

    # მენიუს ჩვენება
    def show_menu(self):
        print("\n========== BOOK MANAGER ==========")
        print("1. ახალი წიგნის დამატება")
        print("2. ყველა წიგნის ნახვა")
        print("3. წიგნის ძებნა")
        print("4. წიგნის წაშლა სათაურით")
        print("5. გამოსვლა")
        print("==================================")

    # წიგნის დამატება
    def add_book(self):
        title = input("შეიყვანეთ წიგნის სათაური: ")
        author = input("შეიყვანეთ ავტორი: ")
        year_input = input("შეიყვანეთ გამოცემის წელი: ")

        try:
            year = int(year_input)

            book = Book(title, author, year)
            self.manager.add_book(book)

            print("\nწიგნი წარმატებით დაემატა!")

        except ValueError as error:
            print(f"\nშეცდომა: {error}")

        except TypeError as error:
            print(f"\nშეცდომა: {error}")

    # ყველა წიგნის ნახვა
    def show_books(self):
        self.manager.show_books()

    # წიგნის ძებნა
    def search_book(self):
        title = input("შეიყვანეთ საძიებო წიგნის სათაური: ")

        try:
            results = self.manager.search_book(title)

            if not results:
                print(f"\nწიგნი '{title}' ვერ მოიძებნა.")
                return

            print("\nმოძიებული წიგნები:")

            for book in results:
                print("--------------------")
                book.display_info()

        except ValueError as error:
            print(f"\nშეცდომა: {error}")

        except TypeError as error:
            print(f"\nშეცდომა: {error}")

    # წიგნის წაშლა სათაურით
    def delete_book(self):
        title = input("შეიყვანეთ წასაშლელი წიგნის სათაური: ")

        try:
            deleted = self.manager.delete_book(title)

            if deleted is None:
                print(f"\nწიგნი '{title}' ვერ მოიძებნა.")
                return

            print("\nწიგნი წარმატებით წაიშალა!")
            print(f"წაშლილი წიგნი: {deleted.title}")

        except ValueError as error:
            print(f"\nშეცდომა: {error}")

        except TypeError as error:
            print(f"\nშეცდომა: {error}")

    # პროგრამის მთავარი ციკლი
    def run(self):

        while True:
            self.show_menu()

            choice = input("აირჩიეთ მოქმედება: ").strip()

            if choice == "1":
                self.add_book()

            elif choice == "2":
                self.show_books()

            elif choice == "3":
                self.search_book()

            elif choice == "4":
                self.delete_book()

            elif choice == "5":
                print("\nპროგრამა დასრულდა.")
                break

            else:
                print("\nარასწორი არჩევანი. სცადეთ თავიდან.")
