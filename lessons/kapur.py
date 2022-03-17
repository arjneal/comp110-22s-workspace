"""Codifies words, Practice of Elif functions."""


def code(scrambled: str) -> list[str]:
    """Give a scrambled word return word with letters two indices forward."""
    i: int = 0
    result: list[str] = []
    while i < len(scrambled):
        if scrambled[i] == "a":
            scrambled[i] == result.append("c")
        elif scrambled[i] == "b":
            scrambled[i] == result.append('d')
        elif scrambled[i] == 'c':
            scrambled[i] == result.append('e')
        elif scrambled[i] == 'd':
            scrambled[i] == result.append("f")
        elif scrambled[i] == 'e':
            scrambled[i] == result.append("g")
        elif scrambled[i] == 'f':
            scrambled[i] == result.append("h")
        elif scrambled[i] == 'g':
            scrambled[i] == result.append("i")
        elif scrambled[i] == 'k':
            scrambled[i] == result.append("j")
        elif scrambled[i] == 'i':
            scrambled[i] == result.append("k")
        elif scrambled[i] == 'j':
            scrambled[i] == result.append("l")
        elif scrambled[i] == 'k':
            scrambled[i] == result.append("m")
        elif scrambled[i] == 'l':
            scrambled[i] == result.append("n")
        elif scrambled[i] == 'm':
            scrambled[i] == result.append("o")
        elif scrambled[i] == 'n':
            scrambled[i] == result.append("p")
        elif scrambled[i] == 'o':
            scrambled[i] == result.append("q")
        elif scrambled[i] == 'p':
            scrambled[i] == result.append("r")
        elif scrambled[i] == 'q':
            scrambled[i] == result.append("s")
        elif scrambled[i] == 'r':
            scrambled[i] == result.append("t")
        elif scrambled[i] == 's':
            scrambled[i] == result.append("u")
        elif scrambled[i] == 't':
            scrambled[i] == result.append("v")
        elif scrambled[i] == 'u':
            scrambled[i] == result.append("x")
        elif scrambled[i] == 'v':
            scrambled[i] == result.append("y")
        elif scrambled[i] == 'w':
            scrambled[i] == result.append("z")
        elif scrambled[i] == 'x':
            scrambled[i] == result.append("a")
        elif scrambled[i] == 'y':
            scrambled[i] == result.append("b")
        elif scrambled[i] == 'z':
            scrambled[i] == result.append("c")
        i += 1
    return result


original: str = input("Give me an all-lowercase word: ")
print(code(original))