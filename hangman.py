import random
import string
from words import words

def get_valid_word(words):
    picked_word = random.choice(words)
    
    while "-" in picked_word or ' ' in picked_word:
        picked_word = random.choice(words)
        
    return picked_word.upper()

def hangman():
    word = get_valid_word(words)
    print(f"I have a {len(word)}-letter word. Can you guess what it is?")
    word_letters = set(word) # letters in a word without duplicates
    alphabet = set(string.ascii_uppercase)
    used_letters = set()
    lives = 10
    tries = 0
    while len(word_letters) > 0:
        user_letter = input("Guess a letter: ").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                correct_letters = [letter if letter in used_letters else '-' for letter in word]
                print("Current word: ", " ".join(correct_letters))
            else:
                lives -= 1
                print(f"Character does not exist. Life left: {lives}")
                if lives == 0:
                    print("Game Over!")
                    print(f"You've used all your life. The word is {word}")
                    return
            
            tries += 1

        elif user_letter in used_letters:
            print("You have already used that character. Please try again.") 
        else:
            print("Invalid character. Please try again.")
            
    print(f"You guessed all the letters in {tries} attempts. The word is: {word}")
        
    
hangman()

# TODO limit attempts