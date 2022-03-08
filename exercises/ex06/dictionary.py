"""Usage of dictionaries in an Exercise."""

__author__ = "730484878"


def invert(a: dict[str, str]) -> dict[str, str]:
    """Given a dictionary of strings inverts the original function."""
    invert_a: dict[str, str] = dict()
    for key in a:
        if a[key] in invert_a:
            raise KeyError("Duplicate Keys.")
        invert_a[a[key]] = key
    return invert_a


def favorite_color(og_dict: dict[str, str]) -> str:
    """Returns the favorite color that is most frequent in a group."""
    color_dict: dict[str, int] = {} 
    # First half of favorite_color creates a new dictionary assigning the colors too an integer value that represents how many times they have been repeated. 
    for name in og_dict:
        if og_dict[name] in color_dict:
            color_dict[og_dict[name]] += 1
        else: 
            color_dict[og_dict[name]] = 1
    # Second half of favorite_color returns the key (color) that has the highest integer (how many people answered that color).
    highest_color: str = "" 
    ctr_variable: int = 0
    for color in color_dict: 
        if color_dict[color] > ctr_variable:
            ctr_variable = color_dict[color]
            highest_color = color 
    return highest_color 
    # returns the highest_color.


def count(value_list: list[str]) -> dict[str, int]:
    """Counts all the values in a list and returns them as key values in a dictionary."""
    result_dict: dict[str, int] = {} 
    for index in value_list:
        if index in result_dict:
            result_dict[index] += 1
        else:
            result_dict[index] = 1
    return result_dict
