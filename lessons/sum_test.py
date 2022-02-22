"""Tests for the sum function."""

from lessons.sum import sum 


def test_sum_empty() -> None:
    xs: list[float] = []
    assert sum([]) == 0.0 

    # When the function is run this is shown and it shows why it's wrong and what [] is equal to.


def test_sum_single_item() -> None:
    xs: list[float] = [110]
    assert sum([110]) == 110


def test_sum_many_items() -> None: 
    xs: list[float] = [1.0, 2.0, 3.0]
    assert sum(xs) == 6.0


def test_sum_many_items_again() -> None:
    assert sum([-1.0, 1.0, -2.0, 2.0]) == 0.0 
    