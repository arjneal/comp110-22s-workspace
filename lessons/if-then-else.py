"""Tests."""

from __future__ import annotations


class StringList:
    items: list[str]
    
    def __init__(self, items: list[str]):
        """Init."""
        self.items = items
   
    def __mul__(self, r: int) -> StringList:
        """MUL."""
        result: list[str] = [] 
        for item in self.items:
            result.append(item * r)
        nsl: StringList = StringList(result)
        return nsl
    

s1: StringList = StringList(["a", "b", "c"])
print(s1.items)
s2: StringList = s1 * 3
print(s2.items)
