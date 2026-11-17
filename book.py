
class Book:
    def __init__(self, title, author, year):

        if not isinstance(title, str):
            raise TypeError("სათაური ტექსტური უნდა იყოს.")

        if not title.strip():
            raise ValueError("სათაური ცარიელი არ უნდა იყოს.")

        if not isinstance(author, str):
            raise TypeError("ავტორი ტექსტური უნდა იყოს.")

        if not author.strip():
            raise ValueError("ავტორი ცარიელი არ უნდა იყოს.")

        if isinstance(year, bool) or not isinstance(year, int):
            raise TypeError("გამოცემის წელი მთელი რიცხვი უნდა იყოს.")

        if not 1 <= year <= 2026:
            raise ValueError("გამოცემის წელი უნდა იყოს 1-დან 2026-მდე.")

        self.__title = title.strip()
        self.__author = author.strip()
        self.__year = year

    @property
    def title(self):
        return self.__title

    @property
    def author(self):
        return self.__author

    @property
    def year(self):
        return self.__year

    def display_info(self):
        print(f"სათაური: {self.title}")
        print(f"ავტორი: {self.author}")
        print(f"გამოცემის წელი: {self.year}")

