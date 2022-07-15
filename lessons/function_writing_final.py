"""Function Writing."""


def reverse_multiply(x: list[int]) -> list[int]:
    """Given a list returns the list doubled and in reverse order."""
    result: list[int] = []
    i: int = len(x) - 1 
    while i >= 0:
        x[i] *= 2
        result.append(x[i])
        i -= 1
    return result


def free_biscuts(bball: dict[str, list[int]]) -> dict[str, bool]:
    """Maps each game to a bool value."""
    result: dict[str, bool] = {}
    for game in bball:
        total: int = 0
        for points in bball[game]:
            total += points
            if total >= 100:
                result[game] = True
            else: 
                result[game] = False
    return result


# Multiples is a bad function.
def multiples(og: list[int]) -> list[bool]:
    """Should tell us whether each int value is a multiple of the one before it."""
    i: int = 0
    bools: list[bool] = [] 
    while i <= len(og) - 1:
        if i != 0 and (og[i - 1] == og[i]):
            bools.append(True)
        elif i != 0 and (og[i - 1] != og[i]):
            bools.append(False)
        if i == 0:
            if og[i] == og[len(og) - 1]:
                bools.append(True)
            else: 
                bools.append(False)
        i += 1
    return bools


def merged_list(keys: list[str], values: list[int]) -> dict[str, int]:
    """Merges lists together."""
    result: dict[str, int] = {}
    if len(keys) != len(values):
        return result
    i: int = 0
    while i < len(keys):
        result[keys[i]] = values[i]
        i += 1 
    return result

  
# Writing Factorials using recurssion
Factor: int = 5 



def factorial(factor: int) -> int:
    if factor <= 1:
        return 1
    else:
        return factor * factorial(factor - 1)
    

print(factorial(Factor))
