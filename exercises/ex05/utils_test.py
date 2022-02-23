"""Tests the utils.py functions that are used to make sure that they work."""

__author__ = "730484878"

from utils import only_evens, sub, concat


def test_only_evens() -> None:
    """Use test of only evens function.""" 
    test: list[int] = [1, 2, 3, 4, 6, 8]
    assert only_evens(test) == [2, 4, 6, 8]


def test_only_evens_odds_only() -> None:
    """Edge Test- if given only odds should return a blank string."""
    test: list[int] = [1, 3, 5, 7, 9]
    assert only_evens(test) == []


def test_only_evens_blank() -> None:
    """Edge test if given a blank string should not return anything."""
    blank_list: list[int] = [] 
    assert only_evens(blank_list) == [] 


def test_sub() -> None:
    """Use test if given two indices should return what is between the beginning index and the end minus one."""
    b_index: int = 1
    e_index: int = 3 
    test_list: list[int] = [10, 20, 30, 40]
    assert sub(test_list, b_index, e_index) == [20, 30]


def test_sub_negative_begin_index() -> None:
    """Tests to make sure that setting the beginning index to negative would result in sub function returning it to 0."""
    b_index: int = -1
    e_index: int = 3 
    test_list: list[int] = [10, 20, 30, 40]
    assert sub(test_list, b_index, e_index) == [10, 20, 30]


def test_sub_large_end_index() -> None:
    """Tests to make sure that the sub function will readjust the end_index if it is not defined in the code."""
    b_index: int = 1
    e_index: int = 5 
    test_list: list[int] = [10, 20, 30, 40]
    assert sub(test_list, b_index, e_index) == [20, 30, 40]


def test_concat_use() -> None:
    """Use test for concat use."""
    list_one: list[int] = [1, 2, 3, 4]
    list_two: list[int] = [5, 6, 7, 8]
    assert concat(list_one, list_two) == [1, 2, 3, 4, 5, 6, 7, 8]


# Test the concat function with the first function being left blank
def test_concat_blank_first_list() -> None:
    """Verifies that if given a blank first list only the second list is returned."""
    list_one: list[int] = list()
    list_two: list[int] = [5, 6, 7, 8]
    assert concat(list_one, list_two) == [5, 6, 7, 8]


# Tests the concat function if no argument is given for the second list. 
def test_concat_blank_second_list() -> None:
    """Verifies that if given a blank second list only the first list is returned."""
    list_one: list[int] = [1, 2, 3, 4]
    list_two: list[int] = list()
    assert concat(list_one, list_two) == [1, 2, 3, 4]