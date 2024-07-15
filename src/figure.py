from abc import ABC, abstractmethod
from typing import Protocol


class Figure(ABC):

    def check_on_positive_values(self, *args):
        for n in args:
            if n <= 0:
                raise ValueError("Side can not be less or equal than zero")

    def check_on_whole_numbers(self, *args):
        for n in args:
            if not isinstance(n, int) or isinstance(n, bool):
                raise ValueError("Side should be a whole number")

    @abstractmethod
    def get_area(self):
        pass

    @abstractmethod
    def get_perimeter(self):
        pass

    def add_figure(self, other_figure):
        if not isinstance(other_figure, Figure):
            raise ValueError("Should be a Figure")
        return self.get_area + other_figure.get_area
