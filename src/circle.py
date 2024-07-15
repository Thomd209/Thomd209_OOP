from figure import Figure


class Circle(Figure):
    def __init__(self, radius):
        self.check_on_whole_numbers(radius)
        self.check_on_positive_values(radius)
        self.radius = radius

    @property
    def get_area(self):
        return self.radius * 3.14

    @property
    def get_perimeter(self):
        return 2 * 3.14 * self.radius
