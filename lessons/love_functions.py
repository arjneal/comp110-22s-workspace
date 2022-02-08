def love(name: str) -> str:
    """Some examples of tender, loving function definitions."""
    return f"I love you {name}!"


print(love("Holly"))


def spread_love(to: str, n: int) -> str:
    """Generates a string that repeats a loving message n times."""
    love_note: str = ""
    i: int = 0
    while i < n:
        # Do what I need to do
        love_note += love(to) + "\n"
        i += 1
    return love_note