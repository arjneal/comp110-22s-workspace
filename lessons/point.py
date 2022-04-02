"""Example of a Point Class."""
# From CL19


class Point:
    x: float
    y: float

    def __init__(self, x: float, y: float):
        """Initializes a point with its x, y components."""
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        """Produce a str representation of a Point for Python."""
        return f"Point({self.x}, {self.y})"

    def __mul__(self, factor: float):
        """Overload the multiplication operator for Point * float."""
        return Point(self.x * factor, self.y * factor)
    
    def __getitem__(self, index: int) -> float:
        """Allows us to index a float."""
        if index == 0:
            return self.x
        elif index == 1:
            return self.y
        else:
            raise IndexError


a: Point = Point(1.0, 2.0)
b: Point = a * 2.0
c: Point = a + b
print(f"a: {a}")
print(f"b: {b}")
print(f"c: {c}")
print(a[0])
print(a[1])