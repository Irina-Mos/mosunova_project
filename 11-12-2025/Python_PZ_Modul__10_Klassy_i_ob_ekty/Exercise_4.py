class Fraction:
    def __init__(self):
        self.numerator = 1
        self.denominator = 1


    def enter_fraction (self, numerator: int, denominator: int):
        self.numerator = numerator
        self.denominator = denominator

    def enter_numerator(self, numerator):
        self.numerator = numerator

    def enter_denominator(self, denominator):
        self.denominator = denominator


    def get_fraction_info(self):
        print(f"Numerator: {self.numerator}")
        print(f"Denominator: {self.denominator}")

    def get_numerator(self):
        return self.numerator

    def get_denominator(self):
        return self.denominator

    def summation(self, numerator_1: int, denominator_1: int):
        summ = self.numerator / self.denominator + numerator_1 / denominator_1
        return summ

    def subtraction(self, numerator_1: int, denominator_1: int):
        minus = self.numerator / self.denominator - numerator_1 / denominator_1
        return minus

    def multiplication(self, numerator_1: int, denominator_1: int):
        multi = self.numerator / self.denominator * numerator_1 / denominator_1
        return multi

    def division(self, numerator_1: int, denominator_1: int):
        div = (self.numerator / self.denominator) / (numerator_1 / denominator_1)
        return div

def dr():
    dr_1 = Fraction()
    dr_1.enter_fraction(1, 2)
    dr_1.enter_numerator(2)
    dr_1.get_fraction_info()
    print(dr_1.summation(4, 5))

dr()

        # nod = 0
        # numerator_2 = 1
        # denominator_2 = 1
        # if self.denominator > denominator_1:
        #     for i in range(1, self.denominator + 1):
        #         if i % denominator_1 == 0:
        #             nod = i
        #             numerator_2 = numerator_1 * (i // denominator_1) + self.numerator
        #             denominator_2 = nod
        #         else:
        #             nod = self.denominator * denominator_1
        #             denominator_2 = nod
        #             numerator_2 = self.numerator * denominator_1 + numerator_1 * self.denominator
        # elif self.denominator == denominator_1:
        #     pass

