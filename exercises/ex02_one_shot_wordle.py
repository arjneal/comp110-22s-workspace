"""EX02 a one-shot wordle."""

__author__ = "730484878"


secret_word: str = "python"
guess_word: str = input(f"What is your {len(secret_word)}- letters guess? ")

while len(guess_word) != len(secret_word):
    guess_word = input(f"That was not {len(secret_word)}-letters! Try again: ")

white_box: str = "\U00002B1C"
green_box: str = "\U0001F7E9"
yellow_box: str = "\U0001F7E8"

i = 0

emoji_storage: str = ""

while i < len(secret_word): 
    matching_indices: str = (guess_word[i])
    if matching_indices == secret_word[i]:
        emoji_storage += (green_box)
    else:
        track_characters: bool = False 
        idx: int = 0
        while not track_characters and idx < len(secret_word):
            if matching_indices == secret_word[idx]: 
                track_characters = True 
            idx += 1
        if track_characters: 
            emoji_storage += yellow_box
        else: 
            emoji_storage += white_box
    i = i + 1
print(emoji_storage)
if guess_word == secret_word: 
    print("Woo! You got it!")
else: 
    print("Not quite, Play again soon!")
