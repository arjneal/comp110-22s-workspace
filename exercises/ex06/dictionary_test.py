"""Tests the dictionary file."""

__author__ = "730484878"

from dictionary import invert, favorite_color, count


def test_empty_dict_invert() -> None:
    """Given an empty dictionary test to see output of invert."""
    empty_dict: dict[str, str] = {}
    assert invert(empty_dict) == {} 


def test_invert_use_case() -> None:
    """Typical use case of inverting dictionaries."""
    use_dictionary = {'Neal': 'Kapur', 'James': 'Bond'}
    assert invert(use_dictionary) == {'Kapur': 'Neal', 'Bond': 'James'}


def test_invert_given_identical() -> None:
    """Edge Case: testing invert if given a dictionary with matching key and value."""  
    identical_dict = {'a': 'a', 'b': 'b', 'c': 'c'} 
    assert invert(identical_dict) == {'a': 'a', 'b': 'b', 'c': 'c'} 


def test_favorite_color() -> None:
    """Tests to see if the favorite color integer returns the color answered most frequently in a string."""
    sample_color: dict[str, str] = {'Neal': 'blue', 'Walter': 'green', 'Joey': 'yellow', 'James': 'blue'}
    assert favorite_color(sample_color) == 'blue'


def test_no_resposes_favorite_color() -> None:
    """Given an empty dictionary should not return anything."""
    empty_fav_color: dict[str, str] = {} 
    assert favorite_color(empty_fav_color) == ''


def test_tie_favorite_color() -> None:
    """Tests to see that if there is a tie between two colors, the color that appears first in the dict. is returned."""
    tie_color: dict[str, str] = {'Walter': 'green', 'Joey': 'yellow', 'James': 'blue'}
    assert favorite_color(tie_color) == 'green'


def test_count_usage() -> None:
    """Tests a use case of list counter."""
    values: list[str] = ['Neal', 'James', 'Dave', 'Neal']
    assert count(values) == {'Neal': 2, 'James': 1, 'Dave': 1}


def test_count_equals() -> None:
    """Edge test that returns all ones if all of the values are equal."""
    equal_values: list[str] = ['Neal', 'James', 'Dave']
    assert count(equal_values) == {'Neal': 1, 'James': 1, 'Dave': 1}


def test_count_empty_list() -> None:
    """Tests the count function if given an empty list."""
    empty_list: list[str] = []
    assert count(empty_list) == {}
    # If given a list that is empty the count variable should return an empty list. 