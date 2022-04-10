"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = "730484878"


class Simpy:
    """Simpy class similar to Numpy Library."""
    values: list[float]

    def __init__(self, value: list[float]):
        """Initialize values to an object."""
        self.values = value

    def __str__(self) -> str:
        """String representation of the object."""
        return f"Simpy({self.values})"
    
    def fill(self, fill_val: float, iter: int) -> None:
        """Fill the object with certain number of iterations of specific value."""
        i: int = 0 
        self.values = []
        while i < iter: 
            self.values.append(fill_val)
            i += 1

    def arange(self, start: float, stop: float, step: float = 1.0) -> None:
        """Arranges the values in a numerical order."""
        if step != 0.0:
            # Start is the first value in the range
            # Stop is the second 
            # Step is the increment amount between each value. 
            i: float = 0.0
            iterate: float = ((stop - start) / step) - 1 
            self.values = [] 
            self.values.append(start)
            while i < iterate:
                value: float = self.values[len(self.values) - 1] + step
                self.values.append(value)
                i += 1
        else: 
            return None
    
    def sum(self) -> float:
        """Compute and return the sum of all the values."""
        summation: float = 0.0
        for value in self.values:
            summation += value
        return summation

    def __add__(self, rhs: Union[Simpy, float]) -> Simpy:
        """Operator Overloading: addition."""
        # Try to implement with for.. in loops as well. 
        # Value must be reset to 0 whenever entering a loop as loop will continue to contain old value if not reinitiated to 0.
        if isinstance(rhs, Simpy):
            simp_list: list[float] = []
            i: int = 0 
            while i < len(self.values):
                append_val: float = 0.0
                append_val: float = rhs.values[i] + self.values[i]
                simp_list.append(append_val)
                i += 1
            return Simpy(simp_list)
        if isinstance(rhs, float):
            new_list: list[float] = [] 
            for value in self.values:
                new_val: float = rhs + value
                new_list.append(new_val)
            return Simpy(new_list)

    def __pow__(self, rhs: Union[Simpy, float]) -> Simpy:
        """Operator Overloading: Powers - takes both Simpy or Float Value."""
        float_list: list[float] = [] 
        if isinstance(rhs, Simpy):
            i: int = 0 
            while i < len(self.values):
                val: float = 0.0
                val = self.values[i] ** rhs.values[i]
                float_list.append(val)
                i += 1 
            return Simpy(float_list)
        if isinstance(rhs, float):
            for value in self.values:
                val: float = 0.0 
                val = value ** rhs
                float_list.append(val)
            return Simpy(float_list)
    
    def __eq__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Creates a mask for a function determines if two values are equal to eachother."""
        if isinstance(rhs, float):
            bools: list[bool] = []
            for value in self.values:
                if rhs == value:
                    bools.append(True)
                else:
                    bools.append(False)
            return bools
        if isinstance(rhs, Simpy):
            bools_results: list[bool] = []
            i: int = 0 
            while i < len(self.values):
                if self.values[i] == rhs.values[i]:
                    bools_results.append(True)
                else:
                    bools_results.append(False)
                i += 1
            return bools_results
    
    def __gt__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Compare a Simpy."""
        if isinstance(rhs, float):
            result_bools: list[bool] = [] 
            for value in self.values: 
                if value > rhs:
                    result_bools.append(True)
                else:
                    result_bools.append(False)
            return result_bools
        if isinstance(rhs, Simpy):
            new_list: list[bool] = [] 
            i: int = 0 
            while i < len(self.values):
                if self.values[i] > rhs.values[i]:
                    new_list.append(True)
                else:
                    new_list.append(False)
                i += 1
            return new_list
    
    def __getitem__(self, rhs: Union[int, list[bool]]) -> Union[float, Simpy]:
        """Overload Operator: get item index."""
        # First need to call a list[bool] to get the rhs value: then you can get a simpy from that. 
        # Because rhs: list[bool] and self.values: list are correlated.
        # Ex. 3rd index self.values and 3rd index of rhs are related.
        # __gt__ operator determines if the condition is met then __getitem__ overloads.
        if isinstance(rhs, int):
            return self.values[rhs]
        else:
            result: list[float] = [] 
            i: int = 0
            while i < len(self.values):
                if rhs[i]: 
                    result.append(self.values[i])
                i += 1
            return Simpy(result)