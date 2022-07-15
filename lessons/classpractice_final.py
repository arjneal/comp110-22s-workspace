"""Class practice writing for the final exam."""

from re import M


class HotCocoa:
    has_whip: bool
    flavor: str
    marshmallow_count: int
    sweetness: int

    def __init__(self, h: bool, f: str, mm: int, s: int):
        """Initializes the attributes of the HotCocoa class."""
        self.has_whip = h 
        self.flavor = f
        self.marshmallow_count = mm
        self.sweetness = s
    
    def mallow_adder(self, mallows: int): 
        """Increases the marshmallow count and sweetness."""
        self.marshmallow_count += mallows
        self.sweetness *= (mallows * 2)
    
    def calorie_count(self) -> float:
        """Returns the amount of calories."""
        calories: float = 0.0
        if self.flavor == "vanilla" or "peppermint":
            calories += 30.0
        else:
            calories += 20.0
        if self.has_whip:
            calories += 100.0
        calories += (self.marshmallow_count / 2)
        return calories


class TimeSpent:
    name: str
    purpose: str
    minutes: int

    def __init__(self, name: str, purpose: str, minute: int):
        """Initializes the time spent on something."""
        self.name = name
        self.purpose = purpose
        self.minutes = minute
    
    def add_time(self, increase: int) -> None:
        """Adds time to the minutes attribute."""
        self.minutes += increase
    
    def reset(self) -> int:
        """Returns the value that was previously stored in minutes then resets the program."""
        storage: int = self.minutes
        self.minutes = 0 
        return storage
    
    def report(self) -> str:
        """Reports the time spent."""
        hours: int = self.minutes // 60
        minutes: int = self.minutes % 60
        return f"{self.name} has spent {hours} hours and {minutes} minutes on {self.purpose}"



    
