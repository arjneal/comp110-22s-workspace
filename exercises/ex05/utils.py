__author__ = "730484878"

"""Collection of unit functions that implement lists."""


# Only_Evens states that given a list of numbers if it is divisble by 2 add it to the list even_numbers and return that list. 
def only_evens(a: list[int]) -> list[int]:
    """Return all the even numbers."""
    i: int = 0
    even_numbers: list[int] = list()
    while i < len(a):
        if a[i] % 2 == 0:
            even_numbers.append(a[i])
        i += 1
    return even_numbers 


def sub(a: list[int], begin_index: int, end_index: int) -> list[int]:
    """Returns the first and last indices of a function."""
    indices_list: list[int] = list()
    if begin_index < 0:
        begin_index = 0
    if end_index > len(a):
        end_index = len(a)
    i: int = begin_index
    while i <= (end_index - 1): 
        indices_list.append(a[i])
        i += 1
    return indices_list 
# While loop is main body of the function, the two if statements come before and settle any addendums or errors that may occur.
# If begin_index too small or end_index too large not correlated with the list then sub function will still run after correcting these errors. 


def concat(a: list[int], b: list[int]) -> list[int]:
    """Given two lists concat will concatonate them together to form one list."""
    concat_list: list[int] = list()
    concat_list = a
    concat_list += b
    return concat_list 
# Adds both concat functions to a blank list, thereby 'adding' them. 
