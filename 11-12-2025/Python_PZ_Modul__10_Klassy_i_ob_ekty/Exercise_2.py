class City:
    def __init__(self):
        self.city_name = ""
        self.region = ""
        self.country = ""
        self.number_of_residents = 0
        self.postal_code = ""
        self.telephone_code = ""

    def enter_city (self, city_name: str, region: str, country: str, number_of_residents: int, postal_code: str, telephone_code: str):
        self.city_name = city_name
        self.region = region
        self.country = country
        self.number_of_residents = number_of_residents
        self.postal_code = postal_code
        self.telephone_code = telephone_code

    def enter_city_name(self, city_name):
        self.city_name = city_name

    def enter_region(self, region):
        self.region = region

    def enter_country(self, country):
        self.country = country

    def enter_number_of_residents(self, number_of_residents):
        self.number_of_residents = number_of_residents

    def enter_postal_code(self, postal_code):
        self.postal_code = postal_code

    def enter_telephone_code(self, telephone_code):
        self.telephone_code = telephone_code

    def get_city_info(self):
        print(f"City name: {self.city_name}")
        print(f"Region: {self.region}")
        print(f"Country: {self.country}")
        print(f"Number of residents: {self.number_of_residents} ")
        print(f"Postal code: {self.postal_code}")
        print(f"Telephone code: {self.telephone_code}")

    def get_city_name(self):
        return self.city_name

    def get_region(self):
        return self.region

    def get_country(self):
        return self.country

    def get_number_of_residents(self):
        return self.number_of_residents

    def get_postal_code(self):
        return self.postal_code

    def get_telephone_code(self):
        return self.telephone_code