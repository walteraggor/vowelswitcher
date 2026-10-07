# Vowel Switcher

[![Tests](https://github.com/walteraggor/vowelswitcher/actions/workflows/tests.yml/badge.svg)](https://github.com/walteraggor/vowelswitcher/actions/workflows/tests.yml)

A small Python program that swaps the vowels in a piece of text. Each vowel is replaced by the one at the opposite end of `aeiou`:

| Vowel | Becomes |
|---|---|
| `a` | `u` |
| `e` | `o` |
| `i` | `i` |
| `o` | `e` |
| `u` | `a` |

Capital vowels are swapped in the same way and stay capital. So `Elena` becomes `Olonu` and `hello world` becomes `holle werld`. Consonants, digits, spaces and punctuation are left as they are.

Because the swap is symmetric, switching a text twice gives back the original.

## Run it

You need Python 3. There are no packages to install.

```bash
git clone https://github.com/walteraggor/vowelswitcher.git
cd vowelswitcher
python vowel_switch.py Elena
```

```
Olonu
```

Give it as many words as you like:

```bash
python vowel_switch.py hello world
```

```
holle werld
```

Without any text, it asks for some:

```
Text to switch: A quick brown fox
U qaick brewn fex
```

## Use it in your own code

```python
from vowel_switch import switch

print(switch("Elena"))   # Olonu
```

## How it works

```python
SWAPS = str.maketrans("aeiouAEIOU",
                      "uoieaUOIEA")


def switch(text):
    return text.translate(SWAPS)
```

1. `str.maketrans` builds a lookup table from two strings of the same length. Each letter in the first string is paired with the letter in the same position in the second: `a` with `u`, `e` with `o`, and so on. The strings are written one above the other so that the pairs line up.
2. `text.translate(SWAPS)` goes through the text one character at a time. A character that is in the table is replaced by its partner. Any other character is copied as it is.
3. The table is built once, when the file is loaded, and used again every time `switch` is called.

### Tracing `switch("Elena")`

| Character | In the table? | Becomes | Result so far |
|---|---|---|---|
| `E` | yes | `O` | `O` |
| `l` | no | `l` | `Ol` |
| `e` | yes | `o` | `Olo` |
| `n` | no | `n` | `Olon` |
| `a` | yes | `u` | `Olonu` |

### The same thing written as a loop

`translate` does the work of the loop below, which is how the first version of this program was written. It gives the same results and shows each step:

```python
def switch(old_string):
    new_string = ""
    old_letters = "aeiouAEIOU"
    new_letters = "uoieaUOIEA"
    for char in old_string:
        if char in old_letters:
            index = old_letters.index(char)
            char = new_letters[index]
        new_string = new_string + char
    return new_string
```

For each character, `old_letters.index(char)` finds its position among the vowels, and the character is replaced by the letter at the same position in `new_letters`. For `'e'` the position is 1, and `new_letters[1]` is `'o'`.

## Tests

```bash
python -m unittest
```

The tests check every vowel in both cases, that nothing else changes, that switching twice gives back the original, and that the program works from the command line. GitHub runs them on Linux and Windows for every push and pull request.

## Ideas for extending it

- Decide what should happen to accented vowels such as `é`. At the moment they are left alone.
- Read the text from a file and write the result to another file.
