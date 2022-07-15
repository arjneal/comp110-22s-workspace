"""Celebrating the Christmas Spirit!"""

from __future__ import annotations

class ChristmasTreeFarm:
    plots: list[int]

    def __init__(self, plots: int, initial_planting):
        """Initialize."""
        i: int = 0
        while i < initial_planting:
            self.plots.append(1)
            i += 1
        while i < len(self.plots):
            self.plots.append(0)
            i += 1 

    def plant(self, pindex: int) -> None:
        """Determines where trees should be planted."""
        self.plots[pindex] = 1 
    
    def growth(self) -> None:
        """Grows the planted trees."""
        i: int = 0 
        while i < len(self.plots):
            if self.plots[i] != 0: 
                self.plots[i] += 1 
            i += 1 

    def harvest(self, replant: bool) -> int:
        i: int = 0 
        conty: int = 0
        while i < len(self.plots):
            if self.plots[i] >= 5:
                self.plots.pop(i)
                if replant:
                    self.plots[i] = 1
                    conty += 1 
                else:
                    self.plots[i] = 0 
            i += 1 
        return conty
    
    def __add__(self, rhs: ChristmasTreeFarm) -> None:
        """Overload the addition operator."""
        for value in self.plots:
            n_val: int = 0
            for val in rhs.plots:
                n_val = val + value

                

    


