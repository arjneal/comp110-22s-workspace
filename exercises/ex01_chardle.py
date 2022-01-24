"""EX01 Chardle."""

__author__ = "730484878"


five_character_word: str = input("Enter a 5-character word: ")
if len(five_character_word) != 5:
    exit("Error: Word must contain 5 characters")
single_character: str = input("Enter a single Character: ")
if len(single_character) != 1:
    exit("Error: Character must be a single character.")
character_counter: int = 0

print("searching for " + single_character + " in " + five_character_word)
if five_character_word[0] == single_character:
    print(single_character + " found at index 0")
    character_counter = character_counter + 1
if five_character_word[1] == single_character:
    print(single_character + " found at index 1")
    character_counter = character_counter + 1
if five_character_word[2] == single_character:
    print(single_character + " found at index 2")
    character_counter = character_counter + 1
if five_character_word[3] == single_character:
    print(single_character + " found at index 3")
    character_counter = character_counter + 1
if five_character_word[4] == single_character:
    print(single_character + " found at index 4")
    character_counter = character_counter + 1
if character_counter == 0:
    print("No instances of " + single_character + " found in " + five_character_word)
if character_counter == 1:
    print("1 instance of " + single_character + " found in " + five_character_word)
if character_counter == 2:
    print("2 instances of " + single_character + " found in " + five_character_word)
if character_counter == 3:
    print("3 instances of " + single_character + " found in " + five_character_word)
if character_counter == 4:
    print("4 instances of " + single_character + " found in " + five_character_word)
if character_counter == 5:
    print("5 instances of " + single_character + " found in " + five_character_word)