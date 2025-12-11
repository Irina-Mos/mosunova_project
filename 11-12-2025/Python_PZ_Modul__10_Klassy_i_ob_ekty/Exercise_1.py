class Human:
    def __init__(self):
        self.full_name = ""
        self.date_of_birth = ""
        self.phone_number = ""
        self.city = ""
        self.country = ""
        self.home_address = ""

    def enter_human (self, full_name: str, date_of_birth: str, phone_number: str, city: str, country: str, home_address: str):
        self.full_name = full_name
        self.date_of_birth = date_of_birth
        self.phone_number = phone_number
        self.city = city
        self.country = country
        self.home_address = home_address

    def enter_full_name(self, full_name):
        self.full_name = full_name

    def enter_date_of_birth(self, date_of_birth):
        self.date_of_birth = date_of_birth

    def enter_phone_number(self, phone_number):
        self.phone_number = phone_number

    def enter_city(self, city):
        self.city = city

    def enter_country(self, country):
        self.country = country

    def enter_home_address(self, home_address):
        self.home_address = home_address

    def get_human_info(self):
        print(f"Full name: {self.full_name}")
        print(f"Date of birth: {self.date_of_birth}")
        print(f"Phone number: {self.phone_number}")
        print(f"City: {self.city} ")
        print(f"Country: {self.country}")
        print(f"Home address: {self.home_address}")

    def get_full_name(self):
        return self.full_name

    def get_date_of_birth(self):
        return self.date_of_birth

    def get_phone_number(self):
        return self.phone_number

    def get_city(self):
        return self.city

    def get_country(self):
        return self.country

    def get_home_address(self):
        return self.home_address

def Kolin():
    kolin = Human()
    kolin.enter_human("Kolin Robinson", "14.11.1987", "+2352633477", "NY", "USA", "125 BS")
    kolin.get_human_info()
    print(kolin.get_full_name())

print(Kolin())