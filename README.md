# Shape Array (practice scaffold)

Small, OOP-focused practice project in Python for working with basic shapes and a collection wrapper.

## Layout
- `src/shape_array/`: package root exposing `ShapeArray`, `Point`, `Line`, `Circle`
- `shapes/`: shape types implementing a common interface
- `geometry.py`: shared math helpers
- `io.py`: simple JSON/dict serialization helpers
- `tests/`: pytest coverage for shapes, array, and I/O
- `examples/` and `__main__.py`: quick demos

## Dev setup
1) Activate your env (e.g., `conda activate shapearray`).
2) Install test dependency: `python -m pip install -r requirements.txt`
3) Install in editable mode: `python -m pip install -e .`
4) Run tests: `pytest`
5) Run the demo: `PYTHONPATH=src python -m shape_array` (or just `python -m shape_array` after step 3).

## Notes
- Intended for practicing OOP patterns in Python only (no external deps by default).
- Extend `io.py` and `geometry.py` as needed; current implementations are minimal on purpose.
