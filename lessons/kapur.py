

scramble: str = input("Give me an all lower-case word: ")


def codifier(scrambled: str) -> str:
    """Given a scrambled word return word with letters two indices forward."""
    a: dict[str, str] = {
        'a': 'c',
        'b': 'd',
        'c': 'e',
        'd': 'f',
        'e': 'g',
        'f': 'h',
        'g': 'i',
        'h': 'j',
        'i': 'k',
        'j': 'l',
        'k': 'm',
        'l': 'n',
        'm': 'o',
        'n': 'p',
        'o': 'q',
        'p': 'r',
        'q': 's',
        'r': 't',
        's': 'u',
        't': 'v',
        'u': 'x',
        'v': 'y',
        'w': 'z',
        'x': 'a',
        'y': 'b',
        'z': 'c'}
    i: int = 0
    result: str = ""
    while i < len(scrambled):
        for letter in a:
            if letter == scrambled[i]:
                result += a[letter]
        i += 1
    return result


def main() -> str: 
    return codifier(scramble)


if __name__ == "__main__":
    main()
