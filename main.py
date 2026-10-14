import configs as cfg
import random
import json

hangman_art = {
    0: ("   ",
        "   ",
        "   "),
    1: (" o ",
        "   ",
        "   "),
    2: (" o ",
        " | ",
        "   "),
    3: (" o ",
        " | ",
        "/  "),
    4: (" o ",
        " | ",
        "/ \\"),
    5: (" o ",
        "/| ",
        "/ \\"),
    6: (" o ",
        "/|\\",
        "/ \\"),
}

mistakes = 0

print("\033[32m", end="")


def check_letter(char, word, guessed):
    global mistakes
    if char in guessed:
        print('Already Guessed!')

    elif char in word:
        print('Successful')

    else:
        mistakes += 1
        print("\n".join(hangman_art[mistakes]))

def main():
    with open(cfg.WORDS) as f:
        words = json.load(f)

    word = random.choice(list(words))
    guessed = set()
    length = len(word)

    print('_  ' * length)

    while mistakes < 6:
        print(" ".join(c if c in guessed else "_" for c in word))
        char = input('Type in a letter: ')
        check_letter(char, word, guessed)
        guessed.add(char)

        if all(c in guessed for c in word):
            print("You won!")
            break
    if mistakes == 6:
        print(f"You Lost! The Answer was '{word}'")


if __name__ == "__main__":
    main()