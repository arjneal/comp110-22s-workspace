"""Tests for linked list utils."""

import pytest
from exercises.ex10.linked_list import is_equal, Node, last, value_at, max, linkify, scale

__author__ = "730484878"


def test_last_empty() -> None:
    """Last of an empty linked List should raise a ValueError."""
    with pytest.raises(ValueError):
        last(None)


def test_last_non_empty() -> None:
    """Last of a non-empty list should return its last data value."""
    linked_list = Node(1, Node(2, Node(3, None)))
    assert last(linked_list) == 3


def test_value_at_base_index() -> None:
    """Tests the first index base case returns the first data value in Node."""
    linked_list = Node(10, Node(20, Node(30, None)))
    assert value_at(linked_list, 0) == 10


def test_value_at_index_range() -> None:
    """Tests that for a large index the value_at function will not run."""
    linked_list = Node(10, Node(20, Node(30, None)))
    with pytest.raises(IndexError):
        value_at(linked_list, 3)


def test_max_node_list() -> None:
    """Tests to see if the correct max value is provided."""
    linked_list = Node(10, Node(20, Node(30, None)))
    assert max(linked_list) == 30


def test_max_edge() -> None:
    """Tests to see if the correct max value is provided."""
    linked_list = Node(2, Node(15, Node(28, Node(7, None))))
    assert max(linked_list) == 28


def test_max_empty_list() -> None:
    """If given empty list, return a ValueError."""
    with pytest.raises(ValueError):
        max(None)


def test_linkify_random_list() -> None:
    """Assert that linkify function is working properly."""
    assert is_equal(linkify([1, 2, 3]), Node(1, Node(2, Node(3, None))))


def test_linkify_blank_list() -> None:
    """Assert that if given a blank list linkify will return nothing."""
    assert is_equal(linkify([]), None)


def test_scale_base_case() -> None:
    """Assert that the scale function works."""
    assert is_equal(scale(linkify([1, 2, 3]), 2), Node(2, Node(4, Node(6, None))))


def test_scale_factor_one() -> None:
    """Assert that if the factor is one the function will return the correct Node."""
    assert is_equal(scale(linkify([1, 2, 3]), 1), Node(1, Node(2, Node(3, None))))