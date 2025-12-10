class Stadium:
    def __init__(self):
        self.name = ""
        self.open_date = ""
        self.country = ""
        self.city = ""
        self.capacity = ""

    def enter_stadium (self):
        self.name = input("Enter the stadium name: ")
        self.open_date = input("Enter the opening date: ")
        self.country = input("Enter the country: ")
        self.city = float(input("Enter the city: "))
        self.capacity = input("Enter the capacity: ")

    def enter_name(self, name):
        self.name = name

    def enter_open_date(self, open_date):
        self.open_date = open_date

    def enter_country(self, country):
        self.country = country

    def set_city(self, city):
        self.city = city

    def enter_capacity(self, capacity):
        self.capacity = capacity



    def get_stadium_info(self):
        print(f"Name: {self.name}")
        print(f"Opening date: {self.open_date}")
        print(f"Country: {self.country}")
        print(f"City: {self.city} ")
        print(f"Capacity: {self.capacity}")


    def get_name(self):
        return self.name

    def get_open_date(self):
        return self.open_date

    def get_country(self):
        return self.country

    def get_city(self):
        return self.city

    def get_capacity(self):
        return self.capacity
