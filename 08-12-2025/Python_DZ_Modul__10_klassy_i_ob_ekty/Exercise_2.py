class Book:
    def __init__(self):
        self.title = ""
        self.year = 0
        self.publisher = ""
        self.genre = ""
        self.author = ""
        self.price = 0.0

    def enter_book (self, title: str, year: int, publisher: str, genre: str, author: str, price: float):
        self.title = title
        self.year = year
        self.publisher = publisher
        self.genre = genre
        self.author = author
        self.price = price

    def enter_title(self, title: str):
        self.title = title

    def enter_year(self, year: int):
        self.year = year

    def enter_publisher(self, publisher: str):
        self.publisher = publisher

    def set_genre(self, genre: str):
        self.genre = genre

    def enter_author(self, author: str):
        self.author = author

    def enter_price(self, price: float):
        self.price = price

    def get_book_info(self):
        print(f"Title: {self.title}")
        print(f"Year of publication: {self.year}")
        print(f"Publisher: {self.publisher}")
        print(f"Genre: {self.genre} ")
        print(f"Author: {self.author}")
        print(f"Price, $: {self.price}")

    def get_title(self):
        return self.title

    def get_year(self):
        return self.year

    def get_publisher(self):
        return self.publisher

    def get_genre(self):
        return self.genre

    def get_author(self):
        return self.author

    def get_price(self):
        return self.price
