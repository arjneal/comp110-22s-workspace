"""Structured Wordle Game."""


_author_ = "730484878"

i = 0


def contains_char(secret_word: str, character: str) -> bool: 
    """Determines if a string contains the character."""
    # Will be useful in determining whether or not to print yellow boxes in the output of the Wordle game. 
    assert len(character) == 1
    i = 0
    while i < len(secret_word):
        if secret_word[i] == character:
            # Indexes through the entire word and if character is found returns an assesment of True. 
            return True
        i += 1 
    return False 
# Returns a statement of false if the character is not found. 


def emojified(guess: str, secret: str) -> str: 
    # Emojified will return a string of emoji's given the guess word and secret word.
    """Emojifies whether or not the secret word is equal to the guess word."""
    assert len(guess) == len(secret)
    white_box: str = "\U00002B1C"
    green_box: str = "\U0001F7E9"
    yellow_box: str = "\U0001F7E8"
    # Emoji variables. 
    idx = 0
    # Initialized counter variable (idx) to 0.
    emoji_storage: str = ""
    # Blank string that will collect the emoji_boxes in the while loop and return them after the loop has completed. 
    while idx < len(secret):
        if secret[idx] == guess[idx]:
            # Notice secret and guess are indexed with the same variable (idx) so the same letter at same index would be green box. (Ex.secret[3]=guess[3] then green)
            emoji_storage += green_box
        else:
            if contains_char(secret, guess[idx]):
                # if the character found in the index variable [idx] of guess is found anywhere in the word it will print a yellow box. (Ex. secret[5] = guess[3] then yellow box.)
                emoji_storage += yellow_box
            else:
                emoji_storage += white_box
        idx += 1
    return emoji_storage 
# The string holder variable is returned that way it contains every box on the same line. 


def input_guess(guess_length: int) -> str:
    """Determines if the guess is the correct character length."""
    guess_word: str = input(f"Enter a {guess_length} letter word.")
    while len(guess_word) != guess_length:
        guess_word: str = input(f"That wasn't {guess_length} chars! Try again: ")
    # If the guess_word is not equal to the length of the guess then it runs a loop until that condition is no longer false. 
    return guess_word  


def main() -> None:
    """The entrypoint of the program and main game loop."""
    guess_attempts: int = 1
    # Initialized to 1 instead of 0 because Human numbering starts with 1's not 0's.
    won: bool = False
    secret_word: str = "codes"
    while guess_attempts < 7 and not won: 
        print(f"=== Turn {guess_attempts}/ 6 ===")
        guess_word = input_guess(len(secret_word))
        print(emojified(guess_word, secret_word)) 
        if guess_word == secret_word:
            print(f"You won in {guess_attempts}/6 turns") 
            won = True
        guess_attempts += 1
    if not won:
        print("X/6- Sorry, try again tomorrow!")
# Won variable is initialized to False within the while loop condition it is changed to True (not False) the while loop will stop running if either one of the statements becomes False
# For example, if guess attempts is greater than or equal to 7 then the function would stop running because the rhs would be False- False and True (not won) would not evaluate to True. 
# Once the while loop ONLY reaches the condition of False on the (rhs) and stops running then the last line of code print(X/6- Sorry Try Again would print). This is because the user has reached the maximum amount of attempts and still has yet to guess the correct word. 
