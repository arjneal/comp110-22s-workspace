"""Examples of importing in python."""


from lessons import helpers


def main() -> None:
    """Entrypoint of program."""
    print(helpers.powerful(2, 12))
    # Notice that we had to reference the module before we were able to print the function. 
    print(f"The answer: {helpers.THE_ANSWER}")


# Idiom for making a module able to run as a module. 
# or have its global definitions imported. 
if __name__ == "__main__":
    main()
else:
    # It is not idiomatic to have an else branch. 
    print(f"helpers.py was imported: {__name__}")