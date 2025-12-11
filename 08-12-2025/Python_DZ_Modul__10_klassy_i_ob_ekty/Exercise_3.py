class Stadium:
    def __init__(self):
        self.name = ""
        self.open_date = ""
        self.country = ""
        self.city = ""
        self.capacity = ""

    def enter_stadium (self, name: str, open_date: str, country: str, city: str, capacity: str):
        self.name = name
        self.open_date = open_date
        self.country = country
        self.city = city
        self.capacity = capacity

    def enter_name(self, name: str):
        self.name = name

    def enter_open_date(self, open_date: str):
        self.open_date = open_date

    def enter_country(self, country: str):
        self.country = country

    def set_city(self, city: str):
        self.city = city

    def enter_capacity(self, capacity: str):
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
