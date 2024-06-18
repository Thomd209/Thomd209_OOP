from figure import Figure


class Square(Figure):
    def __init__(self, width):
        if width < 0:
            raise ValueError("Width can not be less than zero")
        self.width = width

    @property
    def get_area(self):
        return self.width ** 2

    @property
    def get_perimeter(self):
        return self.width * 4
