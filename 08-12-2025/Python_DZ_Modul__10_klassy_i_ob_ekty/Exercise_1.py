class Automobile:
    def __init__(self):
        self.model = ""
        self.year_of_manufacture = 0
        self.manufacturer = ""
        self.engine_capacity = 0.0
        self.car_color = ""
        self.price = 0.0

    def enter_car (self):
        self.model = input("Enter the model: ")
        self.year_of_manufacture = int(input("Enter the year of manufacture: "))
        self.manufacturer = input("Enter the manufacturer: ")
        self.engine_capacity = float(input("Enter the engine's capacity: "))
        self.car_color = input("Enter the car color: ")
        self.price = float(input("Enter the price: "))

    def enter_model(self, model):
        self.model = model

    def enter_year(self, year_of_manufacture):
        self.year_of_manufacture = year_of_manufacture

    def enter_manufacturer(self, manufacturer):
        self.manufacturer = manufacturer

    def set_engine_capacity(self, engine_capacity):
        self.engine_capacity = engine_capacity

    def enter_color(self, car_color):
        self.car_color = car_color

    def enter_price(self, price):
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

hyundai_solaris = Automobile()

hyundai_solaris.enter_car()
hyundai_solaris.get_car_info()
print(hyundai_solaris.get_model())
print(hyundai_solaris.get_year_of_manufacture())
print(hyundai_solaris.get_manufacturer())
print(hyundai_solaris.get_engine_capacity())
print(hyundai_solaris.get_car_color())
print(hyundai_solaris.get_price())



