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





"""
Line-by-line explanation

def switch(old_string):
Defines a function named switch that takes one argument, old_string, which should be a string. This is the text you want to transform.

""
new_string = ""
Initializes an empty string. We will build the transformed result by adding characters to this variable as we process old_string.

new_letters = "uoiea"
Specifies the replacement sequence for vowels. It corresponds to how each vowel should be changed:

a → u
e → o
i → i
o → e
u → a

old_letters = "aeiou"
Specifies the original vowels we're looking for. The position of each vowel here aligns with the positions in new_letters.

for char in old_string:
Starts a loop that iterates over each character (char) in the input string, from left to right.

if char in old_letters:
Checks whether the current character is one of the lowercase vowels (a, e, i, o, u).

If yes, we will map it to the corresponding character in new_letters.
If no (it's a consonant, space, punctuation, or uppercase letter), we leave it unchanged.

index = old_letters.index(char) (only runs if the if condition is true)
Finds the position of the vowel char inside the string "aeiou".

Example: if char is 'e', then index is 1.

new_char = new_letters[index] (still inside the if)
Picks the replacement vowel from "uoiea" at the same position.

Example: for index = 1, new_letters[1] is 'o', so 'e' becomes 'o'.

else:
This branch handles characters that are not lowercase vowels (e.g., consonants, spaces, punctuation, or uppercase letters). We won't change them.

new_char = char (inside the else)
Keeps the character as is.

new_string += new_char
Appends the transformed (or unchanged) character to new_string.
This line is inside the loop, so it runs for every character, building the final output step by step.

return new_string
After the loop finishes (i.e., all characters have been processed), returns the completed transformed string.

Step-by-step trace with input "Elena"
Let's run through the loop character by character:

Input: "Elena"

char = 'E'

'E' is not in "aeiou" (it's uppercase), so we go to the else branch.
new_char = 'E'
new_string = "E"

char = 'l'

'l' is not a vowel.
new_char = 'l'
new_string = "El"

char = 'e'

'e' is in "aeiou" → index = 1
new_char = new_letters[1] = 'o'
new_string = "Elo"

char = 'n'

'n' is not a vowel.
new_char = 'n'
new_string = "Elon"

char = 'a'

'a' is in "aeiou" → index = 0
new_char = new_letters[0] = 'u'
new_string = "Elonu"

Final output: "Elonu"

Notes & improvements

This version does not change uppercase vowels (like 'E'). If you want E → O, we can add uppercase handling using str.maketrans and translate.
It doesn't touch accented characters like é, à. We can add rules if you need that.
"""


print(switch("Elena"))   # -> Elonu   