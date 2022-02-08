"""EX02 a one-shot wordle."""

__author__ = "730484878"


secret_word: str = "lenoir"
guess_word: str = input(f"What is your {len(secret_word)}- letters guess? ")
# Initiates guess word and secret word. 
while len(guess_word) != len(secret_word):
    guess_word = input(f"That was not {len(secret_word)}-letters! Try again: ")

white_box: str = "\U00002B1C"
green_box: str = "\U0001F7E9"
yellow_box: str = "\U0001F7E8"
# initiate variable for yellow boxes, white boxes, and green boxes.
i = 0
# first counter variable allows i to run through and find all matching indices in guess variable.
emoji_storage: str = ""
# Emoji_storage stores the white, green and yellow boxes.   
while i < len(secret_word): 
    matching_indices: str = (guess_word[i])
    if matching_indices == secret_word[i]:
        emoji_storage += (green_box)
    else:
        track_characters: bool = False 
        idx: int = 0
# second counter variable for nested while allows program to run through all the characters in the secret word.  
        while not track_characters and idx < len(secret_word):
            if matching_indices == secret_word[idx]: 
                track_characters = True 
            idx += 1
        if track_characters: 
            emoji_storage += yellow_box
# If this is true emoji storage adds a yellow box. 
        else: 
            emoji_storage += white_box
# if the "if" statement in the nested loop and the if statement in the original loop are both false then it prints a white box.
# AKA if that letter is not in the specific index or anywhere in the word you print a white box in the space. 
    i = i + 1
# Increases the original counter variable so it is not an infinite- loop.
print(emoji_storage)
if guess_word == secret_word: 
    print("Woo! You got it!")
# if the guess_word is correct then this is printed. 
else: 
    print("Not quite, Play again soon!")
