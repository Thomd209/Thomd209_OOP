from figure import Figure


class Rectangle(Figure):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def get_area(self):
        return self.width * self.height

    @property
    def get_perimeter(self):
        return 2 * (self.width + self.height)
