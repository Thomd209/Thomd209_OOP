import math

import pytest as pytest

from src.rectangle import Rectangle


class TestRectangle:
    @pytest.mark.parametrize("width, height", [(2, 3), (3, 5), (10, 7)])
    def test_positive_numbers(self, width, height):
        assert Rectangle(width, height)

    @pytest.mark.parametrize("width, height", [(0, -1), (-10, -100), (-500, -1000)])
    def test_bad_numbers(self, width, height):
        with pytest.raises(ValueError, match="Side can not be less or equal than zero"):
            assert Rectangle(width, height)

    @pytest.mark.parametrize("width, height", [(1, 10), (20, 30), (100, 500), (1000, 3000)])
    def test_whole_numbers(self, width, height):
        assert Rectangle(width, height)

    @pytest.mark.parametrize("width, height", [(True, 1), (False, 3), (5.1, 3), (7, "figure"), ([1, 2, 3], 5),
                                               (9, (4, 5, 6)),  (15, {"1": 3})])
    def test_bad_types(self, width, height):
        with pytest.raises(ValueError, match="Side should be a whole number"):
            assert Rectangle(width, height)

    def test_get_area(self):
        assert math.trunc(Rectangle(2, 3).get_area) == 6

    def test_get_perimeter(self):
        assert math.trunc(Rectangle(2, 3).get_perimeter) == 10

