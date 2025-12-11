class Country:
    def __init__(self):
        self.country_name = ""
        self.continent_name = ""
        self.number_of_inhabitants = 0
        self.telephone_code = ""
        self.capital_name = ""
        self.name_of_cities = []


    def enter_country (self, country_name: str, continent_name: str, number_of_inhabitants: int, telephone_code: str, capital_name: str, name_of_cities: list):
        self.country_name = country_name
        self.continent_name = continent_name
        self.number_of_inhabitants = number_of_inhabitants
        self.telephone_code = telephone_code
        self.capital_name = capital_name
        self.name_of_cities = name_of_cities

    def enter_country_name(self, country_name):
        self.country_name = country_name

    def enter_continent_name(self, continent_name):
        self.continent_name = continent_name

    def enter_number_of_inhabitants(self, number_of_inhabitants):
        self.number_of_inhabitants = number_of_inhabitants

    def enter_telephone_code(self, telephone_code):
        self.telephone_code = telephone_code

    def enter_capital_name(self, capital_name):
        self.capital_name = capital_name

    def enter_name_of_cities(self, name_of_cities):
        self.name_of_cities = name_of_cities

    def get_country_info(self):
        print(f"Country name: {self.country_name}")
        print(f"Continent name: {self.continent_name}")
        print(f"Number of inhabitants in the country: {self.number_of_inhabitants}")
        print(f"Country telephone_code: {self.telephone_code} ")
        print(f"The name of the capital: {self.capital_name}")
        print(f"The name of the cities of the country: {self.name_of_cities}")

    def get_country_name(self):
        return self.country_name

    def get_continent_name(self):
        return self.continent_name

    def get_number_of_inhabitants(self):
        return self.number_of_inhabitants

    def get_telephone_code(self):
        return self.telephone_code

    def get_capital_name(self):
        return self.capital_name

    def get_name_of_cities(self):
        return self.name_of_cities