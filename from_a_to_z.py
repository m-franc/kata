def gimme_the_letters(string):
    list_string = list(string)
    first_letter_value = ord(list_string[0])
    second_letter_value = ord(list_string[2])
    others_letters = first_letter_value
    i = 0
    letters = ""
    while first_letter_value <= second_letter_value:
        letters = letters + chr(others_letters + i)
        first_letter_value += 1
        i += 1
    return letters

print(gimme_the_letters("e-k"))