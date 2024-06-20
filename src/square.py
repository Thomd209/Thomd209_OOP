from figure import Figure


class Square(Figure):
    def __init__(self, width):
        self.check_on_positive_values(width)
        self.check_on_whole_numbers(width)
        self.width = width

    @property
    def get_area(self):
        return self.width ** 2

    @property
    def get_perimeter(self):
        return self.width * 4
