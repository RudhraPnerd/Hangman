# Hangman

A command-line Hangman game written in Python. A random word is chosen, and you guess it one letter at a time. Six wrong guesses and the figure is complete.

## How to play

1. A row of underscores shows the length of the hidden word.
2. Type a letter and press Enter.
3. Correct letters are revealed in the word. Wrong letters add a part to the hangman.
4. Guess every letter before the figure is finished to win.

## Download (Windows)

Grab `Hangman.exe` from the [Releases](../../releases) page and double-click it. No Python needed.

Windows SmartScreen may show a warning because the exe isn't code-signed. Click **More info**, then **Run anyway**.

## Run from source

Requires Python 3.8 or newer.

```
git clone https://github.com/<your-username>/<your-repo>.git
cd <your-repo>
python main.py
```

## Project structure

```
.
├── main.py       # game logic
├── configs.py    # settings (path to the word list)
└── words.json    # word list, stored as {"word": letter_count}
```

## Customizing the word list

`words.json` maps each word to its letter count:

```json
{
  "wolf": 4,
  "apple": 5
}
```

Add your own words in the same format, using lowercase letters only.

## Building the exe yourself

```
python -m pip install pyinstaller
python -m PyInstaller --onefile --add-data "words.json;." main.py
```

The exe is created in the `dist` folder.
