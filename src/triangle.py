import math

from figure import Figure


class Triangle(Figure):
    def __init__(self, a, b, c):
        self.check_on_positive_values(a, b, c)
        self.check_on_whole_numbers(a, b, c)
        self.check_existence(a, b, c)

    def check_existence(self, a, b, c):
        if a + b < c or a + c < b or b + c < a:
            raise ValueError("Triangle can not exist")

    @property
    def get_area(self):
        half_perimeter = self.get_perimeter / 2
        return math.sqrt(half_perimeter * (half_perimeter - self.a)
                         * (half_perimeter - self.b)
                         * (half_perimeter - self.c))

    @property
    def get_perimeter(self):
        return self.a + self.b + self.c
