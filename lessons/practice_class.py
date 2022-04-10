"""Christmas Tree Farm Class"""


class ChristmasTreeFarm:
    plots: list[int]

    def __init__(self, plots: int, initial_planting: int):
        """Initializes the Farm!"""
        self.plots = [] 
        i: int = 0 
        while i < initial_planting:
            self.plots.append(1)
            i += 1 
        while i < plots:
            self.plots.append(0)
            i += 1 
    
    def plant(self, location: int) -> None:
        """Plant method."""
        self.plots[location] = 1 
    
    def growth(self) -> None:
        """Increase size of each planted tree by 1."""
        for tree in self.plots:
            if tree != 0:
                tree += 1 
                self.plots[tree] = tree 

    def __repr__(self) -> str:
        return(f"ChristmasTreeFarm: {self.plots}")


example: ChristmasTreeFarm = ChristmasTreeFarm(5, 4)

example.growth()
print(example)
