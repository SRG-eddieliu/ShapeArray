from __future__ import annotations

from dataclasses import dataclass

from .base import Shape


@dataclass(frozen=True, slots=True)
class Point(Shape):
    """2D point."""

    x: float = 0.0
    y: float = 0.0

    def area(self) -> float:
        return 0.0

    def perimeter(self) -> float:
        return 0.0
    
    def translate(self, dx: float, dy: float) -> Point:
        return Point(self.x + dx, self.y + dy)

    def scale(self, sx: float, sy: float | None = None) -> Point:
        factor_y = sy if sy is not None else sx
        return Point(self.x * sx, self.y * factor_y)

    def distance_to(self, other: Point) -> float:
        from math import hypot
        return hypot(other.x - self.x, other.y - self.y)
    
    # init, eq, str, repr is handled by dataclass
    
