from figure import Figure


class Circle(Figure):
    def __init__(self, radius):
        if radius < 0:
            raise ValueError("Radius can not be less than zero")
        self.radius = radius

    @property
    def get_area(self):
        return self.radius * 3.14

    @property
    def get_perimeter(self):
        return 2 * 3.14 * self.radius
