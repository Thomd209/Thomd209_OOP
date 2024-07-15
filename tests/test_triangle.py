import math

import pytest as pytest

from src.triangle import Triangle


class TestTriangle:
    @pytest.mark.parametrize("a, b, c", [(1, 2, 3), (2, 3, 5)])
    def test_positive_numbers(self, a, b, c):
        assert Triangle(a, b, c)

    @pytest.mark.parametrize("a, b, c", [(-5, 0, -10), (-15, -20, -25)])
    def test_bad_numbers(self, a, b, c):
        with pytest.raises(ValueError, match="Side can not be less or equal than zero"):
            assert Triangle(a, b, c)

    @pytest.mark.parametrize("a, b, c", [(1, 2, 3), (2, 3, 5)])
    def test_whole_numbers(self, a, b, c):
        assert Triangle(a, b, c)

    @pytest.mark.parametrize("a, b, c", [(True, 1, 1), (False, 3, 2), (5.1, 3, 6), (7, 7, "figure"), ([1, 2, 3], 5, 1),
                                         (9, 2, (4, 5, 6)), (15, 3, {"1": 3})])
    def test_bad_types(self, a, b, c):
        with pytest.raises(ValueError, match="Side should be a whole number"):
            assert Triangle(a, b, c)

    @pytest.mark.parametrize("a, b, c", [(6, 2, 3), (2, 7, 3), (10, 3, 5)])
    def test_check_triangle_existing(self, a, b, c):
        with pytest.raises(ValueError, match="Triangle can not exist"):
            assert Triangle(a, b, c)

    def test_get_area(self):
        assert math.trunc(Triangle(2, 4, 5).get_area) == 3

    def test_get_perimeter(self):
        assert math.trunc(Triangle(2, 3, 5).get_perimeter) == 10


