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


print(switch("Elena"))   # -> Elonu
