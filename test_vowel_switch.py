"""Tests for vowel_switch.py.

Run them from this folder with:  python -m unittest
"""

import string
import subprocess
import sys
import unittest
from pathlib import Path

from vowel_switch import switch

SCRIPT = Path(__file__).with_name("vowel_switch.py")


class SwitchTests(unittest.TestCase):
    def test_each_vowel_becomes_its_partner(self):
        pairs = {"a": "u", "e": "o", "i": "i", "o": "e", "u": "a"}
        for vowel, partner in pairs.items():
            with self.subTest(vowel=vowel):
                self.assertEqual(switch(vowel), partner)
                self.assertEqual(switch(vowel.upper()), partner.upper())

    def test_words_and_sentences(self):
        examples = {
            "Elena": "Olonu",
            "hello world": "holle werld",
            "HELLO, World!": "HOLLE, Werld!",
            "A quick brown fox": "U qaick brewn fex",
            "aeiou AEIOU": "uoiea UOIEA",
        }
        for text, expected in examples.items():
            with self.subTest(text=text):
                self.assertEqual(switch(text), expected)

    def test_everything_that_is_not_a_vowel_stays_the_same(self):
        vowels = "aeiouAEIOU"
        others = "".join(character for character in string.printable if character not in vowels)
        self.assertEqual(switch(others), others)

    def test_accented_vowels_are_left_alone(self):
        self.assertEqual(switch("café Zoë Åse"), "cufé Zeë Åso")

    def test_empty_text(self):
        self.assertEqual(switch(""), "")

    def test_the_text_keeps_its_length(self):
        for text in ("Elena", "hello world", string.printable, "line one\nline two\n"):
            with self.subTest(text=text):
                self.assertEqual(len(switch(text)), len(text))

    def test_switching_twice_gives_back_the_original(self):
        for text in ("Elena", "hello world", "AEIOU aeiou", string.printable, "café", ""):
            with self.subTest(text=text):
                self.assertEqual(switch(switch(text)), text)


class ScriptTests(unittest.TestCase):
    """The file run the way a person runs it: python vowel_switch.py"""

    def run_script(self, *arguments, typed=""):
        finished = subprocess.run([sys.executable, str(SCRIPT), *arguments], input=typed,
                                  stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                  universal_newlines=True, timeout=60)
        self.assertEqual(finished.returncode, 0, finished.stderr)
        self.assertEqual(finished.stderr, "")
        return finished.stdout

    def test_text_on_the_command_line(self):
        self.assertEqual(self.run_script("Elena"), "Olonu\n")

    def test_several_words_on_the_command_line(self):
        self.assertEqual(self.run_script("hello", "world"), "holle werld\n")
        self.assertEqual(self.run_script("hello world"), "holle werld\n")

    def test_without_text_it_asks_for_some(self):
        self.assertEqual(self.run_script(typed="hello world\n"), "Text to switch: holle werld\n")

    def test_importing_the_file_prints_nothing(self):
        finished = subprocess.run([sys.executable, "-c", "import vowel_switch"], cwd=str(SCRIPT.parent),
                                  stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                  universal_newlines=True, timeout=60)
        self.assertEqual((finished.returncode, finished.stdout, finished.stderr), (0, "", ""))


if __name__ == "__main__":
    unittest.main()
