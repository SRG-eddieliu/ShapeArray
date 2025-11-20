import math

import pytest

from shape_array import Circle, Line, Point, ShapeArray
from shape_array import io as io_utils


def test_add_and_len():
    arr = ShapeArray()
    assert len(arr) == 0
    arr.add(Point(1, 2))
    arr.add(Line(Point(0, 0), Point(1, 1)))
    assert len(arr) == 2


def test_extend_and_remove():
    p1 = Point(0, 0)
    p2 = Point(1, 1)
    arr = ShapeArray()
    arr.extend([p1, p2])
    assert len(arr) == 2
    arr.remove(p1)
    assert len(arr) == 1
    assert arr.shapes[0] == p2


def test_translated_and_scaled_return_new_array():
    arr = ShapeArray([Point(1, 2), Line(Point(0, 0), Point(1, 0))])
    moved = arr.translated(1, 1)
    scaled = arr.scaled(2)

    # Originals unchanged
    assert arr.shapes[0] == Point(1, 2)
    assert arr.shapes[1] == Line(Point(0, 0), Point(1, 0))

    # Translated shapes
    assert moved.shapes[0] == Point(2, 3)
    assert moved.shapes[1] == Line(Point(1, 1), Point(2, 1))

    # Scaled shapes
    assert scaled.shapes[0] == Point(2, 4)
    assert scaled.shapes[1] == Line(Point(0, 0), Point(2, 0))


def test_total_area_and_perimeter_mixed_shapes():
    circle = Circle(Point(0, 0), Line(Point(0, 0), Point(0, 1)))  # radius 1
    line = Line(Point(0, 0), Point(3, 4))  # length 5
    point = Point(0, 0)  # area/perimeter 0
    arr = ShapeArray([circle, line, point])

    assert arr.total_area() == pytest.approx(math.pi)
    assert arr.total_perimeter() == pytest.approx(2 * math.pi + 5)


def test_io_round_trip_json():
    arr = ShapeArray(
        [
            Point(1, 2),
            Line(Point(0, 0), Point(1, 1)),
            Circle(Point(0, 0), Line(Point(0, 0), Point(0, 2))),
        ]
    )
    payload = io_utils.shape_array_to_json(arr, indent=None)
    restored = io_utils.shape_array_from_json(payload)

    assert len(restored) == len(arr)
    assert restored.shapes[0] == Point(1, 2)
    assert restored.shapes[1] == Line(Point(0, 0), Point(1, 1))
    assert restored.shapes[2] == Circle(Point(0, 0), Line(Point(0, 0), Point(0, 2)))
