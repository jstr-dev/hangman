import random
import string 
import os 
from english_words import get_english_words_set

words = list(get_english_words_set(['web2'], lower=True))
alphabet = list(string.ascii_lowercase)

def draw_man(stage):
    states = ["--------", "|", "O", "|", "/|\\", "/ \\"]
    draw_state = [stage > i and states[i] or " " * len(states[i]) for i in range(len(states))]
    man = """
        %s|
        %s       |
        %s       |
        %s       |
       %s      |
       %s      |   
              _____       
    """
    print(man % tuple(draw_state))

def hangman():
    word = random.choice(words)
    chars = set(word)
    chars_tried = list()
    lives = 6
    msg = ""

    while lives > 0:
        os.system('cls')
        guessed = "".join(char in chars_tried and char or "_" for char in word)
        draw_man(6 - lives)
        print(f"Word progress: {guessed}")
        print("\nLetters tried: " + ", ".join(chars_tried))
        print("Current Lives:", lives)
        if len(msg) > 0:
            print("\n"+msg)
        inp = input("\nGuess a letter or the word: ").lower()

        if len(inp) == 1: 
            if inp not in alphabet:
                msg = "Enter a valid letter."
                continue
            elif inp in chars_tried:
                msg = "You have already tried this letter, try another."
                continue 
        else:
            if inp == word:
                print("Congratulations, you win!")
                break 
            msg = "That was an incorrect guess, you lose a life."
            lives -= 1
            continue 

        chars_tried.append(inp)

        if inp in chars:
            msg = "Congratulations, you guessed a letter correctly."
            if chars.issubset(set(chars_tried)):
                print("Congratulations, you win!")
                break 
        else:
            lives -= 1
            msg = f"{inp} is not in the word, you lose a life."

    if lives == 0:
        print(f"You lost, the word was: {word}")

    input("Press any key to exit...")
hangman()