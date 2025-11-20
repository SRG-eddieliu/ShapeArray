from __future__ import annotations

from . import Circle, Line, Point, ShapeArray


def main() -> None:
    """
    Simple demo to show shape creation, aggregation, and serialization.
    """
    shapes = ShapeArray(
        [
            Point(1, 2),
            Line(Point(0, 0), Point(3, 4)),
            Circle(Point(0, 0), Line(Point(0, 0), Point(0, 1))),
        ]
    )

    print("Shapes:")
    for s in shapes:
        print("  ", s)

    print(f"Total area: {shapes.total_area():.3f}")
    print(f"Total perimeter: {shapes.total_perimeter():.3f}")


if __name__ == "__main__":
    main()
