class Automobile:
    def __init__(self):
        self.model = ""
        self.year_of_manufacture = 0
        self.manufacturer = ""
        self.engine_capacity = 0.0
        self.car_color = ""
        self.price = 0.0

    def enter_car (self, model: str, year_of_manufacture: int, manufacturer: str, engine_capacity: float, car_color: str, price: float):
        self.model = model
        self.year_of_manufacture = year_of_manufacture
        self.manufacturer = manufacturer
        self.engine_capacity = engine_capacity
        self.car_color = car_color
        self.price = price

    def enter_model(self, model: str):
        self.model = model

    def enter_year(self, year_of_manufacture: int):
        self.year_of_manufacture = year_of_manufacture

    def enter_manufacturer(self, manufacturer: str):
        self.manufacturer = manufacturer

    def set_engine_capacity(self, engine_capacity: float):
        self.engine_capacity = engine_capacity

    def enter_color(self, car_color: str):
        self.car_color = car_color

    def enter_price(self, price: float):
        self.price = price

    def get_car_info(self):
        print(f"Model: {self.model}")
        print(f"Year of manufacture: {self.year_of_manufacture}")
        print(f"Manufacturer: {self.manufacturer}")
        print(f"Engine's capacity, l: {self.engine_capacity} ")
        print(f"Color: {self.car_color}")
        print(f"Price, $: {self.price}")

    def get_model(self):
        return self.model

    def get_year_of_manufacture(self):
        return self.year_of_manufacture

    def get_manufacturer(self):
        return self.manufacturer

    def get_engine_capacity(self):
        return self.engine_capacity

    def get_car_color(self):
        return self.car_color

    def get_price(self):
        return self.price