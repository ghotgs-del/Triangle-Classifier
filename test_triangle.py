import math

import pytest

from triangle import classify_triangle, is_valid_triangle


@pytest.mark.parametrize(
    "a, b, c, expected",
    [
        (3, 4, 5, True),
        (5, 5, 5, True),
        (2, 3, 4, True),
        (1, 2, 3, False),
        (0, 4, 5, False),
        (-1, 2, 3, False),
        (1, 1, 2, False),
        (4, 5, 9, False),
    ],
)
def test_is_valid_triangle(a, b, c, expected):
    assert is_valid_triangle(a, b, c) is expected


@pytest.mark.parametrize(
    "a, b, c, expected",
    [
        (4, 4, 4, "Equilateral"),
        (5, 5, 6, "Isosceles"),
        (4, 5, 6, "Scalene"),
        (3, 4, 5, "Right Scalene"),
        (1, 1, math.sqrt(2), "Right Isosceles"),
        (1, 2, 3, "Invalid"),
        (0, 4, 5, "Invalid"),
        (-5, 5, 5, "Invalid"),
    ],
)
def test_classify_triangle(a, b, c, expected):
    assert classify_triangle(a, b, c) == expected


def test_order_does_not_matter():
    assert classify_triangle(3, 4, 5) == classify_triangle(5, 3, 4)
    assert classify_triangle(5, 5, 6) == classify_triangle(6, 5, 5)


def test_near_right_triangle_with_floats():
    assert classify_triangle(5, 5, 5 * math.sqrt(2)) == "Right Isosceles"