from figure import Figure


class Rectangle(Figure):
    def __init__(self, width, height):
        if width < 0 or height < 0:
            raise ValueError("Side can not be less than zero")
        self.width = width
        self.height = height

    @property
    def get_area(self):
        return self.width * self.height

    @property
    def get_perimeter(self):
        return 2 * (self.width + self.height)
