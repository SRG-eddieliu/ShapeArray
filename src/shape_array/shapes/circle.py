from __future__ import annotations

from dataclasses import dataclass
from math import pi

from .base import Shape
from .line import Line
from .point import Point


@dataclass(frozen=True, slots=True)
class Circle(Shape):
    """
    Circle defined by a center point and a radius line (center to perimeter).
    Radius length is derived from the line length.
    """

    center: Point
    radius_line: Line

    @property
    def radius(self) -> float:
        # Assume the radius line starts at center; if not, this still measures length
        return self.radius_line.length()

    def area(self) -> float:
        return pi * self.radius**2

    def perimeter(self) -> float:
        return 2 * pi * self.radius

    def translate(self, dx: float, dy: float) -> Circle:
        return Circle(self.center.translate(dx, dy), self.radius_line.translate(dx, dy))

    def scale(self, sx: float, sy: float | None = None) -> Circle:
        # Circle scales uniformly; pick uniform factor from sx (ignore sy if provided)
        factor = sx
        scaled_center = self.center.scale(factor, factor)
        scaled_radius_line = self.radius_line.scale(factor, factor)
        return Circle(scaled_center, scaled_radius_line)
