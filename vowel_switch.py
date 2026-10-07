"""Swap the vowels in a piece of text: a and u change places, and so do e and o."""

import sys

# A lookup table for str.translate. Each letter in the first string is replaced
# by the letter in the same position in the second string.
SWAPS = str.maketrans("aeiouAEIOU",
                      "uoieaUOIEA")


def switch(text):
    """Return the text with its vowels swapped. Every other character stays as it is."""
    return text.translate(SWAPS)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        # The text was given on the command line:  python vowel_switch.py hello world
        text = " ".join(sys.argv[1:])
    else:
        text = input("Text to switch: ")
    print(switch(text))
