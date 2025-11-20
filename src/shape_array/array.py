from __future__ import annotations

from dataclasses import dataclass, field
from typing import Iterable, Iterator, List

from .shapes.base import Shape


@dataclass
class ShapeArray:
    """
    Manage a collection of shapes with basic aggregate helpers.

    This keeps a simple mutable list of Shape instances and provides
    bulk transform helpers that return new ShapeArray instances.
    """

    shapes: List[Shape] = field(default_factory=list)

    def __iter__(self) -> Iterator[Shape]:
        return iter(self.shapes)

    def __len__(self) -> int:
        return len(self.shapes)

    def add(self, shape: Shape) -> None:
        """Append a single shape."""
        self.shapes.append(shape)

    def extend(self, shapes: Iterable[Shape]) -> None:
        """Append many shapes."""
        self.shapes.extend(shapes)

    def remove(self, shape: Shape) -> None:
        """Remove a shape by identity/equality."""
        self.shapes.remove(shape)

    def translated(self, dx: float, dy: float) -> ShapeArray:
        """Return a new ShapeArray with all shapes translated."""
        return ShapeArray([shape.translate(dx, dy) for shape in self.shapes])

    def scaled(self, sx: float, sy: float | None = None) -> ShapeArray:
        """Return a new ShapeArray with all shapes scaled."""
        return ShapeArray([shape.scale(sx, sy) for shape in self.shapes])

    def total_area(self) -> float:
        """Sum of areas for all shapes (dimensionless shapes contribute 0)."""
        return sum(shape.area() for shape in self.shapes)

    def total_perimeter(self) -> float:
        """Sum of perimeters/lengths for all shapes."""
        return sum(shape.perimeter() for shape in self.shapes)
