import math

import pytest

from shape_array.shapes.circle import Circle
from shape_array.shapes.line import Line
from shape_array.shapes.point import Point

def test_point_area_perimeter_and_defaults():
    p = Point()
    assert p.area() == 0.0
    assert p.perimeter() == 0.0
    assert p.x == 0.0 and p.y == 0.0


def test_point_translate_scale_and_distance():
    p = Point(2, 3)
    assert p.translate(1, -1) == Point(3, 2)
    assert p.scale(2) == Point(4, 6)
    assert p.scale(2, 3) == Point(4, 9)
    assert p.distance_to(Point(5, 7)) == pytest.approx(5.0)


def test_line_area_and_length():
    line = Line(Point(0, 0), Point(3, 4))
    assert line.area() == 0.0
    assert line.length() == pytest.approx(5.0)
    assert line.perimeter() == pytest.approx(5.0)


def test_line_translate_and_scale():
    line = Line(Point(1, 1), Point(2, 3))
    moved = line.translate(-1, 2)
    assert moved == Line(Point(0, 3), Point(1, 5))

    scaled_uniform = line.scale(2)
    assert scaled_uniform == Line(Point(2, 2), Point(4, 6))

    scaled_non_uniform = line.scale(2, 3)
    assert scaled_non_uniform == Line(Point(2, 3), Point(4, 9))


def test_circle_area_perimeter_and_radius():
    center = Point(0, 0)
    radius_line = Line(center, Point(0, 2))
    circle = Circle(center, radius_line)

    assert circle.radius == pytest.approx(2.0)
    assert circle.area() == pytest.approx(math.pi * 4)
    assert circle.perimeter() == pytest.approx(2 * math.pi * 2)


def test_circle_translate_and_scale():
    center = Point(0, 0)
    radius_line = Line(center, Point(0, 1))
    circle = Circle(center, radius_line)

    translated = circle.translate(2, 3)
    assert translated.center == Point(2, 3)

    scaled = circle.scale(2)
    assert scaled.center == Point(0, 0)  # scaling about origin keeps center at origin
    assert scaled.radius == pytest.approx(2.0)
