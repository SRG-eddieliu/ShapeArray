from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Tuple


class Shape(ABC):
    @abstractmethod
    def area(self) -> float:
        """Return the area of the shape."""

    @abstractmethod
    def perimeter(self) -> float:
        """Return the perimeter/length of the shape."""

    @abstractmethod
    def translate(self, dx: float, dy: float) -> Shape:
        """Return a new shape translated by (dx, dy)."""

    @abstractmethod
    def scale(self, sx: float, sy: float | None = None) -> Shape:
        """Return a new shape scaled by (sx, sy). If sy is None, uniform scaling is applied."""
        