import pytest

from src.rectangle import Rectangle
from src.square import Square


class TestAddFigure:
    def test_add_figure(self):
        rectangle = Rectangle(5, 2)
        square = Square(3)
        assert square.add_figure(rectangle) == 19

    def test_add_figure_negative(self):
        rectangle = Rectangle(5, 2)

        with pytest.raises(ValueError, match="Should be a Figure"):
            assert rectangle.add_figure(10)