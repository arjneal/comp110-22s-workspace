"""Reverse multiply."""


def reverse_multiply(xs: list[int]) -> list[int]:
    """Reverse_multiply a list."""
    result: list[int] = [] 
    i: int = len(xs) - 1
    while i != 0:
        result.append(xs[i] * 2)
        i -= 1
    return result


def free_biscuts(bball: dict[str, list[int]]) -> dict[str, bool]:
    """Returns a value of true if the points add up to 100."""
    result: dict[str, bool] = {}
    for game in bball:
        total_val: int = 0
        for score in bball[game]:
            total_val += score
            if total_val >= 100:
                result[game] = True
            else:
                result[game] = False 
    return result


def multiples(xs: list[int]) -> list[bool]:
    """Returns a bool if the number in the list is a multiple of the one before it."""
    result: list[bool] = []
    i: int = 0
    while i < len(xs):
        if i == 0:
            result.append(xs[i] % xs[len(xs) - 1] == 0)


