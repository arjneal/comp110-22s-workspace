"""Examples of using lists in a simple game."""


from random import randint

# Variable that keeps track of our rolls. Assigned empty list
# str(10), sets up an empty list. 
rolls: list[int] = list() 
rolls.append(randint(1, 6))
rolls.append(randint(1, 6))
print(rolls)

# Access an individual item 
print(rolls[0])
# Access the length of a list (number of items)
