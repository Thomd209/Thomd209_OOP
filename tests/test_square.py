import math

import pytest as pytest

from src.square import Square


class TestSquare:
    @pytest.mark.parametrize("width", [1, 10, 100, 500, 1000])
    def test_positive_numbers(self, width):
        assert Square(width)

    @pytest.mark.parametrize("width", [0, -1, -10, -100, -500, -1000])
    def test_bad_numbers(self, width):
        with pytest.raises(ValueError, match="Side can not be less or equal than zero"):
            assert Square(width)

    @pytest.mark.parametrize("width", [1, 10, 100, 500, 1000])
    def test_whole_numbers(self, width):
        assert Square(width)

    @pytest.mark.parametrize("width", [True, False, 5.1, "figure", [1, 2, 3], (4, 5, 6), {"1": 3}])
    def test_bad_types(self, width):
        with pytest.raises(ValueError, match="Side should be a whole number"):
            assert Square(width)

    def test_get_area(self):
        assert math.trunc(Square(5).get_area) == 25

    def test_get_perimeter(self):
        assert math.trunc(Square(5).get_perimeter) == 20
