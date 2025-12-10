class Book:
    def __init__(self):
        self.title = ""
        self.year = 0
        self.publisher = ""
        self.genre = ""
        self.author = ""
        self.price = 0.0

    def enter_book (self):
        self.title = input("Enter the title of the book: ")
        self.year = int(input("Enter the year of publication: "))
        self.publisher = input("Enter the publisher of the book: ")
        self.genre = input("Enter the genre of the book: ")
        self.author = input("Enter the author of the book: ")
        self.price = float(input("Enter the price of the book: "))

    def enter_title(self, title):
        self.title = title

    def enter_year(self, year):
        self.year = year

    def enter_publisher(self, publisher):
        self.publisher = publisher

    def set_genre(self, genre):
        self.genre = genre

    def enter_author(self, author):
        self.author = author

    def enter_price(self, price):
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