import math

import pytest as pytest

from src.circle import Circle


class TestCircle:
    @pytest.mark.parametrize("radius", [1, 10, 100, 500, 1000])
    def test_positive_numbers(self, radius):
        assert Circle(radius)

    @pytest.mark.parametrize("radius", [0, -1, -10, -100, -500, -1000])
    def test_bad_numbers(self, radius):
        with pytest.raises(ValueError, match="Side can not be less or equal than zero"):
            assert Circle(radius)

    @pytest.mark.parametrize("radius", [1, 10, 100, 500, 1000])
    def test_whole_numbers(self, radius):
        assert Circle(radius)

    @pytest.mark.parametrize("radius", [True, False, 5.1, "figure", [1, 2, 3], (4, 5, 6), {"1": 3}])
    def test_bad_types(self, radius):
        with pytest.raises(ValueError, match="Side should be a whole number"):
            assert Circle(radius)

    def test_get_area(self):
        assert math.trunc(Circle(5).get_area) == 15

    def test_get_perimeter(self):
        assert math.trunc(Circle(5).get_perimeter) == 31

