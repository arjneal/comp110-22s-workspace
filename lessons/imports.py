"""Examples of importing in python."""


from lessons import helpers


def main() -> None:
    """Entrypoint of program."""
    print(helpers.powerful(2, 12))
    print(f"The answer: {helpers.THE_ANSWER}")


if __name__ == "__main__":
    main()
else: 
    print(f"helpers.py was imported: {__name__}")