"""Utility functions for working with Linked Lists."""

from __future__ import annotations
from typing import Optional

__author__ = "730484878"


class Node:
    """An item in a singly-linked list."""
    data: int
    next: Optional[Node]

    def __init__(self, data: int, next: Optional[Node]):
        """Construct a singly linked list. Use none for 2nd argument if tail."""
        self.data = data
        self.next = next
    
    def __str__(self) -> str:
        """Produce a string visualization of the linked lists."""
        if self.next is None:
            return f"{self.data} -> None"
        else:
            return f"{self.data} -> {self.next}"
    

def is_equal(lhs: Optional[Node], rhs: Optional[Node]) -> bool:
    """Tests if two linked lists are deeply (values and order) equal to one another."""
    if lhs is None and rhs is None:
        return True
    elif lhs is None or rhs is None or lhs.data != rhs.data:
        return False 
    else: 
        return is_equal(lhs.next, rhs.next)
    

def last(head: Optional[Node]) -> int:
    """Returns the last value of a Linked List, or raises a ValueError if the list is empty."""
    if head is None:
        raise ValueError("last cannot be called with None")
    else:
        if head.next is None:
            return head.data
        else:
            return last(head.next)


def value_at(head: Optional[Node], index: int) -> int:
    """Determines the value at a specific index."""
    if head is None:
        raise IndexError("Index is out of bounds on the list.")
    if index == 0:
        return head.data 
    else:
        return value_at(head.next, index - 1)


def max(head: Optional[Node]) -> int: 
    """Find the max out of all the nodes in a list."""
    if head is None:
        raise ValueError("Cannot call max with None.")
    # Determine if its higher than the last data point
        # Determine with an If statement.
    # If not do not add it to the variable storing the highest data value.
    if head.next is None:
        return head.data
    value: int = head.data
    if value > max(head.next):
        return value
    return max(head.next)


def linkify(items: list[int]) -> Optional[Node]:
    """Turn an items list into a Node."""
    # Need an if statement seperating this from the rest of the code. 
    if items == []:
        return None
    if len(items) == 1:
        return Node(items[0], None)
    else:
        value: Node = Node(items[0], linkify(items[1:]))
    return value


def scale(head: Optional[Node], factor: int) -> Optional[Node]:
    """Scales a function by a random integer."""
    # Access each member of the Node 
    # Access the data 
    # Multiply head.data by the factor
    if head is None:
        return None
    else:
        result: Node = Node(head.data * factor, scale(head.next, factor))
    return result
    