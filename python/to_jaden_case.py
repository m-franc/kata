def to_jaden_case(string):
    words = string.split(" ")
    new_string = ""
    new_words = []
    for word in words:
        new_words.append(word.capitalize())
    for word in new_words:
        new_string = new_string + word + " "
    return new_string[:-1]

print(to_jaden_case("hello we need to capitalize it"))