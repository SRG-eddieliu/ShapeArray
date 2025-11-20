from __future__ import annotations
from dataclasses import dataclass
from .point import Point
from .base import Shape


@dataclass(frozen=True, slots=True)
class Line(Shape):
    """Line segment defined by two points."""

    start: Point
    end: Point

    def area(self) -> float:
        return 0.0

    def perimeter(self) -> float:
        return self.length()

    def length(self) -> float:
        return self.start.distance_to(self.end)

    def translate(self, dx: float, dy: float) -> Line:
        return Line(self.start.translate(dx, dy), self.end.translate(dx, dy))

    def scale(self, sx: float, sy: float | None = None) -> Line:
        return Line(self.start.scale(sx, sy), self.end.scale(sx, sy))

