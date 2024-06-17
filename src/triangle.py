import math

from figure import Figure


class Triangle(Figure):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def check_existence(self):
        if self.a + self.b < self.c or self.a + self.c < self.b \
                or self.b + self.c < self.a:
            raise ValueError("Triangle can not exist")

    @property
    def get_area(self):
        if self.check_existence() != "Triangle can not exist":
            return math.sqrt(self.get_perimeter * (self.get_perimeter - self.a)
                             * (self.get_perimeter - self.b)
                             * (self.get_perimeter - self.c))

    @property
    def get_perimeter(self):
        if self.check_existence() != "Triangle can not exist":
            return self.a + self.b + self.c
