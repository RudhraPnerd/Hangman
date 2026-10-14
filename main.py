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

print("\n".join(hangman_art[6]))


def main():
    with open(cfg.WORDS) as f:
        words = json.load(f)

    word = random.choice(list(words))
    length = len(word)


if __name__ == "__main__":
    main()