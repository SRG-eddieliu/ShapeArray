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
        """Scale about the origin; unequal magnitudes would require an ellipse."""
        if sy is None:
            sy = sx
        if abs(sx) != abs(sy):
            raise ValueError("Circle requires equal absolute scale factors; anisotropic scaling produces an ellipse")
        return Circle(self.center.scale(sx, sy), self.radius_line.scale(sx, sy))
