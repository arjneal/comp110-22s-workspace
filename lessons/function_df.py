"""An example function definition."""


def my_max(a: int, b: int) -> int:
    # Signature/ "Contract" line: here are the requirements to use me.
    """Returns the largest argument."""
    if a >= b:
        return a 
    return b


x: int = 6
y: int = 5 + 2
z: int = my_max(x, y)
print(z)