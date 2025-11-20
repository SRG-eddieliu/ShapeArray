"""
Serialization helpers for shapes and ShapeArray.

Provides simple dict/JSON conversions for Point, Line, Circle, and ShapeArray.
Schemas are intentionally minimal and rely on the "type" field to dispatch.
"""

from __future__ import annotations

import json
from typing import Any, Dict, List

from .array import ShapeArray
from .shapes.base import Shape
from .shapes.circle import Circle
from .shapes.line import Line
from .shapes.point import Point


# ----- Shape <-> dict -----
def shape_to_dict(shape: Shape) -> Dict[str, Any]:
    """Convert a shape instance to a serializable dict."""
    if isinstance(shape, Point):
        return {"type": "point", "x": shape.x, "y": shape.y}
    if isinstance(shape, Line):
        return {
            "type": "line",
            "start": {"x": shape.start.x, "y": shape.start.y},
            "end": {"x": shape.end.x, "y": shape.end.y},
        }
    if isinstance(shape, Circle):
        return {
            "type": "circle",
            "center": {"x": shape.center.x, "y": shape.center.y},
            "radius_line": {
                "start": {"x": shape.radius_line.start.x, "y": shape.radius_line.start.y},
                "end": {"x": shape.radius_line.end.x, "y": shape.radius_line.end.y},
            },
        }
    raise TypeError(f"Unsupported shape type: {type(shape)!r}")


def shape_from_dict(data: Dict[str, Any]) -> Shape:
    """Instantiate a Shape from a dict produced by shape_to_dict."""
    shape_type = data.get("type")
    if shape_type == "point":
        return Point(x=data["x"], y=data["y"])
    if shape_type == "line":
        start = Point(x=data["start"]["x"], y=data["start"]["y"])
        end = Point(x=data["end"]["x"], y=data["end"]["y"])
        return Line(start=start, end=end)
    if shape_type == "circle":
        center_dict = data["center"]
        center = Point(x=center_dict["x"], y=center_dict["y"])
        r_start = data["radius_line"]["start"]
        r_end = data["radius_line"]["end"]
        radius_line = Line(Point(r_start["x"], r_start["y"]), Point(r_end["x"], r_end["y"]))
        return Circle(center=center, radius_line=radius_line)
    raise ValueError(f"Unknown shape type: {shape_type!r}")


# ----- ShapeArray <-> dict -----
def shape_array_to_dict(shape_array: ShapeArray) -> Dict[str, Any]:
    """Convert a ShapeArray to a dict."""
    return {"shapes": [shape_to_dict(shape) for shape in shape_array]}


def shape_array_from_dict(data: Dict[str, Any]) -> ShapeArray:
    """Instantiate a ShapeArray from a dict produced by shape_array_to_dict."""
    shapes_data: List[Dict[str, Any]] = data.get("shapes", [])
    return ShapeArray([shape_from_dict(item) for item in shapes_data])


# ----- JSON helpers -----
def shape_array_to_json(shape_array: ShapeArray, *, indent: int | None = 2) -> str:
    """Serialize a ShapeArray to a JSON string."""
    return json.dumps(shape_array_to_dict(shape_array), indent=indent)


def shape_array_from_json(payload: str) -> ShapeArray:
    """Deserialize a JSON string into a ShapeArray."""
    data = json.loads(payload)
    return shape_array_from_dict(data)
