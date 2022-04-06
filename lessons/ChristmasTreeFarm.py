"""Exploration with class types. """

from __future__ import annotations


class ChapelHill:
    x: int
    y: int
    is_smiling: bool = False 

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        """Practice with printing objects as strings."""
        return f"the output is ({self.x}, {self.y})"
    
    def __add__(self, rhs: ChapelHill) -> ChapelHill:
        """Practice with overloading operators."""
        return ChapelHill(self.x + self.y, rhs.x + rhs.y)


a: ChapelHill = ChapelHill(2, 4)
b: ChapelHill = ChapelHill(3, 5)
c: ChapelHill = a + b

print(f"Overloading Output: {c}")