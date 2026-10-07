# Vowel Switcher

A small Python function that swaps the vowels in a piece of text. Each lowercase vowel is replaced by the one at the opposite end of `aeiou`:

| Vowel | Becomes |
|---|---|
| `a` | `u` |
| `e` | `o` |
| `i` | `i` |
| `o` | `e` |
| `u` | `a` |

So `"Elena"` becomes `"Elonu"` and `"hello world"` becomes `"holle werld"`. Consonants, spaces, punctuation and capital letters are left as they are.

Because the swap is symmetric, switching a text twice gives back the original.

## Run it

Any version of Python 3 works, and there are no packages to install.

```bash
git clone https://github.com/walteraggor/vowelswitcher.git
cd vowelswitcher
python vowel_switch.py
```

```
Elonu
```

To try your own text, change the string in the last line of `vowel_switch.py`.

## How it works

```python
def switch(old_string):
    new_string = ""
    new_letters = "uoiea"
    old_letters = "aeiou"
    for char in old_string:
        if char in old_letters:
            index = old_letters.index(char)
            char = new_letters[index]
        new_string = new_string + char
    return new_string
```

1. `new_string` starts empty. The result is built up one character at a time.
2. `old_letters` holds the vowels to look for, and `new_letters` holds their replacements in the same positions.
3. The loop visits each character of the input from left to right.
4. If the character is a lowercase vowel, `old_letters.index(char)` finds its position in `"aeiou"`, and the character is replaced by the letter at the same position in `"uoiea"`. For `'e'` the position is 1, and `new_letters[1]` is `'o'`.
5. Any other character is left unchanged.
6. The character is added to `new_string`. When the loop finishes, the completed string is returned.

### Tracing `switch("Elena")`

| Character | Lowercase vowel? | Added | Result so far |
|---|---|---|---|
| `E` | no, it is uppercase | `E` | `E` |
| `l` | no | `l` | `El` |
| `e` | yes, position 1 | `o` | `Elo` |
| `n` | no | `n` | `Elon` |
| `a` | yes, position 0 | `u` | `Elonu` |

## Ideas for extending it

- Switch uppercase vowels too, so that `E` becomes `O`. `str.maketrans` and `str.translate` are a neat way to do it.
- Decide what should happen to accented vowels such as `é`.
