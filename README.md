# ShapeArray

**Starpoint Research Group · Python geometry component**

A small Python software prototype for basic shape interfaces, transformations, aggregate metrics, and JSON/dict serialization.

**Status:** implemented shape and collection components with pytest coverage. The serialization helpers are minimal; this is an early component rather than a production-validated geometry library.

[Package](src/shape_array) · [Shape implementations](src/shape_array/shapes) · [Tests](tests) · [Demo](src/shape_array/__main__.py)

## Layout
- `src/shape_array/`: package root exposing `ShapeArray`, `Point`, `Line`, `Circle`
- `src/shape_array/shapes/`: shape types implementing a common interface
- `src/shape_array/io.py`: simple JSON/dict serialization helpers
- `tests/`: pytest coverage for shapes and the collection
- `src/shape_array/__main__.py`: quick demos

## Design
- Shapes share a common `Shape` ABC, so `ShapeArray` can treat them polymorphically for transforms/metrics.
- `ShapeArray` is effectively a lightweight Composite: it holds many `Shape` instances and exposes aggregate area/perimeter/transform helpers while keeping shapes decoupled from the collection.

## Dev setup
Requires **Python 3.10 or newer** (`dataclass(slots=True)`).

1) Activate your env (e.g., `conda activate shapearray`).
2) Install test dependency: `python -m pip install -r requirements.txt`
3) Install in editable mode: `python -m pip install -e .`
4) Run tests: `pytest`
5) Run the demo: `PYTHONPATH=src python -m shape_array` (or just `python -m shape_array` after step 3).

## Example
Run the built-in demo to see how shapes are aggregated and measured:

Input (shapes created in `__main__.py`):
```
Point(1, 2)
Line(Point(0, 0), Point(3, 4))
Circle(center=Point(0, 0), radius_line=Line(Point(0, 0), Point(0, 1)))
```

Command:
```
PYTHONPATH=src python -m shape_array
```

Output:
```
Shapes:
   Point(x=1, y=2)
   Line(start=Point(x=0, y=0), end=Point(x=3, y=4))
   Circle(center=Point(x=0, y=0), radius_line=Line(start=Point(x=0, y=0), end=Point(x=0, y=1)))
Total area: 3.142
Total perimeter: 11.283
```

## Notes
- Current scope is limited to the provided Python shape types and collection operations.
- Extend `io.py` as needed; current implementations are minimal on purpose.


## Circle scaling

Circle scaling is about the origin. Equal absolute x/y factors preserve a circle, including reflections such as `scale(-2, 2)`. Unequal magnitudes would produce an ellipse and raise `ValueError`; they are no longer silently treated as uniform scaling. Points and lines continue to support independent x/y factors. Bulk transforms return a new collection; a rejected transform leaves the original collection unchanged.
