"""Exploration with class types. """

from __future__ import annotations

from typing import Union


class ChapelHill:
    x: int
    y: int
    l_add: list[int]
    is_smiling: bool = False 

    def __init__(self, x: int, y: int, l_add: list[int] = []):
        """Initializes a class variable."""
        self.x = x
        self.y = y
        self.l_add = l_add

    def __repr__(self) -> str:
        """Practice with printing objects as strings."""
        return f"the output is ({self.x}, {self.y})"
    
    def __add__(self, rhs: ChapelHill) -> ChapelHill:
        """Practice with overloading operators."""
        return ChapelHill(self.x + self.y, rhs.x + rhs.y)

    def __mul__(self, rhs: Union[int, ChapelHill]) -> ChapelHill:
        """Practice with multiplication overloading."""
        if isinstance(rhs, int):
            old_well: ChapelHill = ChapelHill(self.x * rhs, self.y * rhs)
            return old_well
        if isinstance(rhs, ChapelHill):
            davis: ChapelHill = ChapelHill(self.x * rhs.x, self.y * rhs.y)
            return davis
    
    def __getitem__(self, index: int) -> int:
        """Overload subscription notation."""
        result: int = self.l_add[index]
        return result


a: ChapelHill = ChapelHill(2, 4)
b: ChapelHill = ChapelHill(3, 5)
c: ChapelHill = a + b

print(f"Overloading Output: {c}")

d: ChapelHill = a * b
print(f"Overloading Multiplication Output: {d}")

list_for: list[int] = [4, 5, 6, 7]
e: ChapelHill = ChapelHill(2, 3, list_for)
f: int = e[3]
print(f)